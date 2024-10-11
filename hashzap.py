# Tela inicial:
    # Titulo: hashzap
    # Botao: iniciar chat
        # Quando clicar no botao:
        # Abrir um poup/modal/alerta
            # Titulo: bem vindo ao Hashzap
            # Caixa de texto: escreva seu nome no chat
            # Botão: entrar no chat
                # Quando clicar no botão
                # Sumir com o titulo
                # Sumir com botão inciar chat
                    # Carregar chat
                    # Carregar o caompo de enviar mensegem: "Digite sua mensagem"
                    # Botão enviar
                        # Enviar mensegem
                        # Limpar a caixa de mensagem

# importar o flet
import flet as ft

# criar uma função principal para rodar o seu app
def main(pagina):
    # Titulo
    titulo = ft.Text("Hashzap")
    pagina.add(titulo)

    # Botao inicial
    botao = ft.ElevatedButton("Iniciar chat")
    pagina.add(botao)


# execultar essa função com flet
ft.app(main)
                        