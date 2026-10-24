# DEMOS: noticias, galería y orientación de admisiones

## Alcance

Primera versión para revisión; cambios de interfaz limitados a demos/. Producción, laboratorio, DNS, WordPress y configuración de despliegue se conservan. DESIGN_SYSTEM.md pierde los marcadores de conflicto y conserva ambas familias de componentes como variantes compatibles.

- Noticias: tres tarjetas de Semana Cultural 2026 ordenadas por fecha de evento; no son fechas de publicación. Contenido enlazado a las memorias ya existentes.
- Galería: colección inicial de afiches con ampliación, navegación circular y por flechas, cierre nativo con Escape y retorno de foco. Sin JavaScript, abre el original. Los botones de álbum llevan al portal cultural.
- Admisiones: página informativa con la oferta de preescolar, básica y media que figura en la portada institucional; ruta de orientación y preguntas frecuentes. No anuncia convocatorias, plazos, requisitos ni cupos confirmados; no recopila datos. Correo tomado de la portada: ieelcarmen@semcienaga.gov.co.
- Una única hoja institucional; sin estilos inline ni nueva paleta. Se añaden componentes documentados con tokens existentes, contraste de texto sobre verde, foco visible, ajuste móvil y movimiento reducido.

## Revisión del entorno y Actions

Base revisada: main, 96d515879fe1658ba142187de4c77ea4a32ceb91.
Lectura de AGENTS.md, ONBOARDING_AGENTE.md, ESTADO_PROYECTO.md, CONTINUAR_EN_CODEX.md, MEMORIA.md, tarea de laboratorio, fuentes de producción y laboratorio y estilos de DEMOS. Engram local no está disponible en esta sesión; no se creó almacén sustituto.

El workflow deploy-demos.yml publica demos/ ante push en main, feat/website-laboratory o demos/**, con filtros de rutas; admite ejecución manual. La rama feat/demos-community-portal no coincide con esos disparadores. Abrir este PR no despliega; integrarlo en main sí activa la publicación de DEMOS.

La ejecución 40132454760 y el job 120986870598 terminaron con éxito. El log muestra empaquetado, envío aceptado por hosting_deploy, solicitud de purga y HTTP 200. Su verificación HTTP no compara el contenido con el commit. El script no trata isError del resultado MCP como error ni establece timeout de las solicitudes; queda como mejora separada para no mezclar infraestructura con esta interfaz.

## Verificación realizada

- node --check demos/js/galeria.js: correcto.
- Comprobación HTML con html.parser: un h1 por página, IDs únicos, anclas existentes, enlaces locales válidos, sin estilos inline ni enlaces vacíos.
- Ejecución del controlador en Node con DOM simulado: apertura, anterior/siguiente circular, flechas, cierre, retorno de foco y Ctrl+clic correctos.
- DEMOS, Laboratorio y Producción: HTTPS 200 en lectura pública; los tres afiches referenciados responden 200 image/jpeg.
- No se cambió el escudo existente; las imágenes y álbumes dependen del subdominio semanacultural. Fuentes remotas con fallback local.
- Revisión visual real y comportamiento nativo del diálogo pendientes: Chromium no está disponible y la descarga del navegador falló en este entorno. Las comprobaciones simuladas no acreditan distribución visual ni confinamiento nativo del foco.

## Revisión manual antes de integrar

1. Servir el repositorio con python -m http.server 8000 --bind 127.0.0.1 y abrir /demos/.
2. Revisar a 360 px y escritorio: navegación, títulos, imágenes, desbordamiento y legibilidad.
3. Recorrer con Tab; abrir galería con Enter, usar flechas, Tab/Shift+Tab dentro del diálogo y Escape. Confirmar retorno al afiche que lo abrió.
4. Desactivar JavaScript y comprobar enlaces a originales y álbumes.
5. Abrir admisiones, revisar preguntas y correo. Validar con directivas el contenido antes de introducir fechas, documentos o formularios reales.
6. Tras integrar y desplegar, comprobar /, /admisiones.html, CSS, JS y escudo en DEMOS, y comparar contenido servido con el commit. No promover a Producción con este PR.
