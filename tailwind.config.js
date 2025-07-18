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
      }
    },
  },
  plugins: [],
}

