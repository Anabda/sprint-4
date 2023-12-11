from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

class Paciente(Base):
    __tablename__ = 'paciente'

    cpf = Column("CPF", Integer, primary_key=True)
    age = Column(Integer)
    sex = Column(Integer)
    cp = Column(Integer)
    trestbp = Column(Integer)
    chol = Column(Integer)
    fbs = Column(Integer)
    restecg = Column(Integer)
    thalach = Column(Integer)
    exang = Column(Integer)
    oldpeak = Column(Float)
    slope = Column(Integer)
    target = Column(Integer)

    def __init__(self, cpf: int, age:int, sex: int, cp:int, trestbp:int, chol:int, fbs:int, 
                 restecg:int, thalach:int, exang:int, oldpeak:float, slope:int):
        """
        Cria um novo paciente
        
        Arguments:
            cpf: CPF do paciente (somente números)
            age: Idade do paciente 
            sex: Sexo do paciente (0: Mulher, 1: Homem)
            cp: Tipo de dor no peito
            trestbp: Pressão em repouso (mmHg)
            chol: colesterol mg/dl
            fbs: nível de açúcar no sangue maior do que 120 (1: sim; 0: não)
            restecg: eletrocardiograma (0: normal, 1: possui anormalidade ST-T, 2: hipertrofia do ventrículo esquerdo)
            thalach: batimento cardíaco máximo (bpm)
            exang: Possui angina? (1: Sim, 0: Não)
            oldpeak: depressão ST
            slope: pico de ST durante exercício (1: aumentando, 2: constante, 3: diminuindo)
            target: possui problema cardíaco (1: Sim, 0: Não)
        """
        self.cpf = cpf
        self.age = age
        self.sex = sex
        self.cp = cp
        self.trestbp = trestbp
        self.chol = chol
        self.fbs = fbs
        self.restecg = restecg
        self.thalach = thalach
        self.exang = exang
        self.oldpeak = oldpeak
        self.slope = slope
    
    def atualiza_target(self, target):
        self.target=target