const ufSelect = document.getElementById('uf');

async function buscarUFs() {
    const resposta = await fetch('https://servicodados.ibge.gov.br/api/v1/localidades/estados?orderBy=nome', {
        method: "GET",
    });

    const ufs = await resposta.json();
    ufs.forEach(uf => {
        console.log(uf.nome);

        const option = document.createElement("option");
        option.value = uf.sigla;
        option.textContent = uf.nome;

        ufSelect.appendChild(option);
    });
}

buscarUFs();



ufSelect.addEventListener("change", evento => {
    console.log(evento);

    console.log(ufSelect.value);
});