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
          <NuxtLink to="/#rd">
            R&amp;D
          </NuxtLink>
          <span>/</span>
          <span>{{ rd.name }}</span>
        </div>
        <div class="bd">
          <span
            v-for="st in rd.st"
            :key="st"
            :class="badgeClass(st)"
          >{{ st }}</span>
        </div>
        <h1 :style="{ fontSize: titleSize }">
          {{ rd.name }}
        </h1>
        <p class="lead">
          {{ rd.desc }}
        </p>
        <div
          class="facts"
          style="grid-template-columns: repeat(3, 1fr)"
        >
          <div
            v-for="(fact, i) in facts"
            :key="i"
          >
            <span>{{ fact.label }}</span>
            <b>{{ fact.value }}</b>
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
              v-if="rd && rd.body"
              :value="rd"
            />
          </div>
        </div>
      </div>
    </section>

    <section
      v-if="rd.slug === 'discrete-profile'"
      class="sx"
    >
      <div class="wrap">
        <div class="txt">
          <div class="idx">
            // how it works<b>02</b>
          </div>
          <div>
            <div
              v-if="rd && rd.points"
              class="feat"
              style="margin-top: 0; grid-template-columns: repeat(2, 1fr)"
            >
              <div
                v-for="(point, i) in rd.points"
                :key="i"
              >
                <span>0{{ i + 1 }}</span>
                <h4>{{ point }}</h4>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="sx">
      <div class="wrap">
        <div
          v-if="prevRD && nextRD"
          class="pn"
        >
          <NuxtLink :to="`/rd/${prevRD.slug}`">
            <span>← Previous</span>
            <b>{{ prevRD.name }}</b>
          </NuxtLink>
          <NuxtLink :to="`/rd/${nextRD.slug}`">
            <span>Next →</span>
            <b>{{ nextRD.name }}</b>
          </NuxtLink>
        </div>
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'RDPage',

  setup() {
    const route = useRoute()
    const { data: rd } = useAsyncData(`rd-${route.params.slug}`, () =>
      queryContent('rd', route.params.slug as string).findOne(),
    )

    const { data: allRD } = useAsyncData('all-rd', () =>
      queryContent('rd').sort({ order: 1 }).find(),
    )

    return {
      rd,
      allRD,
    }
  },

  head() {
    if (!this.rd) return {}
    return {
      title: `${this.rd.name} — Alex Mosneagu`,
      meta: [
        {
          name: 'description',
          content: this.rd.desc,
        },
      ],
    }
  },

  computed: {
    titleSize(): string {
      if (!this.rd) return 'clamp(44px, 9vw, 148px)'
      return this.rd.name.length > 20
        ? 'clamp(44px, 6vw, 96px)'
        : 'clamp(44px, 9vw, 148px)'
    },

    facts(): Array<{ label: string, value: string }> {
      if (!this.rd) return []
      return [
        { label: 'Status', value: this.rd.st.join(' · ') },
        { label: 'Type', value: this.rd.slug === 'discrete-profile' ? 'Product' : 'R&D project' },
        { label: 'Section', value: 'R&D Lab' },
      ]
    },

    currentIndex(): number {
      if (!this.rd || !this.allRD) return 0
      return this.allRD.findIndex((r: any) => r.slug === this.rd.slug)
    },

    prevRD(): any {
      if (!this.allRD?.length) return null
      const prevIndex = this.currentIndex - 1
      return this.allRD[prevIndex < 0 ? this.allRD.length - 1 : prevIndex]
    },

    nextRD(): any {
      if (!this.allRD?.length) return null
      const nextIndex = this.currentIndex + 1
      return this.allRD[nextIndex >= this.allRD.length ? 0 : nextIndex]
    },
  },

  methods: {
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

.ph h1 {
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

.facts {
  display: grid;
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
