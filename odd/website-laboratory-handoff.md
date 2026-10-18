# Retomar el laboratorio web
Pausa solicitada por el usuario para reiniciar Pi. Fecha de evidencia: 18 de octubre de 2026.
Proyecto: `D:/Leo/Proyectos/IEEC/Landing`. Rama: `feat/website-laboratory`.

## Leer primero
1. Recuperar memoria con `mem_context`, buscar `website-laboratory` en este proyecto y leer la observación completa 1063 (topic `odd/website-laboratory/tasks`).
2. Leer `odd/tasks/website-laboratory.md` completo y reconciliar con este punto de retomada.
3. Leer `laboratorio/README.md` y `laboratorio/index.html`; consultar `git status` antes de editar. No asumir repositorio limpio.

## Estado real al cerrar
- Laboratorio publicado: https://pruebas.elcarmencienaga.edu.co/ . Sitio vacío creado en el pedido existente con costo incluido confirmado por el usuario; no se compraron extras.
- Provisión completada, sitio habilitado tipo `other`. Raíces documentales de laboratorio y producción verificadas distintas y no anidadas. Comparten recursos de hosting: NO afirmar aislamiento de seguridad completo.
- Inventario antes de subir: solamente `default.php`. Se creó únicamente `index.html` por TUS POST201/PATCH204, offset6395. Se conservó `default.php`. No enviar README ni archivos del proyecto al hosting.
- HTML público coincide byte a byte con `laboratorio/index.html`: 6395bytes; SHA256 `6d575067e8af35807a870b8ecece51864d6bc803d4d9454dd28bc5b59a0c0e3f`.
- HTTPS raíz e `/index.html`: HTTP200. HTTP redirige a HTTPS. Certificado validado por cliente HTTP; API SSL active/redirectHTTPS true.
- Producción https://elcarmencienaga.edu.co/ responde200 y su contenido coincide con `index.html` local normalizando finales de línea. No fue destino de escrituras.
- Última comprobación de cierre: job15 exit0, laboratorioHTTPS200/source-matchTrue, producciónHTTPS200/source-matchTrue. No hubo mutaciones remotas en el cierre. Todos los jobs de shell previos estaban terminados; el último también terminó.
- La comprobación estructural HTML pasó (idioma, viewport, noindex, h1, IDs/anclas, vínculo a producción, sin scripts/formularios). No hay prueba visual, móvil real o teclado en navegador: no había navegador en PATH y no se instaló ninguno.
- La lectura literal `content` por API de archivos no coincidió con fuente; causa no determinada. No confundir con despliegue fallido: el contenido HTTP público sí coincidió exactamente. No repetir cargas para investigar esto.

## Pendiente y punto exacto de retomada
- T1 y T2 completas; T3 bloqueada por falta de informe independiente. Subagente `mve1tgzm-a-8fi3` terminó con `assistant reported an error`, sin resultado verificable. No atribuirle PASS ni fase de fallo. No relanzar verificadores ni investigar el harness automáticamente.
- El usuario pidió pausar, no resolver este límite ahora. Al retomar, explicar que la demo funciona pero no tiene cierre independiente/visual, y resolver con el usuario cómo aceptar esos límites antes del cierre pendiente. No volver a crear el sitio ni subir de nuevo el mismo archivo.
- No hay commits propios del laboratorio ni push/PR. No afirmar copia de seguridad remota del código. Archivos están guardados en disco y continuidad en memoria; conservar staging ajeno.
- Assessment previo con escalación de riesgo5 requirió verificador independiente; evaluación nativa unassessable por untracked sin declarar. No se inició lineage/review del laboratorio. No iniciar review sobre todo el staging heredado. Si corresponde una nueva evaluación, delimitar solamente esta unidad y seguir autoridad/consentimiento nativos, sin reconstruir bindings.
- Próximo ejercicio sugerido, todavía no aplicado: editar un título en local, previsualizar, respaldar versión remota antes de reemplazarla, publicar solo laboratorio, verificar y revertir. Primero que el usuario vea la demo. Guía en `laboratorio/README.md`.

## Preservar Git y trabajo anterior
Estado al cierre, antes de agregar este archivo de continuidad:
- Modificados humanos: `CONTINUAR_EN_CODEX.md`, `ESTADO_PROYECTO.md`; además `.gitignore` y `MEMORIA.md` tienen cambios previos.
- Staged existente: `MEMORIA.md` (también con cambios unstaged), `scripts/engram_runtime.py`, `tests/test_engram_runtime.py`.
- Untracked: `.engram/`, `AGENTS.md`, `laboratorio/`, `odd/`.
- No ejecutar `git add .`, `commit -a`, reset, clean, restore ni sobrescribir esos archivos. Futuros commits del laboratorio deben seleccionar solo sus rutas.

## Restricciones vigentes
- No tocar producción, DNS/correo, registro Google Education ni migrar WordPress. Usuario espera activación de licencias; no repetir trámites.
- Sin gastos/extras, formularios, analítica, datos personales/estudiantiles ni contenido oficial inventado. `noindex,nofollow` NO es privacidad ni autenticación.
- Engram anterior quedó operativo pero su cierre fue detenido por el usuario. No ejecutar sus pruebas, revisiones, reinicios ni commits. Pi sí conserva memoria normal y puede pasar contexto a otros agentes cuando se necesite.
- Si hace falta Hostinger en otra tarea autorizada: usar conector ya instalado por `npx.cmd --offline --no-install`, sin descargar. No guardar ni imprimir credenciales, URLs autenticadas o identificadores de cuenta. No usar despliegue de archivo comprimido destructivo. No hay necesidad de acceder a credenciales para simplemente retomar esta lectura.

## Memoria
Proyecto Engram: `elcarmencienaga.edu.co`. 1063 contiene la especificación/tareas; 1064 registra el despliegue. Buscar también `handoff/current-priority` para la prioridad vigente, que se actualiza al cierre. Esta nota evita depender de logs temporales y del historial compactado.
