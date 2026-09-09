---
name: data-product-documentation
description: Generate or update Data Product documentation from a GitHub repository URL using a compatible Markdown template, collecting all unknown details before publishing to Confluence via MCP.
---

# Data Product Documentation

Use this skill when the user wants to document a Data Product from a GitHub repository, or refresh an existing Confluence document after repository changes.

## Required inputs

Collect missing startup inputs together before analyzing the repository:

- `github_repository_url`: HTTPS or SSH URL of the repository to inspect. For private Pedidos Ya repositories, prefer SSH when it is configured, otherwise accept the HTTPS form `https://github.com/PedidosYa/<repository>.git`. Never use the current working directory as a substitute.
- `template_path`: compatible Markdown template path. If not explicitly supplied by the user at startup, the agent MUST list all available templates inside the skill's `assets/templates/` directory and use the `ask_user` tool to let the user select which template they want to apply. Never default silently if multiple templates exist or if the user has not chosen one.
- `confluence_mode`: `create` or `update`.
- `confluence_parent_page_url`: required when `confluence_mode` is `create`.
- `confluence_page_url`: required when `confluence_mode` is `update`.
- `language`: `es` or `en`. Optional parameter. By default, it is set to `es` (Spanish). Only use `en` (English) if the user explicitly requests it.

An optional branch, tag, or commit may be supplied. Use the repository default branch when none is given and state that choice in the draft.

Read [github-access.md](references/github-access.md) before accessing a private repository. Read [template-conventions.md](references/template-conventions.md) before using a template. Read [confluence-workflow.md](references/confluence-workflow.md) before any Confluence operation.

## Workflow

