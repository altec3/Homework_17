from project.setup.inits.db_init import db


class DBTools:

    def insert_data(self, table, data: list[dict]) -> bool:
        try:
            with db.session.begin():
                for item in data:
                    db.session.add(
                        table(
                            **item
                        )
                    )
        except Exception:
            return False
        else:
            return True

    def extract_data(self, table):
        return db.session.query(table).all()

    def get_item_by_id(self, table, item_id: int):
        return db.session.query(table).get(item_id)

    def delete_row(self, table, rid: int) -> bool:
        try:
            with db.session.begin():
                db.session.query(table).filter(table.id == rid).delete()
        except Exception:
            return False
        else:
            return True
