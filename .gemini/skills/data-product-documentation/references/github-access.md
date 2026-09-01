# GitHub access

## Private Pedidos Ya repositories

Prefer the SSH repository URL supplied by the user when their SSH key is configured, in this form:

```text
git@github.com:PedidosYa/<repository>.git
```

Before cloning, run `git ls-remote <repository-url>`. If the system environment has a blank or misconfigured `core.sshCommand`, explicitly prefix the git command with `GIT_SSH_COMMAND="ssh"` (e.g., `GIT_SSH_COMMAND="ssh" git ls-remote <repository-url>`). A response containing branches or tags proves that the active SSH key can read the repository.

Clone only to a newly created temporary subdirectory with a dedicated prefix (e.g., `gemini-data-product-documentation-`) located inside the designated project temporary directory (e.g., `~/.gemini/tmp/gemini-docu` or equivalent), rather than macOS `/var/folders/`, to prevent permission and workspace tool access violations. Do not inspect or reuse the current working directory. Use a shallow clone of the requested branch when repository history is not needed; fetch additional history only when the documentation task requires comparison with earlier revisions.

Register cleanup before cloning. At the end of the workflow, including on failure or interruption, remove only that execution's clone directory after confirming both conditions:

1. Its resolved path is inside the designated project temporary directory (e.g., `~/.gemini/tmp/gemini-docu` or equivalent) or the operating system's temporary directory.
2. Its basename starts with `gemini-data-product-documentation-`.

Never delete the current working directory, the source repository, a path supplied by the user, or a temporary-directory parent. Report that cleanup completed without exposing the temporary path in the published documentation.

If `git ls-remote` or cloning fails because SSH is not configured, offer HTTPS instead of asking for a private key. Do not request or store a private key.

## Other repository URLs

For private repositories without SSH access, accept the HTTPS form:

```text
https://github.com/PedidosYa/<repository>.git
```

Verify it with `git ls-remote <repository-url>` and clone it only to a newly created temporary directory. Git must authenticate through an existing credential helper, GitHub CLI login, operating-system keychain, or a configured GitHub integration. If authentication is unavailable, tell the user to configure one of those mechanisms outside the skill, then retry.

Never embed a username, password, or token in the URL, prompt, generated document, or skill files. For public repositories, SSH or HTTPS may be used without credentials.
