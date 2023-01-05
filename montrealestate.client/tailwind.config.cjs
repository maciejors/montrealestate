/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {},
	},
	plugins: [require('@tailwindcss/forms')],
	theme: {
		extend: {
			colors: {
				primary: '#034694',
				'primary-hover': '#033A80',
				'primary-active': '#022E61',
			},
			backgroundImage: {
				home: "url('https://picsum.photos/id/223/1920/1080')",
			},
		},
	},
};
