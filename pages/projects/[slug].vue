<template>
  <div v-if="project">
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
          <NuxtLink to="/#work">
            Work
          </NuxtLink>
          <span>/</span>
          <span>{{ project.name }}</span>
        </div>
        <div class="bd">
          <span class="ai">{{ project.cat }}</span>
        </div>
        <h1>{{ project.name }}</h1>
        <p class="lead">
          {{ project.line }}
        </p>
        <div class="facts">
          <div
            v-for="(fact, i) in displayFacts"
            :key="i"
          >
            <span>{{ fact[0] }}</span>
            <b>{{ fact[1] }}</b>
          </div>
        </div>
        <div
          v-if="project.slug === 'valconf'"
          class="frame"
        >
          <div class="bar">
            <i /><i /><i />
            <span>ValConf — hero</span>
          </div>
          <div class="vid">
            <div class="play">
              ▶
            </div>
            <h5>Val<em>Conf</em></h5>
            <small>Full-screen video hero · Editorial design</small>
          </div>
        </div>
      </div>
    </header>

    <section class="sx">
      <div class="wrap">
        <div class="txt">
          <div class="idx">
            // overview<b>01</b>
          </div>
          <div class="body">
            <ContentRenderer
              v-if="project && project.body"
              :value="project"
            />
          </div>
        </div>
      </div>
    </section>

    <section class="sx">
      <div class="wrap">
        <div class="txt">
          <div class="idx">
            // highlights<b>02</b>
          </div>
          <div>
            <div
              v-if="project && project.feats"
              class="feat"
              style="margin-top: 0"
            >
              <div
                v-for="(feat, i) in project.feats"
                :key="i"
              >
                <span>0{{ i + 1 }}</span>
                <h4>{{ feat }}</h4>
              </div>
            </div>
          </div>
        </div>
        <div
          v-if="prevProject && nextProject"
          class="pn"
        >
          <NuxtLink :to="`/projects/${prevProject.slug}`">
            <span>← Previous</span>
            <b>{{ prevProject.name }}</b>
          </NuxtLink>
          <NuxtLink :to="`/projects/${nextProject.slug}`">
            <span>Next →</span>
            <b>{{ nextProject.name }}</b>
          </NuxtLink>
        </div>
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import type { ParsedContent } from '@nuxt/content'

interface Project extends ParsedContent {
  slug: string
  name: string
  tag: string
  cat: string
  line: string
  facts?: Array<[string, string]>
  feats?: string[]
  order: number
}

