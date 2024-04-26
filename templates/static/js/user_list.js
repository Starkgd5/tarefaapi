document.addEventListener('DOMContentLoaded', function () {
  const tableBody = document.querySelector('#userTable tbody');

  // Fazendo requisição à API
  fetch('http://192.168.1.7/api/v1/users/')
    .then(response => response.json())
    .then(data => {
      // Preenchendo a tabela com os dados da API
      data.forEach((user, index) => {
        const row = `
          <tr>
            <th scope="row">${index + 1}</th>
            <td>${user.name}</td>
            <td>${user.email}</td>
            <td>
              <button class="btn btn-primary">Editar</button>
              <button class="btn btn-danger">Excluir</button>
            </td>
          </tr>
        `;
        tableBody.innerHTML += row;
      });
    })
    .catch(error => {
      console.error('Erro ao obter dados da API:', error);
    });
});