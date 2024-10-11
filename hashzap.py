# Tela inicial:
    # Titulo: hashzap
    # Botao: iniciar chat
        # Quando clicar no botao:
        # Abrir um poup/modal/alerta
            # Titulo: bem vindo ao Hashzap
            # Caixa de texto: escreva seu nome no chat
            # Botão: entrar no chat
                # Quando clicar no botão
                # fechar popup
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

    def enviar_mensagem(evento):
        texto = ft.Text(campo_enviar_mensagem.value)
        chat.controls.append(texto)
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem")
    botao_enviar = ft.ElevatedButton("enviar", on_click=enviar_mensagem)


    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

    chat = ft.Column()


    def entrar_chat(evento):
        # Fechar popup
        popup.open = False
        # sumir com titulo
        pagina.remove(titulo)
        # sumir com botão iniciar chat
        pagina.remove(botao)
        # carregar chat
        pagina.add(chat)
        # carregar o campo de enviar mensagem
        # carregar o botao enviar
        pagina.add(linha_enviar)
        pagina.update()

    # Criar o popup
    titulo_popup = ft.Text("Bem-vindo ao Hashzap")
    caixa_nome = ft.TextField(label="Digite seu nome")
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)

    popup = ft.AlertDialog(title = titulo_popup, content = caixa_nome,
                            actions = [botao_popup])

    # Botao inicial
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao = ft.ElevatedButton("Iniciar chat", on_click=abrir_popup)

    # colocar os elementos da pagina
    pagina.add(titulo)
    pagina.add(botao)
    
# execultar essa função com flet
ft.app(main)
                        