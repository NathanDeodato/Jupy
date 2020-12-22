import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED


def winJupy():
    sg.theme("DarkGrey11")

    layout = [
        [sg.Text("Jupy$ - Óla! Me chamo Jupy. Fui criado com o objetivo de responder")],
        [sg.Text("ao usúario. Tenho respostas registradas em meu Banco de dados.")],
        [sg.Text("Jupy$ - Tenho informações limitadas, mas espero conseguir ajudar você")],

        [sg.Text("Pergunta$:", size=(9, 0)), sg.Input(size=(51, 0), key="pergunta")],
        [sg.Text("=" * 22), sg.Button("OK", size=(4, 0)), sg.Text("=" * 22)],

        [sg.Output(size=(60, 12))],
        [sg.Text(" " * 38), sg.Text("(C) NT Developer")]
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
