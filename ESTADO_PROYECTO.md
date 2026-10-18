# Continuidad del proyecto — IE El Carmen

Actualizado el 18 de octubre de 2026. Este documento conserva el contexto; no sustituye comprobaciones actuales.

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
