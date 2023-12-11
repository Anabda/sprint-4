from flask_openapi3 import OpenAPI, Info, Tag
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
from flask import redirect

from model import Session, Paciente, modelo
from schemas import *

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)


# tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
paciente_tag = Tag(name="Paciente", description="Cria pacientes na base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/paciente', tags=[paciente_tag],
          responses={"200": PacienteViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_paciente(form: PacienteSchema):
    """Adiciona um novo Paciente à base de dados com a previsão de se tem ou não problema cardíaco
    """
    paciente = Paciente(
        cpf = form.cpf,
        age = form.age,
        sex = form.sex,
        cp = form.cp,
        trestbp = form.trestbp,
        chol = form.chol,
        fbs = form.fbs,
        restecg = form.restecg,
        thalach = form.thalach,
        exang = form.exang,
        oldpeak = form.oldpeak,
        slope = form.slope,
        )
    model=modelo.Model.carrega_modelo('ml_model/doenca_cardiaca.pkl')
    target=modelo.Model.preditor(model,paciente)
    print("target: ", target)
    paciente.atualiza_target(target)
    
    try:           
        session = Session()
        session.add(paciente)
        session.commit()
        print("Inseri!")
        return apresenta_paciente(paciente), 200

    except IntegrityError as e:
        error_msg = "Não foi possível cadastrar o paciente, pois já existe um paciente com esse cpf"
        print("erro: cpf já cadastrado")
        return {"message": error_msg}, 409

    except Exception as e:
        error_msg = "Erro inesperado, o paciente inserido não foi cadastrado"
        print("erro inesperado!")
        return {"message": error_msg}, 400

def atualiza_target(paciente,target):
    paciente.atualiza_target(target)

@app.get('/paciente', tags=[paciente_tag],
            responses={"200": PacienteViewSchema, "404": ErrorSchema})
def get_paciente(query: PacienteBuscaSchema):
    """Encontra um Paciente a partir do nome informado

    Retorna o paciente.
    """
    cpf = query.cpf
    session = Session()
    paciente = session.query(Paciente).filter(Paciente.cpf == cpf).first()
    if paciente:
        return apresenta_paciente(paciente), 200
    error_msg = "Paciente não encontrado"
    return {"mesage": error_msg}, 404