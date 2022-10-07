# Команды для запуска тестов

- **issue-1**: ```python -m doctest -v -o IGNORE_EXCEPTION_DETAIL issue1.py > result_issue1.txt```
- **issue-2.py**: ```python -m pytest -v issue2.py > result_issue2.txt```  
- **issue-3.py**: ```python issue3.py```
- **issue-4.py**: ```python -m pytest -v issue4.py > result_issue4.txt```
- **issue-5.py**: ```python -m pytest -v issue5.py --cov=what_is_year_now --cov-report html > result_issue5.txt```