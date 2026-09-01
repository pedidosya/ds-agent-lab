# {{PROJECT_NAME}}

> 📌 **Nota:** Este documento detalla un **Producto de Machine Learning (ML Product)**, incluyendo especificaciones de sus modelos, features, entrenamiento, orquestación y pipelines técnicos de datos.

> ## Instrucciones para Gemini CLI
>
> Completá este documento usando primero evidencia encontrada en el repositorio de GitHub indicado por el usuario.
>
> Para **cada sección** de este template seguí este proceso:
>
> 1. Buscá evidencia en GitHub antes de escribir contenido.
> 2. Priorizá este orden de fuentes:
>    - `README`, `docs/`, wikis internas exportadas al repo
>    - archivos de configuración
>    - código fuente
>    - SQL
>    - DAGs, workflows y jobs
>    - tests
>    - infraestructura y despliegue
> 3. Si la información está completa y es consistente, completá la sección.
> 4. Si la información falta, es ambigua o se contradice entre fuentes, **no inventes ni asumas nada**.
> 5. Registrá cada campo faltante en una lista de preguntas pendientes.
> 6. **Agrupá todas las preguntas faltantes en un solo bloque** y consultalas al usuario antes de publicar.
> 7. La información provista explícitamente por el usuario se considera fuente válida para completar el documento.
> 8. No elimines secciones aunque no encuentres información.
> 9. No publiques ni actualices Confluence mientras exista al menos un campo requerido sin resolver.
> 10. Solo cuando no queden campos requeridos faltantes, remové estas instrucciones y publicá o actualizá la página en Confluence usando MCP.
>
Reglas adicionales:

- La ausencia de evidencia en GitHub **no** prueba que algo no exista.
- Si una sección no aplica claramente al proyecto, indicá `NO_APLICA` solo cuando haya evidencia suficiente para justificarlo.
- Si un enlace o dato podría existir pero no se puede verificar, agregalo a las preguntas pendientes.
- Consultá siempre de manera proactiva al usuario si posee enlaces a presentaciones de Google Slides o documentos de Google Docs relevantes que desee adjuntar en la sección de Enlaces útiles.
- Antes de publicar, verificá que no queden placeholders `{{...}}`, `PENDIENTE_USUARIO` o notas de trabajo.

---

## Estado

Indicar el estado actual del proyecto.

Valores permitidos:

- POC
- Desarrollo
- AB Testing
- Productivo
- Deprecado
- On Hold

**Estado del proyecto:** {{PROJECT_STATUS}}

Si no surge del repositorio, preguntar al usuario:

`¿Cuál es el estado actual del proyecto: POC, Desarrollo, AB Testing, Productivo, Deprecado u On Hold?`

---

## Responsables

Identificar responsables del proyecto a partir de archivos como `README`, `CODEOWNERS`, ownership metadata o documentación interna del repositorio.

| Rol | Responsable |
| --- | --- |
| Data Scientist | {{DATA_SCIENTIST_OWNER}} |
| Data Engineer | {{DATA_ENGINEER_OWNER}} |
| Data Analyst | {{DATA_ANALYST_OWNER}} |
| Manager | {{MANAGER_OWNER}} |
| Otros | {{OTHER_OWNERS}} |

Si falta algún responsable requerido, preguntar al usuario por nombres o equipos concretos.

---

## Descripción funcional

### ¿Qué hace este proyecto?

{{FUNCTIONAL_DESCRIPTION}}

Explicar el comportamiento funcional del proyecto para una persona que no conoce la implementación.

### ¿Qué problema resuelve y qué KPI de negocio impacta?

{{BUSINESS_PROBLEM_AND_KPI}}

Si el KPI o el problema de negocio no aparecen claramente en GitHub, agregarlo a la lista de preguntas para el usuario.

---

## Tipo de ML Product

### ¿Este modelo se consume online?

{{IS_ONLINE_MODEL}}

Valores sugeridos:

- Sí
- No
- Parcialmente

### Modalidad de consumo

