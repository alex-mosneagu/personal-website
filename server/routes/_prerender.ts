import type { ParsedContent } from '@nuxt/content'
import { serverQueryContent } from '#content/server'

interface ContentItem extends ParsedContent {
  slug: string
}

export default defineEventHandler(async (event) => {
  // This route is only used to provide additional routes for prerendering
  // It won't be accessible in the generated site

  const [ventures, projects, rd] = await Promise.all([
    serverQueryContent(event, 'ventures').find(),
    serverQueryContent(event, 'projects').find(),
    serverQueryContent(event, 'rd').find(),
  ])

  const routes = [
    ...ventures.map((v: ContentItem) => `/ventures/${v.slug}`),
    ...projects.map((p: ContentItem) => `/projects/${p.slug}`),
    ...rd.map((r: ContentItem) => `/rd/${r.slug}`),
  ]

  return {
    routes,
  }
})
