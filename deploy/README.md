# Flujo institucional: Laboratorio → Producción

Estado: implementación para revisión; NO activada ni probada contra Hostinger.
DEMOS es un espacio independiente y no participa de este flujo.

## Operación cotidiana

1. Preparar la actualización en `laboratorio/` y seleccionar en `deploy/release.json`
   los archivos relativos a esa carpeta y el destino productivo. Incluir recursos
   dependientes. Nada de `demos/` se incorpora al paquete.
2. Abrir PR a main. Las comprobaciones de código no publican contenido.
3. Leo revisa y hace merge. Con la activación configurada, el workflow
   **Publish institutional Laboratorio** respalda y publica solo esos archivos en lab.
4. Tras verificar bytes en SFTP y contenido por HTTPS, conserva un artefacto inmutable
   `institutional-candidate` durante 30 días: archivos, hashes, commit y recibo.
5. Leo revisa la web y comunica por chat la aprobación de ESA versión.
6. Solicitar **Protected institutional production**, operación `promote`, indicando
   el ID de la ejecución exitosa de Laboratorio. No usar una rama móvil ni reconstruir
   el contenido desde el main más reciente.
7. El paso prepare verifica procedencia y hashes, muestra el destino y la versión;
   el trabajo publish espera al revisor del entorno `produccion`.
8. Leo autoriza en GitHub. Se respalda, publica y verifica el mismo paquete.
   El resumen muestra el ID de respaldo/despliegue necesario para una reversión.

El chat por sí solo no satisface la protección de GitHub. La conexión disponible en
esta sesión no ofrece crear entornos, configurar secretos ni iniciar workflows;
no se promete poder iniciar desde el chat hasta disponer de una conexión Actions
con permiso de escritura. Mientras tanto Leo puede pulsar Run workflow desde la web.

## Activación inicial desde Chrome Android o escritorio

**No activar la variable hasta completar y comprobar los pasos restantes.**

En el repositorio: Settings → Environments.

- Crear `laboratorio` y `produccion` con esos nombres exactos.
- En `produccion`, Required reviewers: seleccionar **Leo-Omicron**.
- No activar Prevent self-review: el iniciador puede ser la misma cuenta.
- Desactivar la posibilidad de omitir las reglas como administrador.
- Restringir los despliegues a la rama `main` en ambos entornos.
- Revisar visibilidad del repositorio y disponibilidad de estas reglas en el plan.

En cada entorno, cargar estos secretos mediante la interfaz de GitHub:

| Secreto | Contenido |
|---|---|
| `IEEC_SFTP_HOST` | Host SSH/SFTP comprobado en hPanel |
| `IEEC_SFTP_PORT` | Puerto comprobado; no asumir 22 |
| `IEEC_SFTP_USER` | Usuario real del hosting |
| `IEEC_SFTP_KEY` | Clave privada dedicada y autorizada, sin contraseña interactiva |
| `IEEC_KNOWN_HOSTS` | Entrada OpenSSH con identidad del servidor comprobada por canal fiable; incluir puerto si no es 22 |

No compartir claves por chat, no publicar secretos en Git y no usar aceptación automática
de la identidad SSH. La clave pública debe estar autorizada previamente en Hostinger.
Esto requiere verificar soporte SFTP, raíz del usuario, capacidad de almacenamiento y
la extensión POSIX rename. No se han creado claves ni autorizado accesos en esta sesión.
El transporte usa Paramiko 4.0.0; los tests locales no requieren instalarlo.

Comprobar primero lectura/autenticación e inventario del hosting, sin publicaciones.
Probar respaldo y restauración en un destino de prueba acordado antes de habilitar un
encargo institucional. No tomar un test simulado como evidencia de reversión en Hostinger.

