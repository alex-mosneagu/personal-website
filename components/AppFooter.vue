<template>
  <footer class="footer">
    <div class="glow" />
    <div class="wm">
      Alex <em>Mosneagu</em>
    </div>
    <div class="base">
      <span>© 2026 Alex Mosneagu</span>
      <span>Bucharest, RO</span>
      <a href="#top">Back to top ↑</a>
    </div>
  </footer>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'AppFooter',
})
</script>

<style scoped>
.footer {
  position: relative;
  overflow: hidden;
  border-top: 1px solid var(--line);
  padding: 90px 0 0;
  margin-top: 40px;
}

.glow {
  position: absolute;
  width: 1200px;
  height: 500px;
  left: 50%;
  bottom: -300px;
  transform: translateX(-50%);
  background: radial-gradient(closest-side, rgba(198, 255, 61, 0.38), transparent);
  filter: blur(50px);
}

.wm {
  position: relative;
  font-size: 18vw;
  line-height: 0.9;
  letter-spacing: -0.07em;
  font-weight: 800;
  text-align: center;
  white-space: nowrap;
  padding: 0 0.5vw 0.2em;
}

.wm em {
  color: var(--lime);
  font-weight: 400;
  letter-spacing: -0.04em;
}

.base {
  position: relative;
  display: flex;
  justify-content: space-between;
  gap: 20px;
  flex-wrap: wrap;
  padding: 26px 40px;
  font-size: 13px;
  color: var(--mut);
  font-family: 'JetBrains Mono', monospace;
  border-top: 1px solid var(--line);
  background: rgba(11, 11, 11, 0.55);
  backdrop-filter: blur(6px);
}

.base a:hover {
  color: var(--lime);
}

@media (max-width: 900px) {
  .footer {
    padding-top: 60px;
  }

  .base {
    padding: 20px;
  }
}
</style>
