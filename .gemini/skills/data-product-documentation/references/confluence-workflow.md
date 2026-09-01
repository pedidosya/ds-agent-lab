# Confluence workflow

Use the configured Confluence MCP only after all required template fields have been resolved. Inspect its available tools at runtime; tool names differ by MCP implementation.

## Create mode

1. Resolve and read `confluence_parent_page_url` or its page ID with the MCP.
2. Confirm that it is the intended parent and determine the generated page title from the completed template.
3. Create one child page below that parent with the cleaned document body.
4. Read the created page and verify its title, parent, and content.

## Update mode

1. Resolve and read `confluence_page_url` or its page ID with the MCP, including its current version if the MCP provides one.
2. Compare the page body with the completed template and repository evidence.
3. Retain content in sections that have no repository-backed change. Update only sections supported by new evidence or explicit user answers.
4. If a current Confluence statement cannot be validated, label it as an ambiguity in the grouped questions. Do not delete it solely because it was not found in the repository.
5. Update that same page, using the current version or concurrency token when the MCP requires it.
6. Read the updated page and verify the new version, title, and content.

## MCP safeguards

- Use a search or read operation before every create or update operation.
- Never use a write tool when the evidence ledger contains unresolved required fields.
- Never create a new page as a fallback for a failed update.
- If the page cannot be found, access is denied, or a version conflict occurs, stop and report the issue without retrying destructively.
