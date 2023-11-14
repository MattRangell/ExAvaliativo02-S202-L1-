from database import Database

class TeacherCRUD:
    def __init__(self):
        self.db = Database()
    
    def create(self, name, ano_nasc, cpf):
        query = f"CREATE(:Teacher{{name: '{name}', ano_nasc: {ano_nasc}, cpf: '{cpf}'}});"
        self.db.run(query)
    
    def read(self, name):
        query = f"MATCH (t:Teacher{{name:'{name}'}}) RETURN t;"
        result = self.db.run(query)
        return result.single()
    
    def delete(self, name):
        query = f"MATCH (t:Teacher{{name:'{name}'}}) DELETE t;"
        self.db.run(query)
    
    def update(self, name, newCpf):
        query = f"MATCH (t:Teacher{{name:'{name}'}}) SET t.cpf = '{newCpf}';"
        self.db.run(query)
        
teacher_crud = TeacherCRUD()
teacher_crud.create('Chris Lima', 1956, '189.052.396-66')

teacher = teacher_crud.read('Chris Lima')
print(teacher)

teacher_crud.update('Chris Lima', '162.052.777-77')

teacher_crud.delete('Chris Lima')