Describir cómo se consume el producto o modelo.

{{MODEL_CONSUMPTION_DESCRIPTION}}

Ejemplos:

- API online
- Batch
- Pipeline programado
- Tabla
- Archivo
- Evento
- Otro

### Fallback

Si el modelo se consume online, indicar si Ingeniería cuenta con un fallback y cómo funciona.

{{FALLBACK_DESCRIPTION}}

Si el modelo es online y GitHub no lo aclara, preguntar al usuario:

`¿Existe un fallback cuando el modelo o servicio no está disponible? ¿Cómo funciona?`

### Incidencias anteriores

Documentar incidentes previos reportados durante guardias u operación.

{{PREVIOUS_INCIDENTS}}

Si no hay evidencia suficiente, preguntar al usuario:

`¿Se registraron incidentes previos relacionados con este proyecto? En caso afirmativo, ¿cuáles?`

---

## Stakeholders involucrados

Identificar quién produce, mantiene o consume este proyecto.

### Producto

{{PRODUCT_STAKEHOLDERS}}

### Ingeniería

{{ENGINEERING_STAKEHOLDERS}}

Incluir, si aplica:

- equipo consumidor
- mecanismo de integración
- contacto técnico

### Negocio

{{BUSINESS_STAKEHOLDERS}}

### Data

{{DATA_STAKEHOLDERS}}

Si el repositorio no permite identificar stakeholders con suficiente evidencia, agrupar esas preguntas y consultarlas al usuario.

---

## Enlaces útiles

| Recurso | Link |
| --- | --- |
| Repositorio GitHub | {{REPOSITORY_URL}} |
| Proyecto en ML Tool | {{ML_TOOL_URL}} |
| Presentaciones de Google Slides (Opcional) | {{GOOGLE_SLIDES_LINKS}} |
| Documentos de Google Docs (Opcional) | {{GOOGLE_DOCS_LINKS}} |
| Feature Store | {{FEATURE_STORE_URL}} |
| Dashboard / Monitoreo | {{DASHBOARD_URL}} |
| Otra documentación | {{OTHER_DOCUMENTATION_URL}} |

Usar `NO_APLICA` solo si existe evidencia de que no corresponde. Si el recurso podría existir pero no se puede confirmar, consultar al usuario. Consultar siempre proactivamente al usuario si desea incluir enlaces a presentaciones de Google Slides (ej. arquitectura, negocio o avances) o documentos de Google Docs (ej. propuestas o especificaciones) relevantes para el producto de ML.

---

## Métricas

### ¿Cómo se mide el éxito del proyecto?

{{SUCCESS_MEASUREMENT}}

### Métrica principal

{{PRIMARY_METRIC}}

Ejemplo de redacción:

`La métrica principal es {{PRIMARY_METRIC_NAME}} porque permite medir {{PRIMARY_METRIC_REASON}}.`

### Comparación con baseline

{{BASELINE_COMPARISON}}

Describir cómo se compara el rendimiento con una solución anterior, baseline heurístico o control vigente.

Si la métrica o baseline no puede determinarse con evidencia suficiente, consultar al usuario antes de publicar.

---

## Impacto en el negocio

### ¿Cómo se mide el impacto en el negocio?

{{BUSINESS_IMPACT_MEASUREMENT}}

### Resultado o impacto reportado

{{BUSINESS_IMPACT_RESULT}}

Ejemplos:

- ahorro de costos
- incremento de conversión
- reducción de fraude
- mejora en SLA
- reducción de churn

Si el impacto no está documentado en GitHub, no inferirlo a partir de la existencia del proyecto; preguntarlo al usuario.

---

## Documentación operativa

### ¿Cómo correr el proyecto?

{{HOW_TO_RUN}}

### Posibles fallas y cómo solucionarlas

{{KNOWN_FAILURES_AND_FIXES}}

### Alertas usuales y su explicación

{{COMMON_ALERTS}}

Esta sección debe construirse a partir de scripts, `Makefile`, CI/CD, DAGs, jobs, runbooks y documentación operativa del repositorio. Si faltan procedimientos críticos, agrupar preguntas para el usuario.

