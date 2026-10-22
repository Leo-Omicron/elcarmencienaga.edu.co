# -*- coding: utf-8 -*-
import os

html_template = '''<!doctype html>
<html lang="es-CO">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex,nofollow">
  <meta name="description" content="Galería fotográfica y registro audiovisual oficial del Día 4: Gran Foro Educativo Institucional «Salvemos la Ciénaga» 2026. Semana Cultural de la IE El Carmen en Ciénaga, Magdalena.">
  <meta name="theme-color" content="#064e3b">
  <title>Día 4: Gran Foro «Salvemos la Ciénaga» 2026 · Galería Oficial | IE El Carmen</title>

  <!-- Google Fonts: Outfit & Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
    :root {
      --primary: #191253;
      --primary-dark: #0d0933;
      --primary-light: #2c2282;
      --accent-green: #10b981;
      --accent-green-dark: #059669;
      --accent-green-deep: #064e3b;
      --accent-green-light: #d1fae5;
      --accent-teal: #0d9488;
      --accent-gold: #f59e0b;
      --accent-gold-dark: #d97706;
      --accent-gold-light: #fef3c7;
      --accent-blue: #0284c7;
      --accent-blue-dark: #0369a1;
      --accent-blue-light: #e0f2fe;
      --bg-surface: #f8fafc;
      --bg-card: #ffffff;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --border-subtle: #e2e8f0;
      --shadow-sm: 0 2px 4px rgba(6, 78, 59, 0.04);
      --shadow-md: 0 8px 24px rgba(6, 78, 59, 0.08);
      --shadow-lg: 0 20px 35px -8px rgba(6, 78, 59, 0.16);
      --radius-sm: 8px;
      --radius-md: 16px;
      --radius-lg: 24px;
      --radius-full: 9999px;
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
      font-size: 16px;
    }

    body {
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      background-color: var(--bg-surface);
      color: var(--text-main);
      line-height: 1.6;
      overflow-x: hidden;
    }

    h1, h2, h3, h4, h5, .font-heading {
      font-family: 'Outfit', sans-serif;
      font-weight: 700;
      line-height: 1.2;
      color: var(--primary);
    }

    a {
      color: inherit;
      text-decoration: none;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .container {
      width: min(1200px, 100% - 2.5rem);
      margin-inline: auto;
    }

    /* Top Ribbon */
    .top-ribbon {
      background: linear-gradient(90deg, #064e3b 0%, #191253 60%, #0d9488 100%);
      color: #e2e8f0;
      font-size: 0.82rem;
      padding: 0.5rem 0;
      border-bottom: 2px solid var(--accent-green);
    }
    .top-ribbon .container {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 0.5rem;
    }

    /* Header Navegación */
    header {
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(12px);
      position: sticky;
      top: 0;
      z-index: 100;
      border-bottom: 1px solid var(--border-subtle);
      box-shadow: var(--shadow-sm);
    }
    .nav-container {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-block: 0.85rem;
      gap: 1rem;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 0.85rem;
      flex-shrink: 0;
    }
    .brand-logo {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      object-fit: cover;
      border: 2px solid var(--accent-green);
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    }
    .brand-text h2 {
      font-size: 1.15rem;
      font-weight: 800;
      line-height: 1.1;
      color: var(--primary);
    }
    .brand-text p {
      font-size: 0.74rem;
      color: var(--text-muted);
      font-weight: 600;
    }
    .nav-actions {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      flex-wrap: wrap;
      justify-content: flex-end;
    }
    .btn-back-nav {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: #ecfdf5;
      color: var(--accent-green-dark);
      border: 1px solid #a7f3d0;
      padding: 0.45rem 0.95rem;
      border-radius: var(--radius-full);
      font-weight: 700;
      font-size: 0.84rem;
      white-space: nowrap;
    }
    .btn-back-nav:hover {
      background: var(--accent-green-dark);
      color: #ffffff;
      border-color: var(--accent-green-dark);
      transform: translateY(-1px);
    }

    /* Hero de la Galería Dedicada */
    .day-hero {
      background: linear-gradient(180deg, #ffffff 0%, #f0fdf4 50%, #ecfeff 100%);
      padding-block: 3.5rem 3rem;
      border-bottom: 1px solid #d1fae5;
    }
    .breadcrumb-nav {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.84rem;
      font-weight: 600;
      color: var(--text-muted);
      margin-bottom: 1.25rem;
      flex-wrap: wrap;
    }
    .breadcrumb-nav a {
      color: var(--accent-green-dark);
      text-decoration: underline;
    }
    .day-date-tag {
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      background: #d1fae5;
      color: #065f46;
      font-size: 0.82rem;
      font-weight: 800;
      padding: 0.35rem 0.9rem;
      border-radius: var(--radius-full);
      border: 1px solid #a7f3d0;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-bottom: 1rem;
    }
    .day-hero-title {
      font-size: clamp(2.2rem, 4.5vw, 3.5rem);
      font-weight: 900;
      color: var(--primary);
      letter-spacing: -0.02em;
      line-height: 1.12;
      margin-bottom: 1rem;
    }
    .day-hero-title span {
      background: linear-gradient(135deg, #059669 0%, #10b981 50%, #0284c7 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }
    .day-hero-lead {
      font-size: 1.12rem;
      color: var(--text-muted);
      max-width: 900px;
      line-height: 1.65;
      margin-bottom: 2rem;
    }
    .hero-quick-ctas {
      display: flex;
      gap: 0.85rem;
      flex-wrap: wrap;
      align-items: center;
    }
    .btn-cta-primary {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: linear-gradient(135deg, #10b981 0%, #059669 100%);
      color: #ffffff;
      font-weight: 800;
      font-size: 0.95rem;
      padding: 0.85rem 1.6rem;
      border-radius: var(--radius-full);
      box-shadow: 0 4px 14px rgba(5, 150, 105, 0.35);
    }
    .btn-cta-primary:hover {
      background: #047857;
      color: #ffffff;
      transform: translateY(-2px);
    }
    .btn-cta-secondary {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: #ffffff;
      color: var(--primary);
      border: 1.5px solid var(--border-subtle);
      font-weight: 700;
      font-size: 0.95rem;
      padding: 0.85rem 1.5rem;
      border-radius: var(--radius-full);
    }
    .btn-cta-secondary:hover {
      border-color: var(--accent-green);
      background: #f8fafc;
    }

    /* Stats Ribbon */
    .stats-ribbon {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1.25rem;
      margin-top: 2.5rem;
      padding: 1.25rem 1.5rem;
      background: rgba(255, 255, 255, 0.85);
      backdrop-filter: blur(8px);
      border: 1px solid #a7f3d0;
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-sm);
    }
    .stat-item {
      display: flex;
      align-items: center;
      gap: 0.85rem;
    }
    .stat-icon {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.35rem;
      background: #d1fae5;
      color: #065f46;
      flex-shrink: 0;
    }
    .stat-text strong {
      display: block;
      font-size: 1.35rem;
      font-family: 'Outfit', sans-serif;
      color: var(--primary);
      line-height: 1;
    }
    .stat-text span {
      font-size: 0.8rem;
      color: var(--text-muted);
      font-weight: 600;
    }

    /* Secciones */
    .section-padding {
      padding-block: 4.5rem;
    }
    .section-title-wrap {
      text-align: center;
      max-width: 820px;
      margin-inline: auto;
      margin-bottom: 2.75rem;
    }
    .section-eyebrow {
      font-size: 0.84rem;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      font-weight: 800;
      color: var(--accent-green-dark);
      margin-bottom: 0.5rem;
      display: block;
    }
    .section-title {
      font-size: clamp(2rem, 3.5vw, 2.7rem);
      margin-bottom: 0.8rem;
    }
    .section-lead {
      color: var(--text-muted);
      font-size: 1.05rem;
    }

    /* Videos Horizontales 16:9 */
    .video-group-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 0.75rem;
      margin-bottom: 1.5rem;
      padding-bottom: 0.75rem;
      border-bottom: 2px solid #e2e8f0;
    }
    .video-group-header h3 {
      font-size: 1.3rem;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .badge-count {
      display: inline-flex;
      align-items: center;
      padding: 0.3rem 0.8rem;
      border-radius: var(--radius-full);
      font-size: 0.82rem;
      font-weight: 800;
    }

    .videos-h-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 1.75rem;
      align-items: stretch;
      margin-bottom: 3.5rem;
    }
    .video-h-card {
      background: var(--bg-card);
      border-radius: var(--radius-md);
      overflow: hidden;
      border: 1px solid var(--border-subtle);
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .video-h-card:hover {
      transform: translateY(-4px);
      box-shadow: var(--shadow-md);
    }
    .video-h-frame {
      position: relative;
      width: 100%;
      padding-top: 56.25%; /* 16:9 */
      background: #0f172a;
    }
    .video-h-frame iframe {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      border: 0;
    }
    .video-card-body {
      padding: 1.25rem 1.4rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      flex-grow: 1;
      gap: 1rem;
    }
    .video-badge-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      font-size: 0.74rem;
      font-weight: 800;
      padding: 0.25rem 0.65rem;
      border-radius: var(--radius-full);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.5rem;
    }
    .video-badge-pill.green {
      background: #d1fae5;
      color: #065f46;
    }
    .video-badge-pill.blue {
      background: #e0f2fe;
      color: #0369a1;
    }
    .video-badge-pill.gold {
      background: #fef3c7;
      color: #92400e;
    }
    .video-card-body h3 {
      font-size: 1.05rem;
      margin-bottom: 0.4rem;
      color: var(--primary);
    }
    .video-card-body p {
      font-size: 0.88rem;
      color: var(--text-muted);
      line-height: 1.5;
    }
    .btn-yt-link {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.4rem;
      background: #fee2e2;
      color: #991b1b;
      font-weight: 700;
      font-size: 0.85rem;
      padding: 0.55rem 1rem;
      border-radius: var(--radius-sm);
      border: 1px solid #fecaca;
    }
    .btn-yt-link:hover {
      background: #dc2626;
      color: #ffffff;
      border-color: #dc2626;
    }

    /* Grilla de YouTube Shorts (4 Videos Verticales 9:16) */
    .shorts-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 2rem;
      margin-bottom: 3.5rem;
    }
    .short-card-item {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .video-v-mockup {
      position: relative;
      width: 100%;
      max-width: 310px;
      padding-top: 177.77%; /* 9:16 */
      background: #000000;
      border-radius: 28px;
      overflow: hidden;
      border: 5px solid #1e293b;
      box-shadow: 0 14px 30px rgba(0, 0, 0, 0.22);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .video-v-mockup:hover {
      transform: translateY(-4px);
      box-shadow: 0 18px 36px rgba(0, 0, 0, 0.3);
    }
    .video-v-mockup iframe {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      border: 0;
    }
    .short-info {
      text-align: center;
      margin-top: 1.15rem;
      width: 100%;
      max-width: 310px;
    }
    .short-info h4 {
      font-size: 1.05rem;
      color: var(--primary);
      margin-block: 0.35rem 0.25rem;
      line-height: 1.3;
    }
    .short-info p {
      font-size: 0.84rem;
      color: var(--text-muted);
      margin-bottom: 0.75rem;
      line-height: 1.45;
    }

    /* Grilla de Fotos */
    .photos-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 1.5rem;
    }
    .photo-card {
      background: var(--bg-card);
      border-radius: var(--radius-md);
      overflow: hidden;
      border: 1px solid var(--border-subtle);
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      cursor: pointer;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .photo-card:hover {
      transform: translateY(-5px);
      box-shadow: var(--shadow-md);
      border-color: #a7f3d0;
    }
    .photo-frame {
      position: relative;
      width: 100%;
      aspect-ratio: 4 / 3;
      background: #0f172a;
      overflow: hidden;
    }
    .photo-frame img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.4s ease;
    }
    .photo-card:hover .photo-frame img {
      transform: scale(1.04);
    }
    .photo-badge-idx {
      position: absolute;
      top: 0.75rem;
      left: 0.75rem;
      background: rgba(15, 23, 42, 0.78);
      backdrop-filter: blur(6px);
      color: #ffffff;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 0.25rem 0.55rem;
      border-radius: 4px;
      border: 1px solid rgba(255, 255, 255, 0.15);
    }
    .photo-badge-team {
      position: absolute;
      bottom: 0.75rem;
      right: 0.75rem;
      background: rgba(5, 150, 105, 0.9);
      backdrop-filter: blur(6px);
      color: #ffffff;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 0.25rem 0.6rem;
      border-radius: var(--radius-full);
      box-shadow: 0 2px 6px rgba(0,0,0,0.3);
    }
    .photo-body {
      padding: 1.15rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      flex-grow: 1;
      gap: 0.75rem;
    }
    .photo-body h3 {
      font-size: 0.98rem;
      color: var(--primary);
      margin-bottom: 0.3rem;
      line-height: 1.3;
    }
    .photo-body p {
      font-size: 0.84rem;
      color: var(--text-muted);
      line-height: 1.45;
    }
    .photo-zoom-hint {
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--accent-green-dark);
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
    }

    /* Banner Google Fotos */
    .gphotos-banner {
      background: linear-gradient(135deg, #064e3b 0%, #191253 100%);
      border-radius: var(--radius-lg);
      padding: clamp(2rem, 4vw, 3rem);
      color: #ffffff;
      margin-top: 3.5rem;
      box-shadow: var(--shadow-lg);
      position: relative;
      overflow: hidden;
    }
    .gphotos-content {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1.5rem;
      position: relative;
      z-index: 2;
    }
    .btn-gphotos-big {
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      background: linear-gradient(135deg, #10b981 0%, #059669 100%);
      color: #ffffff;
      font-weight: 900;
      font-size: 1rem;
      padding: 0.95rem 1.8rem;
      border-radius: var(--radius-full);
      box-shadow: 0 4px 16px rgba(16, 185, 129, 0.4);
    }
    .btn-gphotos-big:hover {
      background: #047857;
      transform: translateY(-2px);
    }

    /* Barra de Navegación entre Días */
    .day-nav-bar {
      background: #ffffff;
      border-block: 1px solid var(--border-subtle);
      padding: 1.25rem 0;
      margin-top: 3rem;
    }
    .day-nav-bar .container {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
    }

    /* Footer */
    footer {
      background: #0d0933;
      color: #94a3b8;
      padding-block: 3rem 2rem;
      border-top: 4px solid var(--accent-green);
    }
    .footer-content {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1.5rem;
      margin-bottom: 2rem;
    }
    .footer-bottom {
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding-top: 1.5rem;
      text-align: center;
      font-size: 0.8rem;
    }

    /* Lightbox Modal Nativo */
    .lightbox-modal {
      border: none;
      padding: 0;
      background: transparent;
      max-width: 100vw;
      max-height: 100vh;
      width: 100%;
      height: 100%;
      margin: 0;
      overflow: hidden;
    }
    .lightbox-modal::backdrop {
      background: rgba(10, 15, 29, 0.95);
      backdrop-filter: blur(8px);
    }
    .lightbox-inner {
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 1.25rem;
      position: relative;
    }
    .lightbox-close-btn {
      position: absolute;
      top: 1.25rem;
      right: 1.5rem;
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #ffffff;
      font-size: 1.35rem;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 10;
      transition: background 0.2s ease;
    }
    .lightbox-close-btn:hover {
      background: rgba(239, 68, 68, 0.8);
      border-color: #ef4444;
    }
    .lightbox-nav-btn {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.25);
      color: #ffffff;
      font-size: 2.2rem;
      width: 52px;
      height: 52px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 10;
      transition: all 0.2s ease;
      line-height: 1;
    }
    .lightbox-nav-btn:hover {
      background: rgba(16, 185, 129, 0.85);
      border-color: #10b981;
      transform: translateY(-50%) scale(1.08);
    }
    .lb-prev { left: 1.5rem; }
    .lb-next { right: 1.5rem; }

    .lightbox-img-wrap {
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 0;
      padding-block: 1rem;
    }
    .lightbox-img-wrap img {
      max-width: 92vw;
      max-height: 75vh;
      object-fit: contain;
      border-radius: 8px;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6);
    }
    .lightbox-caption-box {
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: var(--radius-md);
      padding: 1rem 1.5rem;
      max-width: 900px;
      width: 100%;
      margin-inline: auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1rem;
    }

    @media (max-width: 768px) {
      .lb-prev { left: 0.5rem; width: 42px; height: 42px; font-size: 1.6rem; }
      .lb-next { right: 0.5rem; width: 42px; height: 42px; font-size: 1.6rem; }
      .lightbox-close-btn { top: 0.75rem; right: 0.75rem; width: 38px; height: 38px; font-size: 1.1rem; }
      .lightbox-caption-box { padding: 0.75rem 1rem; }
    }
  </style>
</head>
<body>

  <!-- Top Ribbon -->
  <div class="top-ribbon">
    <div class="container">
      <div>
        <strong>Semana Cultural Carmelista 2026</strong> · Día 4 · Jueves 22 de Octubre
      </div>
      <div>
        🌿 Foro Educativo: «Salvemos la Ciénaga» · Ciénaga, Magdalena
      </div>
    </div>
  </div>

  <!-- Header -->
  <header>
    <div class="container nav-container">
      <div class="brand">
        <a href="index.html" style="display: flex; align-items: center; gap: 0.85rem;">
          <img class="brand-logo" src="escudo.jpg" alt="Escudo IE El Carmen">
          <div class="brand-text">
            <h2>IE El Carmen</h2>
            <p>Semana Cultural 2026 · Registro Oficial</p>
          </div>
        </a>
      </div>
      <div class="nav-actions">
        <a href="dia1.html" class="btn-back-nav" style="background: #eff6ff; color: #1e40af; border-color: #bfdbfe;" title="Ver Galería del Día 1">
          <span>← Día 1: Historia</span>
        </a>
        <a href="dia2.html" class="btn-back-nav" style="background: #ecfdf5; color: #065f46; border-color: #a7f3d0;" title="Ver Galería del Día 2">
          <span>← Día 2: Emprendimiento</span>
        </a>
        <a href="dia3.html" class="btn-back-nav" style="background: #fef3c7; color: #92400e; border-color: #fde68a;" title="Ver Galería del Día 3">
          <span>← Día 3: Mundialito</span>
        </a>
        <a href="index.html#foro-salvemos-la-cienaga" class="btn-back-nav">
          <span>← Portal Semana Cultural</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="day-hero">
    <div class="container">
      <nav class="breadcrumb-nav" aria-label="Miga de pan">
        <a href="index.html">Inicio</a>
        <span>/</span>
        <a href="index.html#semana-cultural-cronograma">Semana Cultural 2026</a>
        <span>/</span>
        <span>Día 4: Foro Salvemos la Ciénaga</span>
      </nav>

      <span class="day-date-tag">
        🌿 Cuarta Jornada · Jueves 22 de Octubre de 2026
      </span>

      <h1 class="day-hero-title">
        Gran Foro Educativo Institucional: <br>
        <span>«Salvemos la Ciénaga»</span>
      </h1>

      <p class="day-hero-lead">
        «Nuestra Ciénaga también tiene futuro» · Registro audiovisual completo (14 Videos Oficiales) y muestra fotográfica oficial del gran encuentro ecológico carmelita: ponencias científicas con respaldo de GEF-7 e INVEMAR, mesas de bioeconomía con Unicaribe, semilleros de pintura ambiental infantil y círculos de diálogo comunitario por la conservación de nuestro patrimonio natural.
      </p>

      <div class="hero-quick-ctas">
        <a href="#videos" class="btn-cta-primary">
          <span>🎬 Ver 14 Videos Oficiales ↓</span>
        </a>
        <a href="#fotos" class="btn-cta-secondary">
          <span>📸 Ver Galería Destacada (46 Fotos) ↓</span>
        </a>
        <a href="https://photos.app.goo.gl/22MaxHLLRht7NrDy6" target="_blank" rel="noopener noreferrer" class="btn-cta-secondary" style="border-color: #a7f3d0; color: #065f46;">
          <span>☁️ Álbum Completo en Google Fotos ↗</span>
        </a>
      </div>

      <!-- Stats Ribbon -->
      <div class="stats-ribbon">
        <div class="stat-item">
          <div class="stat-icon">📸</div>
          <div class="stat-text">
            <strong>46 Fotos</strong>
            <span>Postales en Alta Definición</span>
          </div>
        </div>
        <div class="stat-item">
          <div class="stat-icon">🎥</div>
          <div class="stat-text">
            <strong>14 Videos</strong>
            <span>10 Panorámicos + 4 Shorts 9:16</span>
          </div>
        </div>
        <div class="stat-item">
          <div class="stat-icon">🔬</div>
          <div class="stat-text">
            <strong>GEF-7 / INVEMAR</strong>
            <span>Alineación &amp; Especies Focales</span>
          </div>
        </div>
        <div class="stat-item">
          <div class="stat-icon">🌱</div>
          <div class="stat-text">
            <strong>Unicaribe</strong>
            <span>Mesas de Bioeconomía</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Sección: Videos Oficiales de YouTube (14 Videos: 10 Horizontales + 4 Shorts) -->
  <section class="section-padding" id="videos" style="background: #ffffff;">
    <div class="container">
      <div class="section-title-wrap">
        <span class="section-eyebrow">Memoria Audiovisual en Directo</span>
        <h2 class="section-title">Registro en Video y Transmisiones Oficiales (14 Videos)</h2>
        <p class="section-lead">
          Revive los momentos más emotivos del Foro Institucional «Salvemos la Ciénaga»: palabras de apertura, actos protocolarios, ponencias científicas sobre biodiversidad, mesas de bioeconomía con Unicaribe, el semillero infantil de arte y las cápsulas verticales en Shorts.
        </p>
      </div>

      <!-- Grupo 1: Videos Panorámicos 16:9 (10 Videos) -->
      <div class="video-group-header">
        <h3>📺 Cobertura Especial en Formato Panorámico (16:9)</h3>
        <span class="badge-count" style="background: #d1fae5; color: #065f46;">10 Videos Oficiales</span>
      </div>

      <div class="videos-h-grid">
        <!-- Video 1 -->
        <div class="video-h-card">
          <div class="video-h-frame">
            <iframe 
              src="https://www.youtube-nocookie.com/embed/ZnR7RV0GbfI?rel=0&playsinline=1&modestbranding=1" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
              allowfullscreen 
              loading="lazy"
              title="FORO INSTITUCIONAL SALVEMOS LA CIENAGA 2026 - 01">
            </iframe>
          </div>
          <div class="video-card-body">
            <div>
              <span class="video-badge-pill green">Panorámico 16:9 · Entrega 01</span>
              <h3>Foro Salvemos la Ciénaga · Entrega 01</h3>
              <p>Apertura oficial, ambientación temática y primeros momentos del gran encuentro ambiental carmelita en el patio central.</p>
            </div>
            <a href="https://youtu.be/ZnR7RV0GbfI" target="_blank" rel="noopener noreferrer" class="btn-yt-link">
              <span>▶ Ver en YouTube ↗</span>
            </a>
          </div>
        </div>

        <!-- Video 2 -->
        <div class="video-h-card">
          <div class="video-h-frame">
            <iframe 
              src="https://www.youtube-nocookie.com/embed/eXrOS5yoYqE?rel=0&playsinline=1&modestbranding=1" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
              allowfullscreen 
              loading="lazy"
              title="FORO INSTITUCIONAL SALVEMOS LA CIENAGA 2026 - 02">
            </iframe>
          </div>
          <div class="video-card-body">
            <div>
              <span class="video-badge-pill green">Panorámico 16:9 · Entrega 02</span>
              <h3>Foro Salvemos la Ciénaga · Entrega 02</h3>
              <p>Intervenciones protocolarias, símbolos patrios y palabras orientadoras de los docentes líderes del PRAE.</p>
            </div>
            <a href="https://youtu.be/eXrOS5yoYqE" target="_blank" rel="noopener noreferrer" class="btn-yt-link">
              <span>▶ Ver en YouTube ↗</span>
            </a>
          </div>
        </div>

        <!-- Video 3 -->
        <div class="video-h-card">
          <div class="video-h-frame">
            <iframe 
              src="https://www.youtube-nocookie.com/embed/iey9SQMnxGg?rel=0&playsinline=1&modestbranding=1" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
              allowfullscreen 
              loading="lazy"
              title="FORO INSTITUCIONAL SALVEMOS LA CIENAGA 2026 - 03">
            </iframe>
          </div>
          <div class="video-card-body">
            <div>
              <span class="video-badge-pill green">Panorámico 16:9 · Entrega 03</span>
              <h3>Foro Salvemos la Ciénaga · Entrega 03</h3>
              <p>Ponencias magistrales sobre biodiversidad, especies focales y participación activa del auditorio estudiantil.</p>
            </div>
            <a href="https://youtu.be/iey9SQMnxGg" target="_blank" rel="noopener noreferrer" class="btn-yt-link">
              <span>▶ Ver en YouTube ↗</span>
            </a>
          </div>
        </div>

        <!-- Video 4 -->
        <div class="video-h-card">
          <div class="video-h-frame">
            <iframe 
              src="https://www.youtube-nocookie.com/embed/c9gfMOhYCzQ?rel=0&playsinline=1&modestbranding=1" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
              allowfullscreen 
              loading="lazy"
              title="FORO INSTITUCIONAL SALVEMOS LA CIENAGA 2026 - 04">
            </iframe>
          </div>
          <div class="video-card-body">
            <div>
              <span class="video-badge-pill green">Panorámico 16:9 · Entrega 04</span>
              <h3>Foro Salvemos la Ciénaga · Entrega 04</h3>
              <p>Semilleros de pintura ambiental infantil, mesas de bioeconomía con Unicaribe y diálogo con las familias.</p>
            </div>
            <a href="https://youtu.be/c9gfMOhYCzQ" target="_blank" rel="noopener noreferrer" class="btn-yt-link">
              <span>▶ Ver en YouTube ↗</span>
            </a>
          </div>
        </div>

        <!-- Video 6 -->
        <div class="video-h-card">
          <div class="video-h-frame">
            <iframe 
              src="https://www.youtube-nocookie.com/embed/qpdILYVPmT0?rel=0&playsinline=1&modestbranding=1" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
              allowfullscreen 
              loading="lazy"
              title="FORO INSTITUCIONAL SALVEMOS LA CIENAGA 2026 - 06">
            </iframe>
          </div>
          <div class="video-card-body">
            <div>
              <span class="video-badge-pill green">Panorámico 16:9 · Entrega 06</span>
              <h3>Foro Salvemos la Ciénaga · Entrega 06</h3>
              <p>Muestras didácticas sobre las variedades de mangle, protección contra la erosión costera y conciencia ambiental.</p>
            </div>
            <a href="https://youtu.be/qpdILYVPmT0" target="_blank" rel="noopener noreferrer" class="btn-yt-link">
              <span>▶ Ver en YouTube ↗</span>
            </a>
          </div>
        </div>

        <!-- Video 7 -->
        <div class="video-h-card">
          <div class="video-h-frame">
            <iframe 
              src="https://www.youtube-nocookie.com/embed/pk7hPoGp_BE?rel=0&playsinline=1&modestbranding=1" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
              allowfullscreen 
              loading="lazy"
              title="FORO INSTITUCIONAL SALVEMOS LA CIENAGA 2026 - 07">
            </iframe>
          </div>
          <div class="video-card-body">
            <div>
              <span class="video-badge-pill green">Panorámico 16:9 · Entrega 07</span>
              <h3>Foro Salvemos la Ciénaga · Entrega 07</h3>
              <p>Reflexión estudiantil y aportes juveniles en torno a los retos de la contaminación y el cambio climático en el Magdalena.</p>
            </div>
            <a href="https://youtu.be/pk7hPoGp_BE" target="_blank" rel="noopener noreferrer" class="btn-yt-link">
              <span>▶ Ver en YouTube ↗</span>
            </a>
          </div>
        </div>

        <!-- Video 8 -->
        <div class="video-h-card">
          <div class="video-h-frame">
            <iframe 
              src="https://www.youtube-nocookie.com/embed/QCr-nwUvpdI?rel=0&playsinline=1&modestbranding=1" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
              allowfullscreen 
              loading="lazy"
              title="FORO INSTITUCIONAL SALVEMOS LA CIENAGA 2026 - 08">
            </iframe>
          </div>
          <div class="video-card-body">
            <div>
              <span class="video-badge-pill green">Panorámico 16:9 · Entrega 08</span>
              <h3>Foro Salvemos la Ciénaga · Entrega 08</h3>
              <p>Intervención de rectoría y directivas: el compromiso carmelita de convertir la conservación ambiental en una práctica formativa diaria.</p>
            </div>
            <a href="https://youtu.be/QCr-nwUvpdI" target="_blank" rel="noopener noreferrer" class="btn-yt-link">
              <span>▶ Ver en YouTube ↗</span>
            </a>
          </div>
        </div>

        <!-- Video 10 -->
        <div class="video-h-card">
          <div class="video-h-frame">
            <iframe 
              src="https://www.youtube-nocookie.com/embed/1R-jjpE6Wlc?rel=0&playsinline=1&modestbranding=1" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
              allowfullscreen 
              loading="lazy"
              title="FORO INSTITUCIONAL SALVEMOS LA CIENAGA 2026 - 10">
            </iframe>
          </div>
          <div class="video-card-body">
            <div>
              <span class="video-badge-pill green">Panorámico 16:9 · Entrega 10</span>
              <h3>Foro Salvemos la Ciénaga · Entrega 10</h3>
              <p>Mesa de Bioeconomía con facilitadores de Unicaribe: formulación de proyectos productivos sostenibles y turismo ecológico regional.</p>
            </div>
            <a href="https://youtu.be/1R-jjpE6Wlc" target="_blank" rel="noopener noreferrer" class="btn-yt-link">
              <span>▶ Ver en YouTube ↗</span>
            </a>
          </div>
        </div>

        <!-- Video 11 -->
        <div class="video-h-card">
          <div class="video-h-frame">
            <iframe 
              src="https://www.youtube-nocookie.com/embed/ytRX6XvNS90?rel=0&playsinline=1&modestbranding=1" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
              allowfullscreen 
              loading="lazy"
              title="FORO INSTITUCIONAL SALVEMOS LA CIENAGA 2026 - 11">
            </iframe>
          </div>
          <div class="video-card-body">
            <div>
              <span class="video-badge-pill green">Panorámico 16:9 · Entrega 11</span>
              <h3>Foro Salvemos la Ciénaga · Entrega 11</h3>
              <p>Muestra cultural, expresión artística y talentos estudiantiles rindiendo homenaje al folclor y la identidad cieguera.</p>
            </div>
            <a href="https://youtu.be/ytRX6XvNS90" target="_blank" rel="noopener noreferrer" class="btn-yt-link">
              <span>▶ Ver en YouTube ↗</span>
            </a>
          </div>
        </div>

        <!-- Video 12 -->
        <div class="video-h-card">
          <div class="video-h-frame">
            <iframe 
              src="https://www.youtube-nocookie.com/embed/YL5MWYGKJVg?rel=0&playsinline=1&modestbranding=1" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
              allowfullscreen 
              loading="lazy"
              title="FORO INSTITUCIONAL SALVEMOS LA CIENAGA 2026 - 12">
            </iframe>
          </div>
          <div class="video-card-body">
            <div>
              <span class="video-badge-pill green">Panorámico 16:9 · Entrega 12</span>
              <h3>Foro Salvemos la Ciénaga · Entrega 12</h3>
              <p>Conclusiones finales, lectura de acuerdos por la Ciénaga Grande y clausura triunfal del Foro Ambiental Carmelista 2026.</p>
            </div>
            <a href="https://youtu.be/YL5MWYGKJVg" target="_blank" rel="noopener noreferrer" class="btn-yt-link">
              <span>▶ Ver en YouTube ↗</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Grupo 2: YouTube Shorts 9:16 (4 Videos Verticales) -->
      <div class="video-group-header">
        <h3>📱 YouTube Shorts Oficiales en Formato Vertical (9:16)</h3>
        <span class="badge-count" style="background: #fef3c7; color: #92400e;">4 Cápsulas Ágiles Móviles</span>
      </div>

      <div class="shorts-grid">
        <!-- Short 1 (Entrega 05) -->
        <div class="short-card-item">
          <div class="video-v-mockup">
            <iframe 
              src="https://www.youtube-nocookie.com/embed/F1w1-B27Mjw?rel=0&playsinline=1&modestbranding=1" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
              allowfullscreen 
              loading="lazy"
              title="FORO INSTITUCIONAL SALVEMOS LA CIENAGA 2026 - 05 · Short">
            </iframe>
          </div>
          <div class="short-info">
            <span class="video-badge-pill gold">Short 9:16 · Cápsula 05</span>
            <h4>Foto Institucional Salvemos la Ciénaga</h4>
            <p>Resumen dinámico de la foto grupal y entusiasmo de los estudiantes.</p>
            <a href="https://youtube.com/shorts/F1w1-B27Mjw?feature=share" target="_blank" rel="noopener noreferrer" class="btn-yt-link">
              <span>▶ Abrir Short ↗</span>
            </a>
          </div>
        </div>

        <!-- Short 2 (Entrega 09) -->
        <div class="short-card-item">
          <div class="video-v-mockup">
            <iframe 
              src="https://www.youtube-nocookie.com/embed/YamZxvLIKao?rel=0&playsinline=1&modestbranding=1" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
              allowfullscreen 
              loading="lazy"
              title="FORO INSTITUCIONAL SALVEMOS LA CIENAGA 2026 - 09 · Short">
            </iframe>
          </div>
          <div class="short-info">
            <span class="video-badge-pill gold">Short 9:16 · Cápsula 09</span>
            <h4>Semillero Infantil de Pintura</h4>
            <p>El color y la creatividad de las niñas carmelitas retratando la Ciénaga.</p>
            <a href="https://youtube.com/shorts/YamZxvLIKao?feature=share" target="_blank" rel="noopener noreferrer" class="btn-yt-link">
              <span>▶ Abrir Short ↗</span>
            </a>
          </div>
        </div>

        <!-- Short 3 (Entrega 13) -->
        <div class="short-card-item">
          <div class="video-v-mockup">
            <iframe 
              src="https://www.youtube-nocookie.com/embed/93jZABfSG2k?rel=0&playsinline=1&modestbranding=1" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
              allowfullscreen 
              loading="lazy"
              title="FORO INSTITUCIONAL SALVEMOS LA CIENAGA 2026 - 13 · Short">
            </iframe>
          </div>
          <div class="short-info">
            <span class="video-badge-pill gold">Short 9:16 · Cápsula 13</span>
            <h4>Mesas de Diálogo y Trabajo en Equipo</h4>
            <p>Comunidad, acudientes y docentes concertando compromisos verdes.</p>
            <a href="https://youtube.com/shorts/93jZABfSG2k?feature=share" target="_blank" rel="noopener noreferrer" class="btn-yt-link">
              <span>▶ Abrir Short ↗</span>
            </a>
          </div>
        </div>

        <!-- Short 4 (Entrega 14) -->
        <div class="short-card-item">
          <div class="video-v-mockup">
            <iframe 
              src="https://www.youtube-nocookie.com/embed/AaQtANVpASg?rel=0&playsinline=1&modestbranding=1" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
              allowfullscreen 
              loading="lazy"
              title="FORO INSTITUCIONAL SALVEMOS LA CIENAGA 2026 - 14 · Short">
            </iframe>
          </div>
          <div class="short-info">
            <span class="video-badge-pill gold">Short 9:16 · Cápsula 14</span>
            <h4>Compromiso Carmelita: «Salvemos la Ciénaga»</h4>
            <p>Cápsula de cierre y mensaje institucional de orgullo por nuestra tierra.</p>
            <a href="https://youtube.com/shorts/AaQtANVpASg?feature=share" target="_blank" rel="noopener noreferrer" class="btn-yt-link">
              <span>▶ Abrir Short ↗</span>
            </a>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- Sección: Galería Fotográfica Destacada (46 Fotos) -->
  <section class="section-padding" id="fotos" style="background: var(--bg-surface);">
    <div class="container">
      <div class="section-title-wrap">
        <span class="section-eyebrow">Registro Fotográfico Oficial</span>
        <h2 class="section-title">Fotografías Destacadas del Día 4 (46 Fotos)</h2>
        <p class="section-lead">
          Una selección de 46 postales exclusivas del Foro «Salvemos la Ciénaga»: ambientación, diálogo comunitario, arte infantil, ponencias científicas y mesas de bioeconomía. Haz clic sobre cualquier fotografía para abrir el visor en pantalla completa con navegación por teclado.
        </p>
      </div>

      <div class="photos-grid">
'''

