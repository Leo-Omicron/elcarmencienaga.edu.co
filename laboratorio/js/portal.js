/**
 * Motor interactivo del Portal Institucional — IE El Carmen
 * Arquitectura Híbrida (Opción A): Cartelera JSON GitOps + Conector WordPress REST API
 * Incluye filtrado animado de tarjetas y personalización dinámica de módulos en construcción.
 */
(function () {
  'use strict';

  /* 1. Menú de navegación móvil adaptable */
  const navToggle = document.getElementById('portal-nav-toggle');
  const navMenu = document.getElementById('portal-nav-menu');

  if (navToggle && navMenu) {
    navToggle.addEventListener('click', function () {
      const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
      navToggle.setAttribute('aria-expanded', String(!isExpanded));
      navMenu.classList.toggle('is-open', !isExpanded);
    });

    navMenu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        if (window.innerWidth <= 720) {
          navToggle.setAttribute('aria-expanded', 'false');
          navMenu.classList.remove('is-open');
        }
      });
    });
  }

  /* 2. Cartelera Híbrida de Actualidad con Filtrado Animado */
  const newsGrid = document.getElementById('portal-news-grid');
  const filterButtons = document.querySelectorAll('.news-filter-btn');
  const statusText = document.getElementById('portal-news-source-text');
  let activeCategory = 'todas';
  let loadedItems = null;
  let filterTimer = null;

  const CATEGORY_NAMES = {
    todas: 'Todas las categorías',
    rectoria: 'Rectoría',
    academico: 'Académico y Ciencia',
    deportes: 'Deportes y Convivencia',
    comunidad: 'Comunidad'
  };

  function prefersReducedMotion() {
    return (
      window.matchMedia &&
      window.matchMedia('(prefers-reduced-motion: reduce)').matches
    );
  }

  function sanitizePlainText(htmlString) {
    const parser = new DOMParser();
    const doc = parser.parseFromString(htmlString || '', 'text/html');
    return (doc.body.textContent || '').trim();
  }

  function formatDateEs(isoDate) {
    try {
      const d = new Date(isoDate);
      if (Number.isNaN(d.getTime())) return isoDate;
      return d.toLocaleDateString('es-CO', {
        day: 'numeric',
        month: 'long',
        year: 'numeric'
      });
    } catch (_) {
      return isoDate;
    }
  }

  function mapWpPostToItem(post) {
    let imageUrl = 'escudo.jpg';
    let imageAlt = 'Comunicado oficial IE El Carmen';
    if (
      post._embedded &&
      post._embedded['wp:featuredmedia'] &&
      post._embedded['wp:featuredmedia'][0] &&
      post._embedded['wp:featuredmedia'][0].source_url
    ) {
      imageUrl = post._embedded['wp:featuredmedia'][0].source_url;
      imageAlt = post._embedded['wp:featuredmedia'][0].alt_text || imageAlt;
    }

    return {
      id: 'wp-' + post.id,
      category: 'comunidad',
      categoryLabel: 'Editorial WordPress',
      date: formatDateEs(post.date),
      author: 'Portal Comunicaciones',
      title: sanitizePlainText(post.title && post.title.rendered),
      summary: sanitizePlainText(post.excerpt && post.excerpt.rendered).slice(0, 190) + '…',
      image: imageUrl,
      imageAlt: imageAlt,
      linkText: 'Leer comunicado completo',
      linkUrl: post.link || '#actualidad',
      pinned: false
    };
  }

  function createNewsCardElement(item, index) {
    const article = document.createElement('article');
    article.className = 'news-card';
    article.setAttribute('data-category', item.category || 'comunidad');
    if (!prefersReducedMotion() && typeof index === 'number') {
      article.style.animationDelay = String(index * 55) + 'ms';
    }

    const mediaDiv = document.createElement('div');
    mediaDiv.className = 'news-card-media';

    const img = document.createElement('img');
    img.className = 'news-card-img';
    img.src = item.image || 'escudo.jpg';
    img.alt = item.imageAlt || item.title;
    img.loading = 'lazy';

    const badge = document.createElement('span');
    badge.className = 'news-category-badge badge-' + (item.category || 'comunidad');
    badge.textContent = item.categoryLabel || 'Institucional';

    mediaDiv.appendChild(img);
    mediaDiv.appendChild(badge);

    const contentDiv = document.createElement('div');
    contentDiv.className = 'news-card-content';

    const metaDiv = document.createElement('div');
    metaDiv.className = 'news-meta';

    const timeSpan = document.createElement('span');
    timeSpan.textContent = item.date || '';

    const authorSpan = document.createElement('span');
    authorSpan.textContent = item.author || 'IE El Carmen';

    metaDiv.appendChild(timeSpan);
    metaDiv.appendChild(authorSpan);

    const h3 = document.createElement('h3');
    h3.className = 'news-card-title';
    h3.textContent = item.title || '';

    const p = document.createElement('p');
    p.className = 'news-card-summary';
    p.textContent = item.summary || '';

    const actionsDiv = document.createElement('div');
    actionsDiv.className = 'news-card-actions';

    const link = document.createElement('a');
    link.className = 'news-card-link';
    link.href = item.linkUrl || '#actualidad';
    if (/^https?:\/\//i.test(link.href)) {
      link.target = '_blank';
      link.rel = 'noopener noreferrer';
    }
    link.textContent = (item.linkText || 'Conocer más') + ' →';
    actionsDiv.appendChild(link);

    if (item.secondaryLinkUrl) {
      const secLink = document.createElement('a');
      secLink.className = 'news-card-link news-card-link-sec';
      secLink.href = item.secondaryLinkUrl;
      if (/^https?:\/\//i.test(secLink.href)) {
        secLink.target = '_blank';
        secLink.rel = 'noopener noreferrer';
      }
      secLink.textContent = (item.secondaryLinkText || 'Ver más') + ' →';
      actionsDiv.appendChild(secLink);
    }

    contentDiv.appendChild(metaDiv);
    contentDiv.appendChild(h3);
    contentDiv.appendChild(p);
    contentDiv.appendChild(actionsDiv);

    article.appendChild(mediaDiv);
    article.appendChild(contentDiv);
    return article;
  }

  function updateStatusCounter(visibleCount, totalCount, category) {
    if (!statusText) return;
    if (category === 'todas') {
      statusText.textContent =
        'Mostrando ' + visibleCount + ' publicaciones · Cartelera Híbrida Activa';
    } else {
      const label = CATEGORY_NAMES[category] || category;
      statusText.textContent =
        'Mostrando ' +
        visibleCount +
        ' de ' +
        totalCount +
        ' publicaciones · ' +
        label;
    }
  }

  function commitCategoryFilter(category) {
    if (!newsGrid) return;

    if (loadedItems && Array.isArray(loadedItems)) {
      const filtered =
        category === 'todas'
          ? loadedItems
          : loadedItems.filter(function (item) {
              return item.category === category;
            });
      newsGrid.replaceChildren();
      filtered.forEach(function (item, idx) {
        newsGrid.appendChild(createNewsCardElement(item, idx));
      });
      updateStatusCounter(filtered.length, loadedItems.length, category);
    } else {
      const staticCards = Array.from(newsGrid.querySelectorAll('.news-card'));
      let visibleIndex = 0;
      staticCards.forEach(function (card) {
        const cardCat = card.getAttribute('data-category');
        const matches = category === 'todas' || cardCat === category;
        card.classList.remove('is-filtering-out');
        card.classList.toggle('is-hidden', !matches);
        card.hidden = !matches;
        if (matches) {
          if (!prefersReducedMotion()) {
            card.style.animation = 'none';
            void card.offsetWidth;
            card.style.animation = '';
            card.style.animationDelay = String(visibleIndex * 55) + 'ms';
          }
          visibleIndex += 1;
        }
      });
      updateStatusCounter(visibleIndex, staticCards.length, category);
    }
  }

  function applyCategoryFilter(category, animate) {
    activeCategory = category;
    filterButtons.forEach(function (btn) {
      const isMatch = btn.getAttribute('data-filter') === category;
      btn.classList.toggle('is-active', isMatch);
      btn.setAttribute('aria-pressed', String(isMatch));
    });

    if (!newsGrid) return;

    if (filterTimer) {
      clearTimeout(filterTimer);
      filterTimer = null;
    }

    if (!animate || prefersReducedMotion()) {
      commitCategoryFilter(category);
      return;
    }

    const currentVisibleCards = newsGrid.querySelectorAll(
      '.news-card:not(.is-hidden)'
    );
    currentVisibleCards.forEach(function (card) {
      card.classList.add('is-filtering-out');
    });

    filterTimer = setTimeout(function () {
      commitCategoryFilter(category);
    }, 150);
  }

  filterButtons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      const category = btn.getAttribute('data-filter') || 'todas';
      applyCategoryFilter(category, true);
    });
  });

  async function initHybridNewsBoard() {
    if (!newsGrid) return;
    try {
      const response = await fetch('data/noticias.json', { cache: 'no-cache' });
      if (!response.ok) return;
      const data = await response.json();
      let items = Array.isArray(data.items) ? data.items.slice() : [];

      if (data.wordpress && data.wordpress.enabled && data.wordpress.endpoint) {
        try {
          const controller = new AbortController();
          const timer = setTimeout(function () {
            controller.abort();
          }, data.wordpress.timeoutMs || 4500);
          const wpResponse = await fetch(data.wordpress.endpoint, {
            signal: controller.signal
          });
          clearTimeout(timer);
          if (wpResponse.ok) {
            const wpPosts = await wpResponse.json();
            if (Array.isArray(wpPosts) && wpPosts.length > 0) {
              const mappedWp = wpPosts.map(mapWpPostToItem);
              const pinned = items.filter(function (i) {
                return i.pinned;
              });
              const regular = items.filter(function (i) {
                return !i.pinned;
              });
              items = pinned.concat(mappedWp, regular).slice(0, 9);
            }
          }
        } catch (_) {
          /* Conserva respaldo local GitOps JSON */
        }
      }

      if (items.length > 0) {
        loadedItems = items;
        applyCategoryFilter(activeCategory, false);
      }
    } catch (_) {
      /* En protocolo file:// o sin red, utiliza las tarjetas HTML pre-renderizadas */
      applyCategoryFilter(activeCategory, false);
    }
  }

  initHybridNewsBoard();

  /* 3. Personalización dinámica de la página de Sección / Módulo en Construcción */
  const constructionTitle = document.getElementById('construction-module-title');
  const constructionBadge = document.getElementById('construction-module-badge');
  const constructionLead = document.getElementById('construction-module-lead');
  const constructionFeatures = document.getElementById('construction-module-features');

  const MODULES_CATALOG = {
    pei: {
      badge: 'Documento Rectoral en Digitalización',
      title: 'Proyecto Educativo Institucional (PEI)',
      lead: 'Estamos preparando el visor interactivo y el documento oficial descargable del Proyecto Educativo Institucional de la I. E. El Carmen, con nuestro horizonte pedagógico, modelo curricular y proyectos transversales.',
      features: [
        'Consulta por capítulos del Horizonte Institucional y Modelo Pedagógico.',
        'Descarga verificada en formato PDF accesible para toda la comunidad.',
        'Articulación con los proyectos obligatorios y las sedes Micael Cotes y Guillermo F. Morán.'
      ]
    },
    'manual-convivencia': {
      badge: 'Normatividad Escolar · Ley 1620',
      title: 'Manual de Convivencia Escolar',
      lead: 'Esta sección alojará la versión digital navegable del Manual de Convivencia Escolar, incluyendo derechos, deberes, ruta de atención integral y protocolos del Comité Escolar de Convivencia.',
      features: [
        'Buscador rápido de acuerdos de convivencia, derechos y estímulos estudiantiles.',
        'Ruta de Atención Integral para la Convivencia Escolar y debido proceso.',
        'Pautas oficiales de presentación personal y uniformes institucionales.'
      ]
    },
    siee: {
      badge: 'Evaluación Académica · Decreto 1290',
      title: 'Sistema Institucional de Evaluación de Estudiantes (SIEE)',
      lead: 'Estamos estructurando la guía pública del SIEE con la escala de valoración institucional, criterios de promoción, planes de apoyo y periodos académicos vigentes.',
      features: [
        'Escala de valoración institucional y equivalencia con la escala nacional.',
        'Criterios de promoción, comisiones de evaluación y seguimiento.',
        'Calendario de entregas de informes periódicos a las familias.'
      ]
    },
    'gobierno-escolar': {
      badge: 'Participación y Democracia Escolar',
      title: 'Órganos del Gobierno Escolar y Estamentos',
      lead: 'Aquí encontrarás las actas públicas, integrantes y canales de participación del Consejo Directivo, Consejo Académico, Personería Estudiantil, Contraloría Escolar y Consejo de Padres.',
      features: [
        'Estructura e integrantes vigentes del Consejo Directivo y Consejo Académico.',
        'Propuestas y seguimiento de la Personería y Contraloría Estudiantil.',
        'Cronograma de asambleas y escuela de padres de familia.'
      ]
    },
    'wordpress-comunidad': {
      badge: 'Arquitectura Híbrida · Módulo Editorial',
      title: 'Portal de Comunicaciones, Blogs Docentes y Foros (WordPress)',
      lead: 'Estamos configurando el módulo editorial en WordPress conectado por API REST a nuestra portada principal para la publicación rápida de circulares, periódico escolar digital, blogs de aula y foros.',
      features: [
        'Publicación inmediata de avisos y circulares desde dispositivos móviles o escritorio.',
        'Espacio de blogs académicos y producción literaria de docentes y estudiantes.',
        'Repositorio histórico de comunicados oficiales de Rectoría.'
      ]
    },
    'plataforma-notas': {
      badge: 'Aplicaciones Web e Intranet Institucional',
      title: 'Plataforma de Gestión Académica, Notas y Consolidados',
      lead: 'Este entorno integrará nuestras aplicaciones web institucionales con inicio de sesión seguro para docentes, directivos y familias: control de notas, consolidados de evaluación y convivencia escolar.',
      features: [
        'Acceso autenticado mediante cuentas institucionales (@elcarmencienaga.edu.co).',
        'Módulo de Consolidados Académicos, seguimiento por periodo y estadísticas.',
        'Herramientas digitales de apoyo pedagógico y gestión de aula.'
      ]
    },
    'redes-sociales': {
      badge: 'Canales Digitales Oficiales en Integración',
      title: 'Nuevas Redes Sociales Institucionales (Facebook, X, YouTube, WhatsApp y TikTok)',
      lead: 'Actualmente nuestro canal oficial verificado y activo es Instagram (@ieelcarmen). Estamos configurando y verificando las cuentas institucionales de Facebook, YouTube, X (Twitter), canal de difusión de WhatsApp y TikTok para ampliar nuestra cobertura comunitaria.',
      features: [
        'Cuenta oficial de Instagram activa y verificada: @ieelcarmen.',
        'Próxima apertura del canal audiovisual en YouTube y página oficial en Facebook.',
        'Canal informativo de WhatsApp y cuenta en X para avisos rápidos a las familias.'
      ]
    }
  };

  if (constructionTitle && window.location.search) {
    const params = new URLSearchParams(window.location.search);
    const modKey = params.get('modulo');
    if (modKey && MODULES_CATALOG[modKey]) {
      const info = MODULES_CATALOG[modKey];
      document.title = info.title + ' | En Construcción · IE El Carmen';
      if (constructionBadge) constructionBadge.textContent = info.badge;
      constructionTitle.textContent = info.title;
      if (constructionLead) constructionLead.textContent = info.lead;
      if (constructionFeatures && Array.isArray(info.features)) {
        constructionFeatures.replaceChildren();
        info.features.forEach(function (featText) {
          const li = document.createElement('li');
          const icon = document.createElement('span');
          icon.className = 'construction-check';
          icon.setAttribute('aria-hidden', 'true');
          icon.textContent = '✓';
          const text = document.createElement('span');
          text.textContent = featText;
          li.appendChild(icon);
          li.appendChild(text);
          constructionFeatures.appendChild(li);
        });
      }
    }
  }
})();
