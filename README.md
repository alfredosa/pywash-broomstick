# pywash-broomstick

This action runs isort and mypy on your code, and fails if the commands fail.

inputs incldue 

isort-version
sort-paths
configuration
requirements-files
profile (For isort)
mypy-path
mypy-flags

## Example usage

```YAML
on: [push]

jobs:
  pywash-broomstick:
    runs-on: ubuntu-latest
    name: Pywash CI/CD
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Run Pywash Broomstick
        id: CI
        uses: alfredosa/pywash-broomstick@main
        with:
          isort-version: latest
          sort-paths: .
          configuration: --check-only --diff
          requirements-files: ./requirements.txt
          profile: black
          mypy-path: .
```
