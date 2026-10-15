export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',

  devtools: { enabled: true },

  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxt/content',
    '@nuxt/fonts',
    '@nuxt/eslint',
  ],

  typescript: {
    strict: true,
    typeCheck: false,
  },

  css: ['~/assets/css/main.css'],

  app: {
    head: {
      htmlAttrs: {
        lang: 'en',
      },
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      ],
    },
  },

  content: {
    documentDriven: false,
    markdown: {
      anchorLinks: false,
    },
  },

  fonts: {
    families: [
      { name: 'Inter Tight', provider: 'google', weights: [400, 500, 600, 700, 800] },
      { name: 'Instrument Serif', provider: 'google', weights: [400], styles: ['normal', 'italic'] },
      { name: 'JetBrains Mono', provider: 'google', weights: [400, 500] },
    ],
  },

  nitro: {
    prerender: {
      crawlLinks: true,
    },
  },

  hooks: {
    async 'nitro:config'(nitroConfig) {
      // Add content routes for prerendering
      const slugs = {
        ventures: ['liveflow', 'devolution-zone', 'old-studio-concept', 'let-go-trading'],
        projects: ['valconf', 'privasee360', 'luce-2025-shop', 'anteco-brun', 'nextservice', 'liveflow-academy'],
        rd: ['utilitara', 'one-cool-hub', 'nextservice', 'carpat', 'acttrace', 'ai-lead-generation', 'discrete-profile'],
      }

      const routes = [
        ...slugs.ventures.map(s => `/ventures/${s}`),
        ...slugs.projects.map(s => `/projects/${s}`),
        ...slugs.rd.map(s => `/rd/${s}`),
      ]

      nitroConfig.prerender = nitroConfig.prerender || {}
      nitroConfig.prerender.routes = nitroConfig.prerender.routes || []

      if (Array.isArray(nitroConfig.prerender.routes)) {
        nitroConfig.prerender.routes.push(...routes)
      }
    },
  },

  runtimeConfig: {
    public: {
      siteUrl: process.env.NUXT_PUBLIC_SITE_URL || 'https://example.com',
    },
  },

  eslint: {
    config: {
      stylistic: true,
    },
  },
})
