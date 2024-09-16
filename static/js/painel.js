let usuario = document.querySelector('div#usuario').textContent
function confirma(){
    resposta = confirm('Deseja realmente exluir sua conta?')
    if (resposta == true){
        alert(`Conta ${usuario} exlcuida com sucesso!`)
        window.location.href = `/${usuario}/delete`
    } else {
        window.location.href = `/${usuario}/painel`
    }
}

function alterar_dados(){
    window.location.href =  `/${usuario}/alterar_dados`
} 

function alterar_senha(){
    window.location.href =  `/${usuario}/alterar_senha`
}