export default function OrdersTable({ rows }: { rows: { item: string; qty: number }[] }) {
  return (
    <table role="table" style={{ marginTop: 16 }}>
      <thead><tr><th>Item</th><th>Qty</th></tr></thead>
      <tbody>
        {rows.map((r, i) => (
          <tr key={i}><td>{r.item}</td><td>{r.qty}</td></tr>
        ))}
      </tbody>
    </table>
  )
}
