$ErrorActionPreference = "Stop"
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install pylint bandit flake8

# Capture baseline reports for the assigned original file.
.\.venv\Scripts\python.exe -m pylint scholarship_disbursement_original.py *> before_reports\pylint_report.txt
.\.venv\Scripts\python.exe -m bandit -r scholarship_disbursement_original.py *> before_reports\bandit_report.txt
.\.venv\Scripts\python.exe -m flake8 scholarship_disbursement_original.py *> before_reports\flake8_report.txt

# Capture reports for the cleaned version.
.\.venv\Scripts\python.exe -m pylint scholarship_disbursement.py *> after_reports\pylint_report.txt
.\.venv\Scripts\python.exe -m bandit -r scholarship_disbursement.py *> after_reports\bandit_report.txt
.\.venv\Scripts\python.exe -m flake8 scholarship_disbursement.py *> after_reports\flake8_report.txt

# Run the program after analysis to verify its behaviour.
.\.venv\Scripts\python.exe scholarship_disbursement.py
Write-Host "Reports saved in before_reports\ and after_reports\. Review the final Pylint score and Bandit findings."
