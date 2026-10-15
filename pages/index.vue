<template>
  <div>
    <header
      id="top"
      class="hero"
    >
      <ClientOnly>
        <HeroGL />
      </ClientOnly>
      <div class="hero-overlay" />
      <div class="wrap hero-content">
        <div class="hgrid">
          <div>
            <h1>
              Full stack.<br>Tech <em>lead.</em>
            </h1>
            <p>
              Frontend Tech Lead and full stack developer with 9+ years of Vue, Nuxt, TypeScript and React. I build products, and R&amp;D prototypes on the side.
            </p>
            <div class="ctas">
              <a
                href="#work"
                class="pill pri"
              >See my work →</a>
              <NuxtLink
                to="/blog"
                class="pill sec"
              >
                Read the blog
              </NuxtLink>
            </div>
          </div>
          <CodeTyping />
        </div>
        <div class="meta">
          <span>Based in <b>Bucharest, RO</b></span>
          <span>Stack <b>Vue · Nuxt · TS · React · Tailwind</b></span>
          <span>Shown at <b>Web Summit 2025 · We Make Future 2026</b></span>
          <span>Scroll <b>↓</b></span>
        </div>
      </div>
    </header>

    <div class="mq">
      <div>Vue <em>·</em> Nuxt <em>·</em> TypeScript <em>·</em> React <em>·</em> Tailwind <em>·</em> Tech leadership <em>·</em> R&amp;D <em>·</em> Vue <em>·</em> Nuxt <em>·</em> TypeScript <em>·</em> React <em>·</em> Tailwind <em>·</em> Tech leadership <em>·</em> R&amp;D <em>·</em></div>
    </div>

    <div class="wrap">
      <div class="stats">
        <div
          v-for="(stat, i) in stats"
          :key="i"
          class="stat"
        >
          <div
            class="n"
            :class="{ sm: stat.isText }"
            v-html="stat.value"
          />
          <div class="l">
            {{ stat.label }}
          </div>
        </div>
      </div>
    </div>

    <section id="about">
      <div class="wrap">
        <div class="sh">
          <div class="idx">
            // about<b>01</b>
          </div>
          <h2>Code that <em>ships.</em><br>Teams that scale.</h2>
          <p>Frontend Tech Lead &amp; full stack developer.</p>
        </div>
        <div class="about">
          <div v-html="aboutHtml" />
          <div class="sk">
            <div class="on">
              Frontend architecture<span>HCLTech</span>
            </div>
            <div>Code standards<span>reviews &amp; typing</span></div>
            <div>Testing strategy<span>unit &amp; E2E</span></div>
            <div>R&amp;D &amp; AI agents<span>LangGraph</span></div>
            <div>Languages<span>Romanian · Italian · English</span></div>
          </div>
        </div>
        <div class="chips">
          <span
            v-for="skill in skills"
            :key="skill"
            :class="{ f: featuredSkills.includes(skill) }"
          >
            {{ skill }}
          </span>
        </div>
      </div>
    </section>

    <section
      id="ventures"
      style="padding-top: 40px"
    >
      <div class="wrap">
        <div class="sh">
          <div class="idx">
            // ventures<b>02</b>
          </div>
          <h2>Ventures<br><em>I'm part of.</em></h2>
          <p>Four ventures, each with its own role. Drag / scroll →</p>
        </div>
      </div>
      <div class="hs">
        <NuxtLink
          v-for="(venture, i) in ventures || []"
          :key="venture.slug"
          :to="`/ventures/${venture.slug}`"
          class="vc"
          :class="{ l: venture.lime }"
        >
          <div class="top">
            <span>Venture 0{{ i + 1 }}</span>
            <span>{{ venture.place }}</span>
          </div>
          <h3 v-html="ventureTitle(venture)" />
          <div class="role">
            {{ venture.role }}
          </div>
          <p class="desc">
            {{ venture.desc }}
          </p>
          <div
            v-if="venture.products && venture.products.length"
            class="pr"
          >
            <span
              v-for="product in venture.products"
              :key="product"
            >{{ product }}</span>
          </div>
          <div class="foot">
            <span
              v-if="venture.badge"
              class="bdg"
            >◆ {{ venture.badge }}</span>
            <span
              v-else-if="venture.inactive"
              class="bdg in"
            >Inactive</span>
            <span v-else />
            <span class="go">View venture →</span>
          </div>
        </NuxtLink>
      </div>
    </section>

    <section id="work">
      <div class="wrap">
        <div class="sh">
          <div class="idx">
            // work<b>03</b>
          </div>
          <h2>Selected <em>projects.</em></h2>
          <p>Websites, e-commerce and platforms.</p>
        </div>
        <NuxtLink
          v-for="(project, i) in projects || []"
          :key="project.slug"
          :to="`/projects/${project.slug}`"
          class="row"
        >
          <span class="i">P/0{{ i + 1 }}</span>
          <div class="main">
            <h3>{{ project.name }}</h3>
            <p>{{ project.line }}</p>
          </div>
          <span class="t">{{ project.tag }}</span>
          <span class="go">View project →</span>
        </NuxtLink>
      </div>
    </section>

    <section id="rd">
      <div class="wrap">
        <div class="sh">
          <div class="idx">
            // r&amp;d<b>04</b>
          </div>
          <h2>R&amp;D <em>Lab.</em></h2>
          <p>Experiments from idea to proof of concept to market.</p>
        </div>
        <NuxtLink
          v-if="showcaseRD"
          :to="`/rd/${showcaseRD.slug}`"
          class="prod"
          style="color: inherit"
        >
          <div>
            <div class="bd">
              <span
                v-for="st in showcaseRD.st"
                :key="st"
                :class="badgeClass(st)"
              >{{ st }}</span>
            </div>
            <h3>Discrete <em>Profile</em></h3>
            <p class="lead">
              The first on-device marketing platform. An SDK that builds user profiles locally with machine learning.
            </p>
            <span class="more">Read more →</span>
          </div>
          <ul>
            <li
              v-for="(point, i) in rdPoints"
              :key="i"
            >
              {{ point }}
            </li>
            <li>Presented at Web Summit 2025</li>
          </ul>
        </NuxtLink>
        <div class="lab">
          <NuxtLink
            v-for="rd in labItems"
            :key="rd.slug"
            :to="`/rd/${rd.slug}`"
            class="lc"
          >
            <div class="bd">
              <span
                v-for="st in rd.st"
                :key="st"
                :class="badgeClass(st)"
              >{{ st }}</span>
            </div>
            <h4>{{ rd.name }}</h4>
            <p>{{ rd.desc }}</p>
          </NuxtLink>
        </div>
      </div>
    </section>

    <section id="journey">
      <div class="wrap">
        <div class="sh">
          <div class="idx">
            // journey<b>05</b>
          </div>
          <h2>The <em>journey.</em></h2>
          <p>9+ years, from custom PHP to modern SPAs.</p>
        </div>
        <div class="tl">
          <div
            v-for="(item, i) in journey"
            :key="i"
            class="it"
            :class="{ now: item.isNow }"
          >
            <div class="when">
              {{ item.when }}<small v-if="item.isEducation">Education</small>
            </div>
            <h3>
              {{ item.role }}<br><em>{{ item.company }}</em>
            </h3>
            <ul>
              <li
                v-for="(point, j) in item.items"
                :key="j"
              >
                {{ point }}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section id="writing">
      <div class="wrap">
        <div class="sh">
          <div class="idx">
            // blog<b>06</b>
          </div>
          <h2>Latest <em>articles.</em></h2>
          <p>Notes on frontend, R&amp;D and AI-assisted development.</p>
        </div>
        <div class="art">
          <NuxtLink
            v-for="post in blogPosts || []"
            :key="post.slug"
            :to="post.draft ? `/blog#${post.slug}` : `/blog/${post.slug}`"
            class="ar"
          >
            <div class="th">
              <b>{{ post.n }}</b>
              <span>{{ post.tag }}</span>
            </div>
            <div class="m">
              Article
            </div>
            <h4>{{ post.title }}</h4>
            <p>{{ post.ex }}</p>
          </NuxtLink>
        </div>
        <div
          class="ctas"
          style="margin-top: 50px"
        >
          <NuxtLink
            to="/blog"
            class="pill sec"
          >
            All articles →
          </NuxtLink>
        </div>
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import type { ParsedContent } from '@nuxt/content'

