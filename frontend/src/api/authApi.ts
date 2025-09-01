import axios from 'axios';

const API_URL = '/api/auth';

export const authApi = {
  register: async ({ username, email, phone, password }: { username: string; email: string; phone: string; password: string; }) => {
    const response = await axios.post(`${API_URL}/register/`, { username, email, phone, password });
    return response.data;
  },
  login: async ({ identifier, password }: { identifier: string; password: string; }) => {
    const response = await axios.post(`${API_URL}/login/`, { identifier, password });
    return response.data;
  },
  logout: async (refreshToken: string) => {
    const response = await axios.post(`${API_URL}/logout/`, { refresh: refreshToken });
    return response.data;
  },
  requestPasswordReset: async (identifier: string) => {
    const response = await axios.post(`${API_URL}/password-reset/request/`, { identifier });
    return response.data;
  },
  confirmPasswordReset: async ({ identifier, code, new_password }: { identifier: string; code: string; new_password: string; }) => {
    const response = await axios.post(`${API_URL}/password-reset/confirm/`, { identifier, code, new_password });
    return response.data;
  },
};
