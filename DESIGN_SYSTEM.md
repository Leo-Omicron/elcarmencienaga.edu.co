# Sistema de diseño institucional — referencia Semana Cultural 2026

## Alcance y autoridad

La reingeniería del 24 de octubre de 2026 toma como referencia explícita la portada de
https://semanacultural.elcarmencienaga.edu.co/ y `dia1.html` a `dia5.html`.
Esta edición se aplica **solo a `demos/`**. Los estilos de Laboratorio, Semana Cultural
y la raíz de producción conservan su comportamiento hasta una promoción aprobada.
La petición actual autoriza reemplazar las reglas anteriores de DEMOS por estos patrones.

## Fuente de verdad

`demos/css/institucional.css` contiene los tokens y la composición original de la portada.
`demos/css/dia1.css` … `dia5.css` conservan las variantes de cada jornada, después de
la hoja base. `demos/css/accesibilidad.css` se carga al final para navegación, foco,
movimiento reducido y los módulos de cierre/noticias/admisiones.
No usar estilos decorativos inline. Las clases `index-detail-*` y `diaN-detail-*`
son declaraciones de la referencia extraídas sin cambiar sus valores; no son una
API para nuevos componentes. Nuevos componentes deben usar nombres semánticos.

## Tokens observados

| Token | Valor | Uso |
|---|---|---|
| `--primary` | `#191253` | Azul profundo, títulos y botones principales |
| `--primary-dark` | `#0d0933` | Profundidad y superficies oscuras |
| `--primary-light` | `#2c2282` | Variante de marca presente en la referencia |
| `--accent-green` | `#10b981` | Comunidad, contacto, emprendimiento |
| `--accent-green-dark` | `#059669` | Estados y enlaces |
| `--accent-gold` | `#f59e0b` | Aniversario, énfasis, contornos |
| `--accent-gold-light` | `#fef3c7` | Badges y superficies suaves |
| `--accent-red` | `#e11d48` | Celebración, badges y variante del Día 5 |
| `--accent-blue` | `#0284c7` | Cobertura audiovisual y deporte |
| `--bg-surface` | `#f8fafc` | Fondo general |
| `--bg-card` | `#ffffff` | Tarjetas y encabezado |
| `--text-main` | `#0f172a` | Texto principal |
| `--text-muted` | `#64748b` | Texto secundario |
| `--border-subtle` | `#e2e8f0` | Separadores |

Las variantes de jornada conservan sus tokens adicionales y sombras originales.
No sustituir el azul por un morado genérico. Los acentos de colores encontrados en
la referencia sí forman parte del diseño autorizado, incluido el botón de Instagram.

## Tipografía, espacio y geometría

- **Outfit** para títulos; **Plus Jakarta Sans** para cuerpo y navegación, con fallback sans-serif.
- Contenedor: `min(1200px, 100% - 2.5rem)` en portada; respetar variantes de galería.
- Radios: 8, 16, 24 píxeles y 9999 píxeles para píldoras.
- Sombras suaves de marca, elevación al hover, transiciones de 0.25 segundos.
- Cabecera blanca fija, escudo circular real, marca y navegación; franja superior degradada.
- Hero de dos columnas, título grande azul/dorado, fondo de halos suaves y afiche íntegro.
- Móvil: columnas apiladas, navegación de jornadas visible, botones envolventes.

## Componentes

| Clases | Contrato |
|---|---|
| `.official-header.header-institucional`, `.nav-wrapper`, `.brand-group`, `.brand-logo` | Encabezado blanco de la referencia, nunca asumir fondo azul por una guía antigua |
| `.env-banner`, `.env-link` | Identificar DEMOS y enlazar al portal publicado |
| `.hero`, `.hero-grid`, `.hero-title`, `.hero-poster-card` | Composición original de portada |
| `.day-hero`, `.badge-pill`, `.breadcrumb-nav` | Hero y ruta de cada galería |
| `.btn-primary`, `.btn-secondary`, `.btn-nav` | Botones de la referencia, foco visible, texto descriptivo |
| `.day-pill-card`, `.days-grid` | Accesos nativos a las cinco galerías |
| `.day-showcase-card`, `.day-showcase-body` | Evento en dos columnas con inversión alternada |
| `.news-card`, `.news-card-img`, `.news-card-content`, `.news-grid` | Noticias con fotografía y acceso a memoria |
| `.photo-card`, `.photos-grid`, `.photo-frame` | Muestra fotográfica, acceso por ratón, Enter y Espacio |
| `.lightbox-*`, `.is-zoomed` | Diálogo nativo, flechas, Escape, zoom y retorno al activador |
| `.closure-section`, `.closure-grid`, `.closure-stats` | Cierre con Santa Misa del 23/10/2026, imagen real y agradecimiento |
| `.admissions-question` | Preguntas desplegables; orientación sin recopilar datos |
| `.official-footer.footer-institucional` | Pie heredado del portal, identificado como DEMOS |

## Contenido y accesibilidad

Preservar los afiches y las fotografías reales, sus proporciones y los enlaces a álbumes
y YouTube. La fuente tiene 12 fotos destacadas en el Día 5 (no confundir con el total del álbum).
El cierre es una memoria, no una convocatoria futura. No mantener un contador a cero.
No inventar cupos, fechas de matrícula ni requisitos. Mantener `noindex,nofollow` en DEMOS.
Usar salto al contenido, landmarks, foco visible, texto alternativo y movimiento reducido.
Los iframes se cargan de forma diferida; su disponibilidad depende de YouTube.

## Promoción

Trabajar mediante PR hacia `main`. Una rama `demos/**` activa el despliegue **solo de DEMOS**
según el workflow existente. La revisión visual de Leo precede a cualquier promoción a
Laboratorio; una aprobación posterior precede a Producción. No sincronizar directorios
completos ni cambiar DNS para promover esta propuesta. Revertir el commit permite recuperar
la versión anterior de DEMOS; verificar el contenido después del despliegue.
