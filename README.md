# Alex Mosneagu — Personal Website

Production-quality personal website built with Nuxt 4, featuring a three.js particle terrain hero, Options API architecture, and static generation for cPanel hosting.

## Features

- **Nuxt 4** with TypeScript strict mode and Options API
- **Three.js** animated particle terrain hero with mouse interaction
- **Nuxt Content** for managing ventures, projects, R&D items, and blog posts
- **Tailwind CSS** via Nuxt Tailwind module
- **Self-hosted fonts** using @nuxt/fonts (no runtime Google Fonts requests)
- **GSAP/ScrollTrigger** for smooth scroll animations
- **Static generation** (`nuxt generate`) for deployment on any static host
- **SEO** basics: per-page meta, sitemap, robots.txt, configurable canonical URLs
- **Accessibility**: semantic HTML, keyboard navigation, focus states, reduced-motion support
- **CI/CD**: GitHub Actions workflow for lint, typecheck, test, and build
- **Testing**: Vitest for unit tests
- **Linting**: ESLint + Prettier

## Tech Stack

- Vue 3 (Options API)
- Nuxt 4
- TypeScript (strict)
- Tailwind CSS
- Three.js
- GSAP
- Nuxt Content
- Vitest

## Getting Started

### Prerequisites

- Node.js 22+ (or compatible version)
- npm

### Installation

```bash
npm install
```

### Development

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view the site.

### Build

```bash
# Generate static site
npm run generate

# Preview the generated site
npm run preview
```

The static files will be in `.output/public/` and can be deployed to any static hosting provider.

### Linting & Type Checking

```bash
# Run ESLint
npm run lint

# Fix linting issues
npm run lint:fix

# Type check
npm run typecheck
```

### Testing

```bash
# Run tests
npm test

# Run tests in watch mode
npm run test:watch
```

## Adding Content

### Ventures

Create a new file in `content/ventures/[slug].md`:

```yaml
---
slug: my-venture
a: My
b: Venture
place: Location
role: Your Role
desc: Short description
products: []
badge: null
order: 5
---

Full description paragraph 1.

Full description paragraph 2.
```

### Projects

Create a new file in `content/projects/[slug].md`:

```yaml
---
slug: my-project
name: My Project
tag: Category · Tech
cat: Category
line: One-line description
facts:
  - [Type, Project Type]
  - [Client, Client Name]
  - [Tech, Technology]
  - ['—', '']
feats:
  - Feature 1
  - Feature 2
  - Feature 3
order: 7
---

Project description paragraph 1.

Project description paragraph 2.
```

### R&D Items

Create a new file in `content/rd/[slug].md`:

```yaml
---
slug: my-rd-item
name: My R&D Project
st:
  - POC
  - AI
desc: Short description
order: 8
---

Full description.
```

### Blog Posts

Create a new file in `content/blog/[slug].md`:

```yaml
---
slug: my-post
n: '05'
tag: Category · Subtag
title: My Post Title
ex: Excerpt for the post
draft: false
order: 5
---

Your article content in Markdown.

## Heading

More content here.
```

To mark a post as "Coming soon", set `draft: true`.

## Deployment

### Static Hosting (cPanel, Netlify, Vercel, etc.)

1. Set the `NUXT_PUBLIC_SITE_URL` environment variable to your production URL:

```bash
export NUXT_PUBLIC_SITE_URL=https://yourdomain.com
```

2. Generate the static site:

```bash
npm run generate
```

3. Upload the contents of `.output/public/` to your hosting provider.

### Environment Variables

- `NUXT_PUBLIC_SITE_URL`: Your site's canonical URL (used for sitemap and SEO)

## Project Structure

```
.
├── assets/          # Global CSS
├── components/      # Vue components (Options API)
├── composables/     # Reusable logic
├── content/         # Content files (Markdown/YAML)
├── layouts/         # Layout components
├── pages/           # Route pages
├── public/          # Static assets
├── server/          # Server routes (sitemap, robots.txt)
├── tests/           # Vitest tests
├── types/           # TypeScript types
└── utils/           # Utility functions
```

## Important Notes

- **Options API**: All Vue components use the Options API (not Composition API or `<script setup>`)
- **No External Links**: The site contains only internal links (no LinkedIn, GitHub, mailto, etc.)
- **Web Summit Date**: Discrete Profile was presented at Web Summit **2025** in Portugal (not 2024)
- **Three.js Hero**: Automatically reduces particle count on mobile and respects `prefers-reduced-motion`
- **Draft Posts**: Blog posts marked as `draft: true` are listed as "Coming soon" on the blog index and do not have individual pages

## License

© 2026 Alex Mosneagu
