# Reingeniería DEMOS — 24 de octubre de 2026

## Alcance

Recrear la portada y cinco galerías de Semana Cultural en DEMOS, con cierre de la
Santa Misa del viernes 23/10, noticias y orientación de admisiones. Autorizado por Leo.
Sin modificaciones a `laboratorio/`, `semanacultural/`, raíz productiva, DNS o WordPress.
Engram local no accesible en esta sesión; se usaron instrucciones y fuentes versionadas.

## Evidencia de referencia

Se descargaron las seis páginas públicas el 24/10/2026. Sus HTML coinciden con los
archivos de `semanacultural/` en main `742b86a` al normalizar CRLF. Se conserva su CSS,
afiche, fotografías, tipografía, navegación de jornadas, videos y enlaces a álbumes.
Las declaraciones inline se extrajeron a clases; scripts a archivos externos.
Se añade navegación móvil explícita, teclado, movimiento reducido y zoom del visor.
No se afirma que la reproducción externa de YouTube esté garantizada.

## Cambios editoriales

Cierre destacado con foto real del altar, agradecimiento y enlace a Día 5. Sustitución
del contador vencido por estado de memoria. Noticias con enlaces locales. Corrección
de ancla rota heredada del Día 4 y pie de DEMOS. Admisiones continúa informativo.
Día 5 contiene 12 fotos destacadas en la fuente real, aunque otros documentos dicen 13.

## Validación reproducible

`python scripts/check_demos.py` (Python 3 y Node.js) comprueba enlaces locales y anclas,
IDs únicos, ausencia de estilos inline, sintaxis JS y, con ejecución de las funciones
del visor, todos los índices, apertura/cierre y navegación circular. Resultado: PASS.
Las cinco galerías tienen 20/34/21/49/12 fotos y 8/3/13/19/2 videos incrustados.
Esto no sustituye una revisión visual en navegador ni acredita reproducción en YouTube.

## Publicación y promoción

Rama `demos/cultural-reengineering`, PR hacia main. El workflow existente despliega
`demos/` cuando recibe un push a `demos/**`; no despliega Laboratorio ni Producción.
El commit incluye solo DEMOS, esta documentación, DESIGN_SYSTEM y el validador.
Verificar ejecución de Actions y contenido publicado antes de anunciar el despliegue.

Recomendación: revisar escritorio/móvil, cinco galerías, teclado, zoom y admisiones en
DEMOS; registrar aprobación de Leo para preparar después la promoción a Laboratorio.
Mantener la misma versión candidata en cada etapa, registrar SHA y evidencias, y
promover a Producción únicamente tras nueva aprobación. Reversión: revertir este commit
y comprobar el contenido que efectivamente publicó Actions. No copiar toda la raíz web.
