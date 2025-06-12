from http.client import HTTPException
import httpx
from ninja import Router, Schema

class AutorSchema(Schema):
    nome: str
    nome_completo: str | None = None
    nascimento: str | None = None
    biografia: str | None = None
    site_oficial: str | None = None

router = Router()

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
