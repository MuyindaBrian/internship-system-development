import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
        <div className="text-center mb-16">
          <h1 className="text-5xl font-bold text-gray-900 mb-4">
            University Internship System
          </h1>
          <p className="text-xl text-gray-600 mb-8">
            Manage internships and maintenance requests efficiently
          </p>
          <div className="flex gap-4 justify-center">
            <Link
              to="/internships"
              className="bg-primary text-white px-8 py-3 rounded-lg font-semibold hover:bg-blue-600 transition"
            >
              Browse Internships
            </Link>
            <Link
              to="/register"
              className="border-2 border-primary text-primary px-8 py-3 rounded-lg font-semibold hover:bg-blue-50 transition"
            >
              Get Started
            </Link>
          </div>
        </div>

        <div className="grid md:grid-cols-3 gap-8 mt-16">
          <div className="bg-white p-8 rounded-lg shadow-md hover:shadow-lg transition">
            <h3 className="text-2xl font-bold text-gray-900 mb-3">Find Internships</h3>
            <p className="text-gray-600">
              Browse and apply for internship positions at your university
            </p>
          </div>
          <div className="bg-white p-8 rounded-lg shadow-md hover:shadow-lg transition">
            <h3 className="text-2xl font-bold text-gray-900 mb-3">Request Maintenance</h3>
            <p className="text-gray-600">
              Submit and track maintenance requests for university facilities
            </p>
          </div>
          <div className="bg-white p-8 rounded-lg shadow-md hover:shadow-lg transition">
            <h3 className="text-2xl font-bold text-gray-900 mb-3">Track Status</h3>
            <p className="text-gray-600">
              Keep track of your applications and maintenance request status
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
