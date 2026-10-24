# Continuidad del proyecto — IE El Carmen

## Estado vigente — 24 de octubre de 2026, 10:05 (Colombia)

**Semana Cultural Carmelista 2026 (100% activa en Producción y Staging):**
- **Día 2 (Feria de Emprendimiento y Creatividad):** Corregido el error de sintaxis en `galleryItems` (faltaba `}` en el objeto 29) en `dia2.html`. El visor interactivo lightbox, zoom y navegación por diapositivas/teclado quedan 100% operativos.
- **Día 3 (Gran Desfile e Inauguración del Mundialito 2026):** Galería completa con 21 fotos destacadas y 13 videos de YouTube (9 panorámicos 16:9 y 4 Shorts 9:16) en producción (`https://semanacultural.elcarmencienaga.edu.co/dia3.html`), incluyendo video de himnos del grado 1°A Sede Guillermo F. Morán.
- **Mundialito Carmelista 2026 (Aplazamiento Oficial):** Partidos de jueves 22 y viernes 23 de octubre **aplazados hasta nueva orden**. Actualizado en producción y staging el afiche oficial con la franja transversal («Aplazados hasta nueva orden.»), tarjeta extraordinaria de alerta roja `#aviso-partidos-mundialito-2026` y banner de alerta en `dia3.html`.
- **Día 4 (Gran Foro Salvemos la Ciénaga & Día de la Ciencia Sede GFM):** Página dedicada `dia4.html` 100% promovida y verificada en producción (`https://semanacultural.elcarmencienaga.edu.co/dia4.html`) con 49 fotografías destacadas optimizadas (46 Foro Central + 3 Sede GFM) y 19 videos oficiales de YouTube (11 panorámicos 16:9 y 8 Shorts 9:16). Incluye enlace directo a la siguiente jornada (`dia5.html`).
- **Día 5 (Gran Cierre, Solemne Santa Misa de Acción de Gracias & 53° Aniversario Institucional):** Implementada la página dedicada `dia5.html` con 12 fotografías destacadas optimizadas en `dia5/`, tarjeta conmemorativa del afiche oficial, 2 videos panorámicos 16:9 en YouTube (Actos Protocolarios `xksuNCG6pZM` y Resumen General `NdgGWWO4WW4`), visor lightbox con navegación por teclado y atajos en `index.html` y `dia4.html`.
- **Flujo de trabajo:** Staging-first riguroso (`lab.elcarmencienaga.edu.co` antes de `semanacultural.elcarmencienaga.edu.co`) verificado con validación visual y sintaxis JS en cada ciclo.

**Google Workspace for Education:** Prioridad de fondo: obtener la aprobación definitiva de Education Fundamentals gratuito (12 días de trial restantes). La web y Gmail ya funcionan.

### Resultado de la comprobación actual

| Área | Estado y evidencia |
|---|---|
| Web | Peticiones públicas propias: HTTPS raíz y www terminan en https://elcarmencienaga.edu.co/, HTTP 200 y validación TLS correcta. robots.txt y sitemap.xml: 200. |
| Redirección | www → raíz implementada y probada anteriormente con preservación de rutas codificadas y consultas. Hoy se volvió a comprobar el destino final; no se repitió toda la batería de rutas. |
| Gmail | Google mostró «Se configuró Gmail». El usuario confirmó prueba exitosa Gmail institucional ↔ Outlook, con recepción en ambas bandejas. No se inspeccionaron mensajes ni encabezados. |
| Propiedad del dominio | Google confirmó la verificación; TXT de propiedad conservado. |
| Suscripción Google | Lectura directa de Administración: Education Fundamentals, Activo, Trial plan, **13 días restantes y 2 licencias asignadas**. No se inspeccionaron las identidades de ambos usuarios. |
| Aprobación educativa | **No confirmada.** Tener Gmail operativo o una suscripción de prueba no acredita aprobación definitiva. |
| Soporte | El usuario abrió el chat emergente de Google; su IA dio orientación general sobre revisión y documentos. No hay número de caso ni confirmación individual de solicitud en revisión aportados. |
| Hostinger | DNS leído por Connector. El beneficio de «correos ilimitados» del plan fue reportado por el usuario, no comprobado; no equivale a licencias de Google. |

### DNS vigente leído en Hostinger

