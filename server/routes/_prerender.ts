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
    ...(ventures as ContentItem[]).map(v => `/ventures/${v.slug}`),
    ...(projects as ContentItem[]).map(p => `/projects/${p.slug}`),
    ...(rd as ContentItem[]).map(r => `/rd/${r.slug}`),
  ]

  return {
    routes,
  }
})
