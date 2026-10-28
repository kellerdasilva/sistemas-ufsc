
const campoCep = document.getElementById("cep");

async function buscarCEP(valorCampoCep) {
    const resultado = await fetch(`https://viacep.com.br/ws/${valorCampoCep}/json/`);

    return await resultado.json();
}

campoCep.addEventListener("input", funcaoEvento);

async function funcaoEvento(evento) {
    const cep = evento.target.value;

    if (cep.length == 8) {
        console.log(cep);

        const retornoCep = await buscarCEP(cep);
        console.log(retornoCep);

        const campoLogradouro = document.getElementById("logradouro");
        campoLogradouro.value = retornoCep.logradouro;

        const campoBairro = document.getElementById("bairro");
        campoBairro.value = retornoCep.bairro;

        const campoCidade = document.getElementById("cidade");
        campoCidade.value = retornoCep.localidade;

        const campoEstado = document.getElementById("estado");
        campoEstado.value = retornoCep.uf;
    }
}
