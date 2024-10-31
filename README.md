
---

# Hashzap 🚀💬

**Hashzap** é um aplicativo de chat desenvolvido em Python com a biblioteca [Flet](https://flet.dev/). Ele permite a interação em tempo real, sendo ideal para aprender sobre construção de interfaces dinâmicas e comunicação em tempo real.

## Recursos ✨

- **Interface Simples e Intuitiva** 🎨: Inclui uma tela inicial com botão para iniciar o chat e um popup para entrada do nome do usuário.
- **Chat em Tempo Real** 💬: As mensagens enviadas são distribuídas em tempo real para todos os participantes conectados.
- **Popup de Login** 👤: Um modal de boas-vindas solicita o nome do usuário antes de iniciar a conversa.
- **UI com Flet** 📱: Utiliza a biblioteca Flet para uma construção de UI amigável e responsiva com Python.

## Pré-requisitos 🛠️

Para rodar o projeto, você precisa de:

- **Python** instalado no sistema.
- A biblioteca **Flet** instalada. Você pode instalar pelo comando:
  ```bash
  pip install flet
  ```

## Como Usar 🚀

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/Emerson10110/Hashzap.git
   ```
2. **Entre na pasta do projeto**:
   ```bash
   cd Hashzap
   ```
3. **Execute o Script**:
   ```bash
   python hashzap.py
   ```

## Funcionamento 🖥️

1. **Tela Inicial**: Exibe o título "Hashzap" e um botão "Iniciar chat".
2. **Popup de Boas-Vindas**: Ao clicar em "Iniciar chat", um popup solicita o nome do usuário.
3. **Entrando no Chat**: Após o login, o usuário entra no chat, onde:
   - **O título e o botão inicial desaparecem.**
   - **O chat carrega com um campo para digitar e enviar mensagens.**
   - **As mensagens são atualizadas em tempo real para todos os usuários conectados.**

## Estrutura do Código 📂

O código principal consiste em:

- **`main`**: Função principal que configura e executa a interface.
- **Funções de Mensagens**: Envio e recebimento de mensagens em tempo real.
- **Popup de Login**: Popup inicial para entrada do nome do usuário.
- **Chat**: Área principal de chat e campo de entrada de mensagens.

## Contribuições 🤝

Sinta-se à vontade para abrir issues e pull requests para melhorias! 

---
