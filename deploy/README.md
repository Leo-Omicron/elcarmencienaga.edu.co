# Flujo institucional vigente: PR → Laboratorio → Producción

Actualizado: 24 de octubre de 2026, Colombia (25 de octubre UTC).
Autoridad operativa para Codex local/nube, Antigravity y cualquier otro agente.
Sustituye el procedimiento habitual de publicar directamente por MCP de Hostinger.

## Separación y responsabilidades

- DEMOS (`demos/`) es experimental e independiente. No se promueve a Laboratorio ni Producción.
- El encargo institucional se implementa en `laboratorio/`, en una rama de trabajo y PR a `main`.
- Leo revisa el PR y hace merge. Actions publica en Laboratorio los archivos seleccionados.
- Leo revisa la web y aprueba la versión concreta. La promoción usa su artefacto exacto.
- Producción y reversión requieren además la aprobación del entorno GitHub `produccion`.
- Los agentes preparan cambios, pruebas, manifiesto, PR, enlaces y evidencias; no aprueban
  en nombre de Leo ni eluden la protección con MCP, SFTP manual o scripts locales.
- MCP de Hostinger puede usarse para consultas autorizadas. DNS, SSL, WordPress, correo,
  infraestructura y recuperación excepcional requieren alcance propio. Una urgencia no
  autoriza a saltarse el flujo; acordar recuperación y respaldo con Leo y registrar resultados.

## Inicio de cualquier agente

1. Leer `AGENTS.md`, esta guía, `ESTADO_PROYECTO.md`, `ONBOARDING_AGENTE.md` y la tarea vigente.
2. Revisar `git status`, rama y remoto. Hacer fetch y comparar con `origin/main`.
   Preservar cambios humanos; no resetear, limpiar ni hacer pull sobre cambios sin revisar.
   Usar rama/worktree separado si hace falta. Nunca publicar por el mero hecho de retomar.
3. Consultar Engram si está disponible, leyendo observaciones completas y contrastando fechas
   con GitHub. Usar la identidad y almacén existentes; no sustituirlos ante un fallo.
4. Consultar `DESIGN_SYSTEM.md` para diseño. No copiar la implementación de DEMOS como release.
5. Identificar destino, archivos, recursos dependientes y URLs de revisión antes de editar.

## Configuración comprobada

Repositorio: `Leo-Omicron/elcarmencienaga.edu.co`.

| Entorno GitHub | Protección configurada |
|---|---|
| `laboratorio` | Selected branches and tags: rama `main`, sin tags; sin revisor obligatorio |
| `produccion` | Rama `main`, sin tags; Required reviewers: `Leo-Omicron`; bypass de administradores desactivado |

Prevent self-review está desactivado deliberadamente: Leo inicia y aprueba desde la misma cuenta.
Wait timer está desactivado. Laboratorio no requiere clic protegido; Producción sí.
Estas reglas se comprobaron en capturas y se ejercitaron en promoción y rollback.
No se auditó ni configuró aquí protección de rama que impida push directo a `main`;
la política de PR debe respetarse y su enforcement mediante ruleset queda pendiente.

Cada entorno tiene sus propios cinco **Environment secrets**:

| Nombre exacto | Contenido |
|---|---|
| `IEEC_SFTP_HOST` | Host SSH/SFTP verificado en hPanel |
| `IEEC_SFTP_PORT` | Puerto SSH/SFTP verificado; no asumir 22 |
| `IEEC_SFTP_USER` | Usuario del alojamiento |
| `IEEC_SFTP_KEY` | Clave privada dedicada sin passphrase interactiva |
| `IEEC_KNOWN_HOSTS` | Entrada OpenSSH de identidad comprobada, con `[host]:puerto` cuando corresponde |

No trasladar estas credenciales a secretos generales, documentación pública, capturas o chat.
La clave ED25519 se generó en el PC de Leo y su pública se registró como
`IEEC-GitHub-Actions` en Hostinger. La privada se copió directamente a GitHub; no está en Git.
SSH se activó en hPanel. La huella ED25519 se contrastó con hPanel antes de aceptar el
primer handshake. Se reutilizó la entrada confiable de `known_hosts`; nunca aceptar
cambios de identidad automáticamente ni usar StrictHostKeyChecking=no.

**Repository variable:** `INSTITUTIONAL_DEPLOY_ENABLED=true` al cierre de esta prueba,
según confirmación de Leo y ejecuciones exitosas. La ausencia o cualquier valor distinto
exactamente de `true` omite los jobs de publicación. Se probó el bloqueo antes de activar.
Cambiar la variable no dispara una ejecución por sí solo ni sustituye la aprobación.
Antes de una sesión nueva, comprobar su estado y ejecuciones pendientes; no cambiarla por rutina.

## Qué dispara cada workflow

