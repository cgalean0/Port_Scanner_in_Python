#Importamos libreria socket para manejar tema redes.
import socket;
from colorama import Fore, Style, Back;

#Pedimos ip a escanear al usuario.
ip = input(Fore.LIGHTBLUE_EX + Style.BRIGHT + "Introduzca la ip a escanear: ");

#Creamos un ciclo que busque conectarse a cada puerto existente.

for puerto in range(1, 65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        #A este sock que especifica que vamos a scanear ipv4 con protocolo tcp le añadimos un timer.
    sock.settimeout(3);
        #En una variable vamos a guardar el valor del puerto al cual logramos conectarnos.
    result = sock.connect_ex((ip, puerto));
        #Ahora comparamos que pasará cuando encuentre un puerto abierto.
    if result == 0:
        print(Fore.GREEN + "Puerto abierto: " + str(puerto));
        sock.close();
    else:
        print(Fore.RED + "Puerto cerrado: " + str(puerto));
        sock.close();