# Inicio de sesión para agentes

1. Leer `deploy/README.md`, `deploy/HANDOFF_CODEX_LOCAL.md`, `ONBOARDING_AGENTE.md`, `ESTADO_PROYECTO.md` y la tarea vigente en `odd/tasks/` antes de actuar; preservar las ediciones humanas, incluidas las de `CONTINUAR_EN_CODEX.md`.
2. Recuperar contexto con `mem_context`, buscar con las herramientas de búsqueda de memoria disponibles y obtener las observaciones completas con `mem_get_observation` (o el equivalente del cliente). No decidir solo por resúmenes ni resultados truncados; si falta acceso a memoria, declararlo.
3. Confirmar el alcance actual: una petición de lectura o auditoría no autoriza escribir en la web, publicar, cambiar Hostinger ni modificar configuraciones.
4. Usar la identidad y el almacén compartidos existentes; no inicializar una base sustituta ante un fallo. Consultar `MEMORIA.md` para comprobación, arranque, respaldos y recuperación.
5. **Regla de Diseño e Interfaz (UI):** Consultar `DESIGN_SYSTEM.md` antes de crear o modificar páginas o componentes en `demos/`, `laboratorio/` o producción. NUNCA inventar paletas moradas genéricas ni estilos en línea arbitrarios; enlazar la hoja de estilos institucional `css/institucional.css` y reutilizar las clases y tokens oficiales (`--primary: #191253`, `--accent-green: #10b981`, `--accent-gold: #f59e0b`).

No versionar recuerdos crudos, bases, respaldos, logs ni secretos. No prometer continuidad sin pérdidas ni dar por desplegada una configuración sin verificarla.

6. **Separación de entornos:** DEMOS es experimental e independiente. Nunca promover DEMOS a Laboratorio/Producción. Encargos institucionales: PR → merge en main → Laboratorio; promoción de la versión exacta solo tras aprobación de Leo y aprobación protegida de GitHub. Consultar `deploy/README.md`. No activar ni publicar como prueba de configuración sin un encargo explícito.

7. **Publicación institucional vigente:** usar GitHub Actions; no publicar directamente por MCP Hostinger, TUS, SFTP manual ni scripts locales para eludir el flujo. La recuperación excepcional requiere alcance y aprobación específicos. Leo hace merge del PR, revisa la URL exacta de Lab y aprueba la versión; producción/rollback requieren además su clic protegido. No reconstruir desde main el contenido aprobado: promover el artefacto de la ejecución de Lab.
8. **Continuidad local:** Codex local tiene encargo explícito de actualizar y releer Engram, conservando el almacén existente, y dejar relevo a Antigravity. Leer `deploy/HANDOFF_CODEX_LOCAL.md`. No afirmar que otras sesiones lo leyeron por haber creado un archivo. Evidencia real y pendientes en `deploy/PRUEBAS_FLUJO_2026-10-24.md`.
