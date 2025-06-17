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
def divisao(request, a: int, b: int):
    try:
        resultado = soap_client.divide(a, b)
        return {"resultado": resultado}
    except Exception as e:
        return {"error": str(e)}
    
@router.get("/subtracao")
def subtracao(request, a: int, b: int):
    try:
        resultado = soap_client.subtrai(a, b)
        return {"resultado": resultado}
    except Exception as e:
        return {"error": str(e)}
    
@router.get("/multiplicacao")
def multiplica(request, a: int, b: int):
    try:
        return {"resultado": soap_client.multiplica(a, b)}
    except Exception as e:
        return {"error": str(e)}