- MX raíz: `1 smtp.google.com.`, TTL 300; coincide con consulta pública a Google DNS.
- SPF raíz: `v=spf1 include:_spf.google.com ~all`, TTL 3600.
- DKIM Google: TXT en `google._domainkey`, TTL 300, clave pública RSA de 2048 bits. Configuración publicada y confirmación del asistente completadas anteriormente; no se ha acreditado `dkim=pass` con encabezados reales.
- TXT de propiedad de Google conservado. No regenerarlo por rutina.
- DMARC: `v=DMARC1; p=none`, TTL 3600. Es monitorización, no política de rechazo.
- Web: ALIAS raíz a `elcarmencienaga.edu.co.cdn.hstgr.net.`; www CNAME a `www.elcarmencienaga.edu.co.cdn.hstgr.net.`, TTL 300.
- Persisten los CNAME de DKIM, autodiscover y autoconfig de Hostinger. No se eliminaron.
- **Cambio detectado respecto del historial:** antes figuraban 14 días/1 licencia y SPF con Google + Hostinger; hoy son 13 días/2 licencias y SPF solo Google. No se atribuye autoría ni se revierte automáticamente. Esta revisión no modificó infraestructura.

### Preparación institucional y privacidad

- El usuario confirma que no existían Workspace/Classroom ni buzones previos en Hostinger; no hay migración histórica reportada.
- Solicitante: docente con autorización del rector confirmada por el usuario. Aproximadamente 1.000 estudiantes; no es un recuento exacto de usuarios o personal.
- Se revisaron visualmente las 7 páginas del PDF privado: Resolución 2293 del 6 de septiembre de 2022, reconocimiento y licencia; Resolución 931 del 11 de julio de 2023, corrección del DANE a **147189001160**. No se certificó autenticidad ni vigencia jurídica actual por una fuente externa.
- Datos personales del solicitante, correo externo, localizador del PDF y copia exacta de DNS quedan **fuera del repositorio público**, en el archivo privado local indicado en CONTINUAR_EN_CODEX.md y en Engram. No publicar resolución, firmas, identificadores, capturas, sesiones ni credenciales.
- El PDF no se ha enviado a Google desde este chat. No hay prueba de carga por otro actor.
- La prueba de correo no autoriza cambiar el contacto público de la portada; sigue pendiente decidirlo con el usuario.

### Próximo paso exacto

1. Retomar el chat oficial de soporte ya abierto por el usuario. Conservar autorización existente para consultar usando solo dominio, edición y estado de prueba, **sin adjuntar la resolución**.
2. Obtener respuesta individual: ¿la solicitud está registrada y pendiente de revisión?, ¿falta una acción?, ¿cuál es el canal oficial para documentos? Solicitar número de caso si corresponde. La respuesta genérica de IA no responde estas preguntas.
3. El chat emergente de apps.google.com no aparece entre las superficies controlables; el usuario debe pegar el texto y traer la respuesta si sigue inaccesible. No afirmar que el agente envió una consulta.
4. Revisar correos de Google en la cuenta institucional y en el contacto externo con el usuario. Si solicitan documentos, confirmar destino y datos antes de cargarlos.
5. No esperar pasivamente hasta el vencimiento: volver a comprobar el contador. Solicitar a soporte una extensión si es necesaria; **no hay extensión concedida ni automática acreditada**.
6. Después de la aprobación: planificar usuarios, grupos/unidades, seguridad y recuperación de administrador, acceso por edades y consentimiento para servicios adicionales. No crear masivamente cuentas de menores ni habilitar servicios sin acordarlo.
7. Pendientes técnicos proporcionales: verificar SPF/DKIM/DMARC en encabezados de prueba, revisar móvil/teclado y preparar la web completa según las prioridades del usuario.

### Repositorio y alcance de esta revisión

- Rama `main`, origin `https://github.com/Leo-Omicron/elcarmencienaga.edu.co.git`.
- Antes de esta revisión ya estaba modificado ESTADO_PROYECTO.md y existían .atl/ y .engram/ sin seguimiento. Se preservaron.
- Se actualizan documentos de continuidad, no HTML ni DNS. Sin commit, push, pull, despliegue ni compras.
- La carpeta .engram/ contiene configuración local: no publicar por accidente. Revisar todo archivo sin seguimiento antes de cualquier commit.
- Engram canónico: `elcarmencienaga.edu.co`, respaldado por .engram/config.json. Resolver con mem_current_project usando el cwd exacto; no inventar session_id.
- PUBLICACION.md sigue siendo la guía de despliegue de la **fase web**: su prohibición de cambiar correo es para esa fase, no el estado actual. Los cambios de correo posteriores tuvieron autorizaciones específicas.
- Los antecedentes debajo conservan el incidente de redirección y su recuperación; sus pendientes de DNS/correo no deben leerse como vigentes.

---

## Antecedentes conservados (no reemplazan el estado vigente)

# Continuidad del proyecto — IE El Carmen

Actualizado el 18 de octubre de 2026. Este documento conserva el contexto; no sustituye comprobaciones actuales.

## Unificación completada — 18 de octubre, 04:55 (Colombia)

