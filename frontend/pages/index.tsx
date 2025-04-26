import QueryForm from '../components/QueryForm';

export default function Home() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Clinical ZKP Research Portal</h1>
      <QueryForm />
    </div>
  );
}