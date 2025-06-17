
from zeep import Client
from zeep.exceptions import Fault
from django.conf import settings

class SoapServiceClient:
    def __init__(self):
        wsdl_url = settings.SOAP_CALCULADORA_WSDL
        self.client = Client(wsdl=wsdl_url)
        
    def soma(self, int_a: int, int_b: int) -> int:
        try:
            response = self.client.service.Add(intA=int_a, intB=int_b)
            return response
        except Fault as fault:
            raise Exception(f"SOAP Fault: {fault.message}")
        except Exception as e:
            raise Exception(f"Erro geral no SOAP: {str(e)}")
        
    def divisao(self, int_a: int, int_b: int) -> int:
        try:
            response = self.client.service.Divide(intA=int_a, intB=int_b)
            return response
        except Fault as fault:
            raise Exception(f"SOAP Fault: {fault.message}")
        except Exception as e:
            raise Exception(f"Erro geral no SOAP: {str(e)}")