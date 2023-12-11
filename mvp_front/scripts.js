
  /*
    --------------------------------------------------------------------------------------
    Função para colocar um item na lista do servidor via requisição POST
    --------------------------------------------------------------------------------------
  */
  const postItem = async (inputCPF, inputAge, inputSex, inputCp, inputTrestbp, inputChol, inputFbs, inputRestecg, 
    inputThalach, inputExang, inputOldpeak, inputSlope) => {
    const formData = new FormData();
    formData.append('cpf', inputCPF);
    formData.append('age', inputAge);
    formData.append('sex', inputSex);
    formData.append('cp', inputCp);
    formData.append('trestbp', inputTrestbp);
    formData.append('chol', inputChol);
    formData.append('fbs', inputFbs);
    formData.append('restecg', inputRestecg);
    formData.append('thalach', inputThalach);
    formData.append('exang', inputExang);
    formData.append('oldpeak', inputOldpeak);
    formData.append('slope', inputSlope);
    console.log(inputCPF, inputAge, inputSex, inputCp, inputTrestbp, 
      inputChol, inputFbs, inputRestecg, inputThalach,
      inputExang, inputOldpeak, inputSlope)
    let url = 'http://127.0.0.1:5000/paciente';
    fetch(url, {
      method: 'post',
      body: formData
    })
    .then((response) => {
      console.log("response: ",response.json());
      console.log("status:",response.ok);
      if (response.ok) {
        alert("Paciente enviado com sucesso!");
        /*
        getItem();
        */
      }
      else {
        alert("Erro: item não adicionado");
      }
    })
    .catch((error) => {
      console.error('Error:', error);        
    });
  }
  
/* Função para chamar dados de um paciente via requisição GET
      --------------------------------------------------------------------------------------
*/
const getItem = (item) => {
  console.log(item)
  let url = 'http://127.0.0.1:5000/paciente?cpf=' + item;
  fetch(url, {
    method: 'get'
  })
  .then(response => response.json())
  .then(data => {
    let inputResposta = document.getElementById("Resposta");
    inputResposta.value = data.target; 
  })
  .catch((error) => {
    console.error('Error:', error);
  });
}



  
  /*
    --------------------------------------------------------------------------------------
    Função para adicionar um novo aparelho 
    --------------------------------------------------------------------------------------
  */
  const newItem = () => {
    document.getElementById("Resposta").innerHTML = "Carregando"
    let inputCPF = document.getElementById("CPF").value;
    let inputAge = document.getElementById("Age").value;
    let inputSex = document.getElementById("Sex").value;
    let inputCp = document.getElementById("Pain").value;
    let inputTrestbp = document.getElementById("Pressure").value;
    let inputChol = document.getElementById("Cholesterol").value;
    let inputFbs = document.getElementById("Sugar").value;
    let inputRestecg = document.getElementById("ECG").value;
    let inputThalach = document.getElementById("heart").value;
    let inputExang = document.getElementById("angina").value;
    let inputOldpeak = document.getElementById("stLow").value;
    let inputSlope = document.getElementById("stPeak").value;
            
    let camposObrigatorios = [
      inputCPF, inputAge, inputSex, inputCp, inputTrestbp, 
      inputChol, inputFbs, inputRestecg, inputThalach,
      inputExang, inputOldpeak, inputSlope
    ];
    let error = false;
    
    for (let i = 0; i < camposObrigatorios.length; i++) {
      let campoObrigatorio = camposObrigatorios[i]
      if (campoObrigatorio === '') {
        error = true;
      } else {
        
      }
    } 
    if (error) {
      alert("Erro: campos obrigatórios não preenchidos");
    } else {
      console.log("teste")
      postItem(
        inputCPF, inputAge, inputSex, inputCp, inputTrestbp, 
        inputChol, inputFbs, inputRestecg, inputThalach,
        inputExang, inputOldpeak, inputSlope
      )
      let target = getItem(inputCPF)
      if (target === 0){
        answer = "Não tem problema cardíaco";
      } else {
        answer = "Tem problema cardíaco";
      }
      document.getElementById("Resposta").innerHTML = answer;
    }    
  }
  
  