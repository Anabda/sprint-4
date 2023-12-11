from model import avaliador, carregador, modelo
import pandas as pd

# Instanciando as Classes
carregador = carregador.Carregador()
avaliador = avaliador.Avaliador()

# Método para testar modelo cart a partir do arquivo correspondente
def test_modelo_cart():
    # Parâmetros
    url_dados = "../Doencas_coracao.csv"
    
    '''
    colunas = [
        "age",
        "sex",
        "cp",
        "trestbps",
        "chol",
        "fbs",
        "restecg",
        "thalach",
        "exang",
        "oldpeak",
        "slope",
        "target"
    ]
    '''

    # Carga dos dados
    dataset=pd.read_csv(url_dados, delimiter=',')

    # Remove as linhas com valores NaN
    dataset = dataset.dropna()

    # Separando os dados
    array=dataset.values
    X = array[:,0:11]
    Y = array[:,11]

    print("Valores de entrada X:")
    print(X)

    print("\nValores de saída Y:")
    print(Y)
    
    # Importando modelo de cart
    modelo_path = "ml_model/doenca_cardiaca.pkl"
    modelo_cart=modelo.Model.carrega_modelo(modelo_path)

    # Obtendo as métricas do cart
    acuracia_cart, recall_cart, precisao_cart, f1_cart = avaliador.avaliar(modelo_cart, X, Y)

    # Testando as métricas do cart
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_cart >= 0.6
    assert recall_cart >= 0.5
    assert precisao_cart >= 0.5
    assert f1_cart >= 0.5
