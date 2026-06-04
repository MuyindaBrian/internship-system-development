import { useState, useEffect } from 'react';
import { maintenanceAPI } from '../services/api';

export default function MaintenanceRequests() {
  const [requests, setRequests] = useState([]);
  const [formData, setFormData] = useState({
    room: '',
    issue: '',
  });
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  useEffect(() => {
    fetchRequests();
  }, []);

  const fetchRequests = async () => {
    try {
      const response = await maintenanceAPI.getAll();
      setRequests(response.data);
    } catch (err) {
      setError('Failed to load maintenance requests');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmitting(true);
    setError('');
    setSuccess('');

    try {
      await maintenanceAPI.create(formData);
      setSuccess('Maintenance request submitted successfully!');
      setFormData({ room: '', issue: '' });
      fetchRequests();
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to submit request');
      console.error('Error:', err);
    } finally {
      setSubmitting(false);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-screen">
        <p className="text-xl text-gray-600">Loading...</p>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      <h1 className="text-4xl font-bold text-gray-900 mb-2">Maintenance Requests</h1>
      <p className="text-gray-600 mb-10">Submit and track maintenance requests</p>

      <div className="grid md:grid-cols-3 gap-8">
        {/* Submit Form */}
        <div className="bg-white p-8 rounded-lg shadow-md">
          <h2 className="text-2xl font-bold text-gray-900 mb-6">Submit Request</h2>

          {error && (
            <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg mb-4">
              {error}
            </div>
          )}

          {success && (
            <div className="bg-green-50 border border-green-200 text-green-700 px-4 py-3 rounded-lg mb-4">
              {success}
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-gray-700 font-semibold mb-2">Room Number</label>
              <input
                type="text"
                name="room"
                value={formData.room}
                onChange={handleChange}
                required
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
                placeholder="e.g., 101"
              />
            </div>

            <div>
              <label className="block text-gray-700 font-semibold mb-2">Issue Description</label>
              <textarea
                name="issue"
                value={formData.issue}
                onChange={handleChange}
                required
                rows="4"
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
                placeholder="Describe the issue..."
              ></textarea>
            </div>

            <button
              type="submit"
              disabled={submitting}
              className="w-full bg-primary text-white py-2 rounded-lg font-semibold hover:bg-blue-600 transition disabled:opacity-50"
            >
              {submitting ? 'Submitting...' : 'Submit Request'}
            </button>
          </form>
        </div>

        {/* Requests List */}
        <div className="md:col-span-2 bg-white p-8 rounded-lg shadow-md">
          <h2 className="text-2xl font-bold text-gray-900 mb-6">Your Requests</h2>

          {requests.length === 0 ? (
            <p className="text-gray-500">No maintenance requests yet</p>
          ) : (
            <div className="space-y-4">
              {requests.map((request) => (
                <div
                  key={request.id}
                  className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition"
                >
                  <div className="flex justify-between items-start">
                    <div>
                      <h3 className="font-semibold text-gray-900">Room {request.room}</h3>
                      <p className="text-gray-600 mt-1">{request.issue}</p>
                      <p className="text-sm text-gray-500 mt-2">
                        Submitted: {new Date(request.created_at).toLocaleDateString()}
                      </p>
                    </div>
                    <span
                      className={`px-3 py-1 rounded-full text-sm font-semibold ${
                        request.status === 'completed'
                          ? 'bg-green-100 text-green-700'
                          : request.status === 'in_progress'
                          ? 'bg-yellow-100 text-yellow-700'
                          : 'bg-gray-100 text-gray-700'
                      }`}
                    >
                      {request.status}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
