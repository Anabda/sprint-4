import numpy as np
import pickle

class Model():
    
    def carrega_modelo(path):
        """
        Carrega o modelo realizado no colab
        """
        if path.endswith('.pkl'):
            model = pickle.load(open(path,'rb'))
            return model
        else:
            raise Exception('Formato de arquivo não suportado')
        return
    
    def preditor(model,form):
        """
        Realiza a predição se é um paciente que está com problema cardíaco ou não
        """
        X_input = np.array([form.age,
                            form.sex,
                            form.cp,
                            form.trestbp,
                            form.chol,
                            form.fbs,
                            form.restecg,
                            form.thalach,
                            form.exang,
                            form.oldpeak,
                            form.slope,
                            ])
        
        X_input=X_input.reshape(1,-1)
        rescaled_X_input = model.scaler.transform(X_input)

        diagnosis = model.predict(rescaled_X_input)
        return int(diagnosis[0])
