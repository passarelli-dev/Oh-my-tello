import speech_recognition as sr
from djitellopy import TelloSwarm

# Funzione per connettersi al drone Tello
def connect_to_swarm():
    swarm = TelloSwarm.fromIps([
        "192.168.1.103",  # Inserisci gli indirizzi IP dei tuoi droni
        "192.168.1.101"
    ])
    swarm.connect()
    swarm.takeoff()
    print("Swarm connected!")

# Funzione principale
def main():
    # Inizializza il riconoscitore vocale
    recognizer = sr.Recognizer()

    # Registra il microfono come sorgente audio
    with sr.Microphone() as source:
        print("Say a command...")
        while True:
            try:
                # Ascolta l'audio
                audio = recognizer.listen(source)

                # Riconosci il testo dall'audio
                command = recognizer.recognize_google(audio).lower()

                # Stampa il comando riconosciuto
                print("You said:", command)

                # Esegui l'azione corrispondente al comando
                if "accenditi" in command:
                    connect_to_swarm()

            except sr.UnknownValueError:
                pass  # Ignora se il riconoscimento non ha avuto successo
            except sr.RequestError as e:
                print("Error connecting to Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    main()
