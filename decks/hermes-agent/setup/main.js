export default ({ app }) => {
  if (typeof document === 'undefined') return

  // Overlay element
  const overlay = document.createElement('div')
  overlay.style.cssText = [
    'display:none', 'position:fixed', 'inset:0', 'z-index:9999',
    'background:rgba(0,0,0,0.82)', 'align-items:center',
    'justify-content:center', 'cursor:zoom-out',
  ].join(';')

  const img = document.createElement('img')
  img.style.cssText = [
    'width:90vw', 'height:88vh', 'object-fit:contain', 'border-radius:8px',
    'background:white', 'padding:1.5rem',
    'box-shadow:0 8px 40px rgba(0,0,0,.5)',
  ].join(';')
  overlay.appendChild(img)
  document.body.appendChild(overlay)

  const close = () => { overlay.style.display = 'none' }
  overlay.addEventListener('click', close)
  document.addEventListener('keydown', e => { if (e.key === 'Escape') close() })

  // Cursor hint on Mermaid shadow hosts
  const style = document.createElement('style')
  style.textContent = '.slidev-slide-container .mermaid { cursor: zoom-in; }'
  document.head.appendChild(style)

  // Capture phase: Mermaid SVG lives inside Shadow DOM of div.mermaid,
  // so clicks are retargeted to the shadow host in the light DOM.
  document.addEventListener('click', e => {
    // Find the mermaid shadow host that was clicked (or is an ancestor of the click target)
    const host = e.target.closest('.mermaid')
    if (!host) return
    if (!host.closest('.slidev-slide-container')) return

    // Get SVG from inside the Shadow DOM
    const svg = host.shadowRoot?.querySelector('svg')
    if (!svg) return

    // Clone and strip mermaid's scale-constrained width/height so the
    // serialized SVG scales freely via viewBox inside the overlay.
    const clone = svg.cloneNode(true)
    clone.removeAttribute('width')
    clone.removeAttribute('height')
    img.src = 'data:image/svg+xml;charset=utf-8,' +
      encodeURIComponent(new XMLSerializer().serializeToString(clone))
    overlay.style.display = 'flex'
    e.stopPropagation()
    e.preventDefault()
  }, true)
}
