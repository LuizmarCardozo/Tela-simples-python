from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Dark purple')
layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar login?')],
    [sg.Button('Login')],
]

# Window
window = sg.Window('Minha primeira tela', layout)

# Events
while True:
    eventos, valores = window.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Login':
        if valores['usuario'] == 'user' and valores['senha'] == '12345':
            print('Sucesso ao entrar!')
