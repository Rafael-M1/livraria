
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
            raise Exception(f"Erro no método Add: {str(e)}")
        
    def divide(self, int_a: int, int_b: int) -> int:
        try:
            return self.client.service.Divide(intA=int_a, intB=int_b)
        except Fault as fault:
            raise Exception(f"SOAP Fault: {fault.message}")
        except Exception as e:
            raise Exception(f"Erro no método Divide: {str(e)}")
        
    def subtrai(self, int_a: int, int_b: int) -> int:
        try:
            return self.client.service.Subtract(intA=int_a, intB=int_b)
        except Fault as fault:
            raise Exception(f"SOAP Fault: {fault.message}")
        except Exception as e:
            raise Exception(f"Erro no método Subtract: {str(e)}")

    def multiplica(self, int_a: int, int_b: int) -> int:
        try:
            return self.client.service.Multiply(intA=int_a, intB=int_b)
        except Fault as fault:
            raise Exception(f"SOAP Fault: {fault.message}")
        except Exception as e:
            raise Exception(f"Erro no método Multiply: {str(e)}")