from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import json


class MinhaTela(BoxLayout):
    def buscarNoJson(self):
        try:
            with open('dados.json', 'r') as arquivo:
                dados = json.load(arquivo)
        except:
            with open('dados.json', 'w') as arquivo:
                dados = {'lista_clientes': ['Maria, João, Graça']}
                json.dump(arquivo, dados)

        self.alterarTexto(dados)

    def alterarTexto(self, dados):
        self.ids.texto.text = str(dados['lista_clientes'])


class Test(App):
    def build(self):
        return MinhaTela()


Test().run()
