## Retrospectiva del Proyecto

### ¿Qué funcionó bien?
* **Gestión visual con Kanban:** Desglosar el proyecto en *Issues* asociadas a Historias de Usuario dentro de GitHub Projects facilitó la organización de tareas y el seguimiento transparente del avance.
* **Enfoque en MVP (Producto Mínimo Viable):** Desarrollar la arquitectura inicial en Python puro para la consola permitió asegurar la lógica base de la aplicación (CRUD de tarjetas) sin sobrecargar la complejidad técnica inicial.
* **Flexibilidad en el flujo de trabajo:** La adaptabilidad entre la interfaz web de GitHub y la terminal local permitió dar continuidad al desarrollo desde diferentes entornos informáticos.

### Retos y Áreas de Mejora
* **Sincronización multi-entorno:** El intercambio de equipos de trabajo requirió especial atención al flujo de sincronización (`git pull`) para evitar conflictos de versiones o archivos desfasados.
* **Diseño previo de la persistencia:** Integrar la estructura del archivo de persistencia (`JSON`) a la par con el CRUD inicial habría agilizado la transición del módulo de almacenamiento.

### Lecciones Aprendidas
* La metodología Kanban es altamente efectiva tanto en equipos de software como en el desarrollo individual para mantener la trazabilidad de los commits vinculados a tareas específicas.
* Elaborar la documentación técnica y el diagrama de arquitectura en fases tempranas proporciona una hoja de ruta clara al escribir el código base del sistema.
