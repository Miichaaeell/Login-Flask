function confirma(){
    resposta = confirm('Deseja realmente exluir sua conta?')
    if (resposta == true){
        alert(`Conta exlcuida com sucesso!`)
        window.location.href = `delete`
    } else {
        window.location.href = `painel`
    }
}

function alterar_dados(){
    window.location.href =  `alterar_dados`
} 

function alterar_senha(){
    window.location.href =  `alterar_senha`
}