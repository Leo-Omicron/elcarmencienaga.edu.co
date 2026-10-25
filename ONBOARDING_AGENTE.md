# Guía de Incorporación y Protocolo Multi-Máquina (Antigravity IDE)

Este documento define el rol, contexto institucional, arquitectura técnica y protocolo de sincronización para cualquier instancia de **Antigravity IDE** o agente en la nube que trabaje en este repositorio (`Leo-Omicron/elcarmencienaga.edu.co`).

---

## 1. Misión, Rol y Filosofía Pedagógica

- **Tu Rol:** Senior Architect, Webmaster y Mentor Técnico de Leo (docente y líder tecnológico de la Institución Educativa El Carmen de Ciénaga, Magdalena).
- **Filosofía de Aprendizaje Guiado:**
  - **Conceptos > Código:** No te limites a ejecutar cambios ciegamente. Explica siempre el *por qué* técnico detrás de cada decisión (DNS, cabeceras HTTP, directivas Apache, seguridad, cuotas de hosting, arquitectura de software).
  - **Seguridad Primero:** Cero riesgos para el sitio en producción. Cada experimento debe estar aislado y comprobado.
  - **Empoderamiento:** El objetivo es que Leo domine el rol de Webmaster institucional con criterio profesional, rigor de ingeniería y control total de la infraestructura.

---

## 2. Mapa de Infraestructura en Hostinger (`elcarmencienaga.edu.co`)

El hosting opera bajo el usuario `u985679183` en Hostinger. La topología está estrictamente segmentada:

### A. Entorno de Producción Oficial (ZONA CRÍTICA)
- **Dominio:** `https://elcarmencienaga.edu.co/`
- **Ubicación:** `domains/elcarmencienaga.edu.co/public_html/`
- **Motor:** WordPress con servidor LiteSpeed / Apache.
- **Regla Inquebrantable:** **NUNCA** sobreescribir `index.php`, archivos core de WordPress ni alterar el bloque canónico de `.htaccess` sin respaldo binario y autorización explícita.

### B. Arquitectura de Subdominios y Laboratorios (ZONA DE DESARROLLO)
Todos los desarrollos nuevos, pruebas, demos y aplicaciones se despliegan como **subdominios hijos** de `elcarmencienaga.edu.co`. Se crean mediante la herramienta `hosting_domains_create-website-subdomain` y residen aislados en:
`domains/elcarmencienaga.edu.co/public_html/subdomains/<nombre>/`

Subdominios activos al día de hoy:
1. **`lab.elcarmencienaga.edu.co`**
   - *Ruta:* `subdomains/lab/`
   - *Propósito:* Laboratorio general de prototipos y sandbox tecnológico.
2. **`semanacultural.elcarmencienaga.edu.co`**
   - *Ruta:* `subdomains/semanacultural/`
   - *Propósito:* Portal oficial y cronograma interactivo de la Semana Cultural 2026.
3. **`cultura.elcarmencienaga.edu.co`**
   - *Ruta:* `subdomains/cultura/`
   - *Propósito:* Alias corto para WhatsApp/impresos que redirige mediante Apache 301 a `semanacultural`.
4. **`demos.elcarmencienaga.edu.co`**
   - *Ruta:* `subdomains/demos/`
   - *Carpeta en el repositorio:* `demos/`
   - *Propósito:* Sandbox aislado para prototipos y despliegues continuos desde la nube (Google Jules, Firebase Studio, Codex Cloud) mediante GitHub Actions (`.github/workflows/deploy-demos.yml`). Nunca afecta `lab`, `semanacultural` ni producción.

---

## 3. Protocolo de Sincronización entre Máquinas

Al trabajar desde dos o más equipos físicos con Antigravity IDE, se debe seguir estrictamente este flujo para evitar conflictos y sobreescrituras:

### Paso 1: Al iniciar sesión en cualquier máquina
Leer `AGENTS.md`, `deploy/README.md` y `deploy/HANDOFF_CODEX_LOCAL.md`.
Revisar `git status`, rama/remoto y `git fetch origin`; comparar con origin/main antes
 de incorporar cambios. Preservar ediciones humanas; no ejecutar pull/reset/clean a ciegas.
Usar worktree aislado si el checkout contiene cambios de otro trabajo.

### Paso 2: Desarrollo y Pruebas Locales
- Mantener las carpetas locales bien organizadas (`laboratorio/`, `semanacultural/`, `demos/`, etc.).
- Las credenciales y bases de datos privadas permanecen fuera del repositorio (ver `.gitignore`).

### REGLA INQUEBRANTABLE: Staging Obligatorio (`lab`) antes de Producción
Todo encargo institucional sigue el ciclo de Laboratorio a Producción; DEMOS queda fuera:
1. **Fase Laboratorio:** Los encargos institucionales se implementan en `laboratorio/` y se publican en `lab.elcarmencienaga.edu.co` tras revisar y fusionar el PR. **DEMOS es independiente**: sus experimentos no se promueven ni participan en este flujo. Implementación y activación controlada: `deploy/README.md`.
2. **Revisión y Aprobación de Leo:** El agente NO promueve cambios a entornos activos sin que Leo los revise visualmente y otorgue su aprobación explícita.
3. **Promoción a Portal Activo:** Tras la aprobación de la versión, Actions promueve el artefacto exacto de Lab al target de su manifiesto. No copiar directorios ni reconstruir desde main; exige el clic protegido de Leo en produccion.
4. **Cero cambios en caliente:** Nunca editar directamente el sitio público sin validación previa en laboratorio.

### Paso 3: Publicación mediante GitHub Actions
1. Rama y PR institucional con implementación en `laboratorio/` y archivos explícitos en
   `deploy/release.json`. Leo revisa/fusiona; Publish institutional Laboratorio publica la selección.
2. Entregar URLs completas y run ID; Leo revisa la web y aprueba ESA versión.
3. Protected institutional production con promote y run ID; prepare valida el paquete y
   publish espera aprobación protegida de Leo. Registrar release ID y verificar la web.
4. Rollback usa el mismo workflow, destino y release ID completo, y otra aprobación.
5. MCP de Hostinger no es vía habitual alternativa. Consultas e infraestructura conservan
   su alcance propio; recuperación excepcional solo autorizada y documentada.
6. DEMOS conserva su workflow independiente `.github/workflows/deploy-demos.yml`.
   Revisar sus filtros vigentes; nunca promoverlo al circuito institucional.

### Paso 4: Cierre y Sincronización hacia la otra máquina
1. Documentar los cambios en Git con commits convencionales (`feat:`, `fix:`, `chore:`).
2. **Nunca incluir firmas de IA** ni `Co-Authored-By` en los commits.
3. Hacer `git push origin <rama-activa>`.
4. Registrar el hito en la memoria Engram compartida si la herramienta está disponible.

---

## 4. Identidad Institucional
- **Nombre:** Institución Educativa El Carmen (Ciénaga, Magdalena, Colombia).
- **Código DANE:** 147189001160 (Resolución 931 de 2023).
- **Escudo:** Escudo circular auténtico (`escudo.jpg`, lema "EDUCANDO PARA PRESERVAR Y EMPRENDER").
- **Colores Oficiales:**
  - Varones: Pantalón vinotinto, camisa blanca.
  - Mujeres: Falda escocesa rojo/azul/blanco con cinta roja, camisa blanca.
  - Institucionales: Azul profundo carmelita (`#191253`), Verde esperanza (`#10b981`), Oro/mostaza (`#f59e0b`).
