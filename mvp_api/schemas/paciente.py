from pydantic import BaseModel
from typing import Optional, List
from model.paciente import Paciente
from datetime import datetime


class PacienteSchema(BaseModel):
    """ Define como um novo paciente a ser inserido deve ser representado
    """ 
    cpf: int
    age:int
    sex: int
    cp:int
    trestbp:int
    chol:int
    fbs:int
    restecg:int
    thalach:int
    exang:int
    oldpeak:float
    slope:int
        
class PacienteBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no cpf do paciente.
    """
    cpf: int = 11111111111

def apresenta_paciente(paciente: Paciente):
    """ Retorna uma representação do paciente.
    """
    return {
        "cpf": paciente.cpf,
        "age": paciente.age,
        "sex": paciente.sex,
        "cp": paciente.cp,
        "trestbp": paciente.trestbp,
        "chol": paciente.chol,
        "fbs": paciente.fbs,
        "restecg": paciente.restecg,
        "thalach": paciente.thalach,
        "exang": paciente.exang,
        "oldpeak": paciente.oldpeak,
        "slope": paciente.slope,
        "target": paciente.target
    }

class PacienteViewSchema(BaseModel):
    """ Define como um paciente será retornado.
    """
    cpf: int = 11111111111
    age:int = 50
    sex: int = 1
    cp:int = 4
    trestbp:int = 140
    chol:int = 200
    fbs:int = 1
    restecg:int = 2
    thalach:int = 150
    exang:int = 1
    oldpeak:float = 1.5
    slope:int = 3
    target: Optional[int] = 1