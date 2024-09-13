# Project Install Instructions

## install

1. clone 
2. pip install -r requirements.txt

## Testing 

1. pytest
2. pytest --pylint
3. pytest --pylin --cov


Ex of pytest --pylint --cov 
(venv) kerim@Kerim:~/Is601/hw2$ pytest --pylint --cov
====================== test session starts =======================
platform linux -- Python 3.10.12, pytest-8.0.0, pluggy-1.4.0 -- /home/kerim/Is601/hw2/venv/bin/python
cachedir: .pytest_cache
rootdir: /home/kerim/Is601/hw2
configfile: pytest.ini
testpaths: tests
plugins: cov-4.1.0, pylint-0.21.0
collected 4 items                                                

tests/__init__.py::PYLINT SKIPPED (file(s) previously ...) [ 25%]
tests/test_calculator.py::PYLINT SKIPPED (file(s) prev...) [ 50%]
tests/test_calculator.py::test_addition PASSED             [ 75%]
tests/test_calculator.py::test_subtraction PASSED          [100%]

---------- coverage: platform linux, python 3.10.12-final-0 ----------
Name                       Stmts   Miss  Cover
----------------------------------------------
calculator/__init__.py         4      0   100%
tests/__init__.py              0      0   100%
tests/test_calculator.py       5      0   100%
----------------------------------------------
TOTAL                          9      0   100%


================== 2 passed, 2 skipped in 0.03s ==================
(venv) kerim@Kerim:~/Is601/hw2$ 