Finalmente, Settings → Secrets and variables → Actions → Variables:
crear `INSTITUTIONAL_DEPLOY_ENABLED` con valor `true`. Antes de esto los trabajos de
publicación se omiten. Esta variable no sustituye las protecciones del entorno.
El flujo productivo consulta además la configuración pública del entorno: exige a
Leo-Omicron como revisor y administrador sin bypass. Si el repositorio pasa a privado
o la API no responde, se detiene; hay que adaptar esa consulta antes de reactivar.

Los secretos de producción pertenecen al entorno `produccion`, no a secretos generales
del repositorio. Los permisos efectivos de la clave SSH deben limitarse cuando el
hosting lo permita; las restricciones del script no sustituyen los permisos del servidor.

## Destinos y alcance

| Destino | Raíz relativa al home SFTP |
|---|---|
| Laboratorio | `domains/elcarmencienaga.edu.co/public_html/subdomains/lab` |
| `portal-cultural` | `domains/elcarmencienaga.edu.co/public_html/subdomains/semanacultural` |
| `portal-principal` | `domains/elcarmencienaga.edu.co/public_html` |

Las rutas son las documentadas en el proyecto; confirmarlas en el servidor antes de
activar. La lista de archivos inicial está vacía: aprobar este PR no es un encargo
para publicar contenido. Cambiar la lista/destino forma parte del PR de cada tarea.

Solo admite archivos estáticos seleccionados. Bloquea PHP, .htaccess, rutas ocultas,
WordPress, symlinks y rutas a subdominios desde una publicación de la raíz. Nunca borra
archivos ajenos para sincronizar una carpeta. No gestiona base de datos ni WordPress.
Para un encargo de ese tipo hará falta una implementación específica y otro respaldo.

## Respaldo y reversión

Antes de escribir se respalda cada archivo sustituido, con hash y permisos originales,
y se registra qué archivos no existían. Los respaldos quedan bajo
`~/.ieec-releases/<destino>/<id>/`, fuera de la raíz web, con directorios privados.
No se suben los respaldos del servidor como artefactos del repositorio público.
No hay purga automática de respaldos: controlar espacio y acordar retención.

Una falla de escritura o de verificación HTTPS intenta restaurar inmediatamente el
respaldo del propio despliegue. Si también falla la restauración, la ejecución falla:
requiere intervención; nunca se garantiza reversión ante pérdida de conectividad.
Una interrupción brusca del runner puede dejar un bloqueo que exige investigación.
La publicación es por archivos, no una conmutación atómica de todo el sitio; durante
unos instantes pueden coexistir recursos de dos versiones.

Para reversión manual: ejecutar **Protected institutional production**, operación
`rollback`, destino e ID del despliegue productivo a revertir; requiere otra aprobación
protegida. Solo revierte el despliegue actual, comprueba integridad del respaldo y rechaza
sobrescribir ediciones posteriores ajenas. Restaura archivos originales y retira únicamente
los archivos nuevos que había añadido ese despliegue. El estado restante permanece igual.
La comprobación manual de la web tras una reversión sigue siendo necesaria.

## GitHub en Android

GitHub documenta aprobaciones de despliegue en GitHub Mobile, incluido Android:
https://github.blog/changelog/2021-04-01-reviewing-deployments-on-github-mobile/

La solicitud pendiente aparece en Inbox/Notificaciones. Habilitar notificaciones de
solicitudes para aprobar despliegues en Ajustes de la app. Revisar el destino y versión,
aprobar o rechazar. No confundir aprobar un PR con autorizar Producción.
La configuración inicial de entornos/secretos se realiza en la web; si una pantalla no
aparece correctamente en Chrome Android, usar Sitio para computadoras. No hay solicitud
de Producción pendiente creada por esta implementación.

## Validación realizada

`python -m unittest discover -s tests -p test_institutional_release.py -v`:
14 pruebas aisladas de empaquetado, hashes, rutas, backups, exclusión de DEMOS,
fallas y reversión. No se conectan al hosting. Probar un ciclo completo real sigue pendiente.