Tras la autorización explícita del propietario, las cuatro variantes HTTP/HTTPS con y sin `www` terminan en `https://elcarmencienaga.edu.co/`, con HTTP 200 y TLS validado. `https://www.elcarmencienaga.edu.co/` devuelve 301; HTTP con `www` requiere dos saltos por la redirección HTTPS ya existente. Se verificaron DANE y correo en la portada recibida.

- Único archivo remoto modificado: `.htaccess`, de 1694 a 1982 bytes. Se agregó un bloque `Canonical host` antes de LiteSpeed/WordPress, conservando todas las reglas anteriores y `DirectoryIndex`. Sin cambios de DNS, correo, HTML ni datos de WordPress.
- Se guardaron fuera del repositorio y de la raíz pública una copia privada del texto original, metadatos, candidatos y una herramienta local de transferencia sin credenciales. La ubicación exacta está en la memoria Engram del proyecto y en la entrega del chat. El texto devuelto por la API ocupa 1693 bytes frente a los 1694 reportados; no se afirma respaldo binario exacto. La restauración del texto más salto final recuperó el tamaño reportado y todas las reglas anteriores.
- La primera prueba temporal 302 detectó que una ruta `/a%20b` se devolvía con un espacio literal. Se restauró inmediatamente la configuración original y se comprobó HTTP 200 antes de corregir. El bloque corregido toma la ruta original de `THE_REQUEST`, sin decodificarla, y conserva la consulta. Se probó como 302 y después se cambió únicamente a 301. Referencia técnica: https://httpd.apache.org/docs/2.4/rewrite/htaccess.html.
- Se limpió únicamente la caché del sitio/CDN mediante Hostinger Connector: antes de la purga, la raíz de `www` todavía servía una respuesta 200 antigua. Después, la URL ordinaria sin parámetros ya devuelve 301 al dominio raíz.
- Comprobaciones propias e independientes: `www` → raíz sin bucles, rutas `/a%20b` y `/a%2520b` preservadas, parámetros como `a=1&b=two` y `q=x%26y` intactos. `robots.txt` y `sitemap.xml` continúan en 200. `/wp-admin/` conserva la redirección 302 a su acceso habitual. No se inició sesión ni se auditó WordPress completo.
- Restauración probada: recuperar las reglas del respaldo y el salto final mediante transferencia puntual de `.htaccess`, releer y comparar, limpiar caché del sitio y repetir las pruebas públicas. Restaurar el servidor no retira redirecciones 301 ya almacenadas por navegadores. No hace falta restaurar bases de datos ni reinstalar WordPress por este cambio.
- Engram ya está operativo con `.engram/config.json`; conserva la autorización, el incidente temporal, la restauración probada y el resultado final. Sin commit ni push; se mantienen los cambios locales anteriores.

Pendientes ajenos a esta redirección: revisión visual/móvil/teclado, recepción institucional del correo y comprobación completa de los datos para una eventual solicitud de Education.

## Comprobación inicial de Codex — 18 de octubre, 04:40 (Colombia)

La portada ya era accesible públicamente con HTTPS. No fue necesario cambiar DNS, reinstalar SSL ni volver a publicar archivos. En ese momento estaba pendiente unificar `www`; quedó completado en la sección anterior.

- Git: actualización por avance rápido de `7829888` a `630d0ac` desde `origin/main`. Se conservaron sin cambios los dos archivos locales sin seguimiento de `.atl/`. No se hizo reset, stash, commit ni push.
- Hostinger Connector confirmó el sitio habilitado, tipo WordPress, usuario `u985679183` y la raíz documentada. La lectura actual de `.htaccess` confirma `DirectoryIndex index.html index.php` y conserva los bloques de WordPress/LiteSpeed; no contiene una redirección de `www` al dominio raíz.
- La consulta `dns_records_list` ahora funciona: raíz ALIAS a `elcarmencienaga.edu.co.cdn.hstgr.net.` y `www` CNAME a `www.elcarmencienaga.edu.co.cdn.hstgr.net.`. También existen MX, SPF, DKIM y DMARC; no se modificaron y su presencia no demuestra que haya buzones operativos.
- Google DNS público devolvió los NS `helios.dns-parking.com` y `aster.dns-parking.com`, A de raíz `145.223.124.208` y `147.79.72.202`, además de AAAA. Son respuestas de CDN observadas, no IP que deban fijarse manualmente. No hubo respuesta CAA ni DS en esa consulta. La consulta UDP directa a cada autoritativo no pudo completarse desde este entorno; no se afirma propagación global.
- `hosting_ssl_status` para la raíz devuelve `active`, proveedor `hssl`, redirección HTTPS activada, vencimiento `2027-01-16T01:59:44Z` y ningún último error. La consulta separada de `www` devuelve 404 en la API, pero la conexión HTTPS pública de `www` valida TLS correctamente: no es prueba de certificado roto.
- Peticiones públicas con `curl.exe`, sin desactivar validación TLS: HTTP raíz → 301 → HTTPS raíz → 200; HTTPS raíz → 200; HTTP `www` → 301 → HTTPS `www` → 200; HTTPS `www` → 200. Ambos nombres muestran DANE `147189001160` y `ieelcarmen@semcienaga.gov.co`. `www` todavía no termina en la URL raíz.
- `/robots.txt` y `/sitemap.xml` responden 200, permiten rastreo y referencian el dominio raíz. `/wp-admin/` redirige a `/wp-login.php`; se comprobó la ruta de acceso, no el inicio de sesión ni la integridad completa de WordPress.
- Las pruebas dirigidas con `--resolve` a ambas IP históricas también respondieron, pero no sustituyen las pruebas públicas ni justifican cambiar DNS a esas IP.
- Limitaciones: no se realizó revisión visual/móvil/teclado, verificación de recepción del correo, comparación byte a byte del HTML desplegado ni auditoría completa de WordPress. El fallo inicial de resolución de `curl` dentro del entorno restringido desapareció al repetir fuera de él; no era evidencia de una caída pública.

