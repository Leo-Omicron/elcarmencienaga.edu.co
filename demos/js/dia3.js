
    const galleryItems = [
      {"file": "dia3/Dia3 (1).jpg", "title": "Apertura del Gran Desfile Folclórico e Inauguración", "desc": "Estudiantes, comparsas y docentes iniciando el recorrido con entusiasmo y alegría por las calles ciengueras."},
      {"file": "dia3/Dia3 (2).jpg", "title": "Comparsas Tradicionales y Expresión Cultural", "desc": "Bailarines luciendo trajes típicos azul rey y dorado, enriqueciendo la tradición folclórica del Caribe magdalenense."},
      {"file": "dia3/Dia3 (3).jpg", "title": "Valores Carmelitas: «Cooperación y Respeto»", "desc": "Estudiantes portando mensajes alusivos al juego limpio, la fraternidad y el trabajo en equipo en el deporte escolar."},
      {"file": "dia3/Dia3 (4).jpg", "title": "Color, Danza y Alegría en el Recorrido", "desc": "La comunidad de vecinos, acudientes y familias acompañando el paso festivo de los grupos estudiantiles."},
      {"file": "dia3/Dia3 (5).jpg", "title": "Llegada y Concentración en Cancha Brisas del Mar", "desc": "El estudiantado formándose para los actos protocolarios y la gran fiesta de apertura deportiva."},
      {"file": "dia3/Dia3 (6).jpg", "title": "Actos Protocolarios y Símbolos Patrios", "desc": "Directivos docentes, jurados y estudiantes entonando los himnos con respeto, orgullo y solemnidad institucional."},
      {"file": "dia3/Dia3 (7).jpg", "title": "Mesa Principal y Docentes Carmelitas", "desc": "El cuerpo directivo y docente liderando con compromiso la jornada deportiva e integradora institucional."},
      {"file": "dia3/Dia3 (8).jpg", "title": "Presentación Oficial de las Delegaciones", "desc": "Equipos de fútbol y grupos de porristas formados con los estandartes representativos de cada grado escolar."},
      {"file": "dia3/Dia3 (9).jpg", "title": "Juramento Deportivo y Compromiso Carmelita", "desc": "Promesa solemne de competir con honor, disciplina, respeto a los rivales y sana convivencia."},
      {"file": "dia3/Dia3 (10).jpg", "title": "Porristas Carmelitas y Animación Infantil", "desc": "Pequeñas animadoras llenando de energía, ritmo, sonrisas y color los actos inaugurales del torneo."},
      {"file": "dia3/Dia3 (11).jpg", "title": "Delegación Grado 4°: «Los Delfines F.C.»", "desc": "Niños y niñas luciendo sus uniformes amarillos y azules con banderines en alto y gran espíritu deportivo."},
      {"file": "dia3/Dia3 (12).jpg", "title": "Delegación Grado 5°: «Jaguares del Amazonas F.C.»", "desc": "Estudiantes portando el escudo emblemático del jaguar y ondeando banderas de paz y esperanza."},
      {"file": "dia3/Dia3 (13).jpg", "title": "Delegación Grado 6°A: Equipo «Fénix»", "desc": "Grupo estudiantil junto a su docente portando la pancarta con estrellas y banderas blancas por la convivencia escolar."},
      {"file": "dia3/Dia3 (14).jpg", "title": "Desfile de la Delegación «Jaguares del Amazonas F.C.»", "desc": "Alumnos del grado 5° marchando orgullosos con camisetas tricolor y banderines azules y blancos en la jornada deportiva."},
      {"file": "dia3/Dia3 (15).jpg", "title": "Desfile Oficial: «Los Delfines F.C.» Grado 4°", "desc": "El equipo y sus porristas desfilando con alegría y coordinación en la jornada deportiva carmelita."},
      {"file": "dia3/Dia3 (16).jpg", "title": "Delegación Grado 3°: «Llaneros F.C.»", "desc": "Trajes folclóricos azul y amarillo, estandarte del corcel llanero y banderines al viento abriendo camino."},
      {"file": "dia3/Dia3 (17).jpg", "title": "Semillero Carmelita: Grado 2° «Construyendo Sueños»", "desc": "Las pequeñas porristas de segundo grado con sus faldas rojas y pompones metálicos llenando de ternura y ovaciones el desfile."}
    ,
      {"file": "dia3/Dia3 (18).jpg", "title": "Delegación Grado 5°: «Jaguares del Amazonas F.C.»", "desc": "Estudiantes y docentes luciendo la camiseta tricolor junto al estandarte representativo del jaguar amazónico."},
      {"file": "dia3/Dia3 (19).jpg", "title": "Marcha Festiva: «Jaguares del Amazonas F.C.»", "desc": "La delegación de quinto grado avanzando con banderas y alegría durante el gran desfile deportivo institucional."},
      {"file": "dia3/Dia3 (20).jpg", "title": "Llegada a la Cancha Brisas del Mar: Grado 5°", "desc": "Concentración en el terreno de juego para los actos protocolarios y el juramento de juego limpio."},
      {"file": "dia3/Dia3 (21).jpg", "title": "La Barra Carmelita: Semillero Infantil con Pompones", "desc": "Los más pequeños de la institución llenando de color, aplausos y alegría las graderías del evento inaugural."}
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
  