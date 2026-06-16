<template>
  <div ref="container" class="cursor-zoom-in" @click="showZoom" title="點擊放大">
    <slot />
  </div>
  <Teleport to="body">
    <div
      v-if="zoomed"
      style="position:fixed;inset:0;z-index:9999;background:rgba(0,0,0,0.82);display:flex;align-items:center;justify-content:center;cursor:zoom-out"
      @click="zoomed = false"
    >
      <img :src="svgDataUri" style="max-width:92vw;max-height:92vh;border-radius:8px;background:white;padding:1.5rem;box-shadow:0 8px 40px rgba(0,0,0,0.5)" />
    </div>
  </Teleport>
</template>

<script setup>
import { ref } from 'vue'

const container = ref(null)
const zoomed = ref(false)
const svgDataUri = ref('')

function showZoom() {
  const svg = container.value?.querySelector('svg')
  if (!svg) return
  svgDataUri.value = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(new XMLSerializer().serializeToString(svg))
  zoomed.value = true
  const onEsc = (e) => {
    if (e.key === 'Escape') { zoomed.value = false; window.removeEventListener('keydown', onEsc) }
  }
  window.addEventListener('keydown', onEsc)
}
</script>
