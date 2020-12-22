import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED


def winJupy():
    sg.theme("DarkGrey11")

    layout = [
        [sg.Text("Jupy$ - ")],
        [sg.Text("Pergunta", size=(9, 0)), sg.Input(size=(30, 0), key="pergunta")],
        [sg.Text(" " * 60), sg.Button("OK", size=(4, 0))],

        [sg.Output(size=(60, 10))]
    ]
    return sg.Window("Jupy$", layout=layout)


window = winJupy()

while True:
    event, values = window.Read()

    # Close window
    if event == sg.WIN_CLOSED:
        break

    


