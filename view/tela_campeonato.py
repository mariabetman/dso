import PySimpleGUI as psg


class TelaCampeonato:
    def __init__(self, controlador_campeonatos):
        self.__controlador_campeonatos = controlador_campeonatos

    def mostra_mensagem(self, msg):
        psg.popup(msg)
