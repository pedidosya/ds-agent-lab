---
name: license-generator
description: Use this skill when the user explicitly asks to use the license-generator skill, or when the user asks to create, generate, add, or update an MIT LICENSE file for a repository.
---

# License Generator Skill

You are a licensing assistant specialized in generating standard MIT license files.

## When to use this skill

Use this skill when the user asks to:

- generate an MIT license
- create a LICENSE file
- add a license to the repository
- create a license for a company, person, or organization
- generate a license for a specific year

## Goal

Generate a valid MIT license and create a file named exactly `LICENSE` in the repository root.

## Inputs to identify

Extract the following information from the user's request:

1. `year`
   - Example: `2024`
   - If the user does not provide a year, use the current year.

2. `copyright_holder`
   - Example: `Acme Corp`
   - This can be a company, person, organization, or project owner.
   - If the user does not provide a copyright holder, ask for it.

## Required behavior

When generating the license:

1. Create or overwrite a file called `LICENSE` in the repository root.
2. The file MUST contain this exact line, replacing the values:

   ```text
   Copyright (c) <YEAR> <COPYRIGHT_HOLDER>
   ```

3. The license MUST follow the standard MIT License format.
4. Do not add extra commentary inside the `LICENSE` file.

## MIT License template

Use this exact template:

```text
MIT License

Copyright (c) <YEAR> <COPYRIGHT_HOLDER>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Example

User request:

```text
Genera una licencia MIT para la empresa 'Acme Corp' para el año 2024.
```

Expected action:

Create a file named `LICENSE` with this content:

```text
MIT License

Copyright (c) 2024 Acme Corp

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Final response

After creating the file, respond briefly.

Example:

```text
Done — created LICENSE for Acme Corp, year 2024.
```