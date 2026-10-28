# Lab 5 — Static Code Analysis Issue Table

**Student:** Prachi Ganesh Joshi  
**SRN:** PES1UG24CS325  
**Section:** F  
**Source:** `scholarship_disbursement.py` from the assigned repository

| Issue | Type | Original line(s) | Description | Fix approach |
|---|---|---:|---|---|
| SQL injection / unsafe query construction | Security (Bandit / code review) | 9 | Student and scheme values were interpolated directly into an SQL string using `%`, so crafted input could alter the query. | Use SQLite parameter placeholders (`?`) and pass values separately. |
| Mutable default argument | Bug / maintainability (Pylint) | 8 | `audit=[]` creates one list shared by calls that omit the argument. | Removed the mutable default; the current interface does not need a persistent audit list. |
| Shell command invocation | Security (Bandit) | 24 | `os.system()` launches a shell for a message that does not require shell execution. | Removed the shell call and use a direct Python `print()` instead. |
| Broad exception swallowed | Reliability (Pylint) | 23–26 | `except Exception: pass` hides failures and makes the archive step appear successful even if it fails. | Removed the unnecessary try/except and shell operation. |
| Global mutable state | Design / maintainability (Pylint) | 5, 14, 18 | A module-level counter and `global` make the disbursement total harder to reason about and test. | Encapsulated the database connection and total in `ScholarshipLedger`. |
| Missing-award handling and repeat disbursement | Logic / reliability | 16–19 | A missing award returned implicitly, and repeated calls could count the same award more than once. | Return `None` for missing/already-disbursed awards and update the total only on the first successful disbursement. |
| Non-PEP 8 function naming | Style (Flake8 / Pylint) | 28 | `bySchemeCount` uses mixed-case naming for a function. | Renamed it to `by_scheme_count`. |
| `== None` comparison | Style / correctness | 29 | Comparing with `None` using equality is not the recommended Python idiom. | Use `is None` through an explicit `None` check. |
| Missing input validation | Reliability | 8–10 | Empty student/scheme names and negative award amounts were accepted. | Validate inputs and reject invalid values with `ValueError`; add a database constraint for non-negative amounts. |

## Verification checklist

- [ ] Run the original and updated scripts.
- [ ] Generate before/after Pylint, Bandit, and Flake8 reports using `run_analysis.ps1` or `run_analysis.sh`.
- [ ] Confirm Bandit reports no findings in the updated script.
- [ ] Confirm Flake8 reports no style violations in the updated script.
- [ ] Confirm the final Pylint score is above 9.5; if it is not, review the generated report and adjust accordingly.
