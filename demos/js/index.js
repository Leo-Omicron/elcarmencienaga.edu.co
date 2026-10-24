
    // Pestañas del cronograma
    function switchDay(dayId, btn) {
      document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));

      const target = document.getElementById(dayId);
      if (target) {
        target.classList.add('active');
      }
      if (btn) {
        btn.classList.add('active');
      }
    }

    // Conmutador A/B de Reproducción de Video
    function switchVideoMode(mode) {
      const btnA = document.getElementById('btn-mode-a');
      const btnB = document.getElementById('btn-mode-b');
      const panelA = document.getElementById('panel-video-inpage');
      const panelB = document.getElementById('panel-video-launcher');
      const noteA = document.getElementById('note-mode-a');
      const noteB = document.getElementById('note-mode-b');

      if (mode === 'a') {
        if (btnA) btnA.classList.add('active');
        if (btnB) btnB.classList.remove('active');
        if (panelA) panelA.style.display = 'block';
        if (panelB) panelB.style.display = 'none';
        if (noteA) noteA.style.display = 'block';
        if (noteB) noteB.style.display = 'none';
      } else {
        if (btnB) btnB.classList.add('active');
        if (btnA) btnA.classList.remove('active');
        if (panelB) panelB.style.display = 'block';
        if (panelA) panelA.style.display = 'none';
        if (noteB) noteB.style.display = 'block';
        if (noteA) noteA.style.display = 'none';
      }
    }

    // Filtro de Medios (Todos, Videos, Fotos)
    function filterMedia(type, btn) {
      document.querySelectorAll('.media-filter-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');

      const videoBox = document.getElementById('media-ab-box');
      const photoBox = document.getElementById('media-photo-group');

      if (type === 'all') {
        if (videoBox) videoBox.style.display = 'block';
        if (photoBox) photoBox.style.display = 'block';
      } else if (type === 'videos') {
        if (videoBox) videoBox.style.display = 'block';
        if (photoBox) photoBox.style.display = 'none';
      } else if (type === 'photos') {
        if (videoBox) videoBox.style.display = 'none';
        if (photoBox) photoBox.style.display = 'block';
      }
    }

    // Lightbox Nativo con <dialog>
    function openLightbox(src, title, caption) {
      const dialog = document.getElementById('photo-lightbox');
      const img = document.getElementById('lightbox-img');
      const titleEl = document.getElementById('lightbox-title');
      const captionEl = document.getElementById('lightbox-caption');

      if (dialog && img) {
        img.src = src;
        img.alt = title || 'Fotografía ampliada';
        if (titleEl) titleEl.textContent = title || '';
        if (captionEl) captionEl.textContent = caption || '';
        dialog.showModal();
      }
    }

    function closeLightbox() {
      const dialog = document.getElementById('photo-lightbox');
      if (dialog) dialog.close();
    }

    // Cerrar lightbox haciendo clic en el backdrop
    const lbDialog = document.getElementById('photo-lightbox');
    if (lbDialog) {
      lbDialog.addEventListener('click', (e) => {
        const rect = lbDialog.getBoundingClientRect();
        const isInDialog = (rect.top <= e.clientY && e.clientY <= rect.top + rect.height &&
          rect.left <= e.clientX && e.clientX <= rect.left + rect.width);
        if (!isInDialog) {
          lbDialog.close();
        }
      });
    }
  