document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('#editUserForm');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Evita que o formulário seja enviado normalmente

        const userId = form.querySelector('input[name="user_id"]').value;
        const username = form.querySelector('#username').value;
        const email = form.querySelector('#email').value;
        const isStaff = form.querySelector('#is_staff').checked;

        // Enviar os dados para a API de edição de usuário (usar fetch ou outra biblioteca para enviar a requisição AJAX)
        // Exemplo de como enviar uma requisição usando fetch:
        fetch(`http://127.0.0.1:8000/api/v1/users/${userId}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                // Adicione quaisquer cabeçalhos de autenticação necessários aqui
            },
            body: JSON.stringify({ username: username, email: email, is_staff: isStaff })
        })
        .then(response => {
            if (response.ok) {
                alert('Usuário editado com sucesso!');
                // Redirecionar para a página de detalhes do usuário, por exemplo
                window.location.href = 'http://127.0.0.1:8000/user_list/';
            } else {
                // Você pode exibir uma mensagem de erro para o usuário, se desejar
                alert('Erro ao editar usúario: ' + response.statusText);
            }
        })
        .catch(error => {
            // Você pode exibir uma mensagem de erro para o usuário, se desejar
            alert('Erro ao editar usuário:' + error);
        });
    });
});
