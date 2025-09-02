import { useEffect, useState } from 'react';
import { paymentsApi, type Transaction } from '../../api/paymentsApi';

export default function Transactions() {
  const [items, setItems] = useState<Transaction[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    paymentsApi
      .getTransactions()
      .then((t) => setItems(t))
      .catch(() => setError('Failed to load transactions'))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div className="text-red-500">{error}</div>;

  return (
    <table className="w-full border">
      <thead>
        <tr>
          <th className="border px-2">Тип</th>
          <th className="border px-2">Сумма</th>
          <th className="border px-2">Статус</th>
          <th className="border px-2">Дата</th>
        </tr>
      </thead>
      <tbody>
        {items.map((t) => (
          <tr key={t.id}>
            <td className="border px-2">{t.type}</td>
            <td className="border px-2">{t.amount}</td>
            <td className="border px-2">{t.status}</td>
            <td className="border px-2">{new Date(t.createdAt).toLocaleString()}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

