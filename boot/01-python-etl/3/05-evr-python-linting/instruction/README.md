# Code linting 

## Concept 

Linting is the automated checking of your source code for programmatic and stylistic errors. This is done by using a lint tool (otherwise known as linter).

We are going to be using [PyLint](https://pylint.pycqa.org/en/latest/) to perform linting on our code. 

## Implement 

1. Change directory in your terminal: 
```
cd 3-ins-python-integration-test/solved/src
```

2. Run pylint on `etl` module and take note of the output: 

```
pylint weather/etl
```

- Note: the output indicates changes that will need to be fixed to meet pylints standards. However, notice that a lot of output from pylint relates to python conventions, and are therefore not an issue with the code. 
- Task: Try fixing one or two pylint warnings and re-run pylint to see if it is fixed.

3. Run pylint on `etl` module with `refactor (R)` and `convention (C)` checks disabled:

```
pylint --disable=R,C weather/etl
```

- Note: Notice that the output now is a lot less and focuses on major issues rather than code convention. 