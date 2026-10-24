
    const galleryItems = [{"file": "dia1/Dia1 (1).jpg", "title": "Apertura y Recorrido de Memoria Histórica", "desc": "Exhibición inaugural de proyectos de memoria y patrimonio cienaguero en el patio central."}, {"file": "dia1/Dia1 (2).jpg", "title": "Murales y Muestras del Legado Cultural", "desc": "Representación gráfica e histórica elaborada por estudiantes de secundaria."}, {"file": "dia1/Dia1 (3).jpg", "title": "Pabellón Temático de Tradición e Identidad", "desc": "Recorrido guiado con paneles informativos sobre los hitos de nuestra región."}, {"file": "dia1/Dia1 (4).jpg", "title": "Exposición de Maquetas y Espacios Patrimoniales", "desc": "Recreación a escala de la arquitectura emblemática de Ciénaga y el Magdalena."}, {"file": "dia1/Dia1 (5).jpg", "title": "Stands Interactivos de Cátedra Carmelita", "desc": "Espacios de diálogo e intercambio de saberes entre docentes y alumnos."}, {"file": "dia1/Dia1 (6).jpg", "title": "Ponencias Estudiantiles y Presentaciones Orales", "desc": "Socialización de investigaciones sobre costumbres, mitos y memorias comunitarias."}, {"file": "dia1/Dia1 (7).jpg", "title": "Comunidad Carmelita en la Jornada Inaugural", "desc": "Participación activa de la comunidad educativa durante la apertura de la semana."}, {"file": "dia1/Dia1 (8).jpg", "title": "Muestra de Trajes Típicos y Expresiones del Folclor", "desc": "Colorido y danza tradicional representando las raíces caribeñas de Ciénaga."}, {"file": "dia1/Dia1 (9).jpg", "title": "Representación y Liderazgo Carmelita", "desc": "Estudiantes destacados portando el mensaje de pertenencia e identidad institucional."}, {"file": "dia1/Dia1 (10).jpg", "title": "Mesa de Exposición y Material Pedagógico", "desc": "Detalle de carteleras, objetos históricos y guías didácticas del evento."}, {"file": "dia1/Dia1 (11).jpg", "title": "Encuentro Interactivo en los Stands", "desc": "Docentes orientadores acompañando la sustentación de proyectos de grado."}, {"file": "dia1/Dia1 (12).jpg", "title": "Creatividad e Investigación Escolar", "desc": "Despliegue de maquetas del ferrocarril, la plaza y el centro histórico."}, {"file": "dia1/Dia1 (13).jpg", "title": "Integración y Trabajo en Equipo", "desc": "Grupos de trabajo compartiendo su experiencia investigativa con los asistentes."}, {"file": "dia1/Dia1 (14).jpg", "title": "Reconocimiento y Cierre de la Jornada", "desc": "Reflexión comunitaria sobre la importancia de preservar nuestra historia viva."}, {"file": "dia1/Dia1 (15).jpg", "title": "Recuerdo Colectivo · Día 1 Semana Cultural", "desc": "Postal conmemorativa del Día de la Memoria y la Cátedra Carmelita 2026."}, {"file": "dia1/Dia1 (16).jpg", "title": "Muestra Gastronómica y Cultural · Región Amazonía", "desc": "Estudiantes de primaria presentando platos típicos, frutos exóticos y tradiciones de la Amazonía colombiana."}, {"file": "dia1/Dia1 (17).jpg", "title": "Danza y Tradición de las Comunidades Amazónicas", "desc": "Trajes típicos, palmas y expresión corporal representando la biodiversidad y cosmovisión de nuestras regiones."}, {"file": "dia1/Dia1 (18).jpg", "title": "Talento Estudiantil y Orgullo Carmelita", "desc": "Los niños de la IE El Carmen viviendo con alegría el rescate de nuestras raíces y herencias culturales."}, {"file": "dia1/Dia1 (19).jpg", "title": "Representación Ancestral y Danzas Autóctonas", "desc": "Puesta en escena con vestuario ancestral, coronas de hojas y danzas tradicionales en honor a la naturaleza."}, {"file": "dia1/Dia1 (20).jpg", "title": "Acompañamiento Docente y Trabajo en Comunidad", "desc": "El docente orientador junto a su grupo de estudiantes celebrando el éxito de su stand de la Amazonía."}];
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
  