<template>
  <div class="cursor-zoom-in" @click.stop="showZoom" title="點擊放大">
    <slot />
  </div>
  <Teleport to="body">
    <div
      v-if="zoomed"
      style="position:fixed;inset:0;z-index:9999;background:rgba(0,0,0,0.82);display:flex;align-items:center;justify-content:center;cursor:zoom-out"
      @click="zoomed = false"
    >
      <img :src="resolvedSrc" style="max-width:92vw;max-height:92vh;border-radius:8px;box-shadow:0 8px 40px rgba(0,0,0,0.5);object-fit:contain" />
    </div>
  </Teleport>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps(['src'])
const zoomed = ref(false)

const resolvedSrc = computed(() => {
  const base = (import.meta.env.BASE_URL || '/').replace(/\/$/, '')
  return props.src.startsWith('/') ? base + props.src : props.src
})

function showZoom() {
  zoomed.value = true
  const onEsc = (e) => {
    if (e.key === 'Escape') { zoomed.value = false; window.removeEventListener('keydown', onEsc) }
  }
  window.addEventListener('keydown', onEsc)
}
</script>
