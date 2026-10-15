<template>
  <div
    ref="container"
    class="hero-gl"
  />
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import type { Scene, WebGLRenderer, PerspectiveCamera, Points, Mesh, Raycaster, Plane, Vector2, Vector3, Clock } from 'three'

export default defineComponent({
  name: 'HeroGL',

  data() {
    return {
      renderer: null as WebGLRenderer | null,
      scene: null as Scene | null,
      camera: null as PerspectiveCamera | null,
      points: null as Points | null,
      wireframe: null as Mesh | null,
      raycaster: null as Raycaster | null,
      plane: null as Plane | null,
      target: null as Vector2 | null,
      mouseScreen: null as Vector2 | null,
      hitPoint: null as Vector3 | null,
      clock: null as Clock | null,
      animationFrame: null as number | null,
      observer: null as IntersectionObserver | null,
      isVisible: true,
      isMobile: false,
      prefersReducedMotion: false,
    }
  },

  mounted() {
    this.isMobile = window.innerWidth < 900
    this.prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches

    if (this.prefersReducedMotion) {
      this.initStaticVersion()
      return
    }

    this.initThree()
    this.setupIntersectionObserver()
  },

  beforeUnmount() {
    this.cleanup()
  },

  methods: {
    initStaticVersion() {
      if (!this.$refs.container) return
      const container = this.$refs.container as HTMLElement
      container.classList.add('static')
      if (document.body) {
        document.body.dataset.gl = 'ok'
      }
    },

    async initThree() {
      if (!this.$refs.container) return

      try {
        const THREE = await import('three')
        const container = this.$refs.container as HTMLElement

        this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true })
        this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
        container.appendChild(this.renderer.domElement)

        this.scene = new THREE.Scene()
        this.camera = new THREE.PerspectiveCamera(50, 1, 0.1, 100)
        this.camera.position.set(0, 3.2, 7.5)
        this.camera.lookAt(0, 0, -1)

        const N = this.isMobile ? 140 : 220
        const geometry = new THREE.PlaneGeometry(22, 14, N, Math.round(N * 0.64))
        geometry.rotateX(-Math.PI / 2)

        const uniforms = {
          t: { value: 0 },
          m: { value: new THREE.Vector2(9, 9) },
          c: { value: new THREE.Color('#C6FF3D') },
        }

        const noise = `vec3 p3(vec3 x){return x-floor(x*(1./289.))*289.;}vec2 p2(vec2 x){return x-floor(x*(1./289.))*289.;}vec3 pm(vec3 x){return p3(((x*34.)+1.)*x);}
float sn(vec2 v){const vec4 C=vec4(.211324865,.366025404,-.577350269,.024390244);vec2 i=floor(v+dot(v,C.yy));vec2 x0=v-i+dot(i,C.xx);vec2 i1=(x0.x>x0.y)?vec2(1,0):vec2(0,1);vec4 x12=x0.xyxy+C.xxzz;x12.xy-=i1;i=p2(i);vec3 p=pm(pm(i.y+vec3(0,i1.y,1))+i.x+vec3(0,i1.x,1));vec3 m=max(.5-vec3(dot(x0,x0),dot(x12.xy,x12.xy),dot(x12.zw,x12.zw)),0.);m=m*m;m=m*m;vec3 x=2.*fract(p*C.www)-1.;vec3 h=abs(x)-.5;vec3 ox=floor(x+.5);vec3 a0=x-ox;m*=1.79284291-.85373472*(a0*a0+h*h);vec3 g;g.x=a0.x*x0.x+h.x*x0.y;g.yz=a0.yz*x12.xz+h.yz*x12.yw;return 130.*dot(m,g);}`

        const vertexShader = noise + `uniform float t;uniform vec2 m;varying float vh;varying float vd;
void main(){vec3 p=position;float h=sn(p.xz*.18+vec2(0.,t*.08))*1.1+sn(p.xz*.5-t*.05)*.3;
float d=distance(p.xz,m);h+=exp(-d*d*.35)*1.6*(.6+.4*sin(t*2.-d*2.));
h*=smoothstep(-.5,3.5,abs(p.x))*.9+.25;p.y=h;vh=h;vec4 mv=modelViewMatrix*vec4(p,1.);vd=-mv.z;gl_Position=projectionMatrix*mv;gl_PointSize=(2.2+h*1.4)*(9./vd);}`

        const fragmentShader = `uniform vec3 c;varying float vh;varying float vd;void main(){float r=length(gl_PointCoord-.5);if(r>.5)discard;float a=smoothstep(.5,0.,r)*clamp(.25+vh*.55,.08,1.)*smoothstep(16.,4.,vd);gl_FragColor=vec4(c*(.6+vh*.5),a);}`

        this.points = new THREE.Points(
          geometry,
          new THREE.ShaderMaterial({
            uniforms,
            vertexShader,
            fragmentShader,
            transparent: true,
            depthWrite: false,
            blending: THREE.AdditiveBlending,
          }),
        )
        this.scene.add(this.points)

        const wireGeometry = new THREE.PlaneGeometry(22, 14, 60, 38)
        wireGeometry.rotateX(-Math.PI / 2)

        this.wireframe = new THREE.Mesh(
          wireGeometry,
          new THREE.ShaderMaterial({
            uniforms,
            wireframe: true,
            transparent: true,
            depthWrite: false,
            vertexShader: vertexShader.replace('gl_PointSize', 'float _ps'),
            fragmentShader: `uniform vec3 c;varying float vh;varying float vd;void main(){gl_FragColor=vec4(c,.07*smoothstep(16.,4.,vd));}`,
          }),
        )
        this.wireframe.position.y = -0.02
        this.scene.add(this.wireframe)

        this.raycaster = new THREE.Raycaster()
        this.plane = new THREE.Plane(new THREE.Vector3(0, 1, 0), 0)
        this.target = new THREE.Vector2(2.5, 1)
        this.mouseScreen = new THREE.Vector2()
        this.hitPoint = new THREE.Vector3()

        window.addEventListener('pointermove', this.onPointerMove)
        window.addEventListener('resize', this.onResize)

        this.clock = new THREE.Clock()
        uniforms.m.value.copy(this.target)

        this.onResize()
        this.animate()

        if (document.body) {
          document.body.dataset.gl = 'ok'
        }
      }
      catch (error) {
        console.error('Failed to initialize WebGL:', error)
        this.initStaticVersion()
      }
    },

    onPointerMove(e: PointerEvent) {
      if (!this.camera || !this.raycaster || !this.plane || !this.target || !this.hitPoint || !this.mouseScreen) return

      const container = this.$refs.container as HTMLElement
      if (!container) return

      const rect = container.getBoundingClientRect()
      this.mouseScreen.set(
        (e.clientX / window.innerWidth) * 2 - 1,
        -(e.clientY / rect.height) * 2 + 1,
      )

      this.raycaster.setFromCamera(this.mouseScreen, this.camera)

      if (this.raycaster.ray.intersectPlane(this.plane, this.hitPoint)) {
        this.target.set(this.hitPoint.x, this.hitPoint.z)
      }
    },

    onResize() {
      if (!this.renderer || !this.camera) return

      const container = this.$refs.container as HTMLElement
      if (!container) return

      const w = container.clientWidth
      const h = container.clientHeight

      this.renderer.setSize(w, h, false)
      this.camera.aspect = w / h
      this.camera.updateProjectionMatrix()
    },

    animate() {
      if (!this.isVisible || !this.renderer || !this.scene || !this.camera || !this.clock || !this.points || !this.target) {
        return
      }

      const material = this.points.material as any
      const uniforms = material.uniforms

      uniforms.t.value = this.clock.getElapsedTime() + 4
      uniforms.m.value.lerp(this.target, 0.05)

      if (this.scene) {
        this.scene.rotation.y = Math.sin(uniforms.t.value * 0.05) * 0.08
      }

      this.renderer.render(this.scene, this.camera)
      this.animationFrame = requestAnimationFrame(() => this.animate())
    },

    setupIntersectionObserver() {
      const container = this.$refs.container as HTMLElement
      if (!container) return

      this.observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            this.isVisible = entry.isIntersecting
            if (this.isVisible && !this.animationFrame) {
              this.animate()
            }
          })
        },
        { threshold: 0.1 },
      )

      this.observer.observe(container)
    },

    cleanup() {
      if (this.animationFrame) {
        cancelAnimationFrame(this.animationFrame)
        this.animationFrame = null
      }

      if (this.observer) {
        this.observer.disconnect()
        this.observer = null
      }

      window.removeEventListener('pointermove', this.onPointerMove)
      window.removeEventListener('resize', this.onResize)

      if (this.renderer) {
        this.renderer.dispose()
        const container = this.$refs.container as HTMLElement
        if (container && this.renderer.domElement && container.contains(this.renderer.domElement)) {
          container.removeChild(this.renderer.domElement)
        }
      }

      if (this.points) {
        this.points.geometry.dispose()
        const material = this.points.material as any
        material.dispose()
      }

      if (this.wireframe) {
        this.wireframe.geometry.dispose()
        const material = this.wireframe.material as any
        material.dispose()
      }
    },
  },
})
</script>

<style scoped>
.hero-gl {
  position: absolute;
  inset: 0;
  z-index: 0;
}

.hero-gl :deep(canvas) {
  display: block;
  width: 100% !important;
  height: 100% !important;
}

.hero-gl.static {
  background: radial-gradient(ellipse at 30% 50%, rgba(198, 255, 61, 0.15), transparent 60%),
    repeating-linear-gradient(90deg, transparent 0 46px, rgba(198, 255, 61, 0.05) 46px 47px);
}
</style>