interface Stat {
  value: string
  label: string
  isText?: boolean
}

interface Journey {
  when: string
  company: string
  role: string
  isNow?: boolean
  isEducation?: boolean
  items: string[]
}

interface Venture extends ParsedContent {
  slug: string
  a: string
  b: string
  place: string
  role: string
  desc: string
  products?: string[]
  badge?: string
  inactive?: boolean
  lime?: boolean
  order: number
}

interface RDItem extends ParsedContent {
  slug: string
  name: string
  desc: string
  st: string[]
  showcase?: boolean
  order: number
}

export default defineComponent({
  name: 'IndexPage',

  setup() {
    const { data: aboutData } = useAsyncData('about', () => queryContent('about').findOne())
    const { data: statsData } = useAsyncData('stats', () => queryContent('stats').findOne())
    const { data: journeyData } = useAsyncData('journey', () => queryContent('journey').findOne())
    const { data: ventures } = useAsyncData('ventures', () => queryContent<Venture>('ventures').sort({ order: 1 }).find())
    const { data: projects } = useAsyncData('projects', () => queryContent('projects').sort({ order: 1 }).find())
    const { data: rdItems } = useAsyncData('rd', () => queryContent<RDItem>('rd').sort({ order: 1 }).find())
    const { data: blogPosts } = useAsyncData('blog', () => queryContent('blog').sort({ order: 1 }).find())

    return {
      aboutData,
      statsData,
      journeyData,
      ventures: ventures as Ref<Venture[] | null>,
      projects,
      rdItems: rdItems as Ref<RDItem[] | null>,
      blogPosts,
    }
  },

  data() {
    return {
      featuredSkills: ['Vue.js', 'Nuxt', 'TypeScript', 'React'],
      rdPoints: [
        'An SDK that builds user profiles locally with machine learning',
        'No server-side profile storage',
        'GDPR by design',
        'Targeting rules updated in real time from a control panel',
      ],
    }
  },

  head() {
    return {
      title: 'Alex Mosneagu — Frontend Tech Lead & Full Stack Developer',
      meta: [
        {
          name: 'description',
          content: 'Frontend Tech Lead and full stack developer with 9+ years of Vue, Nuxt, TypeScript and React. Building products and R&D prototypes.',
        },
      ],
    }
  },

  computed: {
    stats(): Stat[] {
      if (!this.statsData?.items) return []
      return this.statsData.items as unknown as Stat[]
    },

    journey(): Journey[] {
      if (!this.journeyData?.items) return []
      return this.journeyData.items as unknown as Journey[]
    },

    aboutHtml(): string {
      // Return hardcoded content from the about.md file
      return `<p><strong>9+ years</strong> building for the web, from custom PHP platforms and e-commerce to modern SPAs. <strong>Technical Lead Frontend at HCLTech</strong> since Jan 2025, working on frontend architecture, code standards and testing strategy.</p>
<p style="margin-top:22px">I care about <strong>clean, typed, well-tested code</strong>. I'm constantly in R&D mode: prototypes, frontend observability, browser-native tooling and AI agents with LangGraph. I design systems first, then build fast with AI-assisted development. I ran my own studio for years.</p>`
    },

    skills(): string[] {
      return this.aboutData?.skills || []
    },

    showcaseRD(): RDItem | null {
      if (!this.rdItems) return null
      return this.rdItems.find(item => item.showcase) || null
    },

    labItems(): RDItem[] {
      if (!this.rdItems) return []
      return this.rdItems.filter(item => !item.showcase)
    },
  },

  methods: {
    ventureTitle(venture: Venture): string {
      return `${venture.a}<em>${venture.b}</em>`
    },

    badgeClass(st: string): string {
      const map: Record<string, string> = {
        'POC': 'poc',
        'AI': 'ai',
        'On market': 'mk',
      }
      return map[st] || ''
    },
  },
})
</script>