export default defineComponent({
  name: 'ProjectPage',

  setup() {
    const route = useRoute()
    const { data: project } = useAsyncData(`project-${route.params.slug}`, () =>
      queryContent<Project>('projects', route.params.slug as string).findOne(),
    )

    const { data: allProjects } = useAsyncData('all-projects', () =>
      queryContent<Project>('projects').sort({ order: 1 }).find(),
    )

    return {
      project: project as Ref<Project | null>,
      allProjects: allProjects as Ref<Project[] | null>,
    }
  },

  head() {
    if (!this.project) return {}
    return {
      title: `${this.project.name} — Alex Mosneagu`,
      meta: [
        {
          name: 'description',
          content: this.project.line,
        },
      ],
    }
  },

  computed: {
    displayFacts(): Array<[string, string]> {
      if (!this.project || !this.project.facts) return []
      const facts = this.project.facts.filter((f: [string, string]) => f[0] !== '—')
      if (facts.length < 4) {
        facts.push(['Category', this.project.cat])
      }
      return facts
    },

    currentIndex(): number {
      if (!this.project || !this.allProjects) return 0
      return this.allProjects.findIndex(p => p.slug === this.project!.slug)
    },

    prevProject(): Project | null {
      if (!this.allProjects?.length) return null
      const prevIndex = this.currentIndex - 1
      return this.allProjects[prevIndex < 0 ? this.allProjects.length - 1 : prevIndex] || null
    },

    nextProject(): Project | null {
      if (!this.allProjects?.length) return null
      const nextIndex = this.currentIndex + 1
      return this.allProjects[nextIndex >= this.allProjects.length ? 0 : nextIndex] || null
    },
  },

  methods: {
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

.lead {
  font-size: clamp(19px, 2vw, 26px);
  line-height: 1.45;
  color: #bdbdbd;
  max-width: 860px;
  letter-spacing: -0.01em;
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

.facts {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  border-block: 1px solid var(--line);
  margin-top: 70px;
}

.facts div {
  padding: 26px 28px 28px 0;
  border-right: 1px solid var(--line);
  padding-left: 28px;
}

.facts div:first-child {
  padding-left: 0;
}

.facts div:last-child {
  border: 0;
}

.facts span {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  color: var(--mut);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.facts b {
  display: block;
  font-weight: 500;
  font-size: 20px;
  margin-top: 10px;
  letter-spacing: -0.02em;
  line-height: 1.25;
}

.frame {
  margin-top: 50px;
  border: 1px solid var(--line);
  border-radius: 22px;
  overflow: hidden;
  background: #0e0e0e;
}

.frame .bar {
  display: flex;
  gap: 7px;
  padding: 12px 16px;
  border-bottom: 1px solid var(--line);
  align-items: center;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  color: var(--mut);
}

.frame .bar i {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #2a2a2a;
}

.frame .bar i:first-child {
  background: var(--lime);
}

.frame .bar span {
  margin-left: auto;
}

.frame .vid {
  aspect-ratio: 16/8;
  position: relative;
  overflow: hidden;
  background: radial-gradient(120% 100% at 30% 100%, rgba(198, 255, 61, 0.22), transparent 60%),
    repeating-linear-gradient(90deg, transparent 0 46px, rgba(198, 255, 61, 0.07) 46px 47px), #0c0c0c;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: clamp(20px, 4vw, 56px);
}

.frame .vid:before {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  height: 140px;
  top: -140px;
  background: linear-gradient(180deg, transparent, rgba(198, 255, 61, 0.14), transparent);
  animation: scan 5s linear infinite;
}

@keyframes scan {
  to {
    top: 100%;
  }
}

.frame .play {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 84px;
  height: 84px;
  margin: -42px;
  border-radius: 50%;
  border: 1px solid rgba(198, 255, 61, 0.6);
  display: grid;
  place-items: center;
  color: var(--lime);
  font-size: 24px;
  padding-left: 5px;
}

.frame .vid h5 {
  font-size: clamp(34px, 6vw, 96px);
  font-weight: 700;
  letter-spacing: -0.06em;
  line-height: 0.9;
  position: relative;
}

.frame .vid h5 em {
  color: var(--lime);
}

.frame .vid small {
  font-family: 'JetBrains Mono', monospace;
  color: var(--mut);
  font-size: 12px;
  margin-top: 14px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  position: relative;
}

.sx {
  padding: 100px 0 40px;
}

.txt {
  display: grid;
  grid-template-columns: 140px 1fr;
  gap: 30px;
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

.body :deep(p) {
  font-size: 26px;
  line-height: 1.45;
  color: #bdbdbd;
  letter-spacing: -0.015em;
  max-width: 900px;
}

.body :deep(p + p) {
  margin-top: 20px;
}

.feat {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin-top: 40px;
}

.feat div {
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: 28px;
  background: var(--card);
  min-height: 200px;
  display: flex;
  flex-direction: column;
}

.feat span {
  font-family: 'JetBrains Mono', monospace;
  color: var(--lime);
  font-size: 13px;
}

.feat h4 {
  font-size: 26px;
  letter-spacing: -0.035em;
  font-weight: 600;
  margin-top: auto;
  line-height: 1.1;
}

.pn {
  display: grid;
  grid-template-columns: 1fr 1fr;
  border-block: 1px solid var(--line);
  margin-top: 100px;
}

.pn a {
  padding: 40px 0;
  display: block;
  transition: 0.3s;
  color: inherit;
}

.pn a:last-child {
  text-align: right;
  border-left: 1px solid var(--line);
  padding-left: 40px;
}

.pn a:first-child {
  padding-right: 40px;
}

.pn span {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  color: var(--mut);
  text-transform: uppercase;
}

.pn b {
  display: block;
  font-size: clamp(28px, 3.6vw, 52px);
  letter-spacing: -0.05em;
  font-weight: 600;
  margin-top: 10px;
}

.pn a:hover b {
  color: var(--lime);
}

@media (max-width: 900px) {
  .ph {
    padding: 130px 0 50px;
  }

  .facts {
    grid-template-columns: 1fr 1fr;
  }

  .facts div {
    padding: 20px 16px 20px 0;
    border-bottom: 1px solid var(--line);
  }

  .facts div:nth-child(2n) {
    padding-left: 20px;
    border-right: 0;
  }

  .facts div:nth-child(odd) {
    padding-left: 0;
  }

  .frame .play {
    width: 60px;
    height: 60px;
    margin: -30px;
  }

  .txt {
    grid-template-columns: 1fr;
    gap: 16px;
  }

  .body :deep(p) {
    font-size: 20px;
  }

  .feat {
    grid-template-columns: 1fr;
  }

  .pn {
    grid-template-columns: 1fr;
  }

  .pn a:last-child {
    border-left: 0;
    border-top: 1px solid var(--line);
    text-align: left;
    padding-left: 0;
  }

  .pn a:first-child {
    padding-right: 0;
  }

  .sx {
    padding: 70px 0 20px;
  }
}
</style>
