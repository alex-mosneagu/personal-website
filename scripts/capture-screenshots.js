import { chromium } from 'playwright-core'

const baseUrl = 'http://localhost:3001'

async function capture() {
  const browser = await chromium.launch({
    executablePath: '/usr/bin/google-chrome',
    args: [
      '--use-gl=angle',
      '--use-angle=swiftshader',
      '--enable-unsafe-swiftshader',
      '--ignore-gpu-blocklist',
    ],
  })

  try {
    // Desktop hero
    const heroPage = await browser.newPage({ viewport: { width: 1440, height: 900 } })
    await heroPage.goto(`${baseUrl}/?static`, { waitUntil: 'networkidle' })
    await heroPage.evaluate(() => document.fonts.ready)
    await heroPage.waitForSelector('body[data-gl=ok]', { state: 'attached', timeout: 20000 }).catch(() => {})
    // Wait longer for typing animation to complete
    await heroPage.waitForTimeout(3500)
    await heroPage.screenshot({ path: 'docs/screenshots/screenshot-desktop-hero.png' })
    console.log('✓ Desktop hero captured')

    // Desktop full page
    const height = await heroPage.evaluate(() => document.documentElement.scrollHeight)
    await heroPage.setViewportSize({ width: 1440, height })
    await heroPage.screenshot({ path: 'docs/screenshots/screenshot-desktop-full.png', fullPage: true })
    console.log('✓ Desktop full page captured')
    await heroPage.close()

    // Mobile full page
    const mobilePage = await browser.newPage({
      viewport: { width: 390, height: 844 },
      deviceScaleFactor: 2,
    })
    await mobilePage.goto(`${baseUrl}/?static`, { waitUntil: 'networkidle' })
    await mobilePage.waitForSelector('body[data-gl=ok]', { state: 'attached', timeout: 20000 }).catch(() => {})
    await mobilePage.waitForTimeout(1500)
    const mobileHeight = await mobilePage.evaluate(() => document.documentElement.scrollHeight)
    await mobilePage.setViewportSize({ width: 390, height: mobileHeight })
    await mobilePage.screenshot({ path: 'docs/screenshots/screenshot-mobile.png', fullPage: true })
    console.log('✓ Mobile full page captured')
    await mobilePage.close()

    // Project page
    const projectPage = await browser.newPage({ viewport: { width: 1440, height: 900 } })
    await projectPage.goto(`${baseUrl}/projects/valconf`, { waitUntil: 'networkidle' })
    await projectPage.waitForTimeout(800)
    const projectHeight = await projectPage.evaluate(() => document.documentElement.scrollHeight)
    await projectPage.setViewportSize({ width: 1440, height: projectHeight })
    await projectPage.screenshot({ path: 'docs/screenshots/screenshot-project-valconf.png', fullPage: true })
    console.log('✓ Project page captured')
    await projectPage.close()

    // Venture page
    const venturePage = await browser.newPage({ viewport: { width: 1440, height: 900 } })
    await venturePage.goto(`${baseUrl}/ventures/devolution-zone`, { waitUntil: 'networkidle' })
    await venturePage.waitForTimeout(800)
    const ventureHeight = await venturePage.evaluate(() => document.documentElement.scrollHeight)
    await venturePage.setViewportSize({ width: 1440, height: ventureHeight })
    await venturePage.screenshot({ path: 'docs/screenshots/screenshot-venture-devolution.png', fullPage: true })
    console.log('✓ Venture page captured')
    await venturePage.close()

    // Blog index
    const blogPage = await browser.newPage({ viewport: { width: 1440, height: 900 } })
    await blogPage.goto(`${baseUrl}/blog`, { waitUntil: 'networkidle' })
    await blogPage.waitForTimeout(800)
    const blogHeight = await blogPage.evaluate(() => document.documentElement.scrollHeight)
    await blogPage.setViewportSize({ width: 1440, height: blogHeight })
    await blogPage.screenshot({ path: 'docs/screenshots/screenshot-blog.png', fullPage: true })
    console.log('✓ Blog page captured')
    await blogPage.close()

    // Article page
    const articlePage = await browser.newPage({ viewport: { width: 1440, height: 900 } })
    await articlePage.goto(`${baseUrl}/blog/options-api-nuxt`, { waitUntil: 'networkidle' })
    await articlePage.waitForTimeout(800)
    const articleHeight = await articlePage.evaluate(() => document.documentElement.scrollHeight)
    await articlePage.setViewportSize({ width: 1440, height: articleHeight })
    await articlePage.screenshot({ path: 'docs/screenshots/screenshot-article.png', fullPage: true })
    console.log('✓ Article page captured')
    await articlePage.close()

    // R&D page
    const rdPage = await browser.newPage({ viewport: { width: 1440, height: 900 } })
    await rdPage.goto(`${baseUrl}/rd/discrete-profile`, { waitUntil: 'networkidle' })
    await rdPage.waitForTimeout(800)
    const rdHeight = await rdPage.evaluate(() => document.documentElement.scrollHeight)
    await rdPage.setViewportSize({ width: 1440, height: rdHeight })
    await rdPage.screenshot({ path: 'docs/screenshots/screenshot-rd-discrete.png', fullPage: true })
    console.log('✓ R&D page captured')
    await rdPage.close()

    console.log('\n✅ All screenshots captured successfully')
  }
  finally {
    await browser.close()
  }
}

capture().catch(console.error)
