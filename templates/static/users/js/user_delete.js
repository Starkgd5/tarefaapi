document.addEventListener('DOMContentLoaded', function () {
    const deleteUserForm = document.querySelector('#deleteUserForm');
    const deleteUserBtn = document.querySelector('#deleteUserBtn');

    deleteUserBtn.addEventListener('click', function () {
        const userId = deleteUserForm.querySelector('input[name="user_id"]').value;

        if (confirm('Tem certeza de que deseja excluir este usuário?')) {
            fetch(`/api/v1/users/${userId}/`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    // Adicione quaisquer cabeçalhos de autenticação necessários aqui
                }
            })
            .then(response => {
                if (response.ok) {
                    console.log('Usuário excluído com sucesso!');
                    // Redirecionar para a página de lista de usuários, por exemplo
                } else {
                    console.error('Erro ao excluir usuário:', response.statusText);
                    // Exibir uma mensagem de erro para o usuário, se necessário
                }
            })
            .catch(error => {
                console.error('Erro ao excluir usuário:', error);
                // Exibir uma mensagem de erro para o usuário, se necessário
            });
        }
    });
});
