import { QueryClient, QueryClientProvider, useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { listOrders, createOrder } from './api'
import OrdersTable from './OrdersTable'
import { useState } from 'react'

const qc = new QueryClient()

export default function App() {
  return (
    <QueryClientProvider client={qc}>
      <OrdersPage />
    </QueryClientProvider>
  )
}

function OrdersPage() {
  const { data, isLoading } = useQuery({ queryKey: ['orders'], queryFn: listOrders })
  const queryClient = useQueryClient()
  const [item, setItem] = useState('')
  const [qty, setQty] = useState(1)
  const [token, setToken] = useState(localStorage.getItem('token') || '')

  const mutation = useMutation({
    mutationFn: createOrder,
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['orders'] })
  })

  const saveToken = () => { localStorage.setItem('token', token); window.location.reload() }

  if (isLoading) return <p>Loading…</p>

  return (
    <div style={{ padding: 24 }}>
      <h2>Orders</h2>

      <fieldset style={{ marginBottom: 12 }}>
        <legend>Auth Token</legend>
        <input style={{ width: 400 }} value={token} onChange={e=>setToken(e.target.value)} placeholder="Paste JWT here" />
        <button onClick={saveToken} style={{ marginLeft: 8 }}>Save</button>
      </fieldset>

      <form onSubmit={(e) => { e.preventDefault(); mutation.mutate({ item, qty }) }}>
        <input value={item} onChange={e=>setItem(e.target.value)} placeholder="item" />
        <input type="number" value={qty} onChange={e=>setQty(Number(e.target.value))} />
        <button type="submit">Create</button>
      </form>
      <OrdersTable rows={data ?? []} />
    </div>
  )
}
