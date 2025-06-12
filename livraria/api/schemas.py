from ninja import Schema

class LivroSchema(Schema):
    id: int
    titulo: str
    autor: str
    ano_publicacao: int

class LivroIn(Schema):
    titulo: str
    autor: str
    ano_publicacao: int
