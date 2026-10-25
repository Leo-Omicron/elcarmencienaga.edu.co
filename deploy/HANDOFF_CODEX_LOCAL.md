# Encargo autorizado: Codex local → Engram → Antigravity

Leo pidió expresamente al cerrar las pruebas: documentar todo el flujo para agentes
locales, dejar mensaje a Codex local para que actualice Engram y después hacer relevo
a Antigravity. Este archivo es ese mensaje; no acredita que las instancias lo hayan leído.

## Mensaje a Codex local

Codex local: el flujo institucional cambió. Lee primero `AGENTS.md`, `deploy/README.md`
y `deploy/PRUEBAS_FLUJO_2026-10-24.md`. El ciclo PR → Actions Lab → revisión de Leo →
promoción del paquete exacto → aprobación protegida → rollback protegido ya se ejercitó
con dos archivos nuevos. Deja de usar hosting_deploy/TUS/SFTP manual como vía habitual
de publicación institucional. DEMOS es independiente, no un escalón hacia Lab/Prod.

1. Inspecciona tu checkout en `D:\Leo\Proyectos\IEEC\Landing` y preserva TODO cambio
   humano/local, incluidos CONTINUAR_EN_CODEX.md, ESTADO_PROYECTO.md y memoria. Consulta
   origin y rama; fetch y compara. Incorpora el PR de este relevo solo cuando esté fusionado,
   con avance rápido si procede o worktree aparte; no fuerces main ni hagas reset/clean.
2. Lee la documentación completa y los YAML/Python vigentes. Verifica por lectura el
   estado de los runs enlazados, variable, secretos (solo nombres) y protecciones si tienes
   permisos. Una tarea de sincronización de memoria NO autoriza nuevos despliegues.
3. Leo autoriza en este encargo actualizar Engram. La antigua pausa sobre trabajo de
   Engram no bloquea esta actualización de continuidad; no autoriza rediseñar su runtime,
   migrar la base, reinstalar herramientas ni reiniciar aplicaciones indiscriminadamente.
4. Usa mem_current_project con cwd real si existe, mem_context y búsqueda del proyecto;
   recupera observaciones completas antes de actualizar. Confirma identidad y almacén
   existentes con `MEMORIA.md`. No crees base/proyecto alternativo si no responde.
5. Si vas a modificar el almacén, haz primero respaldo con su mecanismo existente y
   comprueba recuperabilidad según MEMORIA.md. No copies una SQLite viva por fuerza.
   Usa los MCP/CLI ya configurados; no inventes nombres de herramientas disponibles.
6. Guarda observaciones curadas por tema, con fecha, fuentes y límites; actualiza el
   punto de continuidad y añade una nota de supersesión al procedimiento antiguo.
   No borres historia válida: el despliegue por MCP ocurrió, pero ya no es la vía vigente.
7. Recupera lo recién guardado mediante la herramienta de lectura y comprueba que el
   contenido completo contiene IDs, separación de entornos y pendientes correctos.
   Informa qué quedó guardado, IDs reales y verificación; si falla, dilo sin afirmar éxito.
8. Deja a Antigravity el mensaje inferior y referencias a las observaciones realmente
   creadas. Usa el mecanismo local compartido/repo; no afirmes haber contactado otra sesión
   si solo dejaste un archivo. Evita mensajes externos fuera del encargo.

### Contenido mínimo a guardar en Engram

- Política obligatoria de PR/main/Actions; Leo hace merge y aprueba contenido y deployment.
- DEMOS separado; MCP de Hostinger no se usa para saltarse protecciones institucionales.
- Entornos main-only, revisor Leo-Omicron, self-review permitido y admin bypass desactivado.
- Cinco nombres de secretos por entorno, variable INSTITUTIONAL_DEPLOY_ENABLED y su efecto;
  sin valores privados. La clave privada no se pide por chat ni se versiona.
- Manifiesto explícito y recursos dependientes, origen laboratorio, targets y límites estáticos.
- Artefacto 30 días, commit/hash/receipt, paquete exacto y diferencia run ID / release ID / SHA.
- PRs #6 y #8, candidato 1a20d000dc2843e5c22024b2be4c2ad3ca2894d6;
  Lab40144556888, promote40145795225, rollback40146188051.
- Release productivo revertido40145795225-1-1a20d000dc2843e5c22024b2be4c2ad3ca2894d6.
- API jobs/capturas acreditan Success; revisión final web reportada por Leo, no auditoría
  independiente de toda producción. Restauración de archivo existente aún no probada en vivo.
- Producción con prueba retirada, Lab conservado; Git/manifiesto conservan prueba y variable
  true al cierre. No repetir promoción/rollback ni limpiar backups al retomar.
- Copias privadas fuera de web, bloqueo global y remoto, límites de atomicidad/caché,
  rechazo de ediciones ajenas y necesidad de verificación manual tras rollback.
- Avisos Node20/24 y Ubuntu, mejora de enlaces exactos, rulesets/retención/privilegios pendientes.
- Interfaz probada Chrome Windows; Android documentado, no probado en este ciclo.

No publicar exportaciones de Engram, bases, WAL/SHM, respaldos, claves, capturas ni logs
con secretos en Git. La guía pública no sustituye el almacén privado existente.
Si no hay acceso a Engram, conserva este relevo en Git y entrega el bloqueo concreto;
no afirmes que la memoria quedó actualizada ni intentes acceder al PC desde la nube.

## Mensaje para Antigravity (después del trabajo de Codex local)

Antigravity: sincroniza tu checkout sin perder cambios; lee AGENTS.md, ONBOARDING_AGENTE.md,
ESTADO_PROYECTO.md y deploy/README.md. Consulta las observaciones de Engram verificadas
por Codex local. Expón en tu primer informe el flujo actual y el estado de las pruebas.

Para un nuevo encargo: rama → implementación en laboratorio/ y manifiesto → pruebas →
PR a main → merge de Leo → Actions Lab → URL exacta y revisión → aprobación de versión →
Actions promote con run ID → aprobación protegida de Leo → comprobación y release ID.
Ante necesidad de reversión, usa rollback protegido del release actual y verifica web.
No uses tus credenciales/MCP para publicar por fuera del flujo ni sincronices DEMOS.
No confundas aprobación previa de otra tarea con permiso general de promover esta versión.

Este relevo NO encarga publicar noticias, cambiar el diseño, arreglar WordPress, tocar DNS,
repetir la prueba ni borrar la página de Laboratorio. Espera el siguiente encargo de Leo.

## Cierre esperado

Codex local entrega confirmación de revisión de Git, memoria escrita y releída, referencias
reales de Engram y relevo dejado para Antigravity. Antigravity confirma lectura al iniciar;
ningún agente declara que otro está actualizado sin evidencia. Las sesiones ya abiertas
necesitan leer el relevo; un merge no cambia automáticamente su contexto.
