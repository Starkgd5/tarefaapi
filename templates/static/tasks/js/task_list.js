document.addEventListener('DOMContentLoaded', function () {
    const tableBody = document.querySelector('#taskTable tbody');
  
    // Fazendo requisição à API
    fetch('http://127.0.0.1:8000/api/v1/tasks/')
      .then(response => response.json())
      .then(data => {
        // Preenchendo a tabela com os dados da API
        data.forEach((task, index) => {
          const row = `
            <tr>
              <th scope="row">${index + 1}</th>
              <td>${task.name}</td>
              <td>${task.status}</td>
              <td>${task.description}</td>
              <td>
                <a href="/user_edit/${task.id}" class="btn btn-primary">Editar</a>
                <a href="/user_delete/${task.id}" class="btn btn-danger">Excluir</a>
              </td>
            </tr>
          `;
          tableBody.innerHTML += row;
        });
      })
      .catch(error => {
        // Exibindo uma mensagem de erro se ocorrer um erro na requisiçõa
        alert('Erro ao obter dados da API: ' + error);
      });
  });