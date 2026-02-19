import axios from 'axios'

const api = axios.create({ baseURL: 'http://localhost:8000' })
api.interceptors.request.use((cfg) => {
  const token = localStorage.getItem('token')
  if (token) cfg.headers.Authorization = `Bearer ${token}`
  return cfg
})

export const listOrders = async () => (await api.get('/orders')).data
export const createOrder = async (payload: { item: string; qty: number }) =>
  (await api.post('/orders', payload)).data
