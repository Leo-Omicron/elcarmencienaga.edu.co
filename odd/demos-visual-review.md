# Revisión visual adicional de DEMOS

Referencia revisada: portada pública de Semana Cultural y dia1.html a dia5.html.
Base: main 3c105be9d66abea9c8a3080f55f85fe9d63888b4 (PR #4 integrado).
Se conservan la reingeniería ya integrada y los trabajos posteriores de PR #5 y #6.

## Comprobaciones

Navegación real en navegador por las seis páginas de referencia. Comparación con
la portada publicada de DEMOS y su apartado #cierre: hero con afiche íntegro,
cabecera blanca, tipografías Outfit/Plus Jakarta Sans, sombras, botones y acentos
de cada jornada. Cierre con Santa Misa del viernes 23 de octubre y acceso al Día 5.

En DEMOS se abrieron los cinco visores, se avanzó con ArrowRight y se cerró con
Escape, comprobando retorno al activador. Contadores observados: 20, 34, 21, 49 y 12.
El Día 4 comienza visualmente por las tres imágenes de GFM (índices 47–49);
su orden de lectura no coincide con el índice numérico, como en la referencia.

Se observó un cierre intermitente al pulsar zoom inmediatamente después de cambiar
de fotografía. La ampliación modifica el rectángulo del diálogo; el detector de
clic exterior heredado se ejecuta después, con la geometría nueva. Se detiene la
propagación del clic de zoom para que ese clic no cierre el mismo visor.
No se modifican los estilos ni el contenido cultural.

Pruebas locales: python scripts/check_demos.py y node scripts/test_demos_zoom.cjs.
La segunda prueba reproduce la propagación que causaba el cierre tras redimensionar.

## Límites

Esta revisión usa el viewport de escritorio disponible. La revisión a anchos
móviles concretos y la reproducción de todos los videos de YouTube siguen pendientes.
No se afirma que la mera presencia del iframe pruebe su reproducción.
No se modificó Laboratorio, Semana Cultural productiva ni la raíz institucional.
La rama demos/visor-zoom-review publica únicamente DEMOS mediante el workflow existente.
