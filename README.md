# bleu
Le grand bleu

## flake8
I added a flake8 configure file
```
[flake8]
import-order-style=pycharm
max-line-length = 100
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
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files
-   repo: https://github.com/PyCQA/flake8
    rev: 6.1.0
    hooks:
    -   id: flake8
-   repo: https://github.com/psf/black
    rev: 23.9.1
    hooks:
    -   id: black
```
