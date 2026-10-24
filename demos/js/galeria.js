/* Visor progresivo: sin JavaScript, cada afiche abre su imagen original. */
(() => {
  const dialog = document.querySelector('.gallery-dialog');
  const links = [...document.querySelectorAll('[data-gallery]')];
  if (!dialog || typeof dialog.showModal !== 'function' || !links.length) return;
  const image = dialog.querySelector('.gallery-image');
  const title = dialog.querySelector('#gallery-title');
  const count = dialog.querySelector('[data-gallery-count]');
  const original = dialog.querySelector('[data-original]');
  let index = 0;
  let opener;

  function show(next) {
    index = (next + links.length) % links.length;
    const link = links[index];
    image.src = link.href;
    image.alt = link.querySelector('img').alt;
    title.textContent = link.dataset.caption;
    count.textContent = `${index + 1} de ${links.length}`;
    original.href = link.href;
  }

  links.forEach((link, position) => {
    link.addEventListener('click', (event) => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      opener = link;
      show(position);
      dialog.showModal();
    });
  });
  dialog.querySelector('[data-close]').addEventListener('click', () => dialog.close());
  dialog.querySelector('[data-prev]').addEventListener('click', () => show(index - 1));
  dialog.querySelector('[data-next]').addEventListener('click', () => show(index + 1));
  dialog.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
      event.preventDefault();
      show(index + (event.key === 'ArrowLeft' ? -1 : 1));
    }
  });
  dialog.addEventListener('close', () => {
    image.removeAttribute('src');
    opener?.focus();
  });
})();
