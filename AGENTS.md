## Development

- **Keep content relevant**: Code, comments, and documentation must contain only information needed to maintain the current system. Omit authors, dates, version histories, task origins, development or reasoning processes, obsolete or failed approaches, and unrelated explanations.
- **Comment only when needed**: Let clear code express intent. Use comments only for essential design intent, constraints, and non-obvious logic.
- **Keep the system current**: Document only the active design, architecture, interfaces, and usage. When an approach changes, update affected content and remove obsolete code, configuration, comments, and documentation. Do not retain historical approaches, comparisons, or compatibility burdens.
- **Make minimal changes**: Perform only necessary changes and validation. Avoid overengineering, excessive defensive code, and overtesting. Obtain explicit user approval before handling or testing extremely unlikely edge cases or concurrency issues.
- **Review before executing**: Check assumptions and proposed approaches, then choose an appropriate implementation path rather than blindly following potentially flawed instructions.
- **Commit at milestones**: Make Git commits at key milestones.

## Environment

- **Isolate dependencies**: Run databases, middleware, and similar dependencies in Docker. Give containers and volumes meaningful names; remove test environments after testing to free disk space.
- **Manage installations and temporary files**: Prefer `C:\Program Files` for development environments and applications. If unavailable or the default installation path differs, use `C:\environment` or `C:\app`. Manage versions carefully. Delete temporary files after use; keep any retained files in `C:\code\tmp`.

## Logging

- **Record clear outcomes**: Log the final status of key business operations, distinguishing success, failure, and partial success.
- **Include context**: Capture key data needed to diagnose issues and reconstruct the business context. Include exception context in error logs and `request_id` or `trace_id` in key business logs.
- **Track tasks**: Log each asynchronous task's ID, execution status, and final result.
- **Trace state changes**: Log the affected object and relevant before and after states.
- **Avoid noise**: Do not repeat meaningless intermediate steps or add logs without diagnostic value.
