/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/base/templates/*.{html,js}",
    "./src/app_rtchat/templates/*.{html,js}",
    "./src/**/*.{html,js}",

  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui'),
  ],
}