import speech_recognition as sr
from djitellopy import TelloSwarm

# Funzione per connettersi al drone Tello
def connect_to_swarm(swarm):
    swarm.connect()
    swarm.takeoff()
    print("Swarm connected!")

# Funzione per interpretare e eseguire comandi specifici
def execute_command(command, swarm):
    if "accenditi" in command:
        connect_to_swarm(swarm)
    elif "gira a destra di" in command:
        distance_str = command.split("di")[1].strip().split(" ")[0]  # Estrai la distanza dal comando
        try:
            distance = float(distance_str)
            print(f"Gira a destra di {distance} centimetri.")
            # Aggiungi qui la logica per far girare l'intero swarm a destra di una certa distanza
            for drone in swarm.drones:
                drone.move_right(distance)
        except ValueError:
            print("Errore: Impossibile interpretare la distanza.")

# Funzione principale
def main():
    recognizer = sr.Recognizer()

    # Crea un'istanza di TelloSwarm
    swarm = TelloSwarm.fromFile("ips.txt")

    with sr.Microphone() as source:
        print("Say a command...")
        while True:
            try:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio, language="it-IT").lower()
                print("You said:", command)
                execute_command(command, swarm)
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print("Error connecting to Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    main()
