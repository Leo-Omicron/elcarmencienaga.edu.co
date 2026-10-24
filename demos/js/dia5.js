
    const galleryItems = [
      {"file": "dia5/Dia5 (1).jpg", "title": "Apertura de la Santa Misa y Altar Conmemorativo", "desc": "Solemne inicio de la Eucaristía de acción de gracias por los 53 años institucionales con el altar en honor a la Virgen del Carmen, ofrendas florales y la comunidad reunida en oración."},
      {"file": "dia5/Dia5 (2).jpg", "title": "Liturgia de la Palabra y Reflexión Sacerdotal", "desc": "El párroco presidiendo la celebración eucarística y compartiendo un mensaje inspirador de fe, vocación, amor a la educación y gratitud por la historia carmelista."},
      {"file": "dia5/Dia5 (3).jpg", "title": "Comunidad Estudiantil Carmelista en Oración", "desc": "Estudiantes luciendo el uniforme institucional de gala, participando con respeto, devoción y recogimiento espiritual en el patio central techado."},
      {"file": "dia5/Dia5 (4).jpg", "title": "Celebración Eucarística y Árbol de Sueños", "desc": "Momento solemne de la Eucaristía frente al mural conmemorativo «Árbol de Sueños» con la participación activa y fraterna de directivos y docentes."},
      {"file": "dia5/Dia5 (5).jpg", "title": "Panorámica del Patio Central de la Sede Principal", "desc": "Amplia concurrencia de la comunidad carmelista colmando los pasillos y áreas techadas durante los actos litúrgicos del aniversario."},
      {"file": "dia5/Dia5 (6).jpg", "title": "Acompañamiento de Familias y Promoción 2026", "desc": "Padres de familia, acudientes y los jóvenes de la Promoción 2026 unidos en acción de gracias por las bendiciones cosechadas en estos 53 años."},
      {"file": "dia5/Dia5 (7).jpg", "title": "Mensaje Institucional del Cuerpo Directivo", "desc": "Palabras de gratitud, exaltación histórica y compromiso institucional dirigidas por las directivas docentes a toda la familia carmelista."},
      {"file": "dia5/Dia5 (8).jpg", "title": "Lecturas Litúrgicas y Oración de los Fieles", "desc": "Miembros de la comunidad educativa elevando súplicas y plegarias junto a la imagen protectora de la Virgen del Carmen en el altar."},
      {"file": "dia5/Dia5 (9).jpg", "title": "Altar Mayor: 53° Aniversario Institucional", "desc": "Hermosa ambientación con arreglos florales, detalles marianos, coro e instrumentos y el mural conmemorativo «I.E. El Carmen Aniversario»."},
      {"file": "dia5/Dia5 (10).jpg", "title": "Gran Asamblea Carmelista en la Eucaristía", "desc": "Vista desde la nave central que refleja el fervor, unidad, hermandad y solemnidad de toda la institución educativa en Ciénaga."},
      {"file": "dia5/Dia5 (11).jpg", "title": "Homenaje al Legado del Profesor Arlin Jiménez", "desc": "Sentido homenaje póstumo en el primer aniversario de la partida de nuestro querido compañero y educador Arlin Jiménez, honrando su memoria y entrega."},
      {"file": "dia5/Dia5 (13).jpg", "title": "Preparación Litúrgica y Sagrados Vasos", "desc": "Disposición solemne de los ornamentos, vasos sagrados, cáliz y ofrendas para la consagración eucarística de aniversario."}
    ];
    let currentPhotoIdx = 0;

    function openLightbox(idx) {
      if (idx < 0 || idx >= galleryItems.length) return;
      currentPhotoIdx = idx;
      updateLightboxContent();

      const dialog = document.getElementById('photo-lightbox');
      if (dialog && !dialog.open) {
        dialog.showModal();
      }
    }

    function updateLightboxContent() {
      const item = galleryItems[currentPhotoIdx];
      const img = document.getElementById('lightbox-img');
      const titleEl = document.getElementById('lightbox-title');
      const captionEl = document.getElementById('lightbox-caption');
      const counterEl = document.getElementById('lightbox-counter');

      if (img && item) {
        img.src = item.file;
        img.alt = item.title || 'Fotografía ampliada';
        if (titleEl) titleEl.textContent = item.title || '';
        if (captionEl) captionEl.textContent = item.desc || '';
        if (counterEl) counterEl.textContent = `Foto ${currentPhotoIdx + 1} de ${galleryItems.length}`;
      }
    }

    function changeLightbox(step) {
      currentPhotoIdx = (currentPhotoIdx + step + galleryItems.length) % galleryItems.length;
      updateLightboxContent();
    }

    function closeLightbox() {
      const dialog = document.getElementById('photo-lightbox');
      if (dialog && dialog.open) {
        dialog.close();
      }
    }

    // Cerrar al hacer clic fuera del modal
    const lbDialog = document.getElementById('photo-lightbox');
    if (lbDialog) {
      lbDialog.addEventListener('click', (e) => {
        const rect = lbDialog.getBoundingClientRect();
        const isInDialog = (rect.top <= e.clientY && e.clientY <= rect.top + rect.height &&
          rect.left <= e.clientX && e.clientX <= rect.left + rect.width);
        if (!isInDialog) {
          closeLightbox();
        }
      });
    }

    // Navegación con flechas del teclado
    document.addEventListener('keydown', (e) => {
      const dialog = document.getElementById('photo-lightbox');
      if (dialog && dialog.open) {
        if (e.key === 'ArrowLeft') {
          changeLightbox(-1);
        } else if (e.key === 'ArrowRight') {
          changeLightbox(1);
        }
      }
    });
  