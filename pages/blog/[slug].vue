<template>
  <div v-if="post">
    <header
      id="top"
      class="ph art-h"
    >
      <div class="glow" />
      <div class="wrap">
        <div class="crumb">
          <NuxtLink to="/">
            Home
          </NuxtLink>
          <span>/</span>
          <NuxtLink to="/blog">
            Blog
          </NuxtLink>
          <span>/</span>
          <span>{{ post.title }}</span>
        </div>
        <div class="bd">
          <span class="ai">{{ post.tag }}</span>
        </div>
        <h1 v-html="articleTitle" />
        <p class="lead">
          {{ post.ex }}
        </p>
      </div>
    </header>

    <article class="post">
      <ContentRenderer :value="post" />
      <div class="end">
        <NuxtLink to="/blog">
          ← Back to blog
        </NuxtLink>
        <a href="#top">Back to top ↑</a>
      </div>
    </article>

    <div style="height: 100px" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'BlogArticle',

  setup() {
    const route = useRoute()
    const { data: post } = useAsyncData(`blog-${route.params.slug}`, () =>
      queryContent('blog', route.params.slug as string).findOne(),
    )

    return {
      post,
    }
  },

  head() {
    if (!this.post) return {}
    return {
      title: `${this.post.title} — Alex Mosneagu`,
      meta: [
        {
          name: 'description',
          content: this.post.ex,
        },
      ],
    }
  },

  computed: {
    articleTitle(): string {
      if (!this.post?.title) return ''
      if (this.post.slug === 'options-api-nuxt') {
        return 'Structuring a Nuxt project with the <em>Options API.</em>'
      }
      const parts = this.post.title.split(' ')
      const lastWord = parts.pop()
      return `${parts.join(' ')} <em>${lastWord}.</em>`
    },
  },
})
</script>

<style scoped>
.ph {
  padding: 170px 0 80px;
  position: relative;
  overflow: hidden;
}

.ph.art-h h1 {
  font-size: clamp(40px, 6.2vw, 96px);
  max-width: 1100px;
}

.glow {
  position: absolute;
  width: 900px;
  height: 520px;
  right: -200px;
  top: -220px;
  background: radial-gradient(closest-side, rgba(198, 255, 61, 0.22), transparent);
  filter: blur(40px);
}

.wrap {
  position: relative;
}

.crumb {
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  color: var(--mut);
  margin-bottom: 40px;
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.crumb a {
  color: var(--lime);
}

.crumb a:hover {
  text-decoration: underline;
}

.bd {
  margin-bottom: 0;
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.bd span {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  padding: 5px 10px;
  border-radius: 999px;
  border: 1px solid var(--line);
  color: #bbb;
  text-transform: uppercase;
}

.bd .ai {
  color: var(--lime);
  border-color: rgba(198, 255, 61, 0.4);
}

.ph h1 {
  line-height: 0.88;
  letter-spacing: -0.06em;
  font-weight: 700;
  margin: 26px 0 30px;
}

.ph h1 :deep(em) {
  color: var(--lime);
  letter-spacing: -0.03em;
}

.lead {
  font-size: clamp(19px, 2vw, 26px);
  line-height: 1.45;
  color: #bdbdbd;
  max-width: 860px;
  letter-spacing: -0.01em;
}

.post {
  max-width: 780px;
  margin: 0 auto;
  padding: 0 40px;
}

.post :deep(p) {
  font-size: 20px;
  line-height: 1.7;
  color: #c4c4c4;
  margin: 0 0 22px;
}

.post :deep(h2) {
  font-size: clamp(30px, 3.6vw, 44px);
  line-height: 1.05;
  letter-spacing: -0.045em;
  margin: 60px 0 20px;
}

.post :deep(code) {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85em;
  background: #1a1a1a;
  color: var(--lime);
  padding: 2px 7px;
  border-radius: 6px;
}

.post :deep(pre) {
  background: rgba(14, 14, 14, 0.9);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 20px 22px;
  margin: 8px 0 30px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 13.5px;
  line-height: 1.7;
  color: #d6d6d6;
  overflow-x: auto;
  white-space: pre;
}

.post :deep(pre code) {
  background: none;
  padding: 0;
  border-radius: 0;
  color: inherit;
}

.end {
  margin-top: 70px;
  padding-top: 26px;
  border-top: 1px solid var(--line);
  display: flex;
  justify-content: space-between;
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
}

.end a {
  color: var(--lime);
}

@media (max-width: 900px) {
  .ph {
    padding: 130px 0 50px;
  }

  .post {
    padding: 0 20px;
  }

  .post :deep(p) {
    font-size: 18px;
  }
}
</style>
