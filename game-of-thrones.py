from pydub import AudioSegment
from pydub.playback import play
import math
from djitellopy import TelloSwarm
import time

def frequenza_a_nota(frequenza):
    # Mappa le frequenze alle note
    frequenza_a = 440
    note = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    mezzo_passo = round(12 * math.log2(frequenza / frequenza_a))
    indice_nota = (mezzo_passo + 9) % 12
    ottava = 4 + (mezzo_passo + 9) // 12
    return f"{note[indice_nota]}{ottava}"

# Inizializza lo sciame
swarm = TelloSwarm.fromFile("ips.txt")

# Carica la colonna sonora del Trono di Spade
song = AudioSegment.from_file("got.mp3", format="mp3")

# Esempio: Fai qualcosa ogni volta che viene suonata una nota
threshold_frequency = 440  # Frequenza approssimativa della nota A in Hz

# Connessione allo sciame
swarm.connect()
swarm.takeoff()

# Definisci un intervallo di tempo tra i chunk di audio (in secondi)
chunk_interval = 0.5

# Buffer per accumulare le note rilevate
note_buffer = []

for i, chunk in enumerate(song[::1000]):
    if chunk.max >= threshold_frequency:
        note = frequenza_a_nota(chunk.max)
        print(f"Nota {note} rilevata nel chunk {i}")

        # Aggiungi la nota al buffer
        note_buffer.append(note)

# Processa le note nel buffer
for note in note_buffer:
    # Esempi di azioni dello sciame in base alla nota
    if 'C' in note:
        swarm.move_up(30)
    elif 'C#' in note:
        swarm.move_left(30)
    elif 'D' in note:
        swarm.move_right(30)
    elif 'D#' in note:
        swarm.move_forward(30)
    elif 'E' in note:
        swarm.move_back(30)
    elif 'F' in note:
        swarm.rotate_counter_clockwise(30)
    elif 'F#' in note:
        swarm.rotate_clockwise(30)
    elif 'G' in note:
        swarm.flip_forward()
    elif 'G#' in note:
        swarm.flip_backward()
    elif 'A' in note:
        swarm.flip_left()
    elif 'A#' in note:
        swarm.flip_right()
    elif 'B' in note:
        swarm.land()

    # Pausa tra le azioni
    time.sleep(chunk_interval)

# Atterra lo sciame alla fine
swarm.land()
