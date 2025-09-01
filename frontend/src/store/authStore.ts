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
  setTokens: (tokens: Tokens) => void;
  clearTokens: () => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  accessToken: null,
  refreshToken: null,
  login: (tokens) => set({ accessToken: tokens.accessToken, refreshToken: tokens.refreshToken }),
  logout: () => set({ accessToken: null, refreshToken: null }),
  setTokens: (tokens) => set({ accessToken: tokens.accessToken, refreshToken: tokens.refreshToken }),
  clearTokens: () => set({ accessToken: null, refreshToken: null }),
}));