gallery_data = [
    ('dia4/Dia4 (1).jpg', 'Escenografía Central: «Salvemos la Ciénaga - Pequeñas Acciones»', 'Mesa principal del evento con centro floral y el mural institucional alusivo a la protección de los recursos naturales y el reciclaje.', 'Ambientación & Protocolo'),
    ('dia4/Dia4 (2).jpg', 'Mural Escolar: «Juntos Podemos Hacer la Diferencia»', 'Carteleras elaboradas por estudiantes con mensajes de sensibilización para salvar los mangles y actuar con compromiso.', 'Sensibilización'),
    ('dia4/Dia4 (3).jpg', 'Equipo Estudiantil en la Mesa de Coordinación', 'Estudiantes de grados superiores apoyando el registro y desarrollo de las actividades del Foro Ambiental.', 'Liderazgo Juvenil'),
    ('dia4/Dia4 (4).jpg', 'Pancartas de Conciencia Ecológica: «Protejamos los Recursos»', 'Espacio decorado con lemas ecológicos y llamados urgentes al reciclaje y la conservación del agua.', 'Conciencia Ambiental'),
    ('dia4/Dia4 (5).jpg', 'Detalles Artísticos: Fauna y Ecosistema de la Ciénaga', 'Representación gráfica de peces, aves y especies nativas que habitan el complejo lagunar de la Ciénaga Grande.', 'Biodiversidad'),
    ('dia4/Dia4 (6).jpg', 'Disposición del Auditorio en el Patio Central Techado', 'Preparativos y bienvenida a los asistentes en las instalaciones de la Institución Educativa El Carmen.', 'Comunidad Educativa'),
    ('dia4/Dia4 (7).jpg', 'Mesa de Diálogo Docente-Estudiantil sobre el Agua', 'Espacio de intercambio de saberes guiado por docentes sobre la problemática del agua y el cuidado de los caños.', 'Diálogo Comunitario'),
    ('dia4/Dia4 (8).jpg', 'Participación de Acudientes y Familias Carmelitas', 'Madres y padres de familia del barrio Micael Cotes integrados en las mesas redondas de concertación ecológica.', 'Participación Familiar'),
    ('dia4/Dia4 (9).jpg', 'Reflexión Juvenil sobre los Retos Ambientales', 'Estudiantes compartiendo sus puntos de vista sobre la contaminación y proponiendo soluciones desde el hogar.', 'Voz Estudiantil'),
    ('dia4/Dia4 (10).jpg', 'Encuentro Intergeneracional por la Conservación', 'Docentes, directivos y alumnas dialogando activamente sobre el sentido de pertenencia por nuestro patrimonio natural.', 'Integración Escolar'),
    ('dia4/Dia4 (11).jpg', 'Toma de Notas y Consensos en las Mesas Redondas', 'Registro escrito de los compromisos ciudadanos adquiridos por cada grupo de trabajo durante la jornada.', 'Compromisos'),
    ('dia4/Dia4 (12).jpg', 'Círculo de Concertación: Cuidemos la Ciénaga Grande', 'Estudiantes de bachillerato analizando los impactos del cambio climático en el departamento del Magdalena.', 'Acción Colectiva'),
    ('dia4/Dia4 (13).jpg', 'Semillero Infantil: Colores por la Naturaleza', 'Estudiantes de primaria expresando su creatividad con témperas y pinceles inspirados en la riqueza de la Ciénaga.', 'Arte & Infancia'),
    ('dia4/Dia4 (14).jpg', 'Pintando la Vida y los Manglares', 'Pequeñas artistas plasmando soles radiantes, agua limpia y paisajes de manglar en sus lienzos escolares.', 'Expresión Artística'),
    ('dia4/Dia4 (15).jpg', 'Creatividad Ecológica desde las Aulas de Primaria', 'La educación artística como canal pedagógico para infundir amor y respeto hacia el medio ambiente.', 'Pedagogía Verde'),
    ('dia4/Dia4 (16).jpg', 'Concentración y Talento de las Niñas Carmelitas', 'Trazos llenos de color y esperanza en la actividad artística guiada por el cuerpo docente.', 'Semillero Carmelita'),
    ('dia4/Dia4 (17).jpg', 'Paletas de Colores y Obras Infantiles en Progreso', 'Mezclas de témperas y acuarelas para retratar la luz y la biodiversidad del Caribe colombiano.', 'Taller de Pintura'),
    ('dia4/Dia4 (18).jpg', 'Futuros Guardianes del Humedal', 'Niños y niñas demostrando que desde la infancia se forja el liderazgo ambiental de nuestra comunidad.', 'Guardianes del Agua'),
    ('dia4/Dia4 (19).jpg', 'Compañerismo y Alegría en la Expresión Pictórica', 'Estudiantes compartiendo pinceles y sonrisas en un ambiente escolar de fraternidad e integración.', 'Convivencia Escolar'),
    ('dia4/Dia4 (20).jpg', 'El Arte al Servicio de la Conciencia Ambiental', 'Obras infantiles que transmiten el mensaje de que nuestra Ciénaga también tiene futuro.', 'Mensaje Ecológico'),
    ('dia4/Dia4 (21).jpg', 'Exhibición de Obras del Semillero de Pintura', 'Muestra del talento artístico de los más pequeños en el marco del Foro Salvemos la Ciénaga.', 'Galería Infantil'),
    ('dia4/Dia4 (22).jpg', 'Apertura Oficial en Atril: Las 3R Ecológicas', 'Docente líder destacando la importancia de Reducir, Reciclar y Reutilizar junto a las banderas de Colombia y Ciénaga.', 'Apertura Oficial'),
    ('dia4/Dia4 (23).jpg', 'Solemnidad e Himnos Institucionales', 'Actos protocolarios con respeto a los símbolos patrios y el himno de la Institución Educativa El Carmen.', 'Actos Protocolarios'),
    ('dia4/Dia4 (24).jpg', 'Moderación del Foro «Salvemos la Ciénaga» 2026', 'Presentación de los objetivos estratégicos de la jornada y motivación al diálogo propositivo.', 'Moderación'),
    ('dia4/Dia4 (25).jpg', 'Presentación de la Agenda y Ejes de Trabajo', 'Socialización de las ponencias académicas, actividades artísticas y mesas de concertación.', 'Agenda Institucional'),
    ('dia4/Dia4 (26).jpg', 'Voz Estudiantil en el Atril Central', 'Intervención de representantes estudiantiles asumiendo el compromiso generacional con la naturaleza.', 'Liderazgo Juvenil'),
    ('dia4/Dia4 (27).jpg', 'Docentes Líderes del Proyecto Ambiental Escolar (PRAE)', 'El equipo pedagógico institucional orientando la visión científica y formativa del foro.', 'Liderazgo Docente'),
    ('dia4/Dia4 (28).jpg', 'Acompañamiento Directivo a las Ponencias Escolares', 'Respaldo del cuerpo docente y coordinadores a los jóvenes expositores durante sus disertaciones.', 'Acompañamiento'),
    ('dia4/Dia4 (29).jpg', 'El Compromiso Carmelita: «Educando para Preservar»', 'Mensaje institucional reafirmando el lema del escudo y la vocación ecológica del plantel.', 'Identidad Carmelita'),
    ('dia4/Dia4 (30).jpg', 'Gran Panorámica: Comunidad Carmelita Reunida', 'Vista general del patio central techado con toda la comunidad educativa frente a la pantalla oficial del Foro 2026.', 'Panorámica Oficial'),
    ('dia4/Dia4 (31).jpg', 'Ponencia Magistral: Alineación Estratégica GEF-7 e INVEMAR', 'Exposición científica sobre la estrategia de sensibilización y comunicación para la Ciénaga Grande de Santa Marta.', 'Ciencia & Conservación'),
    ('dia4/Dia4 (32).jpg', 'Proyección Científica y Validación con el INVEMAR', 'Presentación del respaldo científico institucional y la participación en foros internacionales como IODE-2025.', 'Respaldo Científico'),
    ('dia4/Dia4 (33).jpg', 'Guía Ilustrada de Especies Focales de la Ciénaga', 'Socialización de la meta pedagógica de escalar de 8 a 40 especies focales para democratizar el conocimiento biológico.', 'Especies Focales'),
    ('dia4/Dia4 (34).jpg', 'La Conservación Nace del Autoreconocimiento Comunitario', 'Reflexión clave del foro: «La conservación comienza cuando la comunidad se reconoce en su propia biodiversidad».', 'Filosofía Ecológica'),
    ('dia4/Dia4 (35).jpg', 'Atención Plena del Auditorio a las Exposiciones', 'Estudiantes de décimo y undécimo grado siguiendo con interés el desglose técnico y ambiental.', 'Auditorio Atento'),
    ('dia4/Dia4 (36).jpg', 'Muestra Didáctica sobre Flora y Manglares Nativos', 'Explicación de las variedades de mangle y su papel protector frente a la erosión costera y el cambio climático.', 'Ecosistema de Mangle'),
    ('dia4/Dia4 (37).jpg', 'Sesión de Preguntas e Intercambio de Conocimientos', 'Espacio participativo donde los jóvenes formularon preguntas a los ponentes e invitados especiales.', 'Preguntas & Debate'),
    ('dia4/Dia4 (38).jpg', 'Intervención del Señor Rector de la IE El Carmen', 'El rector dirigiéndose a la comunidad educativa con un mensaje de esperanza, disciplina y liderazgo ambiental.', 'Mensaje de Rectoría'),
    ('dia4/Dia4 (39).jpg', 'El Liderazgo Directivo Respaldando la Educación Verde', 'Palabras motivadoras sobre la importancia de convertir la preservación ambiental en un hábito diario.', 'Dirección Institucional'),
    ('dia4/Dia4 (40).jpg', 'Arraigo Cultural y Pertenencia por Nuestra Tierra', 'Reflexión sobre el orgullo de ser ciengueros y carmelitas, guardianes de uno de los humedales más importantes del mundo.', 'Orgullo Cienguero'),
    ('dia4/Dia4 (41).jpg', 'Reconocimiento y Gratitud a la Comunidad Escolar', 'Agradecimiento a docentes, estudiantes, acudientes y entidades aliadas por el éxito del Foro 2026.', 'Agradecimiento'),
    ('dia4/Dia4 (42).jpg', 'Mesa de Bioeconomía y Economía Sostenible con Unicaribe', 'Estudiantes, docentes y facilitadores universitarios diseñando modelos productivos verdes para la región.', 'Bioeconomía Unicaribe'),
    ('dia4/Dia4 (43).jpg', 'Construcción Colectiva de Propuestas Productivas', 'Debate grupal sobre oportunidades de empleo e ingresos basadas en el turismo ecológico y el aprovechamiento responsable.', 'Desarrollo Sostenible'),
    ('dia4/Dia4 (44).jpg', 'Jóvenes Carmelitas Planteando Soluciones Reales', 'Trabajo en equipo sobre papel craft definiendo compromisos y estrategias viables para la conservación.', 'Propuestas Juveniles'),
    ('dia4/Dia4 (45).jpg', 'Acompañamiento Metodológico Universitario', 'Facilitadores de Unicaribe guiando la formulación de proyectos ambientales con rigor técnico y pertinencia social.', 'Asesoría Universitaria'),
    ('dia4/Dia4 (46).jpg', 'Consolidación del Pliego de Propuestas para la Ciénaga', 'Conclusión exitosa de la Mesa 2 con el documento final de propuestas para el futuro ambiental de Ciénaga.', 'Conclusiones del Foro')
]

