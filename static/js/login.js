function mostrar(){
    let senha = document.querySelector('input#isenha')
    senha.type = senha.type == "text" ? "password" : "text"
}