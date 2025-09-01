import { useEffect } from 'react';
import { authApi } from '../api/authApi';
import { useAuthStore } from '../store/authStore';

export default function Logout() {
  const refreshToken = useAuthStore((state) => state.refreshToken);
  const logoutStore = useAuthStore((state) => state.logout);

  useEffect(() => {
    const doLogout = async () => {
      if (refreshToken) {
        await authApi.logout(refreshToken);
      }
      logoutStore();
    };
    void doLogout();
  }, [refreshToken, logoutStore]);

  return <div>Logging out...</div>;
}
