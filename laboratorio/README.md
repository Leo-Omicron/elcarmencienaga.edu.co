# Primer ejercicio del laboratorio web

Aprende con `index.html`, una página estática de pruebas que no reemplaza el sitio institucional. Publicada y comprobada el 18 de octubre de 2026 en **https://lab.elcarmencienaga.edu.co/**: HTTPS válido, HTTP 200 y HTML servido idéntico al archivo local. La revisión visual en navegador sigue pendiente; la comprobación de estructura no la sustituye.

## Abrir la vista previa

Abre `laboratorio/index.html` directamente en un navegador. Si tienes Python, también puedes ejecutar desde la raíz del repositorio:

```sh
python -m http.server 8000 --directory laboratorio --bind 127.0.0.1
```

Visita `http://127.0.0.1:8000/` y detén el servidor con `Ctrl+C` al terminar. Es una vista previa local, no una publicación ni una prueba de HTTPS. El servidor puede mostrar también este README: no lo expongas a la red pública.

## Tres piezas distintas

| Pieza | Para qué sirve |
| --- | --- |
| GitHub | Guarda y permite revisar versiones del código. Guardar allí no publica automáticamente esta página en el hosting. |
| Hosting | Almacena y sirve el archivo que se suba al laboratorio. Debe tener una raíz verificada y separada de producción. |
| URL | Es la dirección que abre el navegador: `https://lab.elcarmencienaga.edu.co/`. HTTP redirige a HTTPS; comprobar nuevamente después de cada publicación. |

Producción es **https://elcarmencienaga.edu.co/**. Se comprobó HTTP 200 y contenido coincidente con su fuente local después de publicar el laboratorio. No cambies sus archivos, DNS ni configuración para esta práctica. Las raíces verificadas son distintas y no anidadas, pero ambos sitios comparten recursos del plan: no es aislamiento de seguridad o rendimiento.

## Un cambio reversible

1. Conserva fuera de la carpeta que se publicará una copia revisada del `index.html` anterior.
2. En la tarjeta del primer ejercicio, cambia «Mi primera práctica web» por «Aprendo a editar una página». Conserva el aviso de laboratorio.
3. Previsualiza y recarga: comprueba el título, los enlaces, una ventana estrecha y la navegación con Tab. El foco debe verse y «Saltar al contenido» debe funcionar.
4. Tras verificar el destino y su inventario, el responsable publica **solo `index.html`** en la raíz del laboratorio. Si ya existe otro archivo, debe respaldarlo y revisar la autorización antes de sobrescribirlo.
5. Abre la URL del laboratorio: comprueba HTTPS sin avisos, el texto y los enlaces. Comprueba también que producción sigue intacta. No des por publicado un cambio solo porque se subió un archivo.
6. Para deshacer, restaura el `index.html` anterior revisado en el laboratorio, recarga y repite las comprobaciones. No toques producción.

## Límites de seguridad

- Solo `index.html` está destinado al despliegue. **No publiques este README**, el repositorio completo, copias de respaldo ni archivos de configuración.
- Nunca pongas datos de estudiantes, datos personales, fotografías privadas, credenciales ni secretos en el laboratorio, aunque sea una prueba.
- `noindex,nofollow` es una petición a buscadores, no privacidad, autenticación ni control de acceso. Cualquiera con acceso a la URL puede leer la página.
- Esta práctica no instala aplicaciones ni backend, no recoge datos y no modifica el hosting por sí misma.

## Límite de verificación

Las comprobaciones HTTP y de contenido fueron ejecutadas por el responsable de publicación. El subagente de verificación independiente terminó sin entregar un resultado verificable; no se da por aprobada esa revisión. Tampoco se ejecutó revisión visual en navegador. El cierre y los commits locales del laboratorio siguen pendientes; la página de demostración sí está publicada.

Siguiente paso: abrir el laboratorio en tu navegador y revisar esta demostración antes de plantear otro ejercicio.
