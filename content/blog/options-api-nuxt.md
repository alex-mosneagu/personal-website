---
slug: options-api-nuxt
n: '04'
tag: Nuxt · Vue
title: Structuring a Nuxt project with the Options API
ex: The Options API still gives a Nuxt project a clear, predictable shape. Here is how I organize pages, components and data so the codebase stays easy to read and test.
soon: false
order: 4
---

The Composition API gets most of the attention, but the Options API still works very well in Nuxt, especially on teams where many people touch the same code. Its biggest advantage is predictability: every component has the same shape.

## Start with the folders

Keep Nuxt's conventions and add a little structure on top. Pages stay thin and only compose components. Reusable logic lives in `composables/`, and domain types in `types/`.

```
pages/        // routes, thin
components/   // UI, one folder per feature
composables/  // shared logic (useCurrency, useAuth)
types/        // TypeScript interfaces
```

## One order for every component

Pick an order for the options and never break it: `name`, `props`, `emits`, `setup`, `data`, `computed`, `watch`, `methods`, then lifecycle hooks. Reviewers always know where to look.

```typescript
export default defineComponent({
  name: 'ProductCard',
  props: { product: { type: Object as PropType<Product>, required: true } },
  emits: ['select'],
  setup() {
    const { format } = useCurrency()
    return { format }
  },
  data() { return { expanded: false } },
  computed: {
    price(): string { return this.format(this.product.price) }
  },
  methods: {
    toggle() { this.expanded = !this.expanded }
  }
})
```

## Share logic with composables

Options API does not mean giving up composables. Call them in `setup()` and return what the template needs. You keep the readable options layout while reusing the same logic as the rest of the app.

## Keep it testable

Keep methods small and move anything non-trivial into plain functions or composables. With Vitest you can test those directly, and mount the component only to check what it renders and emits. Cypress then covers the full flow.

The result is a codebase where new developers find things quickly and reviews focus on behavior, not on style.
