from sqlite3 import DatabaseError
from unicodedata import name


class Worker:
    name: str
    age: int
    organization: str
    position: str
    language: str

    def __init__(self, name, age, organization, position, language):
        self.name = name
        self.age = age
        self.organization = organization
        self.position = position
        self.language = language

DATA = [
    Worker('Facundo', 72, 'Platzi', 'Technical Coach', 'python'),
    Worker('Luisana', 33, 'Globant', 'UX Designer', 'javascript'),
    Worker('Héctor', 19, 'Platzi', 'Associate', 'ruby'),
    Worker('Gabriel', 20, 'Platzi', 'Associate', 'javascript'),
    Worker('Isabella', 30, 'Platzi', 'QA Manager', 'java'),
    Worker('Lorena', 56, 'Platzi', 'Python Organization', 'python')
]

def run():
    python_workers = [w.name for w in DATA if w.language == 'python']
    platzi_workers = list(filter(lambda w: w.organization != 'Platzi', DATA))
    platzi_workers = list(map(lambda w: w.name, platzi_workers))
    print(platzi_workers)
    


if __name__ == '__main__':
    run()