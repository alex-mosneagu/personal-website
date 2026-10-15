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
          <NuxtLink to="/#ventures">
            Ventures
          </NuxtLink>
          <span>/</span>
          <span>{{ ventureName }}</span>
        </div>
        <div class="bd">
          <span class="ai">Venture {{ ventureNumber }}</span>
        </div>
        <h1 v-html="ventureTitle" />
        <p class="lead">
          {{ venture.desc }}
        </p>
        <span
          v-if="venture.badge"
          class="bdg"
          style="margin-top: 26px"
        >◆ {{ venture.badge }}</span>
        <span
          v-else-if="venture.inactive"
          class="bdg in"
          style="margin-top: 26px"
        >Inactive</span>
        <div class="facts">
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
            // about<b>01</b>
          </div>
          <div class="body">
            <ContentRenderer
              v-if="venture && venture.body"
              :value="venture"
            />
          </div>
        </div>
      </div>
    </section>

    <section
      v-if="venture.products && venture.products.length"
      class="sx"
    >
      <div class="wrap">
        <div class="txt">
          <div class="idx">
            // products<b>02</b>
          </div>
          <div>
            <div
              v-if="venture && venture.products"
              class="pcards"
              style="margin-top: 0"
            >
              <NuxtLink
                v-for="product in venture.products"
                :key="product"
                :to="productLink(product)"
                :class="['lc', { 'pointer-events-none': !productLink(product) }]"
              >
                <div class="bd">
                  <span class="mk">Product</span>
                </div>
                <h4>{{ product }}</h4>
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="sx">
      <div class="wrap">
        <div
          v-if="prevVenture && nextVenture"
          class="pn"
        >
          <NuxtLink :to="`/ventures/${prevVenture.slug}`">
            <span>← Previous</span>
            <b>{{ prevVenture.a + prevVenture.b }}</b>
          </NuxtLink>
          <NuxtLink :to="`/ventures/${nextVenture.slug}`">
            <span>Next →</span>
            <b>{{ nextVenture.a + nextVenture.b }}</b>
          </NuxtLink>
        </div>
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'VenturePage',

  setup() {
    const route = useRoute()
    const { data: venture } = useAsyncData(`venture-${route.params.slug}`, () =>
      queryContent('ventures', route.params.slug as string).findOne(),
    )

    const { data: allVentures } = useAsyncData('all-ventures', () =>
      queryContent('ventures').sort({ order: 1 }).find(),
    )

    return {
      venture,
      allVentures,
    }
  },

  head() {
    if (!this.venture) return {}
    return {
      title: `${this.venture.a}${this.venture.b} — Alex Mosneagu`,
      meta: [
        {
          name: 'description',
          content: this.venture.desc,
        },
      ],
    }
  },

  computed: {
    ventureTitle(): string {
      if (!this.venture) return ''
      return `${this.venture.a}<em>${this.venture.b}</em>`
    },

    ventureName(): string {
      if (!this.venture) return ''
      return this.venture.a + this.venture.b
    },

    ventureNumber(): string {
      if (!this.venture || !this.allVentures) return '01 of 04'
      const index = this.allVentures.findIndex((v: any) => v.slug === this.venture.slug)
      return `0${index + 1} of 04`
    },

    facts(): Array<{ label: string, value: string }> {
      if (!this.venture) return []
      const facts = [
        { label: 'Role', value: this.venture.role },
        {
          label: this.venture.place === 'Italy' ? 'Country' : 'Type',
          value: this.venture.place,
        },
      ]

      if (this.venture.inactive) {
        facts.push({ label: 'Status', value: 'Inactive' })
      }
      else if (this.allVentures) {
        const index = this.allVentures.findIndex((v: any) => v.slug === this.venture.slug)
        facts.push({ label: 'Venture', value: `0${index + 1} of 04` })
      }

      if (this.venture.products && this.venture.products.length) {
        facts.push({ label: 'Products', value: this.venture.products.join(' · ') })
      }
      else if (this.venture.badge) {
        facts.push({ label: 'Showcased', value: this.venture.badge })
      }
      else if (this.venture.desc) {
        facts.push({
          label: 'Focus',
          value: this.venture.desc.replace(' The studio is currently inactive', '').replace(/\.$/, ''),
        })
      }

      return facts
    },

    currentIndex(): number {
      if (!this.venture || !this.allVentures) return 0
      return this.allVentures.findIndex((v: any) => v.slug === this.venture.slug)
    },

    prevVenture(): any {
      if (!this.allVentures?.length) return null
      const prevIndex = this.currentIndex - 1
      return this.allVentures[prevIndex < 0 ? this.allVentures.length - 1 : prevIndex]
    },

    nextVenture(): any {
      if (!this.allVentures?.length) return null
      const nextIndex = this.currentIndex + 1
      return this.allVentures[nextIndex >= this.allVentures.length ? 0 : nextIndex]
    },
  },

  methods: {
    productLink(product: string): string {
      if (product === 'Discrete Profile') return '/rd/discrete-profile'
      if (product === 'LiveFlow Academy') return '/projects/liveflow-academy'
      return ''
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

.ph h1 {
  font-size: clamp(52px, 9vw, 148px);
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

.bdg.in {
  background: transparent;
  border: 1px solid rgba(255, 255, 255, 0.3);
  color: #bbb;
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

.pcards {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
  margin-top: 40px;
}

.lc {
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: 28px;
  min-height: 220px;
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

.lc .bd span.mk {
  background: var(--lime);
  color: #0B0B0B;
  border-color: var(--lime);
}

.lc h4 {
  font-size: 30px;
  letter-spacing: -0.035em;
  font-weight: 600;
  margin-top: auto;
  line-height: 1.05;
  padding-top: 30px;
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

.pointer-events-none {
  pointer-events: none;
  opacity: 0.7;
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

  .pcards {
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
