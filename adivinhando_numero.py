import sys,os
from random import randint
plat = sys.platform
try:
    import PySimpleGUI as sg
except:
    if plat == 'win32':
        os.system('pip install pysimplegui')
        import PySimpleGUI as sg
    elif plat == 'linux':
        os.system('pip3 install pysimplegui')
        import PySimpleGUI as sg
aleatorio = randint(0,100)

class telapython:
  def __init__(self):
    sg.change_look_and_feel('DarkTeal7')
    layout = [
      [sg.Text('Chute um numero de 0 a 100',size=(12,0)),sg.Input(size=(10,10),key='numero')],
      [sg.Button('enviar')],
      [sg.Output(size=(30,10))]
      
    ]
    self.janela = sg.Window('Dados do usuario').layout(layout)

  def iniciar(self):
    while True:
      self.Button, self.values = self.janela.Read()
      num = int(self.values['numero'])
      if aleatorio == num:
          print('Parabens, voce acertou!!')         
      else:
          if num > aleatorio:
              print()
              print('Chute um numero menor')
          else:
              print()
              print('Chute um valor maior')

tela = telapython()
tela.iniciar()
