export interface Venture {
  slug: string
  a: string
  b: string
  place: string
  role: string
  lime?: boolean
  desc: string
  products: string[]
  badge: string | null
  inactive?: boolean
  long: string[]
}

export interface Project {
  slug: string
  name: string
  tag: string
  cat: string
  line: string
  facts: Array<[string, string]>
  paras: string[]
  feats: string[]
}

export interface RDItem {
  slug: string
  name: string
  st: string[]
  desc: string
}

export interface BlogPost {
  slug: string
  n: string
  tag: string
  title: string
  ex: string
  draft?: boolean
}

export interface SEOMeta {
  title: string
  description: string
  ogImage?: string
}
