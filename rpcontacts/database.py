import pathlib
import sqlite3

DATABASE_PATH = pathlib.Path().home() / "rpcontacts_sqlite.db"

class Database:
    def __init__(self, db_path=DATABASE_PATH):
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()
        self._create_table()

    def _create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS contacts(
                id INTEGER PRIMARY KEY,
                name TEXT,
                phone TEXT,
                email TEXT
            );
        """
        self._run_query(query)

    def _run_query(self, query, *query_args):
        result = self.cursor.execute(query, [*query_args])
        self.db.commit()
        return result

    def _add_contact(self, contact):
        insert_query = "insert into contacts values (NULL, ?,?,?);"
        result = self._run_query(insert_query, *contact)

    def _get_all_contacts(self):
        result = self._run_query("select * from contacts")
        return result.fetchall()

    def _get_last_contact(self):
        result = self._run_query(
            "select * from contacts order by id desc limit 1;"
        )
        return result.fetchone()

    def _delete_contact(self, contact_id):
        result = self._run_query("delete from contacts where id = ?", contact_id)
        print(f"deleted: {}", result.fetchone())



