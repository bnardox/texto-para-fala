import pyttsx3



repro = pyttsx3.init()

repro.setProperty('voice', 'pt+m7')

rate = repro.getProperty('rate')
repro.setProperty('rate', rate-50)

def voz(resposta):
    repro.say(resposta)
    repro.runAndWait()

text = str(input('Digite o texto: '))

voz(text)