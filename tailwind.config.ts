import type { Config } from 'tailwindcss'

export default {
  content: [
    './components/**/*.{vue,js,ts}',
    './layouts/**/*.vue',
    './pages/**/*.vue',
    './composables/**/*.{js,ts}',
    './plugins/**/*.{js,ts}',
    './app.vue',
  ],
  theme: {
    extend: {
      colors: {
        bg: '#0B0B0B',
        lime: '#C6FF3D',
        fg: '#fff',
        mut: '#8a8a8a',
        line: 'rgba(255,255,255,.1)',
        card: '#121212',
      },
      fontFamily: {
        sans: ['Inter Tight', 'sans-serif'],
        serif: ['Instrument Serif', 'serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
    },
  },
  plugins: [],
} satisfies Config
