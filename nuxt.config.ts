export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  
  devtools: { enabled: true },
  
  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxt/content',
    '@nuxt/fonts',
    '@nuxt/eslint'
  ],

  typescript: {
    strict: true,
    typeCheck: false
  },

  css: ['~/assets/css/main.css'],

  app: {
    head: {
      htmlAttrs: {
        lang: 'en'
      },
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' }
      ]
    }
  },

  content: {
    documentDriven: false,
    markdown: {
      anchorLinks: false
    }
  },

  fonts: {
    families: [
      { name: 'Inter Tight', provider: 'google', weights: [400, 500, 600, 700, 800] },
      { name: 'Instrument Serif', provider: 'google', weights: [400], styles: ['normal', 'italic'] },
      { name: 'JetBrains Mono', provider: 'google', weights: [400, 500] }
    ]
  },

  nitro: {
    prerender: {
      crawlLinks: true,
      routes: ['/'],
      failOnError: false
    }
  },

  runtimeConfig: {
    public: {
      siteUrl: process.env.NUXT_PUBLIC_SITE_URL || 'https://example.com'
    }
  },

  eslint: {
    config: {
      stylistic: true
    }
  }
})
