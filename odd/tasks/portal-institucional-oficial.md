# Portal Institucional Oficial y Cartelera Híbrida (Opción A)

Objetivo: Implementar en `laboratorio/` la nueva portada institucional definitiva para `elcarmencienaga.edu.co` (`target: portal-principal`), reemplazando el aviso provisional de sitio en construcción por una arquitectura completa con cumplimiento de la Ley 1712 de 2014 (Transparencia), cartelera de actualidad híbrida (`data/noticias.json` + conector REST API de WordPress), horizonte institucional, sedes, oferta educativa, admisiones/PQRSDF y acceso al ecosistema digital y archivo histórico de la Semana Cultural 2026.

## Alcance aprobado por Leo (27/10/2026)

1. **Arquitectura Opción A (Híbrida):**
   - Portada principal estática y modular en `laboratorio/index.html`, enlazando `css/institucional.css` y `css/portal.css` conforme a `DESIGN_SYSTEM.md`.
   - Cartelera de actualidad y avisos alimentada por `data/noticias.json` con soporte nativo en `js/portal.js` para consultar `/wp-json/wp/v2/posts?_embed` cuando se habilite el subdominio editorial de WordPress, manteniendo renderizado estático base y degradación elegante sin JavaScript.
2. **Secciones obligatorias e institucionales:**
   - Cinta superior de aviso institucional + Cabecera oficial fija (`DANE 147189001160`, `NIT 819002071-3`).
   - Hero institucional con acceso directo a actualidad, admisiones y memoria cultural.
   - Cartelera de Actualidad y Avisos Oficiales con filtros por categoría (`Todas`, `Rectoría`, `Académico`, `Deportes`, `Comunidad`).
   - Horizonte Institucional, Símbolos y Sedes (`Sede Principal Micael Cotes` y `Sede Guillermo F. Morán`).
   - Oferta Educativa (Preescolar, Básica Primaria, Básica Secundaria y Media) y Proyectos Pedagógicos Transversales (PRAE, Emprendimiento, Ciencia, Deporte).
   - Transparencia y Normatividad (Ley 1712 de 2014: PEI, Manual de Convivencia, SIEE, Gobierno Escolar, Resoluciones 2293 de 2022 y 931 de 2023, Rendición de Cuentas).
   - Admisiones, Matrículas y Atención al Ciudadano (PQRSDF) sin inventar cupos ni fechas no publicadas.
   - Ecosistema Digital (Plataforma de Aplicaciones / Consolidados, Comunidad WordPress y Archivo Histórico de la Semana Cultural 2026 en `semanacultural.elcarmencienaga.edu.co`).
3. **Página personalizada de Módulos en Construcción (`laboratorio/en-construccion.html`):**
   - Diseño institucional adaptable a escritorio y móvil con hoja de ruta de transformación digital por fases.
   - Personalización dinámica mediante `en-construccion.html?modulo=...` (`pei`, `manual-convivencia`, `siee`, `gobierno-escolar`, `wordpress-comunidad`, `plataforma-notas`) gestionada desde `js/portal.js`.
4. **Manifiesto de publicación (`deploy/release.json`):**
   - Destino configurado en `portal-principal` con los 12 archivos validados (primero se valida en `laboratorio` → `https://lab.elcarmencienaga.edu.co/` tras PR y merge, y solo se promueve a `https://elcarmencienaga.edu.co/` tras revisión y aprobación protegida de Leo).
