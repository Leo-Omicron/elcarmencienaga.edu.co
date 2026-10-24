# -*- coding: utf-8 -*-
"""
Generador de la página oficial del Día 5:
Gran Cierre, Santa Misa de Acción de Gracias & 53° Aniversario Institucional IE El Carmen.
Incluye Álbum Oficial de Google Photos.
"""
import os

photos_data = [
    {
        "file": "dia5/Dia5 (1).jpg",
        "title": "Apertura de la Santa Misa y Altar Conmemorativo",
        "desc": "Solemne inicio de la Eucaristía de acción de gracias por los 53 años institucionales con el altar en honor a la Virgen del Carmen, ofrendas florales y la comunidad reunida en oración.",
        "badge": "Altar Mayor & Misa"
    },
    {
        "file": "dia5/Dia5 (2).jpg",
        "title": "Liturgia de la Palabra y Reflexión Sacerdotal",
        "desc": "El párroco presidiendo la celebración eucarística y compartiendo un mensaje inspirador de fe, vocación, amor a la educación y gratitud por la historia carmelista.",
        "badge": "Liturgia de la Palabra"
    },
    {
        "file": "dia5/Dia5 (3).jpg",
        "title": "Comunidad Estudiantil Carmelista en Oración",
        "desc": "Estudiantes luciendo el uniforme institucional de gala, participando con respeto, devoción y recogimiento espiritual en el patio central techado.",
        "badge": "Estudiantes Carmelitas"
    },
    {
        "file": "dia5/Dia5 (4).jpg",
        "title": "Celebración Eucarística y Árbol de Sueños",
        "desc": "Momento solemne de la Eucaristía frente al mural conmemorativo «Árbol de Sueños» con la participación activa y fraterna de directivos y docentes.",
        "badge": "Mural Árbol de Sueños"
    },
    {
        "file": "dia5/Dia5 (5).jpg",
        "title": "Panorámica del Patio Central de la Sede Principal",
        "desc": "Amplia concurrencia de la comunidad carmelista colmando los pasillos y áreas techadas durante los actos litúrgicos del aniversario.",
        "badge": "Vista Panorámica"
    },
    {
        "file": "dia5/Dia5 (6).jpg",
        "title": "Acompañamiento de Familias y Promoción 2026",
        "desc": "Padres de familia, acudientes y los jóvenes de la Promoción 2026 unidos en acción de gracias por las bendiciones cosechadas en estos 53 años.",
        "badge": "Promo 2026 & Familias"
    },
    {
        "file": "dia5/Dia5 (7).jpg",
        "title": "Mensaje Institucional del Cuerpo Directivo",
        "desc": "Palabras de gratitud, exaltación histórica y compromiso institucional dirigidas por las directivas docentes a toda la familia carmelista.",
        "badge": "Directivas Docentes"
    },
    {
        "file": "dia5/Dia5 (8).jpg",
        "title": "Lecturas Litúrgicas y Oración de los Fieles",
        "desc": "Miembros de la comunidad educativa elevando súplicas y plegarias junto a la imagen protectora de la Virgen del Carmen en el altar.",
        "badge": "Lecturas & Plegarias"
    },
    {
        "file": "dia5/Dia5 (9).jpg",
        "title": "Altar Mayor: 53° Aniversario Institucional",
        "desc": "Hermosa ambientación con arreglos florales, detalles marianos, coro e instrumentos y el mural conmemorativo «I.E. El Carmen Aniversario».",
        "badge": "Muestra del Altar"
    },
    {
        "file": "dia5/Dia5 (10).jpg",
        "title": "Gran Asamblea Carmelista en la Eucaristía",
        "desc": "Vista desde la nave central que refleja el fervor, unidad, hermandad y solemnidad de toda la institución educativa en Ciénaga.",
        "badge": "Asamblea en Oración"
    },
    {
        "file": "dia5/Dia5 (11).jpg",
        "title": "Homenaje al Legado del Profesor Arlin Jiménez",
        "desc": "Sentido homenaje póstumo en el primer aniversario de la partida de nuestro querido compañero y educador Arlin Jiménez, honrando su memoria y entrega.",
        "badge": "Homenaje a Arlin Jiménez"
    },
    {
        "file": "dia5/Dia5 (13).jpg",
        "title": "Preparación Litúrgica y Sagrados Vasos",
        "desc": "Disposición solemne de los ornamentos, vasos sagrados, cáliz y ofrendas para la consagración eucarística de aniversario.",
        "badge": "Ritos Litúrgicos"
    }
]

videos_data = [
    {
        "id": "xksuNCG6pZM",
        "title": "Actos Protocolarios - Himno IE El Carmen",
        "author": "Leonidas \"Omicron\" Asprilla",
        "badge": "Panorámico 16:9 · Actos Protocolarios",
        "desc": "Solemne entonación del Himno de la IE El Carmen por parte de directivos, docentes y la comunidad estudiantil reunida en el marco del 53° Aniversario Institucional."
    },
    {
        "id": "NdgGWWO4WW4",
        "title": "Resumen Semana Cultural IEEC 2026",
        "author": "Leonidas \"Omicron\" Asprilla",
        "badge": "Panorámico 16:9 · Video Especial de Clausura",
        "desc": "Registro audiovisual con los momentos más emotivos y destacados de toda la Semana Cultural Carmelista 2026: ciencia, emprendimiento, comparsas folclóricas, deporte, foros y gran clausura."
    }
]

