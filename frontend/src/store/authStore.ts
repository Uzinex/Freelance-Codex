import { create } from 'zustand';

interface Tokens {
  accessToken: string;
  refreshToken: string;
}

interface AuthState {
  accessToken: string | null;
  refreshToken: string | null;
  login: (tokens: Tokens) => void;
  logout: () => void;
}

const storedAccess = typeof window !== 'undefined' ? localStorage.getItem('accessToken') : null;
const storedRefresh = typeof window !== 'undefined' ? localStorage.getItem('refreshToken') : null;

export const useAuthStore = create<AuthState>((set) => ({
  accessToken: storedAccess,
  refreshToken: storedRefresh,
  login: ({ accessToken, refreshToken }) => {
    if (typeof window !== 'undefined') {
      localStorage.setItem('accessToken', accessToken);
      localStorage.setItem('refreshToken', refreshToken);
    }
    set({ accessToken, refreshToken });
  },
  logout: () => {
    if (typeof window !== 'undefined') {
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
    }
    set({ accessToken: null, refreshToken: null });
  },
}));
