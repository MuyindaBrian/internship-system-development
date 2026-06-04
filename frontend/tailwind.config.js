/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        background: '#f8f9fa',
        foreground: '#1a1a1a',
        primary: '#3b82f6',
        secondary: '#8b5cf6',
        accent: '#ec4899',
      },
    },
  },
  plugins: [],
}
