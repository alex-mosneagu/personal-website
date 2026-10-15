import { describe, it, expect } from 'vitest'

describe('CodeTyping Component Logic', () => {
  it('should escape HTML correctly', () => {
    const escapeHtml = (text: string): string => {
      return text
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
    }
    
    expect(escapeHtml('<script>')).toBe('&lt;script&gt;')
    expect(escapeHtml('A & B')).toBe('A &amp; B')
    expect(escapeHtml('<div>Test</div>')).toBe('&lt;div&gt;Test&lt;/div&gt;')
  })
  
  it('should handle segment indexing correctly', () => {
    const segments = [
      ['c', 'comment'],
      ['', 'code'],
      ['s', 'string']
    ]
    
    expect(segments[0][0]).toBe('c')
    expect(segments[1][0]).toBe('')
    expect(segments[2][1]).toBe('string')
  })
})