| Archivo / nombre visible | Disparador / efecto |
|---|---|
| `institutional-ci.yml` / Validate institutional release | PR con rutas institucionales seleccionadas y push main con rutas definidas en YAML; tests y empaquetado, sin publicar |
| `institutional-laboratorio.yml` / Publish institutional Laboratorio | Push main que toca `laboratorio/**` o `deploy/release.json`; también Run workflow manual en main |
| `institutional-produccion.yml` / Protected institutional production | Solo workflow_dispatch en main; `promote` o `rollback`; prepare y luego publish protegido |

Consultar el YAML vigente para filtros exactos: el push de validación no incluye por sí
solo `laboratorio/**`, aunque el filtro del PR sí. Cambiar solo documentación no publica,
salvo que también cambie el manifiesto o archivos de Laboratorio.
Los workflows de publicación comparten concurrency `institutional-sites`, cancel-in-progress=false;
no cancelar una operación de escritura para iniciar otra. Además existe bloqueo remoto.
No reutilizar Re-run indiscriminadamente: puede producir otra versión y respaldo.

## Manifiesto de cada encargo

`deploy/release.json` es la selección explícita, no un detector automático de cambios:

```json
{
  "target": "portal-cultural",
  "description": "Descripción concreta del encargo y de su alcance",
  "files": ["pagina.html", "css/recurso.css"]
}
```

Los nombres son relativos a `laboratorio/`; no anteponer ese directorio, barras iniciales
ni rutas del servidor. Incluir todos los recursos nuevos/modificados necesarios y revisar
las referencias relativas/absolutas para ambos dominios. No seleccionar carpetas completas.
No enviar una lista vacía para publicar: el workflow la rechaza. Un campo omitido no equivale
al borrado de un archivo remoto. Las eliminaciones editoriales no están implementadas.

Al cierre, el manifiesto aún selecciona SOLO:
- `prueba-flujo-20261024/index.html`
- `prueba-flujo-20261024/css/institucional.css`

No ejecutar de nuevo por rutina: republicaría la prueba en lab y generaría otro candidato.
Para el siguiente encargo hay que sustituir explícitamente esta selección mediante PR.
El rollback remoto no cambia Git ni elimina el artefacto: una nueva promoción podría volver
 a publicar la prueba. No hacerlo sin encargo.

## Desarrollo, merge y revisión de Laboratorio

1. Implementar en rama sin prefijo `demos/`. Respetar contenido institucional, accesibilidad
   y estilos del sitio correspondiente. No editar las copias productivas para publicar.
2. Revisar diff y dependencias. Ejecutar las 14 pruebas con:
   `python -m unittest discover -s tests -p test_institutional_release.py -v`.
   Empaquetar en carpeta nueva con `python scripts/institutional_release.py package
   --commit <SHA-exacto-40-caracteres> --bundle <carpeta-nueva>` para comprobar selección/hashes.
   Usar el comando en una sola línea. Las pruebas aisladas no necesitan Paramiko ni hosting.
3. Abrir PR con problema, alcance, destino, archivos, URLs esperadas, validación y riesgos reales.
4. Leo revisa y fusiona. Con la variable activa, el push dispara Laboratorio. Si estaba
   desactivada durante el merge, habilitar según acuerdo y usar Run workflow en `main`.
5. Esperar Success y artefacto `institutional-candidate`. Abrir el job publish si falla;
   identificar el paso exacto, no volver a ejecutar ni borrar bloqueos a ciegas.
6. Entregar URL completa de CADA página de revisión. El enlace de entorno/resumen actual
   lleva solo a la portada: eso no muestra una página nueva situada en otra carpeta.
   Ejemplo: `laboratorio/prueba-flujo-20261024/index.html` se publica en
   `https://lab.elcarmencienaga.edu.co/prueba-flujo-20261024/index.html`.
7. Registrar run ID (número largo de `/actions/runs/…`), commit y resultado visual de Leo.
   El ordinal visible #3 NO es el ID del run ni el ID del respaldo.
8. Si hay cambios después de revisar, crear otro PR y candidato; renovar revisión/aprobación.

## Qué conserva y verifica el candidato

`institutional-candidate` se conserva 30 días e incluye `files/`, `manifest.json` con
SHA256 de cada archivo, destino, descripción y commit, y `receipt.json` con release,
commit, target laboratorio y hash del manifiesto. No incluye claves ni respaldos del hosting.
Promoción no recompila desde main: descarga ese artefacto y comprueba procedencia.
No editar/reconstruir el ZIP para sustituir una versión caducada; volver a pasar por lab.
El workflow consume main para el código de despliegue; no afirmar que también fija la
versión histórica del publicador al commit del candidato.

## Promover una versión aprobada

En Actions → Protected institutional production → Run workflow:

