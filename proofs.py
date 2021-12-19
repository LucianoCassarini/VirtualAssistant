'''Permite ejecutar cualquier comando de consola'''
import os


'''==========================Abrir un programa=========================='''
#rec de ejemplo
rec = 'abrir steam'
program = rec.replace('abrir ', '')
print(program)

#dirección será igual al directorio donde esté la carpeta DirectAccess
direccion = "L:/Projects/VirtualAssistant/DirectAccess/"
os.system(direccion + program + '.lnk')

'''===========================Apagar PC==========================='''
#---------------------Basic Shutdown Comands-----------------------
#Apagar PC
    #shutdown /s
#apaga en 20 seguntos
    #shutdown /s /t 20
#Cancela apagado
    #shutdown /a
#rec de ejemplo
print("La PC se apagará en 30 segundos")
os.system('shutdown /s /t 30')
print('cancelando apagado programado')
os.system('shutdown /a')

'''=====================Cambiar Fondo de Pantalla=================='''
direccion = "L:/Projects/VirtualAssistant/DirectAccess/"
os.system(direccion+'fondos.url')

