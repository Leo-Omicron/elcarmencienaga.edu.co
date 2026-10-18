# Continuar en Codex local — Landing IE El Carmen

## Punto de partida

Proyecto existente en Windows: `D:\Leo\Proyectos\IEEC\Landing`.
Repositorio: `https://github.com/Leo-Omicron/elcarmencienaga.edu.co`, rama `main`.
No recrear el proyecto ni clonar encima de los archivos existentes. No reinicializar Git.

Primero leer las instrucciones AGENTS.md que apliquen, inspeccionar estado de Git y remoto, y preservar cambios locales. Actualizar desde main solo si puede hacerse sin perder trabajo; resolver divergencias sin reset --hard. Después leer ESTADO_PROYECTO.md, PUBLICACION.md y README.md.

## Encargo y forma de trabajo

El usuario quiere que Codex dirija y ejecute el proyecto. Hostinger Connector ya funciona en su Windows: el chat «Probar conexión a Hostinger» ejecutó hosting_websites_list y obtuvo el sitio habilitado. No depender de Antigravity para continuar. No reinstalar el conector por las limitaciones que tenía el chat anterior en la nube.

Guiar al usuario con pasos sencillos y resultados verificados. No dar por hechos cambios de infraestructura, propagación global ni ejecución en segundo plano. Separar lo observado directamente de los reportes históricos. Pedir información únicamente cuando sea necesaria.

## Prioridad inmediata

Publicar y verificar la portada institucional provisional en el dominio con HTTPS. No es obligatorio desarrollar el sitio definitivo ni usar WordPress ahora. La implementación actual es HTML/CSS estático, sin compilación, credenciales, formularios ni servicios externos.

Antigravity reportó que ya subió index.html, robots.txt y sitemap.xml a la raíz pública y agregó DirectoryIndex index.html index.php conservando WordPress. Comprobar el estado actual antes de volver a publicar.

## Infraestructura conocida

- Dominio correcto: elcarmencienaga.edu.co.
- Registrador externo: Registro Colombia; dominio nuevo sin correo previo.
- Nameservers guardados por el usuario: helios.dns-parking.com y aster.dns-parking.com. También confirmó el asistente en hPanel.
- Sitio Hostinger: usuario u985679183; raíz reportada /home/u985679183/domains/elcarmencienaga.edu.co/public_html.
- IP indicada por la guía de conexión de hPanel: 212.85.29.60. IP de servidor reportada por la API: 195.35.61.110. Antigravity recibió la portada desde ambas con Host correcto. No asumir su arquitectura interna ni usar un valor histórico sin contrastarlo con el panel actual.
- Último bloqueo reportado: API DNS con DNS:4009 Domain not found / DNS:1000 Domain not pointing to Hostinger; hPanel manual también «Dominio no encontrado»; autoritativos sin A web; SSL waiting_for_retry.
- Se recomendó consultar soporte por asociación/provisión de zona, pero no hay respuesta confirmada de soporte en el historial de coordinación.

## Primer diagnóstico requerido

Usar Hostinger Connector para listar el sitio y consultar dominio/zona/SSL. Consultar delegación y registros raíz/www públicamente y en ambos servidores autoritativos. Revisar HTTP y HTTPS para raíz y www sin desactivar validación TLS. Distinguir pruebas con --resolve de navegación pública normal. No repetir cambios de nameservers si ya están correctos.

Si persiste el bloqueo DNS, investigar la asociación del dominio y soporte; no restablecer la zona ni eliminar/recrear el sitio como prueba. No configurar Google ni registros de correo para resolver este problema de web.

Después de obtener un diagnóstico actual, completar las operaciones autorizadas necesarias respetando las reglas aplicables del conector. No comprar, borrar instalaciones o cambiar correo sin la autorización correspondiente. Conservar los datos de WordPress.

## Diseño ya aprobado y recursos

- Escudo completo contrastado con la imagen aportada por el usuario; ya incorporado al HTML.
- Fuente de la copia: repositorio anterior Leo-Omicron/convivencia-escolar-el-carmen, src/assets/escudo.jpg.
- Colores web: azul profundo #191253, verde de acento #43a447, amarillo #ffe500 y blanco. Verde oscuro #27623f para texto legible. Son adaptación para pantalla, no un manual oficial.
- Lema: «Educando para preservar y emprender».
- La portada incluye aviso de construcción, preescolar/básica/media, identificación institucional y contacto.
- Datos contrastados con PEI y membrete: fundación 1973, carácter oficial/mixto, DANE 147189001160, NIT 819002071-3, Resolución 2293 del 6 de septiembre de 2022, dirección Calle 12 No. 1C-57, Ciénaga, y correo ieelcarmen@semcienaga.gov.co.
- Teléfonos y directivos omitidos por diferencias entre fuentes. No publicar estadísticas, cupos SENA o visión fechada como si estuvieran vigentes.
- Comprobaciones realizadas: estructura HTML, anclas, integridad de la imagen, contraste de texto y coincidencia de archivos con el ZIP. No se completó prueba visual desde el entorno de nube; Antigravity reportó vista previa correcta en Windows.

## Plan posterior

1. Web pública accesible, DNS y HTTPS verificados.
2. Confirmar con la institución datos, recepción del contacto y resolución completa de reconocimiento.
3. Consultar si ya existe tenant de Workspace o cobertura de Secretaría de Educación.
4. Tramitar Google Workspace for Education Fundamentals con responsable institucional autorizado. Google decide elegibilidad; el dominio .edu.co y la portada no garantizan aprobación.
5. Añadir únicamente el TXT exacto de verificación que Google entregue. Configurar Gmail/MX/SPF/DKIM/DMARC cuando corresponda, con cuentas y transición preparadas.
6. Desarrollar después el sitio completo: Inicio, Nuestra institución, Oferta educativa, Comunidad educativa, Proyectos y noticias, Transparencia y atención, Contacto. Elegir CMS según necesidades editoriales; WordPress no es una obligación.
7. Completar identidad, documentos públicos, fotos autorizadas, accesibilidad, copias y mantenimiento.

## Referencias privadas

El usuario aportó Plan_Maestro_Web_IE_El_Carmen.md y Crear web institucional.pdf. Hay un paquete descargable de continuidad separado con estos originales. El plan inicial tiene estados antiguos (antes de compra/instalación/repositorio): usarlo como antecedentes, no como estado actual.

No publicar la conversación completa, capturas, respaldos de servidor o documentos privados en este repositorio público. No registrar tokens ni contraseñas. El respaldo local del servidor fue reportado en D:\Leo\Proyectos\IEEC\backup_hostinger_20261017, fuera del proyecto.

## Criterio de finalización inmediato

Confirmar con pruebas reales que https://elcarmencienaga.edu.co/ presenta la portada actual y responde HTTP 200, certificado válido y redirecciones coherentes para HTTP/www; robots y sitemap accesibles. Actualizar ESTADO_PROYECTO.md con hechos actuales y pendientes, sin dar por completada la aprobación de Google.
