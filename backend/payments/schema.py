import strawberry
import strawberry_django
from decimal import Decimal
from typing import List
from django.contrib.auth import get_user_model

from projects.schema import UserType
from .models import Wallet, Transaction
from notifications.tasks import send_system_notification, dispatch_notification


@strawberry_django.type(Wallet)
class WalletType:
    id: strawberry.auto
    user: UserType
    balance: strawberry.auto


@strawberry_django.type(Transaction)
class TransactionType:
    id: strawberry.auto
    wallet: WalletType
    amount: strawberry.auto
    type: strawberry.auto
    status: strawberry.auto
    created_at: strawberry.auto


@strawberry.type
class Query:
    @strawberry.field
    def wallet(self, info) -> WalletType:
        user = info.context.request.user
        if not user.is_authenticated:
            raise Exception("Authentication required")
        return user.wallet

    @strawberry.field
    def transactions(self, info) -> List[TransactionType]:
        user = info.context.request.user
        if not user.is_authenticated:
            raise Exception("Authentication required")
        return list(user.wallet.transactions.order_by("-created_at"))


@strawberry.type
class Mutation:
    @strawberry.mutation
    def deposit(self, info, amount: Decimal) -> WalletType:
        user = info.context.request.user
        if not user.is_authenticated:
            raise Exception("Authentication required")
        wallet = user.wallet
        wallet.balance += amount
        wallet.save()
        Transaction.objects.create(wallet=wallet, amount=amount, type="deposit")
        return wallet

    @strawberry.mutation
    def withdraw(self, info, amount: Decimal) -> WalletType:
        user = info.context.request.user
        if not user.is_authenticated:
            raise Exception("Authentication required")
        wallet = user.wallet
        if wallet.balance < amount:
            raise Exception("Insufficient funds")
        wallet.balance -= amount
        wallet.save()
        Transaction.objects.create(wallet=wallet, amount=amount, type="withdraw")
        return wallet

    @strawberry.mutation
    def transfer(self, info, to_user_id: int, amount: Decimal) -> WalletType:
        user = info.context.request.user
        if not user.is_authenticated:
            raise Exception("Authentication required")
        if user.id == to_user_id:
            raise Exception("Cannot transfer to yourself")
        wallet = user.wallet
        if wallet.balance < amount:
            raise Exception("Insufficient funds")
        User = get_user_model()
        to_user = User.objects.get(pk=to_user_id)
        to_wallet = to_user.wallet
        wallet.balance -= amount
        wallet.save()
        to_wallet.balance += amount
        to_wallet.save()
        Transaction.objects.create(wallet=wallet, amount=amount, type="transfer")
        Transaction.objects.create(wallet=to_wallet, amount=amount, type="transfer")
        dispatch_notification(send_system_notification, to_user.id, 'Payment Received', f'You received {amount} from {user.username}')
        return wallet