| Campo | Valor |
|---|---|
| Branch | `main` |
| operation | `promote` |
| lab_run_id | Run ID exitoso de Laboratorio aprobado por Leo |
| rollback_target | El formulario lo exige; no decide el destino de promote |
| rollback_release | Vacío |

El destino de promote sale del manifiesto. Prepare exige run success en main, evento push
 o workflow_dispatch y path exacto del workflow de Laboratorio; valida hashes, commit y recibo.
Comprueba además por API pública que produccion exige a Leo y no permite bypass.
Si la API no responde o el repositorio pasa a privado, se detiene; adaptar mediante PR,
no eliminar las comprobaciones. No confundir esta consulta con una auditoría completa de rulesets.

Leo revisa el summary (commit, destino, cantidad), abre Review deployments, marca produccion,
añade comentario y pulsa Approve and deploy. Antes de usar credenciales se repite la comprobación.
El chat aprueba el contenido; el clic de GitHub libera el job: ambos tienen funciones distintas.
Tras Success abrir las URLs exactas productivas y registrar el **ID completo de despliegue**
que muestra publish summary: `<run_id>-<run_attempt>-<github.sha>`.
Ese SHA identifica la ejecución productiva; el manifiesto identifica el contenido aprobado.

## Rutas y transporte

| Destino | Raíz bajo el home SFTP | URL |
|---|---|---|
| laboratorio | `domains/elcarmencienaga.edu.co/public_html/subdomains/lab` | https://lab.elcarmencienaga.edu.co/ |
| portal-cultural | `domains/elcarmencienaga.edu.co/public_html/subdomains/semanacultural` | https://semanacultural.elcarmencienaga.edu.co/ |
| portal-principal | `domains/elcarmencienaga.edu.co/public_html` | https://elcarmencienaga.edu.co/ |

El home se obtiene con normalize('.'); autenticación e inventario se comprobaron antes
 de publicar. El ciclo exitoso ejercitó SFTP y POSIX rename. El workflow instala Paramiko
4.0.0, carga known_hosts y rechaza identidades desconocidas; no depende del MCP local.
La clave puede tener alcance del usuario del hosting: los límites del script NO son
 aislamiento de permisos a nivel servidor. Revisar opciones de mínimo privilegio con el proveedor.
`portal-principal` está implementado, pero no se publicó allí en estas pruebas.

Solo archivos estáticos con extensiones permitidas. Rechaza PHP, rutas ocultas, .htaccess,
componentes wp-*, symlinks, escapes y destinos demos/subdomains/laboratorio/semanacultural
 como primer componente del nombre. No administra WordPress, bases, DNS o correo.
No hay vaciado/sincronización destructiva de la raíz ni sustitución global del sitio.

## Respaldo, errores y reversión

Antes de escribir archivos públicos se guarda el contenido anterior de cada archivo
existente y sus permisos, hashes old/new, raíz, target y release previo en
`~/.ieec-releases/<target>/<release>/backup.json` y `files/`, fuera de la web.
Directorios privados 0700, archivos privados 0600 para los creados por el publicador.
Los nuevos archivos se registran con old=null. Se relee el manifiesto antes de publicar.
Cada subida usa temporal exclusivo, chmod, lectura/hash SFTP y POSIX rename.
HTTPS verifica 200 y bytes exactos de texto; imágenes solo respuesta 200 no vacía porque
 la CDN puede transformarlas. Eso no sustituye revisión visual/funcional.

Ante excepción al escribir/verificar se intenta restaurar el despliegue propio; no se
 garantiza recuperación si también falla la red/restauración. Esta ruta automática NO se
 ejercitó con una falla real del hosting. Una cancelación brusca puede dejar archivos
 parciales o bloqueo remoto `~/.ieec-releases/publish.lock`: investigar antes de intervenir.
La publicación es por archivo, no atómica para todo el sitio. No purgar caché/DNS por rutina.
No hay retención/purga automática de respaldos remotos: vigilar espacio y acordar política.

Reversión manual: mismo workflow en main, operation=rollback, lab_run_id vacío,
rollback_target destino exacto, rollback_release ID COMPLETO del despliegue que se revierte.
Es otra ejecución y exige otra aprobación protegida. Aunque el botón diga Approve and deploy,
ejecuta rollback. Antes de restaurar verifica target/raíz, release actual, integridad del
backup y que los archivos actuales coincidan con lo publicado. Rechaza ediciones posteriores
ajenas. Restaura originales y permisos o retira los nuevos; conserva otros archivos.
No limpia directorios vacíos. Solo revierte el despliegue actual y recupera su current previo.
No usar un commit Git, número de PR o run de Lab como rollback_release.

