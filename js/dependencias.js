document.addEventListener("DOMContentLoaded", function () {
    fetchDependencias();

    document.getElementById('dependenciaFormElement').addEventListener('submit', function (event) {
        event.preventDefault();
        saveDependencia();
    });
});

function fetchDependencias() {
    fetch('http://localhost:8000/dependencias')
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro ao buscar dependências: ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            console.log('Dados recebidos:', data); // Adicione esta linha para depuração
            const list = document.getElementById('dependenciasList');
            list.innerHTML = '<ul class="list-group border border-danger">';
            
            if (Array.isArray(data.dependencias)) {
                data.dependencias.forEach(dependencia => {
                    list.innerHTML += `
                        <li class="list-group-item m-2 p-2 border-bottom">
                            <div class="row d-flex justify-content-between">
                                <div class="col"> <strong>${dependencia.nome}</strong></div>
                                <div class="col"> <button class="btn btn-info btn-sm float-end ms-2" onclick="showEditForm(${dependencia.id}, '${dependencia.nome}', ${dependencia.tarifa})">Editar</button></div>
                                <div class="col"> <button class="btn btn-danger btn-sm float-end" onclick="deleteDependencia(${dependencia.id})">Deletar</button></div>
                            </div>
                        </li>`;
                });
            } else {
                list.innerHTML += '<li class="list-group-item">Nenhuma dependência encontrada</li>';
            }

            list.innerHTML += '</ul>';
        })
        .catch(error => console.error('Erro ao buscar dependências:', error));
}

function showAddForm() {
    document.getElementById('dependenciaForm').classList.remove('d-none');
    document.getElementById('dependenciaId').value = '';
    document.getElementById('nome').value = '';
    document.getElementById('tarifa').value = '';
    document.getElementById('formTitle').innerText = 'Adicionar Dependência';
}

function showEditForm(id, nome, tarifa) {
    document.getElementById('dependenciaForm').classList.remove('d-none');
    document.getElementById('dependenciaId').value = id;
    document.getElementById('nome').value = nome;
    document.getElementById('tarifa').value = tarifa;
    document.getElementById('formTitle').innerText = 'Editar Dependência';
}

function saveDependencia() {
    const id = document.getElementById('dependenciaId').value;
    const nome = document.getElementById('nome').value;
    const tarifa = parseFloat(document.getElementById('tarifa').value);
    const method = id ? 'PATCH' : 'POST';
    const url = id ? `http://localhost:8000/dependencias/${id}` : 'http://localhost:8000/dependencias';

    console.log(`Método: ${method}, URL: ${url}, Dados: ${JSON.stringify({ nome: nome, tarifa: tarifa })}`);

    fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nome: nome, tarifa: tarifa })
    })
    .then(response => response.json())
    .then(() => {
        fetchDependencias();
        document.getElementById('dependenciaForm').classList.add('d-none');
    })
    .catch(error => console.error('Erro ao salvar dependência:', error));
}

function deleteDependencia(id) {
    fetch(`http://localhost:8000/dependencias/${id}`, {
        method: 'DELETE'
    })
    .then(() => fetchDependencias())
    .catch(error => console.error('Erro ao deletar dependência:', error));
}
