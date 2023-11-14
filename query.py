from py2neo import Graph

##Questão 01

class Database:
    def __init__(self):
        self.graph = Graph("e5f97f8e.databases.neo4j.io:7687", auth=("neo4j", "L6LaUIq2owcrImSJsoEtPN9qOhFpbkSXwlI-aD6kPDY"))

    def query1(self):
        query = "MATCH (t:Teacher{name:'Renzo'}) RETURN t.ano_nasc, t.cpf"
        result = self.graph.run(query).data()
        return result

    def query2(self):
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.cpf"
        result = self.graph.run(query).data()
        return result

    def query3(self):
        query = "MATCH (c:City) RETURN c.name"
        result = self.graph.run(query).data()
        return result

    def query4(self):
        query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number"
        result = self.graph.run(query).data()
        return result


db = Database()
print(db.query1())
print(db.query2())
print(db.query3())
print(db.query4())

##Questão 02


def query01(self): 
    query = "MATCH (t:Teacher) RETURN MIN(t.ano_nasc) AS youngest, MAX(t.ano_nasc) AS oldest" 
    result = self.graph.run(query).data()[0] 
    return result

def query02(self): 
    query = "MATCH (c:City) RETURN AVG(c.population) AS average" 
    result = self.graph.run(query).data()[0] 
    return result

def query03(self): 
    query = "MATCH (c:City{cep:'37540-000'}) RETURN REPLACE(c.name, 'a', 'A') AS modified_name" 
    result = self.graph.run(query).data()[0] 
    return result

def query04(self): 
    query = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 3, 1) AS character" 
    result = self.graph.run(query).data() 
    return result

db = Database() 
print(db.query01()) 
print(db.query02()) 
print(db.query03()) 
print(db.query04())

