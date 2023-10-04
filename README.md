# bleu
Le grand bleu

## poetry configure: pyproject.toml
I added below contents to pyproject.toml
```
[tool.flake8]
import-order-style = "pycharm"
max-line-length = 120

[tool.isort]
profile = "django"
combine_as_imports = true
include_trailing_comma = true
line_length = 120

#[tool.mypy]
#plugins = ["mypy_django_plugin.main"]
#python_version = "3.11"
#strict = true
#ignore_missing_imports = true

#[[tool.mypy.overrides]]
#module = ["*.migrations.*", "manage"]
#ignore_errors = true

#[tool.django-stubs]
#django_version = "^4.2.5"
#django_apps = ["blog"]
#django_settings_module = "app.bleu.settings"
#ignore_missing_settings = true
#ignore_missing_model_attributes = true
```

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
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
  - repo: https://github.com/psf/black
    rev: 23.9.1
    hooks:
      - id: black
  - repo: https://github.com/PyCQA/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
        #args: ["--config", "pyproject.toml"]
  - repo: https://github.com/PyCQA/isort
    rev: 5.12.0
    hooks:
      - id: isort
  #- repo: local
  #  hooks:
  #    - id: mypy
  #      name: mypy
  #      entry: mypy
  #      language: python
  #      types: [python]
  #      #additional_dependencies: ["django-stubs", "django-environ"]
  #      args: ["--config-file", "pyproject.toml"]
```

## blog
### tables
```

          1:N                1:N
Author <---------> Post <---------> Category
                    |  \
                    |   \
               1:N  |    \ N:M
                    |     \
                    |      \
                 Comment   Tag

```
