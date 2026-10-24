
    const galleryItems = [
      {"file": "dia4/Dia4 (1).jpg", "title": "Mesa de Recepción y Coordinación del Foro", "desc": "Estudiantes en la mesa de bienvenida junto al mural institucional: «Salvemos la Ciénaga con Pequeñas Acciones - Reciclemos»."},
      {"file": "dia4/Dia4 (2).jpg", "title": "Docente Líder en la Apertura Oficial", "desc": "Intervención protocolaria con micrófono desde el atril de madera tallada, junto a las banderas de Colombia y Ciénaga."},
      {"file": "dia4/Dia4 (3).jpg", "title": "Escenario Principal y Pantalla Digital", "desc": "Vista desde el auditorio hacia el atril, las banderas y la pantalla de transmisión con el afiche oficial del Foro."},
      {"file": "dia4/Dia4 (4).jpg", "title": "Cuerpo Directivo, Docente e Invitados Especiales", "desc": "Directivas de la institución, docentes y facilitadores invitados reunidos en el patio escolar durante la jornada académica."},
      {"file": "dia4/Dia4 (5).jpg", "title": "Mesa #8: Redacción de Conclusiones sobre Tecnología", "desc": "Estudiantes de bachillerato redactando en papelógrafo las propuestas de innovación tecnológica y educación ambiental."},
      {"file": "dia4/Dia4 (6).jpg", "title": "Mesa #5: Diálogo Docente y Estudiantes Promo 2026", "desc": "Docente y estudiantes de último grado concertando estrategias ecológicas y compromisos ciudadanos en mesa redonda."},
      {"file": "dia4/Dia4 (7).jpg", "title": "Orientación Pedagógica en las Mesas de Discusión", "desc": "Docente orientador guiando la reflexión de estudiantes de secundaria sobre los retos ambientales de la región."},
      {"file": "dia4/Dia4 (8).jpg", "title": "Semillero Infantil: Expectativa vs. Realidad de la Ciénaga", "desc": "Niña y niño de primaria exhibiendo sus obras en díptico comparando la Ciénaga que sueñan frente al estado actual."},
      {"file": "dia4/Dia4 (9).jpg", "title": "Expresión Artística Infantil con Témperas", "desc": "Estudiante de primaria concentrado pintando los manglares y el agua de la Ciénaga con pincel en su pupitre."},
      {"file": "dia4/Dia4 (10).jpg", "title": "Docentes Acompañando el Taller de Arte Infantil", "desc": "Docentes sonrientes supervisando las actividades pedagógicas y artísticas de los niños en el aula de clases."},
      {"file": "dia4/Dia4 (11).jpg", "title": "Creatividad y Color por el Medio Ambiente", "desc": "Niñas de primaria combinando colores en paletas plásticas para dar vida a sus dibujos sobre la naturaleza carmelita."},
      {"file": "dia4/Dia4 (12).jpg", "title": "Obra Escolar: «La Ciénaga que Sueño»", "desc": "Alumna de primaria mostrando su dibujo desplegable con sol radiante, aves y cerros verdes sobre aguas limpias."},
      {"file": "dia4/Dia4 (13).jpg", "title": "Concentración y Trabajo Pictórico en el Aula", "desc": "Estudiantes de primaria aplicando témpera con dedicación sobre cartulinas en la jornada artística ambiental."},
      {"file": "dia4/Dia4 (14).jpg", "title": "El Mangle como Eje de Vida y Esperanza", "desc": "Niño de primaria sosteniendo con orgullo su pintura de un árbol de mangle con raíces firmes bajo el sol."},
      {"file": "dia4/Dia4 (15).jpg", "title": "Panorámica del Aula de Primaria en Jornada Artística", "desc": "Vista general del salón con los niños trabajando activamente en sus pupitres azules durante el taller de pintura."},
      {"file": "dia4/Dia4 (16).jpg", "title": "Detalle y Enfoque en la Expresión Infantil", "desc": "Primer plano de una estudiante dando los toques finales a su creación artística en favor de los ecosistemas locales."},
      {"file": "dia4/Dia4 (17).jpg", "title": "Trazando la Diferencia: Expectativa y Realidad", "desc": "Estudiante de primaria dividiendo su hoja para plasmar el contraste entre un humedal limpio y uno afectado por residuos."},
      {"file": "dia4/Dia4 (18).jpg", "title": "Docentes Facilitando Materiales y Pinturas", "desc": "Docentes organizando témperas, pinceles y paletas de mezcla para apoyar la creatividad de los pequeños."},
      {"file": "dia4/Dia4 (19).jpg", "title": "Círculo Pedagógico de Diálogo en Primaria", "desc": "Estudiantes sentados en círculo en el aula mientras la docente orienta la reflexión sobre la protección del entorno."},
      {"file": "dia4/Dia4 (20).jpg", "title": "Díptico Ambiental: Contaminación vs. Conservación", "desc": "Estudiante de primaria exhibiendo su cartel comparativo entre un ecosistema floreciente y la realidad amenazada por basuras."},
      {"file": "dia4/Dia4 (21).jpg", "title": "Sustentación Infantil ante el Mural del Foro", "desc": "Dos estudiantes de primaria exponiendo sus dibujos con micrófono frente al telón «Salvemos la Ciénaga con Pequeñas Acciones»."},
      {"file": "dia4/Dia4 (22).jpg", "title": "Intervención Docente: Reducir, Reciclar y Reutilizar", "desc": "Docente con micrófono motivando a los jóvenes junto al atril y el mural con los principios ecológicos de las 3R."},
      {"file": "dia4/Dia4 (23).jpg", "title": "Cartografía Escolar: Mapa de Protección de la Ciénaga", "desc": "Estudiantes sustentando cartel ilustrado con compromisos: reducir la quema de mangle, reutilizar plásticos y cuidar la fauna."},
      {"file": "dia4/Dia4 (24).jpg", "title": "Mesa #4: Estrategias de Conservación y Manglares", "desc": "Grupo de bachillerato exponiendo propuestas para sembrar manglares, no arrojar químicos al agua y educar a la comunidad."},
      {"file": "dia4/Dia4 (25).jpg", "title": "Mesa #3: Biodiversidad y Recursos Pesqueros", "desc": "Sustentación con micrófono sobre la pesca sostenible, tallas mínimas y protección de hábitats acuáticos en la región."},
      {"file": "dia4/Dia4 (26).jpg", "title": "Mesa #7: Economía Sostenible y Bioeconomía", "desc": "Estudiantes y docente de apoyo socializando alternativas productivas respetuosas con los recursos naturales de la Ciénaga."},
      {"file": "dia4/Dia4 (27).jpg", "title": "Mesa #8: Ciencia, Tecnología y Transferencia de Conocimiento", "desc": "Alumnas de bachillerato exponiendo cómo las universidades pueden transferir datos verificables para solucionar problemas locales."},
      {"file": "dia4/Dia4 (28).jpg", "title": "Lectura de Acuerdos de la Mesa de Innovación #8", "desc": "Estudiante leyendo el pliego de acuerdos y propuestas articuladas entre instituciones educativas y comunidades."},
      {"file": "dia4/Dia4 (29).jpg", "title": "Mesa #2: Gestión del Agua, Contaminación y Saneamiento", "desc": "Sustentación con micrófono de propuestas sobre comités de veedores, monitoreo científico del agua y reciclaje integral."},
      {"file": "dia4/Dia4 (30).jpg", "title": "Panorámica Oficial del Auditorio Carmelita", "desc": "Vista general del patio central cubierto colmado de estudiantes, directivos y docentes participando en el Foro 2026."},
      {"file": "dia4/Dia4 (31).jpg", "title": "Ponencia Magistral: Alineación Estratégica GEF-7 e INVEMAR", "desc": "Expositor en atril presentando en pantalla digital el impacto institucional y la validación científica internacional."},
      {"file": "dia4/Dia4 (32).jpg", "title": "Ponencia Estudiantil: Anamnesis y Valor del Ecosistema", "desc": "Estudiante en atril exponiendo datos sobre la Reserva de la Biosfera, el sustento pesquero y el equilibrio climático."},
      {"file": "dia4/Dia4 (33).jpg", "title": "Ponencia Estudiantil: Sumidero de Carbono vs. Presión Humana", "desc": "Exposición sobre las 528.600 hectáreas del complejo lagunar como captador de CO2 frente a la expansión agrícola e infraestructura."},
      {"file": "dia4/Dia4 (34).jpg", "title": "Ponencia Estudiantil: Microplásticos y Comunidades Palafíticas", "desc": "Alumna explicando el estudio biológico en peces (lisa, mojarra) y talleres participativos en Buenavista, Nueva Venecia y Tasajera."},
      {"file": "dia4/Dia4 (35).jpg", "title": "Ponencia Estudiantil: El Motor del Carbono Azul", "desc": "Disertación en atril explicando la tasa anual de secuestro de carbono de los bosques de manglar y su valor de mitigación climática."},
      {"file": "dia4/Dia4 (36).jpg", "title": "Ponencia Estudiantil: Modelación Hidrodinámica HEC-RAS 1-D", "desc": "Alumna exponiendo el modelo computacional 3D de flujo y comportamiento hídrico de los caños hacia la Ciénaga Grande."},
      {"file": "dia4/Dia4 (37).jpg", "title": "Mesa de Honor de Ponentes Estudiantiles", "desc": "Jóvenes expositores reunidos en la mesa principal con arreglo floral bajo los lemas: «¡Salvemos los Mangles!» y «Actúa con Compromiso»."},
      {"file": "dia4/Dia4 (38).jpg", "title": "Mensaje Directivo en el Atril Central", "desc": "Docente directivo dirigiéndose a la comunidad educativa para destacar el sentido de pertenencia por el territorio caribeño."},
      {"file": "dia4/Dia4 (39).jpg", "title": "Mesa Redonda: Articulación con Madres y Familias", "desc": "Docente facilitadora y madres de familia debatiendo con estudiantes propuestas ambientales para aplicar desde el hogar."},
      {"file": "dia4/Dia4 (40).jpg", "title": "Trabajo Colaborativo en Equipos de Bachillerato", "desc": "Estudiantes organizados en mesas de trabajo revisando las preguntas orientadoras y construyendo consensos."},
      {"file": "dia4/Dia4 (41).jpg", "title": "Dinamización Pedagógica: «Somos Comunidad»", "desc": "Docentes acompañando mesa de diálogo juvenil frente al mural escolar, fomentando la argumentación y la participación."},
      {"file": "dia4/Dia4 (42).jpg", "title": "Mesa de Trabajo: Oportunidades y Empleo Sostenible", "desc": "Estudiantes, acudiente y facilitador universitario debatiendo cómo generar ingresos sin degradar los recursos naturales."},
      {"file": "dia4/Dia4 (43).jpg", "title": "Acompañamiento en la Redacción del Pliego Ambiental", "desc": "Docente supervisando la redacción de propuestas de los estudiantes en papel kraft sobre el cuidado del medio ambiente."},
      {"file": "dia4/Dia4 (44).jpg", "title": "Panorámica de las Mesas de Trabajo en el Patio", "desc": "Múltiples mesas redondas funcionando en simultáneo en el patio central con estudiantes de la Promo 2026 y bachillerato."},
      {"file": "dia4/Dia4 (45).jpg", "title": "Diálogo Intergeneracional y Asesoría Técnica", "desc": "Docentes orientadores guiando a estudiantes en la estructura lógica de sus proyectos de conservación escolar."},
      {"file": "dia4/Dia4 (46).jpg", "title": "Consolidación Colectiva del Pliego de Acuerdos", "desc": "Docente y estudiantes dando cierre a la mesa redonda con la firma y redacción final de compromisos por la Ciénaga."},
      {"file": "dia4/gfm/gfm_ciencia_1.jpg", "title": "Pequeños Científicos en Laboratorio Experimental", "desc": "Tres estudiantes carmelitas con batas blancas y gafas de seguridad en su mesa experimental con balanza de madera, recipientes y reactivos frente al mural decorativo «Jugando Ando Experimentando»."},
      {"file": "dia4/gfm/gfm_ciencia_2.jpg", "title": "Taller Audiovisual: «¿Qué es la Ciencia?»", "desc": "Salón de clases infantil con los alumnos en sillitas de colores atentos a la proyección pedagógica sobre la ciencia y la exploración del medio natural."},
      {"file": "dia4/gfm/gfm_ciencia_3.jpg", "title": "Semillero Infantil en Acción Interactiva", "desc": "Vista del aula donde los niños participan en la explicación y demostración práctica de conceptos científicos guiados por sus docentes."}
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
  