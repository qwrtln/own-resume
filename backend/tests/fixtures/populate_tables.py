import sqlite3
from collections import namedtuple

from tests.fixtures.test_resume import test_resume

Basics = namedtuple("Basics", ["name", "summary", "email"])
Work = namedtuple("Work", ["company", "position", "summary"])


if __name__ == "__main__":
    import sys

    basics = Basics(**test_resume["basics"])
    work = [Work(**w) for w in test_resume["work"]]

    db_file = sys.argv[1] if sys.argv[1] else "test_data.db"
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    basics_placeholder = f"({','.join(['?'] * len(basics))})"
    work_placeholder = f"({','.join(['?'] * len(work[0]))})"

    cursor.execute(f"INSERT INTO basics VALUES {basics_placeholder}", basics)
    cursor.executemany(f"INSERT INTO work VALUES {work_placeholder}", work)

    connection.commit()
    connection.close()
