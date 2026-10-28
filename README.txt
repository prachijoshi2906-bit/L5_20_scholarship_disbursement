LAB 5 — STATIC CODE ANALYSIS: SCHOLARSHIP DISBURSEMENT
Student: Prachi Ganesh Joshi
SRN: PES1UG24CS325
Section: F

Included:
- scholarship_disbursement_original.py: original code from the assigned repository, for baseline analysis
- scholarship_disbursement.py: revised implementation
- issues.md: issue table documenting findings and fixes
- run_analysis.ps1: Windows PowerShell script to install tools and generate before/after reports
- run_analysis.sh: Linux/macOS equivalent
- before_reports/ and after_reports/: destination folders for generated reports

Reflection questions are intentionally omitted, as requested.

HOW TO RUN ON WINDOWS (VS CODE TERMINAL / POWERSHELL)
1. Extract this folder.
2. Open a terminal in this folder.
3. Run: Set-ExecutionPolicy -Scope Process Bypass
4. Run: .\run_analysis.ps1
5. Review before_reports and after_reports. The script requires internet access to install Pylint, Bandit and Flake8.

HOW TO RUN THE PROGRAM ONLY
python scholarship_disbursement.py

IMPORTANT
The static-analysis tools could not be installed in the preparation environment because package-index network access was unavailable. Therefore, the report files are generated when you run the script locally; no fabricated report output or score is included. Verify that the final Pylint score is above 9.5 and that Bandit/Flake8 findings are resolved before submission.

SUGGESTED THREE COMMITS (run from your cloned assignment repository after copying in the final files):
1. git add scholarship_disbursement.py && git commit -m "Fix scholarship ledger security issues"
2. git add issues.md && git commit -m "Document static analysis findings and fixes"
3. git add before_reports after_reports && git commit -m "Add before and after static analysis reports"

Do not commit the reflection.md file because you requested to skip reflection questions.
