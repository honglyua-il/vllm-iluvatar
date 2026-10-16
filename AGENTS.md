# License and copyright

Preserving upstream license and copyright notices takes priority when adding,
moving, adapting, or reviewing code in this repository.

For independently authored company code, use this header (with the language's
comment syntax and after any required shebang/encoding declaration):

```python
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright (c) 2026 Shanghai Iluvatar CoreX Semiconductor Co., Ltd.
```

For code copied or adapted from an open-source project:

- Preserve the original applicable license, copyright, attribution, source
  references, and required license text. Never replace them with only the
  company's header or relicense copied code merely by changing its SPDX tag.
- Restore missing original notices from the actual upstream source. Follow the
  source chain, including third-party code carried by an intermediate project.
- Keep a prominent notice that the file was changed, and record its upstream
  path and version/commit. Company contributions may carry an additional company
  copyright notice alongside the original notices.
- Apply these rules to copied functions/classes, renamed or moved code,
  installation patches, monkey patches, and upstream source embedded as strings
  for fingerprinting or tests. Packaging code as a plugin does not erase its
  provenance.
- Carry the applicable third-party license texts with source and binary
  distributions. See `THIRD_PARTY_NOTICES.md` and the component license files.

Do not classify a file as independently authored just because it is new in Git,
uses an `Ilu` name, or has no match against one upstream version. When provenance
is unresolved, retain existing notices and record the unresolved source rather
than guessing ownership. Interface-only bindings and independent wrappers need
content-based review; they are not automatically copies of upstream code.
