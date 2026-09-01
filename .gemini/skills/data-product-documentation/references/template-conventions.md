# Template conventions

A compatible template is a Markdown document with ordered `##` sections, such as `ml_documentation_template.md`.

## Required fields

- Use `{{UPPER_SNAKE_CASE}}` placeholders for required values.
- A field is optional only when the template labels it `Opcional` or `Optional` near the placeholder.
- `PENDIENTE_USUARIO` identifies a field that must be resolved before publishing.
- The template may contain a `## Preguntas pendientes para el usuario` section. It is a working area and must be removed from the final Confluence page.

## Evidence guidance in templates

A template can state, below a section heading, the repository sources that may support its fields and suggested questions when evidence is missing. Those directions are part of the template and must be followed.

## Adding a template

Add a new `.md` file under `assets/templates/` or provide its path when running the skill. Preserve the conventions above so the validation and grouped-question workflow work without changes to the skill.

## Publication validation

Before publishing, the generated document must have no unresolved placeholders, no `PENDIENTE_USUARIO`, no working notes, and no unanswered required questions. A section may use `NO_APLICA` only when repository evidence supports that conclusion.