<style scoped>
/* Hero */
.hero {
  min-height: 100vh;
  padding: 150px 0 40px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  position: relative;
}

.hero-overlay {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    180deg,
    rgba(11, 11, 11, 0.85) 0,
    transparent 30%,
    transparent 62%,
    var(--bg) 100%
  );
  pointer-events: none;
  z-index: 1;
}

.hero-content {
  position: relative;
  z-index: 2;
  width: 100%;
}

.hgrid {
  display: grid;
  grid-template-columns: 1fr 430px;
  gap: 40px;
  align-items: end;
}

.hero h1 {
  font-size: clamp(60px, 11.2vw, 184px);
  line-height: 0.84;
  letter-spacing: -0.065em;
  font-weight: 700;
  margin: 0 0 30px;
  mix-blend-mode: difference;
}

.hero h1 em {
  color: var(--lime);
  font-weight: 400;
  letter-spacing: -0.03em;
  mix-blend-mode: normal;
}

.hero p {
  font-size: 19px;
  color: #c4c4c4;
  max-width: 540px;
  line-height: 1.5;
}

.ctas {
  display: flex;
  gap: 12px;
  margin-top: 34px;
  flex-wrap: wrap;
}

.pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  border-radius: 999px;
  padding: 15px 26px;
  font-weight: 600;
  font-size: 15px;
  transition: 0.3s;
}

