document.addEventListener("DOMContentLoaded", function () {
    fetchTipos();

    document.getElementById('tipoFormElement').addEventListener('submit', function (event) {
        event.preventDefault();
        saveTipo();
    });
});

const baseUrl = 'http://localhost:8000/tipos'; // Ajuste a URL conforme necessário

function fetchTipos() {
    fetch(baseUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro ao buscar tipos: ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            const list = document.getElementById('tiposList');
            list.innerHTML = '<ul class="list-group border border-danger">';
            if (Array.isArray(data.tipos)) {
                data.tipos.forEach(tipo => {
                    list.innerHTML += `
                        <li class="list-group-item m-2 p-2 border-bottom">
                            <div class="row d-flex justify-content-between">
                                <div class="col"> <strong>${tipo.nome}</strong> - ${tipo.descricao}</div>
                                <div class="col"> <button class="btn btn-info btn-sm float-end ms-2" onclick="showEditForm(${tipo.id}, '${tipo.nome}', '${tipo.descricao}')">Editar</button></div>
                                <div class="col"> <button class="btn btn-danger btn-sm float-end" onclick="deleteTipo(${tipo.id})">Deletar</button></div>
                            </div>
                        </li>`;
                });
            } else {
                list.innerHTML += '<li class="list-group-item">Nenhum tipo encontrado</li>';
            }
            list.innerHTML += '</ul>';
        })
        .catch(error => console.error('Erro ao buscar tipos:', error));
}

function showAddForm() {
    document.getElementById('tipoForm').classList.remove('d-none');
    document.getElementById('tipoId').value = '';
    document.getElementById('nome').value = '';
    document.getElementById('descricao').value = '';
    document.getElementById('formTitle').innerText = 'Adicionar Tipo de Dispositivo';
}

function showEditForm(id, nome, descricao) {
    document.getElementById('tipoForm').classList.remove('d-none');
    document.getElementById('tipoId').value = id;
    document.getElementById('nome').value = nome;
    document.getElementById('descricao').value = descricao;
    document.getElementById('formTitle').innerText = 'Editar Tipo de Dispositivo';
}

function saveTipo() {
    const id = document.getElementById('tipoId').value;
    const nome = document.getElementById('nome').value;
    const descricao = document.getElementById('descricao').value;
    const method = id ? 'PATCH' : 'POST';
    const url = id ? `${baseUrl}/${id}` : baseUrl;

    fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nome: nome, descricao: descricao })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(data => {
                console.error('Erro:', data);
                throw new Error(data.detail || 'Erro desconhecido ao salvar o tipo');
            });
        }
        return response.json();
    })
    .then(() => {
        fetchTipos();
        document.getElementById('tipoForm').classList.add('d-none');
    })
    .catch(error => {
        console.error('Erro ao salvar tipo:', error);
    });
}

function deleteTipo(id) {
    if (!confirm('Tem certeza que deseja deletar este tipo de dispositivo?')) {
        return;
    }

    fetch(`${baseUrl}/${id}`, {
        method: 'DELETE'
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro ao deletar tipo: ' + response.statusText);
        }
        fetchTipos();
    })
    .catch(error => console.error('Erro ao deletar tipo:', error));
}
