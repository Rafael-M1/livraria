from ninja import NinjaAPI
from .schemas import LivroSchema, LivroIn
from .models import Livro
from .views_autores import router as autores_router

api = NinjaAPI()

@api.get("/livros", response=list[LivroSchema])
def listar_livros(request):
    return Livro.objects.all()

@api.post("/livros", response=LivroSchema)
def criar_livro(request, data: LivroIn):
    livro = Livro.objects.create(**data.dict())
    return livro

# As novas rotas de outro arquivo foram adicionadas
api.add_router("/autores", autores_router)