1. Validate the repository URL and access it remotely. Verify access with `git ls-remote <url>` (using `GIT_SSH_COMMAND="ssh"` explicitly if the system's `core.sshCommand` environment variable is blank or misconfigured to avoid fork failures). Clone the repository into a newly created temporary subdirectory inside the designated project temporary directory (e.g., `~/.gemini/tmp/gemini-docu` or equivalent project temp directory) rather than the operating system's default `/var/folders/` to prevent permission and workspace tool access violations. Never use the current working directory as a substitute.
2. If the `template_path` input was not provided, scan the skill's `assets/templates/` directory, display the list of found templates to the user, and prompt them to pick one using `ask_user`. Read the selected template and preserve its heading order, tables, and wording. Treat each `{{FIELD_NAME}}` token as required unless the template explicitly labels it optional.
3. **FIRST QUESTION IN UPDATE MODE (MANDATORY):** If `confluence_mode` is set to `update`, the agent MUST ask the user as the very first question *before analyzing or reading the repository*: **"Would you like to update something specific in the documentation, or would you prefer me to scan the entire repository to detect changes automatically?"**.
   - If the user specifies specific fields, sections, or aspects to update, focus the subsequent analysis and changes strictly on those points, merging them into the existing Confluence page while keeping unaffected content untouched.
   - If the user chooses automatic detection, proceed with full repository harvesting as described in step 4.
4. **AUTONOMOUS HARVESTING & CLASSIFICATION FIRST:** 
   - Analyze the repository to classify the type of Data Product. It is an **ML Product** if it contains model training code, predictive scripts, serialized models (`.pkl`, `.pkl`, `.h5`, `.pbtxt`), training pipelines, or modeling dependencies like `lightgbm`, `xgboost`, `scikit-learn`, `optuna`. It is a **General Data Product** if it consists of SQL files, dbt models, Looker dashboards, reports, or ETL pipelines without modeling layers.
   - For **ML Products**, exhaustively inspect and harvest ALL information from configuration files (YAML, JSON), source code, SQL queries, markdown files (including evaluation reports, performance reports, and EDA notebooks/files), and dependencies. Populate metrics, lifts, baseline comparisons, training datasets, update frequencies, pipelines, and technical architecture steps.
   - For **General Data Products**, adapt your harvesting to document input/output tables, schema field mappings, metrics defined in dbt/dashboards, ETL transformation steps, visual links, and refresh frequencies.
5. **SENSIBLE DEFAULTING & CONFLUENCE MERGE:** 
   - If a role (like Data Scientist, Data Engineer, or Data Analyst) is not found in the codebase, but the Git history/dependencies suggest a single-author project (e.g., only one contributor has committed to the codebase), set the author as the Data Scientist and default the other engineering/analytical roles to `NO_APLICA` or `No especificado` if they are not explicitly present.
   - In `update` mode, you MUST merge the existing Confluence page's verified statements for non-code aspects (such as stakeholders, manager, slides/docs links) directly into the new draft to preserve them. Do not ask about fields that are already populated on the existing Confluence page unless repository evidence directly contradicts them.
6. In `update` mode, read the current Confluence page before drafting. Compare it to repository evidence, keep unaffected content, and identify changed, removed, and unverified statements. If repository evidence conflicts with the existing page, ask the user instead of choosing silently.
7. **CRITICAL INTERACTION MANDATE (SEQUENTIAL QUESTIONS BACKUP):** Any information requested by the template that is not explicitly and certainly found in the GitHub repository, or about which you have any doubts, MUST be proactively consulted with the user instead of assuming it or defaulting it without asking. When asking is necessary, under no circumstances are you allowed to group or consolidate multiple questions into a single response. You MUST formulate **exactly one single question per turn**, wait for the user's response, incorporate that information into the draft, and only then proceed with the next question in the subsequent turn.
8. Repeat evidence collection and validation after the user responds. Do not publish while any required field is unresolved or any `{{...}}`, `PENDIENTE_USUARIO`, or working note remains.
9. Show the completed draft and the intended action: create below the parent page, or update the identified existing page. Perform the MCP write only when the user has requested publication or confirmed that action.
10. Verify the returned Confluence page URL, title, and rendered content after the write. Report the result and the repository revision used.
11. Remove the temporary clone in a cleanup step whether the workflow succeeds, fails, or is interrupted. Delete only the directory created for this execution after confirming that it is inside the system temporary directory and has the skill's dedicated prefix.

## Question format

**INDIVIDUAL QUESTION FORMAT (ONE PER TURN):** When formulating your single question for the turn, explain in detail the template field you are trying to resolve, what evidence (or lack thereof) you found in the repository, and ask the user for the specific fact or decision needed. Never show a list of multiple questions for the user to answer at once. This guarantees the user can respond conversationally one by one.

## Output rules

- Keep a working evidence ledger separate from the publishable document.
- Remove the template's agent instructions, placeholders, and pending-question block from the document sent to Confluence.
- Do not create duplicate Confluence pages in `update` mode.
- If no configured Confluence MCP exposes the required read or write operation, stop before publication and explain what capability is unavailable.
- By default, the published documentation on Confluence MUST be written entirely in Spanish. Only document in English if the `language` parameter is explicitly set to `en` by the user.
- The documentation format must be extremely clear, organized, and professional.
- **Rendering Format and Quality Guardrail (MANDATORY):** To prevent raw text/markdown rendering issues on Confluence, NEVER publish raw Markdown text enclosed in simple text paragraphs or poorly wrapped tags. The final published content on Confluence MUST be rendered with maximum structural quality. When publishing or updating pages via MCP, ALWAYS use the `contentFormat` `"html"` parameter and translate the document into semantic, clean, native Confluence-compatible HTML (using correct heading tags `<h1>-<h6>`, lists `<ul>/<ol>/<li>`, standard `<table>` elements with headers `<th>` and rows `<td>`, Status Badges `<span data-type="status" data-color="...">`, panels `<div data-type="panel-info|panel-warning...">`, and formatted blocks). Never leave unrendered raw markdown markers like raw `###`, raw bold `**`, or raw bullet markers `*` in plain text on the published page.
- **Conditional Rules by Product Type (MANDATORY):**
  - **For ML Products:**
    - The "Datasets and training tables" section must ALWAYS be included in the final generated documentation.
    - **Detailed Features and Datasets (MANDATORY):** The features used in ML models must be listed in detail in a table format, including name, type (numeric or categorical), clear description in user-friendly language (non-technical), and origin/source. Additionally, the exact BigQuery table where these datasets reside must be explicitly specified, along with its update frequency. Features must not be grouped or compactly summarized (such as lists of names only) if business descriptions can be provided for each variable.
    - **Dataset Generation and Pipeline Tracking (MANDATORY):** If there is any dataset generated or transformed specifically to feed/train the Data Product, the agent MUST explicitly ask the user for the link to the corresponding orchestration pipeline (e.g. Airflow DAG, dbt job) and its execution time/frequency, in case this information is not fully certain or verifiable from the repository codebase alone. If in doubt, always confirm these values with the user before publishing.
  - **For General Data Products (Dashboards, dbt, Tables):**
    - The "Datasets and training tables" section should be adapted to describe "Tablas de Entrada y Salida" (Input/Output tables), their purposes, and refresh frequencies.
    - Instead of features, the output must document key schema fields and metrics (nombre, tipo, descripción de negocio, procedencia/origen) in a table format to make the data schema understandable for business users.
- **SEQUENTIAL QUESTIONS RULE (ONE BY ONE - MANDATORY):** If, after exhaustive harvesting and Confluence merging, any required field remains completely missing or placeholder `{{...}}` is unresolved, you MUST consult each such missing field individually and sequentially (only one question per conversational turn). It is strictly forbidden to consolidate or ask questions in batches. If you identify multiple missing fields, you must take as many individual conversational turns as necessary to resolve them, one by one. Only if the user explicitly chooses not to answer, skips, or instructs you to proceed, may you leave that field with the literal tag `PENDIENTE_USUARIO` for subsequent manual editing on Confluence.
