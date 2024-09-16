let senha = document.getElementById('inova_senha')
let conf_senha = document.getElementById('iconfirmar_senha')
function mostrar(){
    senha.type = senha.type == 'text' ? 'password' : 'text' 
}
function mostrar2(){
    conf_senha.type = conf_senha.type == 'text' ? 'password' : 'text' 
}

function cancelar(){
    location.href = `painel`
}

function validar(){
    if (senha.value === conf_senha.value){conf_senha.setCustomValidity('')} else {conf_senha.setCustomValidity('As senhas não são iguais')}
}