.pri {
  background: var(--lime);
  color: #0B0B0B;
}

.sec {
  border: 1px solid rgba(255, 255, 255, 0.25);
}

.meta {
  display: flex;
  justify-content: space-between;
  margin-top: 56px;
  font-size: 12px;
  color: var(--mut);
  border-top: 1px solid var(--line);
  padding-top: 18px;
  gap: 20px;
  flex-wrap: wrap;
  font-family: 'JetBrains Mono', monospace;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.meta b {
  color: #fff;
  font-weight: 500;
}

/* Marquee */
.mq {
  border-block: 1px solid var(--line);
  overflow: hidden;
  padding: 26px 0;
  background: var(--lime);
  color: #0B0B0B;
}

.mq div {
  display: flex;
  gap: 50px;
  white-space: nowrap;
  animation: marquee 30s linear infinite;
  font-size: 56px;
  font-weight: 700;
  letter-spacing: -0.04em;
  width: max-content;
}

.mq em {
  font-weight: 400;
}

@keyframes marquee {
  to {
    transform: translateX(-50%);
  }
}

/* Stats */
.stats {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  border-bottom: 1px solid var(--line);
}

.stat {
  padding: 56px 34px;
  border-right: 1px solid var(--line);
}

.stat:last-child {
  border: 0;
}

.stat .n {
  font-size: 96px;
  font-weight: 600;
  letter-spacing: -0.06em;
  line-height: 1;
}

.stat .n :deep(sup) {
  color: var(--lime);
  font-size: 0.5em;
}

.stat .n.sm {
  font-size: 34px;
  line-height: 1.05;
  letter-spacing: -0.03em;
}

.stat .n.sm :deep(em) {
  font-size: 1em;
}

.stat .l {
  color: var(--mut);
  margin-top: 14px;
  font-size: 13px;
  font-family: 'JetBrains Mono', monospace;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* Section common */
section {
  padding: 130px 0;
  position: relative;
}

.sh {
  display: grid;
  grid-template-columns: 140px 1fr 240px;
  gap: 30px;
  align-items: end;
  border-top: 1px solid var(--line);
  padding-top: 26px;
  margin-bottom: 64px;
}

.idx {
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  color: var(--lime);
  align-self: start;
}

.idx :deep(b) {
  display: block;
  font-size: 64px;
  font-weight: 400;
  color: #fff;
  line-height: 1;
  margin-top: 8px;
  letter-spacing: -0.04em;
}

h2 {
  font-size: clamp(46px, 7.4vw, 112px);
  line-height: 0.92;
  letter-spacing: -0.05em;
  font-weight: 600;
}

h2 em {
  color: var(--lime);
}

.sh p {
  color: var(--mut);
  max-width: 300px;
  font-size: 15px;
  line-height: 1.5;
}

/* About */
.about {
  display: grid;
  grid-template-columns: 1.3fr 1fr;
  gap: 80px;
}

.about :deep(p) {
  font-size: 26px;
  line-height: 1.45;
  color: #bdbdbd;
  letter-spacing: -0.01em;
}

.about :deep(p + p) {
  margin-top: 22px;
}

.about :deep(strong) {
  color: #fff;
  font-weight: 500;
}

.sk {
  border-top: 1px solid var(--line);
}

.sk div {
  display: flex;
  justify-content: space-between;
  padding: 18px 0;
  border-bottom: 1px solid var(--line);
  font-size: 20px;
}

.sk span {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  color: var(--mut);
  text-align: right;
  max-width: 55%;
}

.sk div.on {
  color: var(--lime);
}

.chips {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 70px;
}

.chips span {
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 11px 20px;
  font-size: 16px;
  color: #d6d6d6;
  background: var(--card);
  transition: 0.25s;
}

.chips span:hover {
  border-color: var(--lime);
  color: var(--lime);
}

.chips span.f {
  border-color: rgba(198, 255, 61, 0.45);
  color: var(--lime);
}

/* Ventures */
.hs {
  display: flex;
  gap: 20px;
  overflow-x: auto;
  padding: 0 40px 20px;
  padding-left: max(40px, calc(50vw - 620px));
  scroll-padding-left: max(40px, calc(50vw - 620px));
  scroll-snap-type: x mandatory;
  scrollbar-width: thin;
  cursor: grab;
}

.vc {
  flex: 0 0 560px;
  scroll-snap-align: start;
  border: 1px solid var(--line);
  border-radius: 26px;
  padding: 36px;
  background: var(--card);
  min-height: 500px;
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
  transition: transform 0.35s, border-color 0.3s;
  color: inherit;
}

.vc:hover {
  transform: translateY(-6px);
  border-color: rgba(198, 255, 61, 0.5);
}

.vc.l {
  background: var(--lime);
  color: #0B0B0B;
  border: 0;
}

.vc .top {
  display: flex;
  justify-content: space-between;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  opacity: 0.7;
}

.vc h3 {
  font-size: 64px;
  letter-spacing: -0.055em;
  font-weight: 700;
  line-height: 0.9;
  margin-top: 0;
  padding-top: 70px;
}

.vc h3 :deep(em) {
  font-weight: 400;
}

.vc .role {
  margin-top: 22px;
  opacity: 0.9;
  font-size: 13px;
  color: inherit;
  font-family: 'JetBrains Mono', monospace;
}

.vc.l .role {
  color: #0B0B0B;
}

.vc:not(.l) .role {
  color: var(--lime);
}

.vc .desc {
  margin-top: 12px;
  font-size: 17px;
  line-height: 1.5;
  opacity: 0.8;
  max-width: 440px;
}

.vc .pr {
  margin-top: 20px;
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.vc .pr span {
  font-size: 13px;
  padding: 6px 13px;
  border: 1px solid currentColor;
  border-radius: 999px;
}

.vc .foot {
  margin-top: auto;
  padding-top: 26px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}

.vc .go {
  font-weight: 600;
  font-size: 14px;
}

.vc:not(.l) .go {
  color: var(--lime);
}

.bdg {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 7px 12px;
  border-radius: 999px;
  background: var(--lime);
  color: #0B0B0B;
  font-weight: 500;
}

.vc.l .bdg {
  background: #0B0B0B;
  color: var(--lime);
}

.bdg.in {
  background: transparent;
  border: 1px solid rgba(255, 255, 255, 0.3);
  color: #bbb;
}

/* Work */
.row {
  display: grid;
  grid-template-columns: 90px 1fr 210px 130px;
  align-items: center;
  gap: 20px;
  padding: 34px 0;
  border-top: 1px solid var(--line);
  transition: 0.3s;
  color: inherit;
}

.row:last-child {
  border-bottom: 1px solid var(--line);
}

.row:hover {
  padding-left: 20px;
}

.row:hover h3 {
  color: var(--lime);
}

.row .i {
  font-family: 'JetBrains Mono', monospace;
  color: var(--mut);
  font-size: 13px;
}

.row h3 {
  font-size: clamp(34px, 4vw, 56px);
  letter-spacing: -0.05em;
  font-weight: 600;
}

.row .main p {
  color: var(--mut);
  margin-top: 10px;
  font-size: 16px;
  line-height: 1.45;
  max-width: 760px;
  letter-spacing: 0;
}

.row .t {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--mut);
}

.row .go {
  text-align: right;
  color: var(--lime);
  font-size: 14px;
}

/* R&D */
.prod {
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  gap: 60px;
  border: 1px solid rgba(198, 255, 61, 0.35);
  border-radius: 26px;
  padding: 48px;
  margin-bottom: 16px;
  background: linear-gradient(135deg, rgba(198, 255, 61, 0.09), transparent 60%), var(--card);
  position: relative;
  overflow: hidden;
  transition: 0.3s;
}

.prod h3 {
  font-size: clamp(44px, 5.4vw, 84px);
  letter-spacing: -0.05em;
  line-height: 0.92;
  font-weight: 700;
  margin: 22px 0 18px;
}

.prod h3 em {
  color: var(--lime);
}

.prod .lead {
  font-size: 20px;
  line-height: 1.5;
  color: #cfcfcf;
  max-width: 520px;
}

.prod ul {
  list-style: none;
  border-top: 1px solid var(--line);
  align-self: end;
}

.prod li {
  display: flex;
  gap: 14px;
  padding: 16px 0;
  border-bottom: 1px solid var(--line);
  font-size: 17px;
  color: #d6d6d6;
}

.prod li:before {
  content: '→';
  color: var(--lime);
  font-family: 'JetBrains Mono', monospace;
}

.prod .more {
  display: inline-block;
  margin-top: 26px;
  color: var(--lime);
  font-weight: 600;
  font-size: 14px;
}

.bd {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  margin-bottom: 0;
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

.bd .poc {
  color: #ffd23d;
  border-color: rgba(255, 210, 61, 0.4);
}

.bd .mk {
  background: var(--lime);
  color: #0B0B0B;
  border-color: var(--lime);
}

.bd .ai {
  color: var(--lime);
  border-color: rgba(198, 255, 61, 0.4);
}

.lab {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.lc {
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: 28px;
  min-height: 300px;
  display: flex;
  flex-direction: column;
  background: var(--card);
  transition: 0.3s;
  color: inherit;
}

.lc:hover {
  border-color: rgba(198, 255, 61, 0.5);
  transform: translateY(-4px);
}

.lc h4 {
  font-size: 30px;
  letter-spacing: -0.035em;
  font-weight: 600;
  margin-top: auto;
  line-height: 1.05;
  padding-top: 30px;
}

.lc p {
  font-size: 15px;
  line-height: 1.5;
  margin-top: 12px;
  color: var(--mut);
}

/* Journey */
.tl .it {
  display: grid;
  grid-template-columns: 240px 1fr 1fr;
  gap: 30px;
  padding: 40px 0;
  border-top: 1px solid var(--line);
}

.tl .it:last-child {
  border-bottom: 1px solid var(--line);
}

.tl .when {
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  color: var(--lime);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  line-height: 1.7;
}

.tl .when small {
  display: block;
  color: var(--mut);
  font-size: 12px;
}

.tl .it.now .when:after {
  content: '';
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--lime);
  margin-left: 10px;
  animation: blink 1.4s steps(1) infinite;
}

.tl h3 {
  font-size: clamp(30px, 3.4vw, 46px);
  letter-spacing: -0.045em;
  font-weight: 600;
  line-height: 1;
}

.tl h3 em {
  color: var(--lime);
}

.tl ul {
  list-style: none;
}

.tl li {
  padding: 11px 0;
  border-bottom: 1px solid var(--line);
  color: #bdbdbd;
  font-size: 17px;
  line-height: 1.4;
}

.tl li:first-child {
  padding-top: 0;
}

.tl li:last-child {
  border: 0;
}

/* Articles */
.art {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}

.ar {
  display: block;
  color: inherit;
}

.ar .th {
  aspect-ratio: 16/10;
  border-radius: 18px;
  background: repeating-linear-gradient(
      90deg,
      transparent 0 22px,
      rgba(198, 255, 61, 0.14) 22px 23px
    ),
    #141414;
  border: 1px solid var(--line);
  display: grid;
  place-items: center;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  color: var(--lime);
  padding: 16px;
  align-content: end;
  justify-items: start;
  text-align: left;
  transition: 0.3s;
}

.ar:hover .th {
  border-color: rgba(198, 255, 61, 0.5);
}

.ar:hover h4 {
  color: var(--lime);
}

.ar .th b {
  font-weight: 400;
  color: #fff;
  font-size: 44px;
  letter-spacing: -0.04em;
  font-family: 'Inter Tight', sans-serif;
  line-height: 1;
}

.ar .th span {
  display: block;
  margin-top: 8px;
}

.ar .m {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  color: var(--mut);
  margin: 20px 0 10px;
}

.ar h4 {
  font-size: 22px;
  letter-spacing: -0.03em;
  font-weight: 600;
  line-height: 1.18;
}

.ar p {
  color: var(--mut);
  font-size: 15px;
  line-height: 1.5;
  margin-top: 12px;
}

/* Responsive */
@media (max-width: 900px) {
  .hero {
    padding-top: 110px;
  }

  .hgrid,
  .about {
    grid-template-columns: 1fr;
    gap: 40px;
  }

  .meta {
    margin-top: 36px;
  }

  .stats {
    grid-template-columns: 1fr 1fr;
  }

  .stat {
    padding: 34px 20px;
    border-bottom: 1px solid var(--line);
  }

  .stat .n {
    font-size: 64px;
  }

  .stat .n.sm {
    font-size: 22px;
  }

  .sh {
    grid-template-columns: 1fr;
    gap: 16px;
  }

  .idx :deep(b) {
    font-size: 40px;
  }

  section {
    padding: 90px 0;
  }

  .hs {
    padding: 0 20px 20px;
  }

  .vc {
    flex-basis: 84vw;
    min-height: 440px;
    padding: 26px;
  }

  .vc h3 {
    font-size: 42px;
    padding-top: 50px;
  }

  .vc .desc {
    font-size: 15px;
  }

  .chips {
    margin-top: 44px;
  }

  .chips span {
    font-size: 14px;
    padding: 9px 15px;
  }

  .prod {
    grid-template-columns: 1fr;
    padding: 26px;
    gap: 30px;
  }

  .row {
    grid-template-columns: 44px 1fr;
    padding: 26px 0;
  }

  .row h3 {
    font-size: 34px;
  }

  .row .t,
  .row .go {
    grid-column: 2;
    text-align: left;
  }

  .lab,
  .art {
    grid-template-columns: 1fr;
  }

  .lc {
    min-height: 230px;
  }

  .tl .it {
    grid-template-columns: 1fr;
    gap: 16px;
    padding: 30px 0;
  }

  .tl .it ul {
    grid-column: 1;
  }

  .mq div {
    font-size: 34px;
  }

  .about :deep(p) {
    font-size: 20px;
  }
}
</style>
