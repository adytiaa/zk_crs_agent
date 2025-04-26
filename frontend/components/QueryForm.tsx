import { useState } from 'react';

export default function QueryForm() {
  const [query, setQuery] = useState('');
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log('Query submitted:', query);
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-col space-y-4">
      <input
        type="text"
        className="border p-2"
        placeholder="Enter your statistical query..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button className="bg-blue-500 text-white p-2 rounded" type="submit">
        Submit Query
      </button>
    </form>
  );
}