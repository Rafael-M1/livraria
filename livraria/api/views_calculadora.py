from http.client import HTTPException
import httpx
from ninja import Router, Schema
from .soap_client import SoapServiceClient

router = Router()
soap_client = SoapServiceClient()

@router.get("/soma")
def soma(request, a: int, b: int):
    try:
        resultado = soap_client.soma(a, b)
        return {"resultado": resultado}
    except Exception as e:
        return {"error": str(e)}
    
@router.get("/divisao")
def soma(request, a: int, b: int):
    try:
        resultado = soap_client.divisao(a, b)
        return {"resultado": resultado}
    except Exception as e:
        return {"error": str(e)}