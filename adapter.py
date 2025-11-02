class ElementDB:
    def __init__(self, data):
        self.data = data

    def get_elements(self):
        return [{"name": row[0], "complexity_id": row[1]} for row in self.data]

class ElementAdapter:
    def __init__(self, element_db):
        self.element_db = element_db

    def list_names(self):
        elements = self.element_db.get_elements()
        return [el["name"] for el in elements]