El ajuste que entonces requería confirmación se completó después con respaldo, restauración probada y verificaciones, como documenta la sección anterior. Los reportes antiguos siguientes se conservan como antecedentes, no como diagnóstico vigente.

## Objetivo autorizado

Codex dirige el proyecto y realiza las tareas disponibles directamente. Prioridad: portada institucional estática pública en elcarmencienaga.edu.co con HTTPS. No es obligatorio usar WordPress. Preparar después la solicitud de Google Workspace for Education y correo @elcarmencienaga.edu.co; no hay correo previo en este dominio nuevo. No comprar productos ni activar correo todavía.

## Archivos y acceso

Repositorio: Leo-Omicron/elcarmencienaga.edu.co, rama main. Carpeta Windows: D:\Leo\Proyectos\IEEC\Landing. El escudo y colores confirmados están integrados. PUBLICACION.md documenta despliegue reversible.

Hostinger Connector quedó comprobado en el chat local de Codex «Probar conexión a Hostinger»: hosting_websites_list devolvió elcarmencienaga.edu.co habilitado. Los nueve servidores MCP están registrados en Windows. No reinstalar ni solicitar credenciales por chat. El chat de coordinación en la nube no dispone de esos MCP locales, aunque sí tiene acceso de escritura a GitHub.

## Hechos reportados y pendientes de comprobación actual

- Antigravity publicó index.html, robots.txt y sitemap.xml en /home/u985679183/domains/elcarmencienaga.edu.co/public_html y ajustó DirectoryIndex index.html index.php conservando WordPress. Sus peticiones dirigidas devolvieron HTTP 200. Verificar el contenido actual antes de nuevas escrituras.
- El usuario guardó en Registro Colombia helios.dns-parking.com y aster.dns-parking.com y confirmó el asistente en hPanel. Las capturas lo documentan. No repetir ni revertir la delegación sin evidencia que lo justifique.
- La guía actual de conexión de hPanel indicaba A @ -> 212.85.29.60, TTL 300; CNAME www -> elcarmencienaga.edu.co. La API había informado IP de servidor 195.35.61.110. Antigravity obtuvo la portada por ambas IP con Host correcto; la función interna de cada IP no quedó demostrada. Confirmar en datos actuales de Hostinger antes de editar DNS.
- Último reporte de Antigravity: DNS autoritativo respondía sin A de la web; API DNS daba DNS:4009 y DNS:1000; el editor manual devolvió «Dominio no encontrado». SSL estaba waiting_for_retry. No asumir que esto sigue igual hoy, ni que una cola interna es su causa.
- Se recomendó consultar soporte Hostinger por asociación/provisión de zona. No se ha recibido respuesta de soporte en el chat de coordinación.

## Siguiente trabajo de Codex local

1. Revisar el checkout, instrucciones locales y MCP disponibles; usar Hostinger Connector.
2. Consultar sitio, asociación del dominio, zona DNS actual y SSL, sin escrituras inicialmente.
3. Consultar delegación y registros A/CNAME en ambos autoritativos y resolutores públicos; comprobar HTTP/HTTPS para raíz y www. Distinguir comprobación directa por IP de navegación pública normal.
4. Si persiste «Dominio no encontrado», determinar la causa con evidencia y soporte; no restablecer la zona, borrar WordPress o repetir cambios de nameservers a ciegas.
5. Resolver los cambios necesarios dentro del alcance autorizado y las reglas aplicables del conector; comprobar resultado real. No modificar MX ni configurar Workspace todavía.
6. Actualizar este estado y presentar al usuario resultados comprobados y próximos pasos sencillos.

Google determina elegibilidad para Education. Una web activa es un requisito y no garantiza aprobación. La verificación TXT y posterior configuración de Gmail son fases separadas.
