<template>
  <div>
    <header
      id="top"
      class="ph"
    >
      <div class="glow" />
      <div class="wrap">
        <div class="crumb">
          <NuxtLink to="/">
            Home
          </NuxtLink>
          <span>/</span>
          <span>Blog</span>
        </div>
        <div
          class="idx"
          style="font-family: 'JetBrains Mono', monospace; font-size: 13px; color: var(--lime)"
        >
          // blog
        </div>
        <h1>Notes &amp; <em>articles.</em></h1>
        <p class="lead">
          Writing about frontend, R&amp;D and AI-assisted development.
        </p>
      </div>
    </header>

    <section style="padding: 20px 0 60px">
      <div class="wrap">
        <NuxtLink
          v-for="post in posts"
          :id="post.soon ? post.slug : undefined"
          :key="post.slug"
          :to="post.soon ? `#${post.slug}` : `/blog/${post.slug}`"
          class="brow"
        >
          <span class="i">{{ post.n }}</span>
          <div>
            <h3>{{ post.title }}</h3>
            <p>{{ post.ex }}</p>
          </div>
          <span class="t">{{ post.tag }}</span>
          <span
            class="go"
            :class="{ s: post.soon }"
          >
            {{ post.soon ? 'Coming soon' : 'Read article →' }}
          </span>
        </NuxtLink>
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'BlogPage',

  setup() {
    const { data: posts } = useAsyncData('blog-posts', () =>
      queryContent('blog').sort({ order: 1 }).find(),
    )

    return {
      posts,
    }
  },

  head() {
    return {
      title: 'Blog — Alex Mosneagu',
      meta: [
        {
          name: 'description',
          content: 'Writing about frontend, R&D and AI-assisted development.',
        },
      ],
    }
  },
})
</script>

<style scoped>
.ph {
  padding: 170px 0 80px;
  position: relative;
  overflow: hidden;
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

.ph h1 {
  font-size: clamp(52px, 9vw, 148px);
  line-height: 0.88;
  letter-spacing: -0.06em;
  font-weight: 700;
  margin: 26px 0 30px;
}

.ph h1 em {
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

.brow {
  display: grid;
  grid-template-columns: 90px 1fr 190px 120px;
  gap: 20px;
  align-items: center;
  padding: 38px 0;
  border-top: 1px solid var(--line);
  transition: 0.3s;
  color: inherit;
}

.brow:last-child {
  border-bottom: 1px solid var(--line);
}

.brow:hover {
  padding-left: 20px;
}

.brow:hover h3 {
  color: var(--lime);
}

.brow .i {
  font-family: 'JetBrains Mono', monospace;
  color: var(--mut);
  font-size: 13px;
}

.brow h3 {
  font-size: clamp(28px, 3.4vw, 46px);
  letter-spacing: -0.045em;
  font-weight: 600;
  line-height: 1.05;
}

.brow p {
  color: var(--mut);
  margin-top: 12px;
  font-size: 17px;
  line-height: 1.5;
  max-width: 760px;
}

.brow .t {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  color: var(--mut);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.brow .go {
  text-align: right;
  color: var(--lime);
  font-size: 14px;
}

.brow .go.s {
  color: var(--mut);
}

@media (max-width: 900px) {
  .ph {
    padding: 130px 0 50px;
  }

  .brow {
    grid-template-columns: 44px 1fr;
    padding: 28px 0;
  }

  .brow .t,
  .brow .go {
    grid-column: 2;
    text-align: left;
  }
}
</style>