Tras rollback, verificar web con recarga forzada/consulta nueva: un 404 en archivos nuevos
 retirados es esperado, no una caída general. La CDN/navegador pueden conservar respuestas;
comprobar origen si hay dudas. El comando rollback actual no hace comprobación HTTP ni
relectura final de todas las eliminaciones: Success requiere complemento de comprobación web.

## Teléfono, avisos y límites de la prueba

El usuario operó esta configuración y las aprobaciones en Chrome de Windows. No se probó
la app Android en esta sesión. GitHub documenta aprobación de deployments en Mobile:
https://github.blog/changelog/2021-04-01-reviewing-deployments-on-github-mobile/
Si no aparece una función en la app, usar Chrome Android, sesión de la misma cuenta y
Sitio para computadoras. No dar por comprobado Run workflow en la app. Entornos/secretos
se configuraron por web. Los conectores de esta sesión permiten PRs pero no ofrecieron
administrar secretos/entornos ni workflow_dispatch: Leo hizo esos clics.

Actions avisó de acciones basadas en Node20 forzadas a Node24 y migración de ubuntu-latest
a Ubuntu26. Las ejecuciones terminaron bien; queda mantenimiento por PR de versiones y
runner, con revisión de compatibilidad y validaciones. No se cambiaron workflows al documentar.
No afirmar que todos los escenarios están certificados: ver [evidencias y pendientes](PRUEBAS_FLUJO_2026-10-24.md).
Encargo de continuidad: [Codex local → Engram → Antigravity](HANDOFF_CODEX_LOCAL.md).

## Apéndice: reproducir el alta de credenciales sin exponerlas

Solo si hay encargo de configurar/rotar accesos; no regenerar la clave operativa al retomar.
En Windows se usó PowerShell y OpenSSH, clave dedicada bajo `$env:USERPROFILE\.ssh`.
Antes de ssh-keygen comprobar que NO existan ni el archivo privado ni su .pub; no sobrescribir.
Ejemplo de creación inicial con nombre de esta instalación:

```powershell
$ieecKeyPath = Join-Path $env:USERPROFILE ".ssh\ieec_github_actions"
if ((Test-Path $ieecKeyPath) -or (Test-Path "$ieecKeyPath.pub")) {
    Write-Host "Ya existe una clave. No se sobrescribió nada."
} else {
    New-Item -ItemType Directory -Force -Path (Split-Path $ieecKeyPath) | Out-Null
    ssh-keygen -t ed25519 -C "IEEC-GitHub-Actions" -f $ieecKeyPath
}
```

En el alta se dejó passphrase vacía para ejecución desatendida. Copiar solo `.pub` al
formulario público de hPanel, nombre IEEC-GitHub-Actions. El archivo SIN .pub es privado.
Verificar host/puerto/usuario y huella en hPanel. Para la primera conexión, comprobar
la huella ANTES de aceptar; no usar ssh-keyscan como sustituto de esa comprobación.
Lectura SSH con IdentitiesOnly=yes, PasswordAuthentication=no, KbdInteractiveAuthentication=no
 y HostKeyAlgorithms=ssh-ed25519; ejecutar únicamente pwd para comprobar autenticación.
SFTP usa `-P` mayúscula para puerto; SSH usa `-p`. Después de confiar la identidad, SFTP
con BatchMode=yes y StrictHostKeyChecking=yes permite pwd/listado sin aceptar identidades nuevas.

Para extraer la entrada ya confiable del host exacto, reemplazar host/puerto por los
verificados sin incluir otras entradas del equipo:

```powershell
$ieecHostEntry = @(ssh-keygen -F "[HOST_VERIFICADO]:PUERTO" -f "$env:USERPROFILE\.ssh\known_hosts" | Where-Object { $_.Trim() -and -not $_.StartsWith("#") })
if ($ieecHostEntry.Count -gt 0) {
    ($ieecHostEntry -join "`n") | Set-Clipboard
} else {
    Write-Host "No se encontró el servidor. Detener la configuración."
}
```

Copiar la privada directamente al campo Value del Environment secret correspondiente:

```powershell
Get-Content "$env:USERPROFILE\.ssh\ieec_github_actions" -Raw | Set-Clipboard
```

Conservar contenido completo y saltos de línea; no fotografiar ni pegar en chat.
Después de guardar, reemplazar el contenido del portapapeles con
`Set-Clipboard -Value "Listo"`. Esto no garantiza eliminar historial/sincronización de
portapapeles del sistema: no usar ese historial para conservar credenciales.
GitHub oculta valores al guardar; una captura de nombres solo confirma creación,
no exactitud. La conexión real exitosa fue la comprobación funcional de esta instalación.
La rotación futura debe registrar nueva pública, actualizar ambos entornos y verificar
antes de retirar la antigua; coordinarla con Leo, sin publicar valores ni borrar accesos a ciegas.
