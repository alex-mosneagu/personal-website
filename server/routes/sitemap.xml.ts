import { serverQueryContent } from '#content/server'

export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig()
  const siteUrl = config.public.siteUrl

  const [ventures, projects, rd, blog] = await Promise.all([
    serverQueryContent(event, 'ventures').find(),
    serverQueryContent(event, 'projects').find(),
    serverQueryContent(event, 'rd').find(),
    serverQueryContent(event, 'blog').where({ draft: { $ne: true } }).find(),
  ])

  const staticPages = [
    '',
    '/blog',
  ]

  const dynamicPages = [
    ...ventures.map((v: any) => `/ventures/${v.slug}`),
    ...projects.map((p: any) => `/projects/${p.slug}`),
    ...rd.map((r: any) => `/rd/${r.slug}`),
    ...blog.map((b: any) => `/blog/${b.slug}`),
  ]

  const allPages = [...staticPages, ...dynamicPages]

  const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${allPages.map(page => `  <url>
    <loc>${siteUrl}${page}</loc>
    <changefreq>monthly</changefreq>
    <priority>${page === '' ? '1.0' : '0.8'}</priority>
  </url>`).join('\n')}
</urlset>`

  setResponseHeader(event, 'Content-Type', 'application/xml')
  return sitemap
})
