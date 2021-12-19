import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os


# cambio de nombre
name = 'eva'

#Flag
flag = 1

# ====================Convertidor de voz a texto=================

listener = sr.Recognizer()

engine = pyttsx3.init()

'''Esto funcionaba para elegir las voces peroahora solo tiene 1 en ingles'''
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# editing default configuration
engine. setProperty('rate', 178)
engine.setProperty('volume', 0.7)

'''---------coonvierte texto a voz---------'''
def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    flag = 1
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()

            # solo contesta si lo llamas por su nombre
            if name in rec:
                rec = rec.replace(name, '')
                flag = run(rec)
            else:
                talk("Creo que no te entiendo ")
    except:
        pass
    return flag

#--------------------------------------------RUN------------------------------------------
def run(rec):

    global flag
    '''##############################Arreglar Funcion de la hora########################'''
    if 'hora' in rec:
        hrs = datetime.datetime().now().strftime('%H:%M')
        talk("Son las " + hrs)

    elif 'hola' in rec:
        talk('Hola, buenos días')

    elif 'reproduce' in rec:
        search = rec.replace('reproduce', '')
        talk('Reproduciendo' + search)
        # reprouce la busqueda en youtube
        pywhatkit.playonyt(search)

    elif 'busca' in rec:
        order = rec.replace('busca', '')
        wikipedia.set_lang('es')
        info = wikipedia.summary(order, 1)
        talk(info)

    elif 'chiste' in rec:
        joke = pyjokes.get_joke('es')
        print(joke)
        talk(joke)

    elif 'apagar' in rec:
        os.system('shutdown /s /t 30')

    elif ('cancelar' in rec) and ('apagado' in rec):
        os.system('shutdown /a')

    elif 'abrir' in rec:
        program = rec.replace('abrir ', '')
        program = program.replace(' ', '')
        talk('abriendo' + program)
        direccion = "L:/Projects/VirtualAssistant/DirectAccess/"
        os.system(direccion + program + '.lnk')

    elif 'fondo' in rec:
        talk('Abriendo WallpaperEngine...')
        direccion = "L:/Projects/VirtualAssistant/DirectAccess/"
        os.system(direccion + 'fondos.url')

    elif 'chau' in rec:
        flag = 0
        talk("Adios Señor...")

    else:
        talk("Creo que no te entiendo")

    return flag

while flag:
    flag = listen()

# ---------------------------------------------------------------
