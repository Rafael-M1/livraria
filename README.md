# Atividade 1 - Configuração inicial do projeto, ambiente virtual

Comandos usados:
Criar ambiente virtual:
- python -m venv venv

Inicializar o ambiente virtual:
- venv\Scripts\activate

Para instalar o django e django ninja:
- pip install django django-ninja

Criar projeto Django:
- django-admin startproject livraria
- cd livraria

Criar um app chamado 'api':
- python manage.py startapp api

Registrar o app 'api' criado no arquivo settings.py:
```python
INSTALLED_APPS = [
    ...,
    'api',
]
```
# Atividade 2 - Criar endpoint para retornar dados de livros e para salvar dados de livros

Configurar Django Ninja, criando as seguintes rotas no arquivo api/views.py:
```python
# api/views.py

from ninja import NinjaAPI
from .schemas import LivroSchema, LivroIn
from .models import Livro

api = NinjaAPI()

@api.get("/livros", response=list[LivroSchema])
def listar_livros(request):
    return Livro.objects.all()

@api.post("/livros", response=LivroSchema)
def criar_livro(request, data: LivroIn):
    livro = Livro.objects.create(**data.dict())
    return livro
```

Criar modelo para entidade Livro:
```python
# api/models.py

from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano_publicacao = models.IntegerField()

    def __str__(self):
        return self.titulo
```

Criar schema para entidade Livro:
```python
# api/schemas.py

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
```

Adicionar rota do Ninja no urls.py
```python
# livraria/urls.py

from django.contrib import admin
from django.urls import path
from api.views import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
```

Fazer migração no banco de dados na nova entidade:
```
python manage.py makemigrations
python manage.py migrate
```

Para inicializar/start o servidor:
```
python manage.py runserver
```

# Atividade 3 - Criar endpoint para consumir dados de uma API externa

Instalar o módulo httpx para fazer requisições HTTP:
```
pip install httpx
```

Adicionar novas rotas no arquivo views.py:
```python
# api/views.py
from .views_autores import router as autores_router
...

api.add_router("/autores", autores_router)
```

Criar o novo arquivo de views com o nome de views_autores.py:
```python
# api/views_autores.py

from http.client import HTTPException
import httpx
from ninja import Router
from ninja.schema import Schema

router = Router()

class AutorSchema(Schema):
    nome: str
    nome_completo: str | None = None
    nascimento: str | None = None
    biografia: str | None = None
    site_oficial: str | None = None

@router.get("/jk-rowling", response=AutorSchema)
def get_jk_rowling(request):
    url = "https://openlibrary.org/authors/OL23919A.json"
    try:
        response = httpx.get(url, timeout=10.0)
        response.raise_for_status()
        data = response.json()

        return AutorSchema(
            nome=data.get("name"),
            nome_completo=data.get("fuller_name"),
            nascimento=data.get("birth_date"),
            biografia=data.get("bio") if isinstance(data.get("bio"), str) else data.get("bio", {}).get("value"),
            site_oficial=(data.get("links", [{}])[0].get("url") if data.get("links") else None),
        )
    except httpx.HTTPError:
        raise HTTPException(500, "Erro ao buscar autor")

```

# Atividade 4 - Atualizar arquivo requirements.txt
Sempre que adicionar ou remover dependências, é necessário atualizar o requirements.txt por meio do comando:
```
pip freeze > requirements.txt
```

Quando for instalar o projeto usar o comando a seguir para instalar todas dependências:
```
pip install -r requirements.txt
```