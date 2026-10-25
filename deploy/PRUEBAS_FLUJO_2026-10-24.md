# Evidencias del ciclo institucional — 24 de octubre de 2026 (Colombia)

Ciclo ejecutado por Leo desde GitHub web; la conversación cruza el 25 de octubre UTC.
Se documentan evidencias, no una garantía universal de recuperación.

## Código integrado

- [PR #6](https://github.com/Leo-Omicron/elcarmencienaga.edu.co/pull/6): flujos institucionales,
  publicador SFTP, pruebas, reglas iniciales. Commit de implementación
  `34a7a55826382d18c923af95ec7e3d11331acf3f`; merge main
  `1692ee55fbe48d871c0ba0459a4dad1cc17ea442`.
- [PR #8](https://github.com/Leo-Omicron/elcarmencienaga.edu.co/pull/8): página aislada y
  selección explícita de dos archivos. Commit de propuesta
  `e49cc6559876ef6a4299173584ffa840c83aad9c`; merge y candidato revisado
  `1a20d000dc2843e5c22024b2be4c2ad3ca2894d6`.
- 14 pruebas aisladas del publicador y empaquetado local de dos archivos aprobados.
  Validación del PR y de main mostraron Success. Actionlint v1.7.12 se ejecutó en la
  implementación inicial para los tres workflows; no equivale a prueba remota.

## Configuración e identidad

Capturas verificaron entornos laboratorio/produccion, main como única rama, los cinco
secretos en cada entorno, revisor Leo-Omicron y bypass desactivado en produccion.
Clave privada creada y conservada por Leo; pública registrada en hPanel. SSH inicialmente
inactivo, luego activado. Huella ED25519 contrastada con hPanel antes del primer yes.
Autenticación por clave con pwd y listado SFTP de subdomains confirmaron acceso y carpetas
cultura/demos/lab/semanacultural. No copiar claves, huellas transcritas de capturas ni logs
privados a este documento. Credenciales e inventario deben verificarse si cambian.

La variable se creó primero false, después Leo la cambió a true. El merge del PR #6
produjo validación exitosa y publicación lab omitida, demostrando el bloqueo inicial:
- [CI main](https://github.com/Leo-Omicron/elcarmencienaga.edu.co/actions/runs/40143416444)
- [Lab omitido](https://github.com/Leo-Omicron/elcarmencienaga.edu.co/actions/runs/40143416427)

## Ejecuciones reales

| Operación | Run ID | Evidencia |
|---|---|---|
| Lab manual main | [40144556888](https://github.com/Leo-Omicron/elcarmencienaga.edu.co/actions/runs/40144556888) | publish success; empaquetado, publicación/verificación y conservación del artefacto success |
| Promoción | [40145795225](https://github.com/Leo-Omicron/elcarmencienaga.edu.co/actions/runs/40145795225) | prepare success; pausa Waiting y aprobación de Leo capturadas; publish success |
| Reversión | [40146188051](https://github.com/Leo-Omicron/elcarmencienaga.edu.co/actions/runs/40146188051) | prepare success; segunda pausa Waiting y aprobación; publish success |

Además de las capturas, el agente consultó después la API de jobs para los tres runs:
los jobs relevantes están completed/success. No se descargaron logs privados ni copias
remotas como evidencia pública. No confundir el ordinal del workflow #1/#2/#3 con run ID.

**ID completo del despliegue productivo revertido:**
`40145795225-1-1a20d000dc2843e5c22024b2be4c2ad3ca2894d6`.
Destino portal-cultural. Artefacto de Lab: institutional-candidate, retención configurada
30 días. Artefacto intermedio de promoción: selected-production-candidate.

## Contenido y revisión web

Solo se seleccionaron `prueba-flujo-20261024/index.html` y
`prueba-flujo-20261024/css/institucional.css`. Página noindex,nofollow, sin datos recogidos,
con título «Un cambio pequeño, un proceso verificable.» e identificador
`IEEC-FLUJO-20261024-V1`. Noindex no constituye control de acceso.

- Lab: https://lab.elcarmencienaga.edu.co/prueba-flujo-20261024/index.html
- Producción durante prueba: https://semanacultural.elcarmencienaga.edu.co/prueba-flujo-20261024/index.html
- Portada de control: https://semanacultural.elcarmencienaga.edu.co/

La captura de Lab mostró título, identificador y estilos correctos. Hubo confusión inicial
porque el enlace del resumen llevaba a la portada: se resolvió abriendo la ruta completa.
Lección: entregar enlaces exactos en cada PR/revisión; mejorar resumen automático en otro PR.

Después de rollback Leo confirmó textualmente: «Todos los resultados en la web salieron
como tu indicaste!». Esto acredita su comprobación reportada: prueba retirada de Producción,
prueba disponible en Lab y portada cultural cargando. No se presenta como auditoría HTTP
independiente del agente ni comparación de toda la portada antes/después.

## Qué quedó demostrado y qué sigue pendiente

Demostrado: autenticación SFTP desde Actions, empaquetado, hash/HTTPS de los dos textos,
conservación de candidato, promoción desde Lab, protección efectiva con dos aprobaciones,
registro de cambios y reversión de archivos NUEVOS. El ciclo ejercitó escritura/rename
remotos y respaldo de metadatos de ausencia, no recuperación de bytes previos de estas páginas.

Pendiente de prueba real separada: sobrescribir un archivo de prueba YA existente y
restaurar sus bytes/permisos; falla real y recuperación automática; apagado/interrupción,
lock abandonado, corrupción de backup o edición fuera del flujo; publicación en
portal-principal; experiencia de aprobación Android; revisión exhaustiva de galerías,
WordPress y accesibilidad del sitio completo. Hay tests aislados para varios fallos,
pero no se deben presentar como ejercicios reales de Hostinger.

No se modificaron DNS, WordPress o base de datos como parte del ciclo. El alcance del
paquete no incluyó portadas/galerías ni DEMOS. No se certifica seguridad de todo el hosting.

## Estado para el siguiente agente

- Producción: prueba revertida; no repetir rollback del mismo release ya revertido.
- Lab: prueba conservada, según comprobación de Leo.
- Git main y release.json aún contienen la prueba. Rollback remoto NO revierte Git.
- Variable true al cierre; no dejarla como supuesto eterno ni disparar publicaciones al retomar.
- No hay purga automática de backups; no borrarlos para cerrar la prueba.
- Documentación de continuidad debe fusionarse antes de que los agentes locales la adopten.
- Pendientes: mantenimiento Node/runner, enlaces exactos en summaries, protección de main,
  política de retención/privilegios y prueba de restauración de archivo existente.
