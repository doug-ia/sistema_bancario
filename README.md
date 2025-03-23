<h1>Projeto: 🏦💸 Sistema Bancário Simples</h1>

<h2> 📃 Descrição</h2>

Este é um projeto simples de um sistema bancário desenvolvido em Python. Ele permite realizar operações de depósito, saque, resetar limite de saques e visualizar o extrato bancário. O projeto foi criado com o intuito de praticar conceitos básicos de Python, como variáveis globais, listas, controle de fluxo e tratamento de exceções.

<h2>📋 Funcionalidades</h2>

<ul>
  <li>Realizar depósitos com validação de valores positivos.</li>

  <li>Realizar saques com as seguintes restrições:</li>
  
    Máximo de 3 saques diários.

    Limite de R$ 500,00 por saque.

    Saque não pode exceder o saldo disponível.
  

  <li>Resetar o limite de saques diários.</li>

  <li>Visualizar o extrato bancário contendo depósitos e saques realizados.</li>
</ul>

<h2>🚫 Regras de Negócio</h2>

<ul>
  <li>Apenas valores positivos podem ser depositados.</li>
  
  <li>O limite diário de saques é de 3 vezes.</li>
  
  <li>O valor máximo de saque permitido é de R$ 500,00.</li>
  
  <li>Caso o saldo seja insuficiente, o saque será negado.</li>
</ul>

<h2>✏️ Estrutura do Projeto</h2>

<ul> O projeto é composto por um único arquivo Python contendo todas as funções necessárias:</ul>

    1. realizar_deposito(): Função responsável por realizar depósitos.

    2. realizar_saque(): Função responsável por realizar saques seguindo as regras de negócio.

    3. resetar_limite_saques(): Função para redefinir o limite de saques diários.

    4. realizar_extrato(): Função para exibir o extrato bancário.

    5. Estrutura de repetição para exibir o menu de opções.


<h2>▶️ Como Executar</h2>

<ul>
  <li>Certifique-se de ter o Python instalado em seu computador.</li>
  
  <li>Faça o download ou clone este repositório.</li>
  
  <li>Abra o terminal no diretório do projeto.</li>

  <li>Execute o script com o comando:</li>

    python nome_do_arquivo.py

</ul>


<h2>👨‍💻 Exemplo de Uso</h2>

---------- Menu -----------

1 - Para realizar DEPÓSITO

2 - Para realizar SAQUE

3 - Para resetar limite de saques

4 - Para Visualizar o EXTRATO

5 - Para sair

    Escolha uma opção:


<h2>📝 Melhorias Futuras</h2>

<ul>
  <li>Implementação de autenticação de usuário.</li>
  
  <li>Persistência de dados em arquivos ou banco de dados.</li>
  
  <li>Interface gráfica para melhorar a experiência do usuário.</li>
</ul>

<h2>🤖 Tecnologias Utilizadas</h2>

<ul>
  <li>Python 3.x</li>
</ul>

<h2>🫂 Contribuições</h2>
Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork deste repositório e propor melhorias.
