export default defineEventHandler((event) => {
  const config = useRuntimeConfig()
  const siteUrl = config.public.siteUrl

  const robots = `User-agent: *
Allow: /

Sitemap: ${siteUrl}/sitemap.xml`

  setResponseHeader(event, 'Content-Type', 'text/plain')
  return robots
})
