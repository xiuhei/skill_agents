## Development Guidelines

##### Development Standards

- Keep only the information and current, valid state necessary to understand and maintain the system in code, comments, and documentation. Do not include metadata such as authors, dates, version histories, task origins, development processes, obsolete or failed approaches, reasoning processes, or irrelevant explanations.
- Omit comments when the code clearly expresses its intent. Use comments only to explain essential design decisions, constraints, and non-obvious logic.
- Documentation must describe only the current design, architecture, interfaces, and usage. When an approach changes, update the relevant content directly and remove outdated information. Do not retain historical approaches or comparisons with them. When replacing an implementation, also remove obsolete code, configuration, comments, and documentation. Do not leave old and new approaches coexisting or introduce legacy compatibility burdens.
- Follow the principles of minimal necessary changes and minimal necessary validation. Avoid overengineering and excessive validation.
- Avoid excessive defensive programming and overtesting. Edge cases or concurrency issues that are extremely unlikely to occur require explicit user approval before adding handling or tests. Do not expand the codebase solely for theoretical robustness.
- User instructions may contain flawed assumptions or proposed approaches. Before starting a task, review the instructions critically and look for the best available approach to prevent errors from accumulating. Do not blindly follow the proposed implementation path.
- Make Git commits at key milestones.

##### Environment

- Run databases, middleware, and similar dependencies in Docker. Use meaningful names for containers and volumes. Remove test environments after testing to free disk space.
- Install development environments and applications in the default location, `C:\Program Files`. If that location is unavailable or the default installation path differs, install them in `C:\environment` or `C:\app`. Manage versions carefully. Delete temporary files after use, or keep them in `C:\code\tmp`.
