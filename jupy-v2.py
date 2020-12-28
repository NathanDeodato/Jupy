import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED


def winJupy():
    sg.theme("DarkGrey11")

    layout = [
        [sg.Text("Jupy$ - Óla! Me chamo Jupy. Fui criado com o objetivo de responder")],
        [sg.Text("ao usúario. Tenho respostas registradas em meu Banco de dados.")],
        [sg.Text("Jupy$ - Tenho informações limitadas, mas espero conseguir ajudar você")],

        [sg.Text("_" * 68)],

        [sg.Text(" " * 46), sg.Text("-- OPÇÕES --")],
        [sg.Radio("Comando Jupy", group_id="opc"), sg.Radio("Hardware", group_id="opc"), sg.Radio("Linguagem de Programção", group_id="opc"), sg.Radio("Console", group_id="opc")],
        
        [sg.Text("_" * 68)],

        [sg.Text("Pergunta$:", size=(10, 0)), sg.Input(size=(46, 0), key="pergunta"), sg.Button("Send", size=(5, 0))],

        [sg.Output(size=(66, 12))],
        [sg.Text(" " * 45), sg.Text("(C) NT Developer")]
    ]
    return sg.Window("Jupy$-v2", layout=layout)


window = winJupy()

while True:
    event, values = window.Read()

    # Close window
    if event == sg.WIN_CLOSED:
        break

    # Pergunta
    perg = str(values["pergunta"])

    if event == "OK":
        pass
