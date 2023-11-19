# bleu
Le grand bleu

## Branchies
- take-one
  - By using Django's GenericView with Templates for the blog app
- take-two
  - TBD

## pre-commit
You should use the virtualenv, then activate it to execute below commands.
```
$ poetry add pre-commit
$ pre-commit install --install-hooks -t pre-commit -t prepare-commit-msg -t commit-msg -t pre-push
```

### .pre-commit-config.yaml
```
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files
- repo: local
  hooks:
    - id: ruff
      name: ruff
      entry: ruff
      language: python
      types: [python]
```

### pyptoject.toml
```
[tool.ruff]
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".git-rewrite",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".pytype",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "venv",
]

line-length = 88
indent-width = 4

[tool.ruff.lint]
#select = ["E4", "E7", "E9", "F"]
ignore = []
fixable = ["ALL"]
unfixable = []
dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"
```