---

## Documentación técnica

### Features utilizadas

Documentar nombre, tipo, descripción y origen de cada feature relevante.

{{FEATURES_USED}}

Formato sugerido:

| Feature | Tipo | Descripción | Origen |
| --- | --- | --- | --- |
| {{FEATURE_NAME}} | {{FEATURE_TYPE}} | {{FEATURE_DESCRIPTION}} | {{FEATURE_SOURCE}} |

### Datasets y tablas de entrenamiento

Identificar y documentar las tablas de BigQuery u otros almacenes utilizadas para el entrenamiento de los modelos, indicando su nombre, frecuencia de actualización y el link a su correspondiente proceso de actualización (ej. un DAG de Airflow, pipeline de Merovingian o script de ETL).

| Dataset / Tabla de entrenamiento | Frecuencia de actualización | Link al proceso de actualización | Descripción / Origen |
| --- | --- | --- | --- |
| {{TRAINING_DATASET_NAME}} | {{TRAINING_DATASET_UPDATE_FREQUENCY}} | {{TRAINING_DATASET_UPDATE_PROCESS_LINK}} | {{TRAINING_DATASET_DESCRIPTION}} |

Si no se encuentra evidencia con absoluta certeza del origen, frecuencia o link de actualización en el repositorio de GitHub, preguntar explícitamente al usuario:
`¿Cuál es el nombre de las tablas utilizadas para entrenar los modelos, cada cuánto se actualizan y cuál es el link a su proceso o pipeline de actualización (ETL/DAG)? No asumas esta información si no estás seguro.`

### Pipelines de entrenamiento de los modelos

Documentar si existen pipelines de entrenamiento formales dentro del proyecto (ej. en carpetas como `training_pipelines/` u orquestados en la plataforma) y cuál es su frecuencia de ejecución o re-entrenamiento (ej. manual, semanal, mensual, o automatizado por triggers).

{{TRAINING_PIPELINES_DETAILS}}

Si la existencia o frecuencia de actualización de los pipelines de entrenamiento no se puede verificar con certeza en el repositorio de GitHub, preguntar explícitamente al usuario:
`¿Existen pipelines de entrenamiento formales para este modelo en producción? En caso afirmativo, ¿con qué frecuencia se ejecutan o se actualizan (manual, programado, etc.)? No asumas esta información si no estás seguro.`

### Output del proyecto

Indicar si el output es una API, tabla, archivo, evento u otro artefacto; describir su estructura y uso.

{{PROJECT_OUTPUT}}

### Tools utilizadas

Documentar herramientas como Feature Store, ML Tool, QAT, orquestadores, serving, monitoreo u otras, y de qué forma participan.

{{TOOLS_USED}}

### Arquitectura de la solución

Describir detalladamente el ML pipeline, dependencias principales, flujo de datos, entrenamiento, validación, despliegue y consumo.

{{SOLUTION_ARCHITECTURE}}

---

## Preguntas pendientes para el usuario

> Completar esta sección **solo si** faltó información luego de revisar GitHub. Todas las preguntas deben agruparse acá antes de cualquier publicación en Confluence.

{{GROUPED_USER_QUESTIONS}}

Si no quedan preguntas pendientes, reemplazar esta sección completa por:

`Sin preguntas pendientes. Toda la información requerida fue resuelta con evidencia del repositorio o respuestas explícitas del usuario.`

---

## Regla final de publicación en Confluence

Antes de publicar o actualizar en Confluence mediante MCP, verificar:

- no quedan campos requeridos sin completar
- no quedan placeholders `{{...}}`
- no quedan preguntas pendientes para el usuario
- las respuestas del usuario ya fueron incorporadas al documento final

Solo después de cumplir esas condiciones:

1. remover las instrucciones operativas y placeholders
2. generar la versión final en Markdown limpio
3. crear o actualizar la página de Confluence mediante MCP
4. confirmar al usuario qué página fue publicada o actualizada
