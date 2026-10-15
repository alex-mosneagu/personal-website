import { describe, it, expect } from 'vitest'

describe('Content Helpers', () => {
  it('should correctly filter draft posts', () => {
    const posts = [
      { slug: 'post-1', draft: false },
      { slug: 'post-2', draft: true },
      { slug: 'post-3', draft: false },
    ]

    const published = posts.filter(p => !p.draft)

    expect(published).toHaveLength(2)
    expect(published.map(p => p.slug)).toEqual(['post-1', 'post-3'])
  })

  it('should sort items by order field', () => {
    const items = [
      { slug: 'c', order: 3 },
      { slug: 'a', order: 1 },
      { slug: 'b', order: 2 },
    ]

    const sorted = items.sort((a, b) => a.order - b.order)

    expect(sorted.map(i => i.slug)).toEqual(['a', 'b', 'c'])
  })
})

describe('Badge Class Helper', () => {
  it('should return correct badge classes', () => {
    const badgeClass = (st: string): string => {
      const map: Record<string, string> = {
        'POC': 'poc',
        'AI': 'ai',
        'On market': 'mk',
      }
      return map[st] || ''
    }

    expect(badgeClass('POC')).toBe('poc')
    expect(badgeClass('AI')).toBe('ai')
    expect(badgeClass('On market')).toBe('mk')
    expect(badgeClass('Unknown')).toBe('')
  })
})
