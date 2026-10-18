# Publicación provisional en Hostinger

## Objetivo y alcance

Servir la portada estática del repositorio `Leo-Omicron/elcarmencienaga.edu.co` en `https://elcarmencienaga.edu.co/`, conservando la instalación WordPress y sus datos. No instalar temas ni plugins para esta fase. No comprar productos, eliminar instalaciones ni modificar correo.

El reporte aportado por el propietario identifica el sitio como WordPress y su raíz como `/home/u985679183/domains/elcarmencienaga.edu.co/public_html`. Antes de escribir, confirmar estos datos con una consulta actual de Hostinger y comprobar que se trata del mismo sitio.

## Preparación

1. Obtener la última versión de `main` y confirmar que el HTML contiene «Nuestro sitio web está en construcción» y el DANE `147189001160`.
2. Inspeccionar los archivos existentes y las reglas activas: `index.html`, `index.php`, `.htaccess` y orden `DirectoryIndex`. Revisar si existe una web con contenido previo que deba conservarse.
3. Guardar fuera de `public_html` una copia identificable de cualquier archivo que se vaya a sustituir y de `.htaccess`. Registrar dónde quedó y comprobar que se puede leer. No subir copias, tokens, credenciales ni `wp-config.php` al repositorio.
4. Comprobar que hay una copia recuperable de WordPress antes de tocar reglas de entrada.

## Subida estática, reversible

1. Publicar únicamente `index.html`, `robots.txt` y `sitemap.xml` en la raíz pública confirmada.
2. Conservar `index.php`, `wp-admin`, `wp-content`, `wp-includes`, la base de datos y la configuración de WordPress.
3. Comprobar qué devuelve `/`. Si `index.php` tiene prioridad, ajustar de forma puntual el orden a `DirectoryIndex index.html index.php`, fuera del bloque gestionado por WordPress, preservando el resto de `.htaccess`. No reemplazar todo ese archivo con una plantilla.
4. Comprobar `/index.html` y `/`. Si hay caché que sirve la página anterior, purgar solo la caché del sitio afectado.
5. No aplicar una herramienta de despliegue que vacíe la raíz. Ante una herramienta que sustituye todo el sitio, usar transferencia puntual de archivos.

## Dominio y DNS

1. Consultar NS, A/AAAA, CNAME de `www`, MX, TXT y estado DNSSEC actuales. Guardar el inventario antes de cambios. Los NS del plan inicial son históricos y no deben tratarse como valores actuales.
2. Obtener del panel de este alojamiento la IP y los destinos exactos asignados. No inventar IP ni nameservers.
3. Si el dominio ya apunta correctamente al alojamiento, conservar la configuración.
4. Si necesita cambios de A/CNAME, modificar solo los registros de web necesarios. Si hay AAAA, comprobar que apunta al servicio correcto; no borrarlo sin establecer que causa el problema.
5. Si es necesario delegar nameservers, preparar antes la zona completa y conservar registros de correo/verificación. Puede requerirse acceso independiente al registrador externo y revisión de DNSSEC; el acceso a Hostinger por sí solo no lo otorga.
6. No cambiar MX, SPF, DKIM ni DMARC para publicar esta portada.

## HTTPS y comprobación externa

1. Activar o comprobar SSL para dominio raíz y `www`; confirmar certificado vigente y nombres cubiertos.
2. Cuando ambos nombres tengan HTTPS válido, redirigir HTTP a HTTPS y `www` al dominio raíz, preservando rutas. Evitar bucles y reglas contradictorias con las existentes.
3. Verificar externamente las cuatro variantes: HTTP/HTTPS con y sin `www`. La final debe ser `https://elcarmencienaga.edu.co/`.
4. Confirmar HTTP 200 y contenido real de la portada, no solamente que responde el servidor. Confirmar DANE y correo en la página recibida.
5. Confirmar HTTP 200 para `/robots.txt` y `/sitemap.xml`; sin bloqueo de rastreo ni encabezado `X-Robots-Tag: noindex` en esta portada pública.
6. Revisar móvil, teclado, anclas y enlace de correo. La página no instala un formulario de recepción.
7. Verificar que WordPress sigue accesible en su ruta administrativa habitual.
8. Entregar resultados: commit publicado, archivos modificados, ubicación privada de copia, cambios DNS si los hubo, resultado HTTPS/redirecciones y cualquier bloqueo pendiente. No incluir secretos.

## Restauración

Restaurar los archivos sustituidos y las reglas de entrada a partir de la copia. Si antes no había `index.html`, retirar únicamente el HTML provisional; el `index.php` conservado debe recuperar la entrada. Restaurar también robots/sitemap anteriores cuando corresponda. No borrar WordPress ni restaurar una base de datos por este cambio de archivos estáticos.

## Solicitud posterior de Education

Antes de solicitarlo, comprobar que el sitio es accesible públicamente, que el correo institucional recibe mensajes y que los datos están vigentes. Preparar la resolución completa de reconocimiento, responsable autorizado y consulta sobre tenant previo. Los TXT de verificación y eventuales cambios de MX de Google son una fase separada.
