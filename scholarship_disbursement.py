"""Maintain a simple in-memory scholarship disbursement ledger."""

import sqlite3
from typing import Optional


class ScholarshipLedger:
    """Store scholarship awards and track successful disbursements."""

    def __init__(self) -> None:
        """Create an in-memory database for the demonstration."""
        self.connection = sqlite3.connect(":memory:")
        self.connection.execute(
            """
            CREATE TABLE awards (
                id INTEGER PRIMARY KEY,
                student TEXT NOT NULL,
                scheme TEXT NOT NULL,
                amount INTEGER NOT NULL CHECK (amount >= 0),
                disbursed INTEGER NOT NULL DEFAULT 0
            )
            """
        )
        self.disbursed_total = 0

    def grant(self, student: str, scheme: str, amount: int) -> int:
        """Create an award safely and return its database ID."""
        if not student.strip():
            raise ValueError("Student name must not be empty.")
        if not scheme.strip():
            raise ValueError("Scholarship scheme must not be empty.")
        if amount < 0:
            raise ValueError("Scholarship amount cannot be negative.")

        cursor = self.connection.execute(
            "INSERT INTO awards (student, scheme, amount, disbursed) "
            "VALUES (?, ?, ?, 0)",
            (student, scheme, amount),
        )
        self.connection.commit()
        return int(cursor.lastrowid)

    def disburse(self, award_id: int) -> Optional[int]:
        """Disburse an award once; return its amount or None if unavailable."""
        row = self.connection.execute(
            "SELECT amount, disbursed FROM awards WHERE id = ?",
            (award_id,),
        ).fetchone()
        if row is None or row[1]:
            return None

        amount = int(row[0])
        self.connection.execute(
            "UPDATE awards SET disbursed = 1 WHERE id = ?",
            (award_id,),
        )
        self.connection.commit()
        self.disbursed_total += amount
        return amount

    def archive(self) -> None:
        """Report that archive step reached without invoking a shell."""
        print("Archiving awards...")

    def by_scheme_count(self, scheme: Optional[str]) -> int:
        """Return the number of awards for a scheme."""
        if scheme is None:
            return 0
        result = self.connection.execute(
            "SELECT COUNT(*) FROM awards WHERE scheme = ?",
            (scheme,),
        ).fetchone()
        return int(result[0]) if result else 0


def main() -> None:
    """Run a small demonstration of the scholarship ledger."""
    ledger = ScholarshipLedger()
    first_award = ledger.grant("Ishaan", "Merit", 50000)
    ledger.grant("Divya", "Need-based", 75000)

    print(ledger.disburse(first_award), ledger.disburse(9))
    print(ledger.by_scheme_count("Merit"), ledger.disbursed_total)
    ledger.archive()


if __name__ == "__main__":
    main()
