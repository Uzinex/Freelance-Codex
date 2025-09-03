import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Register from './pages/Register';
import Login from './pages/Login';
import ResetPasswordRequest from './pages/ResetPasswordRequest';
import ResetPasswordConfirm from './pages/ResetPasswordConfirm';
import Logout from './pages/Logout';
import ProjectsList from './pages/projects/ProjectsList';
import ProjectDetail from './pages/projects/ProjectDetail';
import CreateProject from './pages/projects/CreateProject';
import PrivateRoute from './components/PrivateRoute';
import Wallet from './pages/payments/Wallet';
import Transactions from './pages/payments/Transactions';
import Transfer from './pages/payments/Transfer';
import ChatList from './pages/chat/ChatList';
import ChatRoom from './pages/chat/ChatRoom';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
        <Route path="/reset-password" element={<ResetPasswordRequest />} />
        <Route path="/reset-password/confirm" element={<ResetPasswordConfirm />} />
        <Route
          path="/logout"
          element={
            <PrivateRoute>
              <Logout />
            </PrivateRoute>
          }
        />
        <Route
          path="/wallet"
          element={
            <PrivateRoute>
              <Wallet />
            </PrivateRoute>
          }
        />
        <Route
          path="/wallet/transactions"
          element={
            <PrivateRoute>
              <Transactions />
            </PrivateRoute>
          }
        />
        <Route
          path="/wallet/transfer"
          element={
            <PrivateRoute>
              <Transfer />
            </PrivateRoute>
          }
        />
        <Route
          path="/chat"
          element={
            <PrivateRoute>
              <ChatList />
            </PrivateRoute>
          }
        />
        <Route
          path="/chat/:roomId"
          element={
            <PrivateRoute>
              <ChatRoom />
            </PrivateRoute>
          }
        />
        <Route path="/projects" element={<ProjectsList />} />
        <Route
          path="/projects/new"
          element={
            <PrivateRoute>
              <CreateProject />
            </PrivateRoute>
          }
        />
        <Route path="/projects/:id" element={<ProjectDetail />} />
      </Routes>
    </BrowserRouter>
  );
}
