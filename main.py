import pyttsx3
from tkinter import *


#configurando app
app = Tk()
app.title('Texto para fala')
app.configure(height=300, width=400, bg='#262933')


#configurando voz
repro = pyttsx3.init()
repro.setProperty('voice', 'pt+m7')

rate = repro.getProperty('rate')
repro.setProperty('rate', rate-50)

#função para reproduzir voz
def voz(resposta):
    repro.say(resposta)
    repro.runAndWait()

#definindo caixa de texto
text = Text(app, height=5, width=53)
text.place(x = 75, y =100 , width = 250, height = 80)



#text = str(input('Digite o texto: '))
#voz(text)
app.mainloop()