<template>
  <nav class="nav">
    <NuxtLink
      to="/"
      class="logo"
    >
      alex<span>.</span>m
    </NuxtLink>
    <NuxtLink
      to="/#work"
      class="lk"
    >
      Work
    </NuxtLink>
    <NuxtLink
      to="/#ventures"
      class="lk"
    >
      Ventures
    </NuxtLink>
    <NuxtLink
      to="/#rd"
      class="lk"
    >
      R&amp;D
    </NuxtLink>
    <NuxtLink
      to="/#journey"
      class="lk"
    >
      Journey
    </NuxtLink>
    <NuxtLink
      to="/blog"
      class="talk"
    >
      Blog
    </NuxtLink>
  </nav>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'AppNav',
})
</script>

<style scoped>
.nav {
  position: fixed;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 20;
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 8px 8px 8px 20px;
  background: rgba(18, 18, 18, 0.72);
  backdrop-filter: blur(14px);
  border: 1px solid var(--line);
  border-radius: 999px;
  font-size: 14px;
  white-space: nowrap;
}

.logo {
  font-weight: 800;
  letter-spacing: -0.04em;
  margin-right: 14px;
}

.logo span {
  color: var(--lime);
}

.lk {
  padding: 10px 13px;
  color: #cfcfcf;
  transition: color 0.3s;
}

.lk:hover {
  color: #fff;
}

.talk {
  background: var(--lime);
  color: #0B0B0B;
  padding: 10px 18px;
  border-radius: 999px;
  font-weight: 600;
}

@media (max-width: 900px) {
  .nav {
    top: 12px;
    padding: 6px 6px 6px 14px;
    gap: 0;
    max-width: calc(100vw - 16px);
  }

  .lk {
    display: block;
    padding: 9px 7px;
    font-size: 12.5px;
  }

  .logo {
    margin-right: 6px;
  }

  .talk {
    padding: 9px 13px;
    font-size: 12.5px;
  }
}
</style>
