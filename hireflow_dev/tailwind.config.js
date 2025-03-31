/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,jsx,ts,tsx}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      },
      colors: {
        'buttonpair-purple': '#5e72e5',
        'buttonpair-black': '#182b4d',
        default: '#0983ff',
      },
    },
  },
  plugins: [],
}