cards_html = []
for idx, (img_file, title, desc, tag) in enumerate(gallery_data):
    card = f'''        <!-- Foto {idx + 1} -->
        <article class="photo-card" onclick="openLightbox({idx})">
          <div class="photo-frame">
            <img src="{img_file}" alt="{title}" loading="lazy">
            <span class="photo-badge-idx">{idx + 1} / 46</span>
            <span class="photo-badge-team">{tag}</span>
          </div>
          <div class="photo-body">
            <div>
              <h3>{title}</h3>
              <p>{desc}</p>
            </div>
            <span class="photo-zoom-hint">🔍 Ampliar fotografía</span>
          </div>
        </article>'''
    cards_html.append(card)

html_template += '\n\n'.join(cards_html)

html_template += '''
      </div>

      <!-- Banner Álbum Oficial en Google Fotos -->
      <div class="gphotos-banner">
        <div class="gphotos-content">
          <div style="max-width: 650px;">
            <span style="background: rgba(16, 185, 129, 0.2); color: #6ee7b7; font-size: 0.82rem; font-weight: 800; padding: 0.3rem 0.85rem; border-radius: var(--radius-full); display: inline-block; margin-bottom: 0.75rem;">
              ☁️ Repositorio Institucional en la Nube
            </span>
            <h3 style="font-size: clamp(1.4rem, 2.8vw, 1.9rem); color: #ffffff; margin-bottom: 0.6rem; font-family: 'Outfit', sans-serif;">
              ¿Deseas descargar todas las fotos en resolución original?
            </h3>
            <p style="font-size: 0.95rem; color: #cbd5e1; line-height: 1.6;">
              Accede al álbum oficial del Foro Salvemos la Ciénaga en Google Fotos para ver el archivo completo, compartir con familiares y conservar el registro histórico escolar.
            </p>
          </div>
          <div style="display: flex; flex-direction: column; gap: 0.5rem; align-items: center;">
            <a href="https://photos.app.goo.gl/22MaxHLLRht7NrDy6" target="_blank" rel="noopener noreferrer" class="btn-gphotos-big">
              <span>📸 Ver Álbum en Google Fotos ↗</span>
            </a>
            <span style="font-size: 0.8rem; color: #94a3b8; text-align: center;">
              Abre directamente en la app de fotos de tu celular o navegador
            </span>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- Barra de Navegación entre Días -->
  <div class="day-nav-bar">
    <div class="container">
      <a href="dia3.html" class="btn-back-nav" style="background: #fef3c7; color: #92400e; border-color: #fde68a;">
        <span>← Ver Galería Día 3: Mundialito &amp; Desfile</span>
      </a>

      <div style="font-size: 0.92rem; font-weight: 700; color: var(--primary);">
        <span>Siguiente Jornada: </span>
        <a href="index.html#invitacion-misa-dia5" style="color: var(--accent-green-dark); text-decoration: underline;">
          Viernes 23 · Gran Cierre, Santa Misa &amp; Aniversario 53 Años →
        </a>
      </div>
    </div>
  </div>

  <!-- Footer -->
  <footer>
    <div class="container">
      <div class="footer-content">
        <div class="brand">
          <img class="brand-logo" src="escudo.jpg" alt="Escudo IE El Carmen">
          <div>
            <h3 style="color: #ffffff; font-size: 1.15rem; margin-bottom: 0.2rem;">Institución Educativa El Carmen</h3>
            <p style="font-size: 0.82rem; color: #94a3b8;">Ciénaga, Magdalena · Barrio Micael Cotes · Calle 18B # 38-34</p>
          </div>
        </div>
        <div>
          <a href="index.html" style="color: var(--accent-green); font-weight: 700;">Semana Cultural 2026</a>
        </div>
      </div>

      <div class="footer-bottom">
        <p>© 2026 Institución Educativa El Carmen. Entorno de Laboratorio (lab.elcarmencienaga.edu.co). Todos los derechos reservados.</p>
      </div>
    </div>
  </footer>

  <!-- Lightbox Modal Nativo con Navegación -->
  <dialog id="photo-lightbox" class="lightbox-modal">
    <div class="lightbox-inner">
      <button type="button" class="lightbox-close-btn" onclick="closeLightbox()" aria-label="Cerrar visor">✕</button>
      <button type="button" class="lightbox-nav-btn lb-prev" onclick="changeLightbox(-1)" aria-label="Foto anterior">‹</button>
      <button type="button" class="lightbox-nav-btn lb-next" onclick="changeLightbox(1)" aria-label="Siguiente foto">›</button>

      <div class="lightbox-img-wrap">
        <img id="lightbox-img" src="" alt="Fotografía ampliada">
      </div>

      <div class="lightbox-caption-box">
        <div>
          <h4 id="lightbox-title" style="color: #ffffff; font-size: 1.1rem; margin-bottom: 0.2rem;"></h4>
          <p id="lightbox-caption" style="color: #94a3b8; font-size: 0.88rem; margin: 0;"></p>
        </div>
        <div style="display: flex; align-items: center; gap: 0.75rem;">
          <span id="lightbox-counter" style="font-size: 0.78rem; font-weight: 700; color: #cbd5e1; background: rgba(255,255,255,0.12); padding: 0.3rem 0.65rem; border-radius: 4px;">
            Foto 1 de 46
          </span>
          <span style="font-size: 0.75rem; color: #64748b; background: rgba(255,255,255,0.06); padding: 0.3rem 0.5rem; border-radius: 4px;">
            Teclas ← / → / ESC
          </span>
        </div>
      </div>
    </div>
  </dialog>

  <script>
    const galleryItems = [
'''

items_json = []
for f, t, d, tag in gallery_data:
    items_json.append(f'      {{"file": "{f}", "title": "{t}", "desc": "{d}"}}')

html_template += ',\n'.join(items_json)

html_template += '''
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
  </script>
</body>
</html>
'''

target_path = os.path.join(os.path.dirname(__file__), '..', 'laboratorio', 'dia4.html')
target_path = os.path.abspath(target_path)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print('laboratorio/dia4.html created successfully at:', target_path)
print('File size:', os.path.getsize(target_path), 'bytes')
