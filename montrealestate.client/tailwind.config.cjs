/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],  theme: {
    extend: {},
  },
  plugins: [],
  theme: {
    extend: {
      colors: {
        'primary': '#034694',
        'primary-hover': '#033A80', 
        'primary-active': '#022E61', 
      },
    },
  },
}
