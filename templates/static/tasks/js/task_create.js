document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('#createTaskForm');
    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Evita que o formulário seja enviado normalmente

        // Coletando os dados do formulário
        const name = document.querySelector('#name').value;
        const description = document.querySelector('#description').value;
        const userId = document.querySelector('#user_id').value;

        // Enviando os dados para a API
        fetch('http://127.0.0.1:8000/api/v1/tasks/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name: name, description: description, user: userId })
        })
        .then(response => {
            if (response.ok) {
                alert('Tarefa criada com sucesso!');
                // Você pode redirecionar o usuário para outra página após o sucesso, se desejar
                window.location.href = 'http://127.0.0.1:8000/task_list/';
            } else {
                // Extraindo informações adicionais da resposta em caso de erro
                response.json().then(data => {
                    const errorMessage = data.message || response.statusText;
                    alert('Erro ao criar tarefa: ' + errorMessage);
                }).catch(error => {
                    alert('Erro ao criar tarefa: ' + response.statusText);
                });
            }
        })
        .catch(error => {
            // Tratamento de exceção para erros de rede
            alert('Erro ao criar tarefa: ' + error.message);
        });
    });
});
