document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('#createUserForm');
    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Evita que o formulário seja enviado normalmente

        // Coletando os dados do formulário
        const userName = document.querySelector('#username').value;
        const email = document.querySelector('#email').value;
        const isStaff = document.querySelector('#is_staff').checked;

        // Enviando os dados para a API
        fetch('http://127.0.0.1:8000/api/v1/users/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username: userName, email: email, is_staff: isStaff })
        })
        .then(response => {
            if (response.ok) {
                alert('Usuário criado com sucesso! ');
                // Você pode redirecionar o usuário para outra página após o sucesso, se desejar
                window.location.href = 'http://127.0.0.1:8000/user_list/';
            } else {
                // Você pode exibir uma mensagem de erro para o usuário, se desejar
                alert('Erro ao criar usúario: ' + response.statusText);
            }
        })
        .catch(error => {
            console.error('Erro ao criar usuário:', error);
            // Você pode exibir uma mensagem de erro para o usuário, se desejar
            alert('Erro ao criar usuário:' + error);
        });
    });
});
