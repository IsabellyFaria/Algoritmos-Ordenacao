const inputFile = document.getElementById("file");
const caixaArquivo = document.getElementById("arquivo-enviado");
const botaoRemover = caixaArquivo.querySelector("button");
const formulario = document.getElementById("formulario")

// começa escondido
caixaArquivo.style.display = "none";

inputFile.addEventListener("change", function () {
    if (this.files && this.files.length > 0) {
        const nome = this.files[0].name;

        const spanNome = caixaArquivo.querySelector("span");
        spanNome.textContent = nome;

        caixaArquivo.style.display = "block";
    }
});

// remover arquivo
botaoRemover.addEventListener("click", function (e) {
    e.preventDefault();

    // limpa o input
    inputFile.value = "";

    // esconde a caixa
    caixaArquivo.style.display = "none";
});

formulario.addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData();
    formData.append('ordenacao', $('#ordenacoes').val());
    formData.append('indice', $('#indice-input').val());

    console.log("Ordenação:", $('#ordenacoes').val());
    console.log("Índice:", $('#indice-input').val());
    console.log("Arquivo:", $('#file')[0].files[0]);
    console.log(this.action);

    if ($('#file')[0].files.length > 0) formData.append('arquivo', $('#file')[0].files[0]);
    else { alert("Escolha um arquivo"); return }

    $.ajax({
        url: this.action,
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function (response) {
            if (response.status){
                window.open(response.path, "_blank");
            }
            else{
                alert("Deu ruim");
            }
        },
        error: function (xhr, status, error) {
            alert("Erro no servidor");
            console.log(xhr.status);
            console.log(xhr.responseText);
            console.log(status);
            console.log(error);
        }
    });
});
