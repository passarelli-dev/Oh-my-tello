# Librerie 
import socket
import threading
import time

# Ogni istanza di tello ha un proprio IP, per comodita lasciamo la porta del socket di default
telloUno = ('192.168.1.100', 8889)
telloDue = ('192.168.1.101', 8889)

# IP e porta del socket locale
indirizzoLocaleUno = ('', 9010)
indirizzoLocaleDue = ('', 9011)

# Crea socket UDP tra il PC e Tello
socketTelloUno = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketTelloDue = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Crea socket UDP tra Tello e il PC
socketTelloUno.bind(indirizzoLocaleUno)
socketTelloDue.bind(indirizzoLocaleDue)

def send(message, delay):
  # Prova ad inviare il messaggio, altrimenti stampa l'eccezione
  try:
    socketTelloUno.sendto(message.encode(), telloUno)
    socketTelloDue.sendto(message.encode(), telloDue)
    print("Invio Messaggio: " + message)
  except Exception as e:
    print("Errore nel mandare: " + str(e))

  # Stop di un tot di secondi
  time.sleep(delay)

# Receive the message from Tello
def receive():
  # Continuously loop and listen for incoming messages
  while True:
    # Try to receive the message otherwise print the exception
    try:
      risposta1, ip_address = socketTelloUno.recvfrom(128)
      risposta2, ip_address = socketTelloDue.recvfrom(128)
      print("Ricevuto response da TELLO #1: " + risposta1.decode(encoding='utf-8'))
      print("Ricevuto response da Tello #2: " + risposta2.decode(encoding='utf-8'))
    except Exception as e:
      # If there's an error close the socket and break out of the loop
      socketTelloUno.close()
      socketTelloDue.close()
      print("Errore Ricevuto: " + str(e))
      break

# Crea e avvia un thread per ricevere i messaggi in background
# Utilizza la funzione receive come target del thread
threadRicezione = threading.Thread(target=receive)
threadRicezione.daemon = True
threadRicezione.start()

# Distanza tra i lati del quadrato
distanza_lati_quadrato = 100

# Angolo di rotazione
angolo_rotazione = 90

# Direzione di rotazione (cw = in senso orario, ccw = in senso antiorario)
direzione_rotazione = "cw"

# Metti tello in modalita comando
send("command", 3)

# Manda il comando takeoff
send("takeoff", 8)

# Avvolgi il drone in un quadrato
for i in range(4):
  # Vola in avanti
  send("forward " + str(distanza_lati_quadrato), 4)
  # Ruota a destra
  send(direzione_rotazione + " " + str(angolo_rotazione), 3)

# Atterra
send("land", 5)

# Stampa
print("Missione Completata!")

# Chiudi i socket
socketTelloUno.close()
socketTelloDue.close()