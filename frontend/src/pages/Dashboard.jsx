import { useState, useEffect } from 'react';
import { internshipsAPI, maintenanceAPI } from '../services/api';

export default function Dashboard({ user }) {
  const [myInternships, setMyInternships] = useState([]);
  const [myMaintenance, setMyMaintenance] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [internshipsRes, maintenanceRes] = await Promise.all([
          internshipsAPI.getAll(),
          maintenanceAPI.getAll(),
        ]);
        setMyInternships(internshipsRes.results || []);
        setMyMaintenance(maintenanceRes.results || []);
      } catch (error) {
        console.error('Error fetching dashboard data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return <div className="flex items-center justify-center h-screen">Loading...</div>;
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      <h1 className="text-4xl font-bold text-gray-900 mb-2">Welcome, {user?.name || 'User'}!</h1>
      <p className="text-gray-600 mb-10">Here&apos;s your dashboard overview</p>

      <div className="grid md:grid-cols-2 gap-10">
        {/* My Internships */}
        <div className="bg-white p-8 rounded-lg shadow-md">
          <h2 className="text-2xl font-bold text-gray-900 mb-6">My Internships</h2>
          {myInternships.length === 0 ? (
            <p className="text-gray-500">No internships applied yet</p>
          ) : (
            <div className="space-y-4">
              {myInternships.map((internship) => (
                <div
                  key={internship.id}
                  className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition"
                >
                  <h3 className="font-semibold text-gray-900">{internship.title}</h3>
                  <p className="text-gray-600">{internship.description}</p>
                  <p className="text-sm text-gray-500 mt-2">Status: {internship.status}</p>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* My Maintenance Requests */}
        <div className="bg-white p-8 rounded-lg shadow-md">
          <h2 className="text-2xl font-bold text-gray-900 mb-6">My Maintenance Requests</h2>
          {myMaintenance.length === 0 ? (
            <p className="text-gray-500">No maintenance requests submitted</p>
          ) : (
            <div className="space-y-4">
              {myMaintenance.map((request) => (
                <div
                  key={request.id}
                  className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition"
                >
                  <h3 className="font-semibold text-gray-900">Room {request.room}</h3>
                  <p className="text-gray-600">{request.issue}</p>
                  <p className="text-sm text-gray-500 mt-2">Status: {request.status}</p>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
