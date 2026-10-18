# Inicio de sesión para agentes

1. Leer `ESTADO_PROYECTO.md` y la tarea vigente en `odd/tasks/` antes de actuar; preservar las ediciones humanas, incluidas las de `CONTINUAR_EN_CODEX.md`.
2. Recuperar contexto con `mem_context`, buscar con las herramientas de búsqueda de memoria disponibles y obtener las observaciones completas con `mem_get_observation` (o el equivalente del cliente). No decidir solo por resúmenes ni resultados truncados; si falta acceso a memoria, declararlo.
3. Confirmar el alcance actual: una petición de lectura o auditoría no autoriza escribir en la web, publicar, cambiar Hostinger ni modificar configuraciones.
4. Usar la identidad y el almacén compartidos existentes; no inicializar una base sustituta ante un fallo. Consultar `MEMORIA.md` para comprobación, arranque, respaldos y recuperación.

No versionar recuerdos crudos, bases, respaldos, logs ni secretos. No prometer continuidad sin pérdidas ni dar por desplegada una configuración sin verificarla.
