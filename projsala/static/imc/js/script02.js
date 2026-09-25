const carregarMensagem=()=>{
    const section_mensagem=document.getElementById("requisicao_imc");
    const url_mensagem=section_mensagem.dataset.url;
    fetch(url_mensagem).then(response=>response.json()).then(data=>{
        const paragrafo=document.getElementById("mensagem");
        paragrafo.innerText= data.mensagem;
    })
}