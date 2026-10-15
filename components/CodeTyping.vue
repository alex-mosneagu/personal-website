<template>
  <div class="code-card">
    <div class="bar">
      <i />
      <i />
      <i />
      <span>AlexMosneagu.vue</span>
    </div>
    <pre class="code-content"><span v-html="displayHtml" /><span
v-if="!isComplete"
                                                                 class="cursor"
    /></pre>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

type Segment = [string, string]

export default defineComponent({
  name: 'CodeTyping',

  data() {
    return {
      src: [
        ['c', '<!-- AlexMosneagu.vue -->'],
        ['', '\n<'],
        ['t', 'script'],
        ['', '>\nexport default {\n  name: '],
        ['s', '\'AlexMosneagu\''],
        ['', ',\n  data() {\n    return {\n      role: '],
        ['s', '\'Frontend Tech Lead\''],
        ['', ',\n      years: '],
        ['s', '\'9+\''],
        ['', ',\n      city: '],
        ['s', '\'Bucharest\''],
        ['', ',\n      stack: [\'Vue\', \'Nuxt\', \'TS\', \'React\']\n    }\n  },\n  computed: {\n    focus() { return '],
        ['s', '\'full stack\''],
        ['', ' }\n  },\n  methods: {\n    ship(idea) { '],
        ['c', '// idea → POC → market'],
        ['', '\n      return this.build(idea) }\n  }\n}\n</'],
        ['t', 'script'],
        ['', '>'],
      ] as Segment[],
      displayHtml: '',
      segmentIndex: 0,
      charIndex: 0,
      isComplete: false,
      intervalId: null as number | null,
      prefersReducedMotion: false,
    }
  },

  mounted() {
    this.prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches

    if (this.prefersReducedMotion) {
      this.showComplete()
    }
    else {
      this.tick()
    }
  },

  beforeUnmount() {
    if (this.intervalId) {
      clearTimeout(this.intervalId)
    }
  },

  methods: {
    escapeHtml(text: string): string {
      return text
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
    },

    showComplete() {
      this.displayHtml = this.src.map(([cls, text]) => {
        if (cls) {
          return `<span class="${cls}">${this.escapeHtml(text)}</span>`
        }
        return this.escapeHtml(text)
      }).join('')
      this.segmentIndex = this.src.length
      this.isComplete = true
    },

    tick() {
      if (this.segmentIndex >= this.src.length) {
        this.isComplete = true
        return
      }

      const [cls, text] = this.src[this.segmentIndex]
      this.charIndex += 2
      const part = text.slice(0, this.charIndex)
      const currentSegment = cls
        ? `<span class="${cls}">${this.escapeHtml(part)}</span>`
        : this.escapeHtml(part)

      const completedHtml = this.src
        .slice(0, this.segmentIndex)
        .map(([c, t]) => (c ? `<span class="${c}">${this.escapeHtml(t)}</span>` : this.escapeHtml(t)))
        .join('')

      this.displayHtml = completedHtml + currentSegment

      if (this.charIndex >= text.length) {
        const finalSegment = cls
          ? `<span class="${cls}">${this.escapeHtml(text)}</span>`
          : this.escapeHtml(text)

        this.displayHtml = this.src
          .slice(0, this.segmentIndex)
          .map(([c, t]) => (c ? `<span class="${c}">${this.escapeHtml(t)}</span>` : this.escapeHtml(t)))
          .join('') + finalSegment

        this.segmentIndex++
        this.charIndex = 0
      }

      this.intervalId = window.setTimeout(() => this.tick(), 22)
    },
  },
})
</script>

<style scoped>
.code-card {
  background: rgba(14, 14, 14, 0.82);
  backdrop-filter: blur(10px);
  border: 1px solid var(--line);
  border-radius: 18px;
  overflow: hidden;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12.5px;
  line-height: 1.7;
  box-shadow: 0 30px 80px rgba(0, 0, 0, 0.5);
}

.bar {
  display: flex;
  align-items: center;
  gap: 7px;
  padding: 12px 16px;
  border-bottom: 1px solid var(--line);
  color: var(--mut);
  font-size: 12px;
}

.bar i {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #2a2a2a;
}

.bar i:first-child {
  background: var(--lime);
}

.bar span {
  margin-left: auto;
}

.code-content {
  padding: 16px 18px;
  min-height: 300px;
  color: #d6d6d6;
  white-space: pre;
}

.code-content :deep(.t) {
  color: var(--lime);
}

.code-content :deep(.s) {
  color: #e9ffb8;
}

.code-content :deep(.c) {
  color: #6b6b6b;
}

.cursor {
  display: inline-block;
  width: 7px;
  height: 15px;
  background: var(--lime);
  vertical-align: -3px;
  animation: blink 1s steps(1) infinite;
}

@keyframes blink {
  50% {
    opacity: 0;
  }
}

@media (max-width: 900px) {
  .code-content {
    min-height: 250px;
    font-size: 11px;
  }
}
</style>