GOOGLE_PHOTOS_URL = "https://photos.app.goo.gl/YaMUhVX1TrMMA7Ed6"

def generate_dia5_html():
    cards_html = []
    for idx, p in enumerate(photos_data):
        cards_html.append(f'''        <!-- Foto {idx + 1} -->
        <div class="photo-card" onclick="openLightbox({idx})" role="button" tabindex="0" onkeydown="if(event.key==='Enter')openLightbox({idx})">
          <div class="photo-frame">
            <img src="{p["file"]}" alt="{p["title"]}" loading="lazy">
            <span class="photo-badge-idx">{p["badge"]} · {idx + 1}/{len(photos_data)}</span>
            <div class="photo-zoom-hint">🔍 Toca para ampliar</div>
          </div>
          <div class="photo-body">
            <h4>{p["title"]}</h4>
            <p>{p["desc"]}</p>
          </div>
        </div>''')

    cards_block = "\n".join(cards_html)

    items_js = []
    for p in photos_data:
        t = p["title"].replace('"', '\\"')
        d = p["desc"].replace('"', '\\"')
        items_js.append(f'      {{"file": "{p["file"]}", "title": "{t}", "desc": "{d}"}}')
    gallery_items_str = ",\n".join(items_js)

    video_cards = []
    for idx, v in enumerate(videos_data, 1):
        video_cards.append(f'''        <!-- Video {idx}: {v["title"]} -->
        <div class="video-h-card">
          <div class="video-h-frame">
            <iframe 
              src="https://www.youtube-nocookie.com/embed/{v["id"]}?rel=0&playsinline=1&modestbranding=1" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
              allowfullscreen 
              loading="lazy"
              title="{v["title"]}">
            </iframe>
          </div>
          <div class="video-card-body">
            <div>
              <span class="video-badge-pill red">{v["badge"]}</span>
              <h3>{v["title"]}</h3>
              <p>{v["desc"]}</p>
            </div>
            <a href="https://youtu.be/{v["id"]}" target="_blank" rel="noopener noreferrer" class="btn-yt-link">
              <span>▶ Ver en YouTube ↗</span>
            </a>
          </div>
        </div>''')
    videos_block = "\n\n".join(video_cards)

    html = f'''<!doctype html>
<html lang="es-CO">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex,nofollow">
  <meta name="description" content="Galería fotográfica y registro audiovisual oficial del Día 5: Gran Cierre de la Semana Cultural, Santa Misa de Acción de Gracias y Conmemoración del 53° Aniversario Institucional de la IE El Carmen en Ciénaga, Magdalena.">
  <meta name="theme-color" content="#881337">
  <title>Día 5: Santa Misa &amp; 53° Aniversario Institucional · Galería Oficial | IE El Carmen</title>

  <!-- Google Fonts: Outfit & Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
    :root {{
      --primary: #191253;
      --primary-dark: #0d0933;
      --primary-light: #2c2282;
      --accent-red: #e11d48;
      --accent-red-dark: #be123c;
      --accent-red-deep: #881337;
      --accent-red-light: #ffe4e6;
      --accent-gold: #f59e0b;
      --accent-gold-dark: #d97706;
      --accent-gold-light: #fef3c7;
      --accent-green: #10b981;
      --accent-green-dark: #059669;
      --bg-surface: #f8fafc;
      --bg-card: #ffffff;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --border-subtle: #e2e8f0;
      --shadow-sm: 0 2px 4px rgba(136, 19, 55, 0.04);
      --shadow-md: 0 8px 24px rgba(136, 19, 55, 0.08);
      --shadow-lg: 0 20px 35px -8px rgba(136, 19, 55, 0.16);
      --radius-sm: 8px;
      --radius-md: 16px;
      --radius-lg: 24px;
      --radius-full: 9999px;
    }}

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      scroll-behavior: smooth;
      font-size: 16px;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      background-color: var(--bg-surface);
      color: var(--text-main);
      line-height: 1.6;
      overflow-x: hidden;
    }}

    h1, h2, h3, h4, h5, .font-heading {{
      font-family: 'Outfit', sans-serif;
      font-weight: 700;
      line-height: 1.2;
      color: var(--primary);
    }}

    a {{
      color: inherit;
      text-decoration: none;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .container {{
      width: min(1200px, 100% - 2.5rem);
      margin-inline: auto;
    }}

    /* Top Ribbon */
    .top-ribbon {{
      background: linear-gradient(90deg, #881337 0%, #191253 60%, #b45309 100%);
      color: #e2e8f0;
      font-size: 0.82rem;
      padding: 0.5rem 0;
      border-bottom: 2px solid var(--accent-gold);
    }}
    .top-ribbon .container {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 0.5rem;
    }}

    /* Header Navegación */
    header {{
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(12px);
      position: sticky;
      top: 0;
      z-index: 100;
      border-bottom: 1px solid var(--border-subtle);
      box-shadow: var(--shadow-sm);
    }}
    .nav-container {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-block: 0.85rem;
      gap: 1rem;
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 0.85rem;
      flex-shrink: 0;
    }}
    .brand-logo {{
      width: 44px;
      height: 44px;
      border-radius: 50%;
      object-fit: cover;
      border: 2px solid var(--accent-gold);
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    }}
    .brand-text h2 {{
      font-size: 1.15rem;
      font-weight: 800;
      line-height: 1.1;
      color: var(--primary);
    }}
    .brand-text p {{
      font-size: 0.74rem;
      color: var(--text-muted);
      font-weight: 600;
    }}
    .nav-actions {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      flex-wrap: wrap;
      justify-content: flex-end;
    }}
    .btn-back-nav {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: #fff1f2;
      color: var(--accent-red-dark);
      border: 1px solid #fecdd3;
      padding: 0.45rem 0.95rem;
      border-radius: var(--radius-full);
      font-weight: 700;
      font-size: 0.84rem;
      white-space: nowrap;
    }}
    .btn-back-nav:hover {{
      background: var(--accent-red-dark);
      color: #ffffff;
      border-color: var(--accent-red-dark);
      transform: translateY(-1px);
    }}

    /* Hero de la Galería Dedicada */
    .day-hero {{
      background: linear-gradient(180deg, #ffffff 0%, #fff1f2 40%, #fdf2f8 80%, #f8fafc 100%);
      padding-block: 3.5rem 3rem;
      border-bottom: 1px solid #fecdd3;
    }}
    .breadcrumb-nav {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.84rem;
      font-weight: 600;
      color: var(--text-muted);
      margin-bottom: 1.25rem;
      flex-wrap: wrap;
    }}
    .breadcrumb-nav a:hover {{
      color: var(--accent-red-dark);
    }}
    .hero-badges-wrap {{
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
      margin-bottom: 1rem;
    }}
    .badge-pill {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.35rem 0.85rem;
      border-radius: var(--radius-full);
      font-size: 0.8rem;
      font-weight: 800;
      letter-spacing: 0.02em;
    }}
    .badge-pill.red {{
      background: #ffe4e6;
      color: #9f1239;
      border: 1px solid #fecdd3;
    }}
    .badge-pill.gold {{
      background: #fef3c7;
      color: #92400e;
      border: 1px solid #fde68a;
    }}
    .badge-pill.blue {{
      background: #e0e7ff;
      color: #3730a3;
      border: 1px solid #c7d2fe;
    }}
    .badge-pill.green {{
      background: #d1fae5;
      color: #065f46;
      border: 1px solid #a7f3d0;
    }}

    .day-hero h1 {{
      font-size: clamp(2rem, 4vw, 3.1rem);
      margin-bottom: 1rem;
      color: #881337;
      letter-spacing: -0.02em;
    }}
    .day-hero-lead {{
      font-size: clamp(1rem, 1.4vw, 1.15rem);
      color: #475569;
      max-width: 860px;
      margin-bottom: 1.8rem;
      line-height: 1.65;
    }}
    .hero-stats-row {{
      display: flex;
      gap: 1.5rem;
      flex-wrap: wrap;
      align-items: center;
      padding-top: 1.25rem;
      border-top: 1px dashed #fecdd3;
    }}
    .stat-box {{
      display: flex;
      align-items: baseline;
      gap: 0.45rem;
    }}
    .stat-num {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.8rem;
      font-weight: 900;
      color: #881337;
      line-height: 1;
    }}
    .stat-label {{
      font-size: 0.85rem;
      color: var(--text-muted);
      font-weight: 600;
    }}

    /* Sección Padding */
    .section-padding {{
      padding-block: 3.5rem;
    }}
    .section-title-wrap {{
      margin-bottom: 2.25rem;
      text-align: center;
      max-width: 800px;
      margin-inline: auto;
    }}
    .section-eyebrow {{
      display: inline-block;
      text-transform: uppercase;
      font-size: 0.78rem;
      font-weight: 800;
      letter-spacing: 0.1em;
      color: var(--accent-red-dark);
      margin-bottom: 0.5rem;
    }}
    .section-title {{
      font-size: clamp(1.75rem, 3vw, 2.35rem);
      margin-bottom: 0.75rem;
      color: var(--primary);
    }}
    .section-lead {{
      color: var(--text-muted);
      font-size: 1rem;
      line-height: 1.6;
    }}

    /* Tarjeta Conmemorativa Solemne */
    .solemn-card {{
      background: linear-gradient(135deg, #ffffff 0%, #fff7ed 50%, #fdf2f8 100%);
      border-radius: var(--radius-lg);
      border: 1px solid #fecdd3;
      border-left: 6px solid var(--accent-red);
      box-shadow: var(--shadow-md);
      padding: 2rem;
      margin-bottom: 3rem;
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 2rem;
      align-items: center;
    }}
    @media (max-width: 900px) {{
      .solemn-card {{
        grid-template-columns: 1fr;
      }}
    }}
    .solemn-card h3 {{
      font-size: 1.5rem;
      color: #881337;
      margin-bottom: 0.75rem;
    }}
    .solemn-card p {{
      color: #475569;
      font-size: 0.95rem;
      line-height: 1.65;
      margin-bottom: 1.25rem;
    }}
    .solemn-meta-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
      margin-bottom: 1.5rem;
    }}
    .solemn-meta-list li {{
      display: flex;
      align-items: center;
      gap: 0.6rem;
      font-size: 0.9rem;
      color: #1e293b;
    }}
    .solemn-meta-list li span.icon {{
      font-size: 1.15rem;
      flex-shrink: 0;
    }}
    .solemn-flyer-frame {{
      background: #ffffff;
      padding: 0.75rem;
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-sm);
      border: 1px solid #fecdd3;
      text-align: center;
    }}
    .solemn-flyer-frame img {{
      max-width: 100%;
      height: auto;
      max-height: 380px;
      object-fit: contain;
      border-radius: var(--radius-sm);
    }}

    /* Grid de Videos Horizontales 16:9 */
    .video-group-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.5rem;
      padding-bottom: 0.75rem;
      border-bottom: 2px solid #fecdd3;
      flex-wrap: wrap;
      gap: 0.75rem;
    }}
    .video-group-header h3 {{
      font-size: 1.35rem;
      color: #881337;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .badge-count {{
      font-size: 0.8rem;
      font-weight: 800;
      padding: 0.3rem 0.75rem;
      border-radius: var(--radius-full);
    }}

    .videos-h-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(420px, 1fr));
      gap: 2rem;
      margin-bottom: 2.5rem;
    }}
    @media (max-width: 540px) {{
      .videos-h-grid {{
        grid-template-columns: 1fr;
      }}
    }}
    .video-h-card {{
      background: var(--bg-card);
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-subtle);
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .video-h-card:hover {{
      transform: translateY(-4px);
      box-shadow: var(--shadow-md);
      border-color: #fecdd3;
    }}
    .video-h-frame {{
      position: relative;
      width: 100%;
      padding-top: 56.25%; /* 16:9 */
      background: #000000;
    }}
    .video-h-frame iframe {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border: none;
    }}
    .video-card-body {{
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      flex-grow: 1;
      gap: 1.25rem;
    }}
    .video-badge-pill {{
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 0.25rem 0.65rem;
      border-radius: 4px;
      margin-bottom: 0.5rem;
    }}
    .video-badge-pill.red {{
      background: #ffe4e6;
      color: #9f1239;
    }}
    .video-card-body h3 {{
      font-size: 1.18rem;
      color: var(--primary);
      margin-bottom: 0.45rem;
      line-height: 1.3;
    }}
    .video-card-body p {{
      color: var(--text-muted);
      font-size: 0.88rem;
      line-height: 1.55;
    }}
    .btn-yt-link {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.82rem;
      font-weight: 700;
      color: #881337;
      padding-top: 0.6rem;
      border-top: 1px dashed var(--border-subtle);
    }}
    .btn-yt-link:hover {{
      color: var(--accent-red);
      transform: translateX(3px);
    }}

    /* Galería Fotográfica */
    .photos-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 1.5rem;
    }}
    @media (max-width: 680px) {{
      .photos-grid {{
        grid-template-columns: 1fr;
      }}
    }}
    .photo-card {{
      background: var(--bg-card);
      border-radius: var(--radius-md);
      border: 1px solid var(--border-subtle);
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      cursor: pointer;
      transition: all 0.28s ease;
      outline: none;
    }}
    .photo-card:hover, .photo-card:focus-visible {{
      transform: translateY(-4px);
      box-shadow: var(--shadow-md);
      border-color: #fecdd3;
    }}
    .photo-frame {{
      position: relative;
      width: 100%;
      height: 250px;
      background: #0f172a;
      overflow: hidden;
    }}
    .photo-frame img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.45s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .photo-card:hover .photo-frame img {{
      transform: scale(1.05);
    }}
    .photo-badge-idx {{
      position: absolute;
      top: 12px;
      left: 12px;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(4px);
      color: #ffffff;
      font-size: 0.72rem;
      font-weight: 700;
      padding: 0.25rem 0.6rem;
      border-radius: 4px;
      border: 1px solid rgba(255, 255, 255, 0.15);
    }}
    .photo-zoom-hint {{
      position: absolute;
      bottom: 10px;
      right: 10px;
      background: rgba(136, 19, 55, 0.88);
      backdrop-filter: blur(4px);
      color: #ffffff;
      font-size: 0.74rem;
      font-weight: 700;
      padding: 0.25rem 0.65rem;
      border-radius: var(--radius-full);
      opacity: 0.9;
      transition: opacity 0.2s ease;
    }}
    .photo-card:hover .photo-zoom-hint {{
      opacity: 1;
      background: var(--accent-red-dark);
    }}
    .photo-body {{
      padding: 1.25rem;
      flex-grow: 1;
      display: flex;
      flex-direction: column;
    }}
    .photo-body h4 {{
      font-size: 1.05rem;
      color: var(--primary);
      margin-bottom: 0.4rem;
      line-height: 1.3;
    }}
    .photo-body p {{
      color: var(--text-muted);
      font-size: 0.85rem;
      line-height: 1.5;
    }}

    /* Banner Google Fotos */
    .gphotos-banner {{
      background: linear-gradient(135deg, #881337 0%, #191253 60%, #4c0519 100%);
      border-radius: var(--radius-lg);
      padding: clamp(2rem, 4vw, 3rem);
      color: #ffffff;
      margin-top: 3.5rem;
      box-shadow: var(--shadow-lg);
      position: relative;
      overflow: hidden;
      border: 1px solid rgba(245, 158, 11, 0.3);
    }}
    .gphotos-content {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1.5rem;
      position: relative;
      z-index: 2;
    }}
    .btn-gphotos-big {{
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
      color: #0f172a;
      font-weight: 900;
      font-size: 1rem;
      padding: 0.95rem 1.8rem;
      border-radius: var(--radius-full);
      box-shadow: 0 4px 16px rgba(245, 158, 11, 0.4);
    }}
    .btn-gphotos-big:hover {{
      background: #b45309;
      color: #ffffff;
      transform: translateY(-2px);
    }}

    /* Lightbox Modal Nativo con Navegación */
    .lightbox-modal {{
      border: none;
      border-radius: var(--radius-lg);
      padding: 0;
      background: transparent;
      max-width: min(1040px, 94vw);
      max-height: 92vh;
      margin: auto;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.85);
      overflow: hidden;
    }}
    .lightbox-modal::backdrop {{
      background: rgba(15, 23, 42, 0.94);
      backdrop-filter: blur(12px);
    }}
    .lightbox-inner {{
      background: #0f172a;
      border-radius: var(--radius-lg);
      border: 1px solid rgba(255, 255, 255, 0.15);
      overflow: hidden;
      position: relative;
      display: flex;
      flex-direction: column;
    }}
    .lightbox-img-wrap {{
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #000000;
      min-height: 280px;
    }}
    .lightbox-inner img {{
      max-width: 100%;
      max-height: 72vh;
      object-fit: contain;
      display: block;
      margin: 0 auto;
    }}
    .lightbox-caption-box {{
      padding: 1.25rem 1.75rem;
      background: #0f172a;
      color: #ffffff;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
    }}
    .lightbox-close-btn {{
      position: absolute;
      top: 15px;
      right: 15px;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: rgba(0, 0, 0, 0.7);
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.35);
      font-size: 1.4rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
      z-index: 10;
    }}
    .lightbox-close-btn:hover {{
      background: var(--accent-red);
      border-color: var(--accent-red);
      transform: scale(1.08);
    }}
    .lightbox-nav-btn {{
      position: absolute;
      top: 45%;
      transform: translateY(-50%);
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: rgba(0, 0, 0, 0.65);
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.35);
      font-size: 1.8rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
      z-index: 10;
    }}
    .lightbox-nav-btn:hover {{
      background: rgba(225, 29, 72, 0.9);
      border-color: var(--accent-red);
      transform: translateY(-50%) scale(1.1);
    }}
    .lightbox-nav-btn.lb-prev {{
      left: 15px;
    }}
    .lightbox-nav-btn.lb-next {{
      right: 15px;
    }}

    /* Barra de Navegación entre Días */
    .day-nav-bar {{
      background: #ffffff;
      border-top: 1px solid var(--border-subtle);
      border-bottom: 1px solid var(--border-subtle);
      padding-block: 1.25rem;
    }}
    .day-nav-bar .container {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
    }}

    /* Footer */
    footer {{
      background: var(--primary-dark);
      color: #e2e8f0;
      padding-top: 3.5rem;
      padding-bottom: 2rem;
      border-top: 3px solid var(--accent-gold);
    }}
    .footer-content {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1.5rem;
      margin-bottom: 2.5rem;
    }}
    .footer-bottom {{
      text-align: center;
      font-size: 0.8rem;
      color: #94a3b8;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      padding-top: 1.75rem;
    }}
  </style>
</head>
<body>

  <!-- Top Ribbon Oficial -->
  <div class="top-ribbon">
    <div class="container">
      <div>
        <span>🕊️ Gran Clausura Oficial de la Semana Cultural Carmelista 2026</span>
        <span style="opacity: 0.6; margin-inline: 0.5rem;">|</span>
        <span>53 Años de Vida Institucional (1973 - 2026)</span>
      </div>
      <div>
        <a href="index.html" style="color: var(--accent-gold); font-weight: 700;">← Volver al Portal Oficial</a>
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
            <h2>IE El Carmen de Ciénaga</h2>
            <p>Semana Cultural 2026 · Día 5: Gran Cierre &amp; Aniversario</p>
          </div>
        </a>
      </div>
      <div class="nav-actions">
        <a href="dia1.html" class="btn-back-nav" style="background: #eff6ff; color: #1e40af; border-color: #bfdbfe;" title="Ver Galería del Día 1">
          <span>← Día 1</span>
        </a>
        <a href="dia2.html" class="btn-back-nav" style="background: #ecfdf5; color: #065f46; border-color: #a7f3d0;" title="Ver Galería del Día 2">
          <span>← Día 2</span>
        </a>
        <a href="dia3.html" class="btn-back-nav" style="background: #fef3c7; color: #92400e; border-color: #fde68a;" title="Ver Galería del Día 3">
          <span>← Día 3</span>
        </a>
        <a href="dia4.html" class="btn-back-nav" style="background: #d1fae5; color: #065f46; border-color: #a7f3d0;" title="Ver Galería del Día 4">
          <span>← Día 4: Foro</span>
        </a>
        <a href="index.html" class="btn-back-nav" style="background: #f1f5f9; color: var(--primary); border-color: #cbd5e1;">
          <span>← Portal Semana Cultural</span>
        </a>
        <a href="{GOOGLE_PHOTOS_URL}" target="_blank" rel="noopener noreferrer" class="btn-back-nav" style="background: #eff6ff; color: #1e40af; border-color: #bfdbfe; font-weight: 700;">
          <span>☁️ Álbum Google Fotos ↗</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Hero Día 5 -->
  <section class="day-hero">
    <div class="container">
      <nav class="breadcrumb-nav" aria-label="Ruta de navegación">
        <a href="index.html">Inicio</a>
        <span>›</span>
        <a href="index.html#cronograma">Semana Cultural 2026</a>
        <span>›</span>
        <span style="color: #881337; font-weight: 800;">Día 5: Santa Misa &amp; 53° Aniversario Institucional</span>
      </nav>

      <div class="hero-badges-wrap">
        <span class="badge-pill red">🕊️ Santa Misa de Acción de Gracias</span>
        <span class="badge-pill gold">🎂 53 Años de Historia (1973 - 2026)</span>
        <span class="badge-pill blue">🎖️ Homenaje al Profesor Arlin Jiménez</span>
        <span class="badge-pill green">📍 Sede Principal · Ciénaga</span>
      </div>

      <h1>Día 5: Solemne Santa Misa de Acción de Gracias &amp; 53° Aniversario</h1>
      <p class="day-hero-lead">
        Con profundo júbilo y recogimiento espiritual celebramos el 53° Aniversario de fundación de nuestra querida 
        <strong>Institución Educativa El Carmen de Ciénaga</strong>. Una jornada solemne de acción de gracias con la comunidad 
        educativa reunida en torno al altar, bendición sacerdotal, honores patrios y el sentido homenaje póstumo a la memoria 
        y legado de nuestro recordado maestro <strong>Arlin Jiménez</strong>.
      </p>

      <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; margin-bottom: 1.5rem;">
        <a href="#fotos" class="btn-back-nav" style="background: var(--accent-red); color: #ffffff; border-color: var(--accent-red); padding: 0.65rem 1.3rem; font-size: 0.9rem;">
          <span>📸 Ver Fotos Destacadas (12) ↓</span>
        </a>
        <a href="#videos" class="btn-back-nav" style="background: #ffe4e6; color: #9f1239; border-color: #fecdd3; padding: 0.65rem 1.3rem; font-size: 0.9rem;">
          <span>📺 Ver Videos en YouTube ↓</span>
        </a>
        <a href="{GOOGLE_PHOTOS_URL}" target="_blank" rel="noopener noreferrer" class="btn-back-nav" style="background: #fef3c7; color: #92400e; border-color: #fde68a; padding: 0.65rem 1.3rem; font-size: 0.9rem;">
          <span>☁️ Abrir Álbum en Google Fotos ↗</span>
        </a>
      </div>

      <div class="hero-stats-row">
        <div class="stat-box">
          <span class="stat-num">53</span>
          <span class="stat-label">Años de Historia Carmelista</span>
        </div>
        <div style="width: 1px; height: 32px; background: #fecdd3;"></div>
        <div class="stat-box">
          <span class="stat-num">12</span>
          <span class="stat-label">Fotografías Destacadas</span>
        </div>
        <div style="width: 1px; height: 32px; background: #fecdd3;"></div>
        <div class="stat-box">
          <span class="stat-num">2</span>
          <span class="stat-label">Videos Oficiales en YouTube</span>
        </div>
        <div style="width: 1px; height: 32px; background: #fecdd3;"></div>
        <div class="stat-box">
          <span class="stat-num">100%</span>
          <span class="stat-label">Gratitud y Sentido de Pertenencia</span>
        </div>
      </div>
    </div>
  </section>

  <!-- Tarjeta Solemne / Invitación Institucional -->
  <section class="section-padding" style="background: #ffffff; padding-bottom: 1rem;">
    <div class="container">
      <div class="solemn-card">
        <div>
          <span class="badge-pill red" style="margin-bottom: 0.75rem;">Conmemoración &amp; Eucaristía</span>
          <h3>53 Años Educando para Preservar y Emprender</h3>
          <p>
            Desde 1973, nuestra institución ha forjado generaciones de ciudadanos comprometidos con Ciénaga y el Magdalena. 
            Esta Eucaristía reunió a directivos docentes, maestros, padres de familia, alumnos de todas las sedes y jóvenes 
            de la Promoción 2026 en un solo corazón, dando gracias al Creador y a nuestra patrona, la Virgen del Carmen.
          </p>
          <ul class="solemn-meta-list">
            <li>
              <span class="icon">🎂</span>
              <span><strong>Gala Conmemorativa:</strong> 53 años de labor pedagógica y servicio a la comunidad cienguera.</span>
            </li>
            <li>
              <span class="icon">🕊️</span>
              <span><strong>Santa Misa Solemne:</strong> Eucaristía de acción de gracias por las metas alcanzadas en la Semana Cultural 2026.</span>
            </li>
            <li>
              <span class="icon">🕯️</span>
              <span><strong>In Memoriam:</strong> Primer aniversario del viaje a la eternidad de nuestro docente <strong>Arlin Jiménez</strong>.</span>
            </li>
            <li>
              <span class="icon">📍</span>
              <span><strong>Lugar:</strong> Patio techado de la Sede Principal (Calle 18B # 38-34, Barrio Micael Cotes).</span>
            </li>
          </ul>

          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
            <a href="#videos" class="btn-back-nav" style="background: var(--accent-red); color: #ffffff; border-color: var(--accent-red); padding: 0.6rem 1.2rem;">
              <span>📺 Ver Videos de la Jornada ↓</span>
            </a>
            <a href="#fotos" class="btn-back-nav" style="background: #fef3c7; color: #92400e; border-color: #fde68a; padding: 0.6rem 1.2rem;">
              <span>📸 Explorar Galería de Fotos ↓</span>
            </a>
            <a href="{GOOGLE_PHOTOS_URL}" target="_blank" rel="noopener noreferrer" class="btn-back-nav" style="background: #eff6ff; color: #1e40af; border-color: #bfdbfe; padding: 0.6rem 1.2rem;">
              <span>☁️ Álbum en Google Fotos ↗</span>
            </a>
          </div>
        </div>

        <div class="solemn-flyer-frame">
          <a href="afiche_misa.png" target="_blank" title="Clic para ampliar el afiche conmemorativo">
            <img src="afiche_misa.png" alt="Afiche Oficial de la Santa Misa - 53 Años IE El Carmen" loading="lazy">
          </a>
          <p style="font-size: 0.75rem; color: var(--text-muted); margin-top: 0.5rem; font-weight: 600;">
            Tarjeta conmemorativa oficial de la Santa Misa
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- Sección: Videos en Streaming (Panorámicos 16:9) -->
  <section class="section-padding" id="videos" style="background: #ffffff; border-top: 1px solid var(--border-subtle);">
    <div class="container">
      <div class="section-title-wrap">
        <span class="section-eyebrow">Registro Audiovisual Oficial</span>
        <h2 class="section-title">Videos Conmemorativos en YouTube</h2>
        <p class="section-lead">
          Revive la solemnidad de los actos protocolarios con el himno institucional y el video resumen que compila 
          los momentos más memorables de la Semana Cultural Carmelista 2026.
        </p>
      </div>

      <div class="video-group-header">
        <h3>📺 Cobertura Especial en Formato Panorámico (16:9)</h3>
        <span class="badge-count" style="background: #ffe4e6; color: #9f1239;">2 Videos Oficiales</span>
      </div>

      <div class="videos-h-grid">
{videos_block}
      </div>
    </div>
  </section>

  <!-- Sección: Galería Fotográfica Oficial -->
  <section class="section-padding" id="fotos" style="background: var(--bg-surface); border-top: 1px solid var(--border-subtle);">
    <div class="container">
      <div class="section-title-wrap">
        <span class="section-eyebrow">Galería Fotográfica Oficial</span>
        <h2 class="section-title">Registro Fotográfico Destacado ({len(photos_data)})</h2>
        <p class="section-lead">
          Haz clic o toca cualquier imagen para abrirla en pantalla completa con el visor interactivo y navegar entre las fotos.
        </p>
      </div>

      <div class="photos-grid">
{cards_block}
      </div>

      <!-- Banner Álbum Oficial en Google Fotos -->
      <div class="gphotos-banner">
        <div class="gphotos-content">
          <div style="max-width: 650px;">
            <span style="background: rgba(245, 158, 11, 0.2); color: #fde68a; font-size: 0.82rem; font-weight: 800; padding: 0.3rem 0.85rem; border-radius: var(--radius-full); display: inline-block; margin-bottom: 0.75rem;">
              ☁️ Repositorio Institucional en la Nube
            </span>
            <h3 style="font-size: clamp(1.4rem, 2.8vw, 1.9rem); color: #ffffff; margin-bottom: 0.6rem; font-family: 'Outfit', sans-serif;">
              ¿Deseas revivir y descargar todas las fotos en resolución original?
            </h3>
            <p style="font-size: 0.95rem; color: #cbd5e1; line-height: 1.6;">
              Accede al álbum conmemorativo oficial de la Santa Misa y los 53 años de la IE El Carmen en Google Fotos para compartir con familiares, docentes y egresados.
            </p>
          </div>
          <div style="display: flex; flex-direction: column; gap: 0.5rem; align-items: center;">
            <a href="{GOOGLE_PHOTOS_URL}" target="_blank" rel="noopener noreferrer" class="btn-gphotos-big">
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
      <a href="dia4.html" class="btn-back-nav" style="background: #ecfdf5; color: #065f46; border-color: #a7f3d0;">
        <span>← Ver Galería Día 4: Foro «Salvemos la Ciénaga» &amp; Sede GFM</span>
      </a>

      <div style="font-size: 0.92rem; font-weight: 700; color: var(--primary);">
        <span>Clausura Exitosa: </span>
        <a href="index.html" style="color: var(--accent-red-dark); text-decoration: underline;">
          Volver a la Portada Oficial de la Semana Cultural 2026 →
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
            <p style="font-size: 0.82rem; color: #94a3b8;">Ciénaga, Magdalena · Barrio Micael Cotes · Calle 18B # 38-34 · Código DANE: 147189001160</p>
          </div>
        </div>
        <div>
          <a href="index.html" style="color: var(--accent-gold); font-weight: 700;">Semana Cultural Carmelista 2026</a>
        </div>
      </div>

      <div class="footer-bottom">
        <p>© 2026 Institución Educativa El Carmen. Portal Oficial de la Semana Cultural (semanacultural.elcarmencienaga.edu.co). Todos los derechos reservados.</p>
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
            Foto 1 de {len(photos_data)}
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
{gallery_items_str}
    ];
    let currentPhotoIdx = 0;

    function openLightbox(idx) {{
      if (idx < 0 || idx >= galleryItems.length) return;
      currentPhotoIdx = idx;
      updateLightboxContent();

      const dialog = document.getElementById('photo-lightbox');
      if (dialog && !dialog.open) {{
        dialog.showModal();
      }}
    }}

    function updateLightboxContent() {{
      const item = galleryItems[currentPhotoIdx];
      const img = document.getElementById('lightbox-img');
      const titleEl = document.getElementById('lightbox-title');
      const captionEl = document.getElementById('lightbox-caption');
      const counterEl = document.getElementById('lightbox-counter');

      if (img && item) {{
        img.src = item.file;
        img.alt = item.title || 'Fotografía ampliada';
        if (titleEl) titleEl.textContent = item.title || '';
        if (captionEl) captionEl.textContent = item.desc || '';
        if (counterEl) counterEl.textContent = `Foto ${{currentPhotoIdx + 1}} de ${{galleryItems.length}}`;
      }}
    }}

    function changeLightbox(step) {{
      currentPhotoIdx = (currentPhotoIdx + step + galleryItems.length) % galleryItems.length;
      updateLightboxContent();
    }}

    function closeLightbox() {{
      const dialog = document.getElementById('photo-lightbox');
      if (dialog && dialog.open) {{
        dialog.close();
      }}
    }}

    // Cerrar al hacer clic fuera del modal
    const lbDialog = document.getElementById('photo-lightbox');
    if (lbDialog) {{
      lbDialog.addEventListener('click', (e) => {{
        const rect = lbDialog.getBoundingClientRect();
        const isInDialog = (rect.top <= e.clientY && e.clientY <= rect.top + rect.height &&
          rect.left <= e.clientX && e.clientX <= rect.left + rect.width);
        if (!isInDialog) {{
          closeLightbox();
        }}
      }});
    }}

    // Navegación con flechas del teclado
    document.addEventListener('keydown', (e) => {{
      const dialog = document.getElementById('photo-lightbox');
      if (dialog && dialog.open) {{
        if (e.key === 'ArrowLeft') {{
          changeLightbox(-1);
        }} else if (e.key === 'ArrowRight') {{
          changeLightbox(1);
        }}
      }}
    }});
  </script>
</body>
</html>
'''
    return html

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    lab_out = os.path.join(base_dir, '..', 'laboratorio', 'dia5.html')
    sem_out = os.path.join(base_dir, '..', 'semanacultural', 'dia5.html')

    content = generate_dia5_html()
    with open(lab_out, 'w', encoding='utf-8') as f:
        f.write(content)
    with open(sem_out, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Generated {lab_out} ({len(content)} bytes)")
    print(f"Generated {sem_out} ({len(content)} bytes)")
