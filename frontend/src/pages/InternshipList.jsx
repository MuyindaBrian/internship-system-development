import { useState, useEffect } from 'react';
import { internshipsAPI } from '../services/api';

export default function InternshipList() {
  const [internships, setInternships] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchInternships = async () => {
      try {
        const response = await internshipsAPI.getAll();
        setInternships(response.results || []);
      } catch (err) {
        setError('Failed to load internships');
        console.error('Error:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchInternships();
  }, []);

  if (loading) {
    return (
      <div className="flex items-center justify-center h-screen">
        <p className="text-xl text-gray-600">Loading internships...</p>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      <h1 className="text-4xl font-bold text-gray-900 mb-2">Available Internships</h1>
      <p className="text-gray-600 mb-10">Browse and apply for internship positions</p>

      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg mb-6">
          {error}
        </div>
      )}

      {internships.length === 0 ? (
        <div className="bg-white p-8 rounded-lg shadow-md text-center">
          <p className="text-gray-600 text-lg">No internships available at the moment</p>
        </div>
      ) : (
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {internships.map((internship) => (
            <div
              key={internship.id}
              className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition"
            >
              <h3 className="text-xl font-bold text-gray-900 mb-2">{internship.title}</h3>
              <p className="text-gray-600 mb-4">{internship.description}</p>
              <div className="space-y-2 mb-4">
                <p className="text-sm text-gray-500">
                  <strong>Company:</strong> {internship.company}
                </p>
                <p className="text-sm text-gray-500">
                  <strong>Duration:</strong> {internship.duration}
                </p>
                <p className="text-sm text-gray-500">
                  <strong>Status:</strong>{' '}
                  <span className={internship.status === 'active' ? 'text-green-600' : 'text-gray-600'}>
                    {internship.status}
                  </span>
                </p>
              </div>
              <button className="w-full bg-primary text-white py-2 rounded-lg hover:bg-blue-600 transition">
                Apply Now
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
