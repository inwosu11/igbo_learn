/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
  './templates/**/*.html',
  './vocab/templates/**/*.html',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Poppins', 'ui-sans-serif', 'system-ui'], // add font fallback
      },
      colors: {
        primary: '#6366F1',    // Indigo 500
        secondary: '#FACC15',  // Yellow 400
        accent: '#F43F5E',     // Rose 500
        success: '#10B981',    // Emerald 500
        info: '#06B6D4',       // Cyan 400
        bg: '#F9FAFB',         // Gray 50
        textbase: '#1F2937',   // Gray 800
      },
    },
  },
  plugins: [],
}

