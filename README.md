# Institución Educativa El Carmen · Ciénaga

Portada institucional provisional, estática y sin compilación. Presenta el aviso de construcción, identidad, oferta general, identificación y contacto. No requiere WordPress, Node.js, base de datos ni secretos.

## Archivos para producción

- `index.html`: página completa con CSS y recurso gráfico incorporados.
- `robots.txt`: permite rastreo y referencia el sitemap.
- `sitemap.xml`: URL institucional principal.

No subir `.git`, documentos de trabajo, copias de seguridad ni este README al directorio público. El paquete `ie-el-carmen-provisional.zip`, preparado localmente fuera del repositorio, contiene solo los tres archivos públicos.

## Abrir localmente

Se puede abrir `index.html` directamente. Para usar un servidor de desarrollo:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

## Publicar y verificar

Ver [PUBLICACION.md](PUBLICACION.md). El despliegue en Hostinger, la delegación DNS y el certificado HTTPS deben verificarse aparte: guardar archivos en GitHub no publica el dominio.

## Recursos y decisiones

- Escudo completo contrastado visualmente con la referencia aportada por el propietario y recuperado de `Leo-Omicron/convivencia-escolar-el-carmen`, archivo `src/assets/escudo.jpg`. Se conserva la imagen original sin redibujar, recolorear ni deformar. Se incorpora en el HTML para evitar dependencias de otro sitio.
- Paleta web derivada del escudo aportado: azul profundo `#191253`, verde de acento `#43a447`, amarillo `#ffe500` y blanco. Verde oscuro `#27623f` para textos legibles. Los valores son una adaptación para pantalla, no especificaciones de un manual oficial de marca.
- Identidad y contacto contrastados entre PEI y membrete: carácter oficial/mixto, fundación 1973, DANE 147189001160, NIT 819002071-3, Resolución 2293 de 2022, dirección y correo `ieelcarmen@semcienaga.gov.co`.
- PEI consultado: documento con actualización indicada 2024, disponible en Drive en enero de 2025. Datos estables utilizados; no se copió su visión fechada a 2025, directivos, estadísticas ni promesas de programas vigentes.
- Teléfonos omitidos porque las fuentes presentan valores diferentes. La vigencia y recepción del correo requieren comprobación institucional.
- No se incluyen fotografías de estudiantes, analítica, formularios, cookies ni recursos externos.

## Google Workspace for Education

La web es una base de información institucional. Google exige una web educativa activa, reconocimiento oficial y solicitante perteneciente a la institución; determina la elegibilidad y puede solicitar documentos adicionales. Una portada provisional y un dominio .edu.co no garantizan aprobación.

Fuente: https://knowledge.workspace.google.com/admin/getting-started/editions/qualifications-for-google-workspace-for-education

## Estado de entrega

Página preparada para publicación. Consultar el informe de entrega del chat para saber qué commit se guardó y si el dominio se verificó. No interpretar este README como prueba de despliegue.
