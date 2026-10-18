# Continuidad y respaldo de Engram

Los agentes comparten el almacén existente, no una base nueva por sesión. El arranque persistente y el guardado/lectura posterior al reinicio están comprobados. El verificador independiente informó PASS de recuperación aislada y lecturas con las configuraciones de ambos MCP, pero falló al entregar el informe final y su carpeta de evidencia ya no está disponible. No se afirma un cierre completo con ese informe faltante. Estado completo en `odd/tasks/engram-continuity.md`. No garantiza pérdida cero ni habilita nube.

## Estado aplicado en esta máquina

La tarea Windows `IEEC-Engram` ejecuta respaldo y arranque al iniciar sesión con permisos de usuario normal. Su última prueba terminó con código 0. Usa la copia de la herramienta en `<data-dir>/runtime/engram_runtime.py`; si cambia el código del repositorio, esa copia necesita actualización explícita. El servidor comprobado usa `<data-dir>/runtime-tmp` para `TEMP` y `TMP`. Las entradas Engram de Codex y Antigravity apuntan al mismo almacén y temporales estables; sus procesos ya abiertos deben recargarse para tomar los cambios. No se reiniciaron esas aplicaciones.

## Identidad y funciones

- `.engram/config.json` identifica el proyecto como `elcarmencienaga.edu.co`; no contiene las memorias. No modificarlo para crear otra identidad.
- El almacén compartido existente es `C:/Users/usuario/.gemini/antigravity-ide/engram`. Contiene `engram.db` y `.instance-id`; no trasladarlos, reemplazarlos ni inicializar otro almacén ante un error.
- Pi usa HTTP local y sus comprobaciones nativas de propietario/instancia. Mantener `ENGRAM_URL` sin definir; no parchear paquetes instalados.
- Codex y Antigravity usan MCP por stdio. Sus procesos deben usar el mismo `ENGRAM_DATA_DIR` y `TEMP`/`TMP` persistentes en `<data-dir>/runtime-tmp`. El CLI no cambia sus configuraciones.

## Comprobar, arrancar y respaldar

Desde la raíz del repositorio, con Python 3 y el ejecutable Engram ya instalado, sustituir `<data-dir>` por la ruta existente anterior y `<engram.exe>` por el ejecutable aprobado:

```text
python scripts/engram_runtime.py check --data-dir "<data-dir>"
python scripts/engram_runtime.py serve --data-dir "<data-dir>" --engram "<engram.exe>"
python scripts/engram_runtime.py backup --data-dir "<data-dir>"
python scripts/engram_runtime.py verify-backup --data-dir "<data-dir>" "<respaldo.db>"
```

`--help` y la ayuda de cada subcomando explican las opciones. Éxito: código 0 y JSON; error operativo: código 1, stdout vacío y mensaje en stderr; argumentos inválidos: código 2. No se imprimen recuerdos ni credenciales.

| Operación | Garantía y límite |
| --- | --- |
| `check` | Solo lectura: compara `.instance-id` con `http://127.0.0.1:7437/health`, sin proxy ni redirecciones y con timeout de 3 segundos. Windows puede agotar 0,5 segundos antes de informar que un puerto está cerrado. |
| `serve` | Si ya responde la misma instancia, no hace cambios. Si la conexión es rechazada, respalda antes de lanzar `engram serve`, separado y sin stdio heredado. Configura `ENGRAM_DATA_DIR`, `TEMP`, `TMP` y `ENGRAM_CLOUD_AUTOSYNC=0` solo en el hijo, sobrescribiendo un valor heredado `1` para desactivar autosync. Espera acotada; nunca mata ni reinicia procesos. |
| `backup` | API SQLite (incluye WAL confirmado), nombre único en `<data-dir>/backups`, `quick_check` y conteos de observations/sessions/user_prompts (esquema Engram 3.4.0). No copia el archivo vivo. |
| `verify-backup` | Abre el respaldo en modo lectura y devuelve integridad/conteos. No restaura ni sobrescribe la base activa. |

Un puerto ajeno, respuesta inválida o identidad no verificable provoca rechazo sin lanzar ni detener nada. Un fallo posterior al lanzamiento puede dejar el hijo activo: no repetir reinicios a ciegas; comprobar primero. Los respaldos incompletos conservan extensión `.partial` y no son recuperación validada. No hay rotación ni borrado automático.

## Recuperación y mantenimiento

1. Guardar la ruta y los conteos del JSON de `backup`; ejecutar `verify-backup` sobre ese archivo. Revisar espacio disponible y proteger el acceso al directorio privado.
2. Probar la recuperación en un directorio temporal aislado, nunca sobre el almacén activo. El responsable copia allí **el respaldo ya consistente**, usa la CLI pública de Engram con `ENGRAM_DATA_DIR` aislado y verifica lecturas/conteos. No apuntar Pi/MCP a esa prueba.
3. Antes de cualquier restauración real, detenerse y obtener autorización: esta herramienta no ofrece restauración destructiva. Conservar el original y el respaldo; no reemplazar una base abierta.
4. Antes de dar el trabajo por terminado, resolver la falta del informe final independiente. Su consulta intermedia informó recuperación y lecturas MCP exitosas, pero no entregó el contrato detallado ni el veredicto completo. No repetir automáticamente la verificación ni afirmar que las aplicaciones ya abiertas fueron recargadas. Una respuesta inesperada del comprobador no demuestra corrupción del respaldo.

Los respaldos reducen el riesgo, pero no sustituyen una política de copias protegidas y probadas. La nube no se enrola ni activa aquí. Mantener fuera de Git bases, WAL/SHM, respaldos, logs, memorias crudas, secretos y configuraciones privadas; de `.engram/` solo se permite `config.json`. Los archivos privados del runtime viven fuera del repositorio, bajo el almacén compartido.
