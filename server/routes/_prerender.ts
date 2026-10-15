import { serverQueryContent } from '#content/server'

export default defineEventHandler(async (event) => {
  // This route is only used to provide additional routes for prerendering
  // It won't be accessible in the generated site
  
  const [ventures, projects, rd] = await Promise.all([
    serverQueryContent(event, 'ventures').find(),
    serverQueryContent(event, 'projects').find(),
    serverQueryContent(event, 'rd').find()
  ])
  
  const routes = [
    ...ventures.map((v: any) => `/ventures/${v.slug}`),
    ...projects.map((p: any) => `/projects/${p.slug}`),
    ...rd.map((r: any) => `/rd/${r.slug}`)
  ]
  
  return {
    routes
  }
})
