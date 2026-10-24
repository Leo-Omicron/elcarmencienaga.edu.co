// Accesibilidad compartida de las galerías DEMOS.
const photoDialog = document.querySelector('dialog');
let photoTrigger;
document.querySelectorAll('[onclick^="openLightbox("]').forEach(card => {
  card.addEventListener('click', () => { photoTrigger = card; });
  card.addEventListener('keydown', event => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault(); card.click();
    }
  });
});
const zoomButton = document.querySelector('.lightbox-zoom-btn');
zoomButton?.addEventListener('click', () => {
  const zoomed = photoDialog.classList.toggle('is-zoomed');
  zoomButton.setAttribute('aria-pressed', String(zoomed));
  zoomButton.textContent = zoomed ? 'Reducir imagen −' : 'Ampliar imagen +';
});
photoDialog?.addEventListener('close', () => {
  photoDialog.classList.remove('is-zoomed');
  zoomButton?.setAttribute('aria-pressed', 'false');
  if (zoomButton) zoomButton.textContent = 'Ampliar imagen +';
  photoTrigger?.focus();
});
