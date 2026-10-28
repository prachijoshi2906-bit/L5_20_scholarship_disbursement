#!/usr/bin/env bash
set -euo pipefail
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pylint bandit flake8

pylint scholarship_disbursement_original.py > before_reports/pylint_report.txt 2>&1 || true
bandit -r scholarship_disbursement_original.py > before_reports/bandit_report.txt 2>&1 || true
flake8 scholarship_disbursement_original.py > before_reports/flake8_report.txt 2>&1 || true

pylint scholarship_disbursement.py > after_reports/pylint_report.txt 2>&1 || true
bandit -r scholarship_disbursement.py > after_reports/bandit_report.txt 2>&1 || true
flake8 scholarship_disbursement.py > after_reports/flake8_report.txt 2>&1 || true

python scholarship_disbursement.py
printf 'Reports saved in before_reports/ and after_reports/. Review final Pylint score and Bandit findings.\n'
