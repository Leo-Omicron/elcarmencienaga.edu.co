<<<<<<< HEAD
# Sistema de Diseño y Guía de Estilos — I.E. El Carmen

Este documento define la **identidad visual, tokens CSS y componentes estándar** de la Institución Educativa El Carmen (Ciénaga, Magdalena, Colombia). 

> **DIRECTRIZ PARA AGENTES DE IA (Google Jules, Codex, Antigravity):**
> Al crear páginas, secciones o componentes en `demos/`, `laboratorio/` o producción, **NO inventes estilos CSS en línea ni paletas moradas genéricas**. Enlaza siempre `css/institucional.css` y reutiliza las clases y componentes documentados en esta guía.

---

## 1. Identidad Institucional y Tokens

- **Institución:** Institución Educativa El Carmen (Ciénaga, Magdalena).
- **Código DANE:** 147189001160 (Resolución 931 de 2023).
- **Lema Institucional:** «Educando para Preservar y Emprender».
- **Tipografías Oficiales:**
  - Títulos y encabezados: `Outfit` (pesos 600, 700, 800).
  - Textos y cuerpo: `Plus Jakarta Sans` (pesos 400, 500, 600, 700).

### Paleta de Colores Oficiales

| Variable CSS | Hexadecimal | Nombre / Uso |
|---|---|---|
| `--primary` | `#191253` | Azul profundo carmelita (Color principal de marca y encabezados) |
| `--primary-dark` | `#0d0933` | Azul noche profundo (Footers y ribbons) |
| `--accent-green` | `#10b981` | Verde esperanza (Bordes activos, badges de éxito, botones) |
| `--accent-green-dark` | `#059669` | Verde esmeralda institucional (Hover de botones y enlaces) |
| `--accent-gold` | `#f59e0b` | Oro / Mostaza (Detalles destacados, franjas, líneas de acento) |
| `--accent-gold-light` | `#fef3c7` | Fondo suave de alertas y badges dorados |
| `--accent-wine` | `#7f1d1d` | Vinotinto oficial (Color del pantalón del uniforme masculino) |
| `--bg-surface` | `#f8fafc` | Fondo neutro de la página (Gris ultra claro) |
| `--bg-card` | `#ffffff` | Blanco puro para tarjetas elevadas |

---

## 2. Cómo Enlazar la Hoja de Estilos

En el `<head>` de cualquier documento HTML nuevo:

```html
<!-- Google Fonts Oficiales -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">

<!-- Estilos Institucionales Compartidos -->
<link rel="stylesheet" href="css/institucional.css">
```

---

## 3. Catálogo de Componentes Estándar

### A. Encabezado Institucional (Header)
```html
<header class="header-institucional">
  <div class="container nav-wrapper">
    <div class="brand-group">
      <img src="assets/escudo.png" alt="Escudo IE El Carmen" class="brand-logo">
      <div class="brand-text">
        <h2>I.E. El Carmen</h2>
        <p>Ciénaga, Magdalena · DANE 147189001160</p>
      </div>
    </div>
    <nav>
      <ul class="nav-links">
        <li><a href="#inicio">Inicio</a></li>
        <li><a href="#noticias">Noticias</a></li>
        <li><a href="#galeria">Galería</a></li>
        <li><a href="#contacto" class="btn-primary">Contacto</a></li>
      </ul>
    </nav>
  </div>
</header>
```

### B. Sección Hero
```html
<section class="hero-institucional">
  <div class="container">
    <span class="badge badge-gold">Portal Oficial de Demostración</span>
    <h1>Educando para Preservar y Emprender</h1>
    <p>Formación integral con rigor académico, compromiso ambiental y liderazgo comunitario en Ciénaga.</p>
  </div>
</section>
```

