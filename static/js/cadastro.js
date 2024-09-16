let senha =  document.getElementById('isenha')
let conf_senha = document.getElementById('iconfirmpass')

// mostrar ou esconder a senha no formulário
function mostrar(){
    senha.type = senha.type == 'text' ? 'password' : 'text'
}
function mostrar1(){
    conf_senha.type = conf_senha.type == 'text' ? 'password' : 'text'
}

// validar senhas iguais antes de enviar formulário
function confirmar_senha(){
    if (senha.value === conf_senha.value){conf_senha.setCustomValidity('')} else {conf_senha.setCustomValidity('As senhas não são iguais')}

}
