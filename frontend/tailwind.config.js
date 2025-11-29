/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        urdu: {
          primary: '#1e40af',
          secondary: '#3b82f6',
          accent: '#10b981',
          dark: '#1f2937',
          light: '#f3f4f6',
        },
      },
      fontFamily: {
        urdu: ['Noto Nastaliq Urdu', 'serif'],
      },
    },
  },
  plugins: [],
}