### C. Tarjeta de Noticias o Eventos (Cards Grid)
```html
<div class="grid-cards">
  <article class="card-institucional">
    <div>
      <span class="badge badge-green">Evento Académico</span>
      <h3>Gran Foro Salvemos la Ciénaga</h3>
      <p>Espacio de debate ambiental y científico liderado por docentes y estudiantes de la institución.</p>
    </div>
    <a href="#" class="btn-primary btn-green">Leer Más →</a>
  </article>
</div>
```

### D. Reproductor de Video de YouTube (16:9 Panorámico y 9:16 Shorts)
```html
<!-- Video Panorámico 16:9 -->
<div class="video-responsive-16-9">
  <iframe src="https://www.youtube.com/embed/VIDEO_ID" title="Video Institucional" allowfullscreen></iframe>
</div>

<!-- Video Vertical Shorts 9:16 -->
<div class="video-responsive-9-16">
  <iframe src="https://www.youtube.com/embed/VIDEO_ID" title="Short Institucional" allowfullscreen></iframe>
</div>
```

### E. Cajas de Alerta
```html
<!-- Alerta Verde / Éxito o Noticia Positiva -->
<div class="alerta-box alerta-verde">
  <div>
    <strong>⚽ Vuelve el Mundialito Carmelista</strong>
    <p>Programación oficial de partidos intercursos disponible para la comunidad.</p>
  </div>
  <a href="#" class="btn-primary btn-green">Ver Fixture ↓</a>
</div>

<!-- Alerta Roja / Aviso Urgente o Aplazamiento -->
<div class="alerta-box alerta-roja">
  <div>
    <strong>🚨 Comunicado de Última Hora</strong>
    <p>Jornada suspendida temporalmente por disposición institucional.</p>
  </div>
</div>
```

### F. Pie de Página Institucional (Footer)
```html
<footer class="footer-institucional">
  <div class="container footer-grid">
    <div>
      <h4>Institución Educativa El Carmen</h4>
      <p>Ciénaga, Magdalena · Colombia</p>
      <p>Código DANE: 147189001160</p>
      <p style="margin-top: 0.5rem; color: #f59e0b; font-weight: 600;">«Educando para Preservar y Emprender»</p>
    </div>
    <div>
      <h4>Sedes Institucionales</h4>
      <p>• Sede Principal</p>
      <p>• Sede Guillermo F. Morán</p>
    </div>
    <div>
      <h4>Contacto</h4>
      <p>contacto@elcarmencienaga.edu.co</p>
    </div>
  </div>
  <div class="footer-bottom">
    <p>© 2026 Institución Educativa El Carmen. Todos los derechos reservados.</p>
  </div>
</footer>
```
=======
# Design System - Institución Educativa El Carmen de Ciénaga

This document defines the official UI components and styles for the web properties of the institution.

## 1. Colors
*   **Deep Blue (Primary):** `#191253`
*   **Green (Secondary):** `#10b981` (Accent: `#43a447`)
*   **Gold (Highlight):** `#f59e0b` (Accent: `#ffe500`)
*   **Text (Dark):** `#333333`
*   **Background (Light):** `#f9fafb`
*   **White:** `#ffffff`

**Rule:** Do not use inline purple styles under any circumstances.

## 2. Components

### 2.1 Official Header (`.official-header`)
*   **Background:** Deep Blue (`#191253`)
*   **Content:** Must include the institution's shield on the left and the name "I.E. El Carmen de Ciénaga" on the right (or next to it).
*   **Navigation:** Links should be white and hover to Gold (`#ffe500`).

### 2.2 News Section (`.news-section`)
*   **Background:** Light gray/white.
*   **Title:** Deep Blue, centered.
*   **Cards (`.news-card`):** White background, subtle shadow, rounded corners. Include an image, title, excerpt, and a "Read More" button in Green.

### 2.3 YouTube Video Player (`.video-container`)
*   **Responsive Wrapper:** A wrapper to make the `iframe` responsive (16:9 aspect ratio).
*   **Container:** Should have a subtle border or shadow reflecting institutional colors.
>>>>>>> origin/feat/website-laboratory-5574583775295612613
