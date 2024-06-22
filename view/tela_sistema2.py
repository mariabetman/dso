import PySimpleGUI as psg
psg.set_options(font=('Arial Bold', 16))
layout = [
   [psg.Text('Nome ', size=(15,1)),psg.Input(expand_x=True, key='nome')],
   [psg.Text('CPF ', size=(15,1)), psg.Input(expand_x=True, key='cpf')],
   [psg.Text('Data de Nascimento ', size=(15,1)), psg.Input(expand_x=True, key='data_nascimento')],
   [psg.OK(), psg.Cancel()]
]
window = psg.Window('Form', layout, size=(715,207))
event, values = window.read()
print(values)
window.close()