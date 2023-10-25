from pydub import AudioSegment
from pydub.playback import play
import math
from djitellopy import TelloSwarm

def frequency_to_note(frequency):
    # Mappa le frequenze alle note
    frequenza_a = 440
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    half_steps = round(12 * math.log2(frequency / frequenza_a))
    note_index = (half_steps + 9) % 12
    octave = 4 + (half_steps + 9) // 12
    return f"{notes[note_index]}{octave}"

# Inizializza lo sciame
swarm = TelloSwarm.fromIps([
    "192.168.1.100",
    "192.168.1.103"
])

# Carica la colonna sonora del Trono di Spade
song = AudioSegment.from_file("got.mp3", format="mp3")

# Esempio: Fai qualcosa ogni volta che viene suonata una nota
threshold_frequency = 440  # Frequenza approssimativa della nota A in Hz

# Connessione allo sciame
swarm.connect()
swarm.takeoff()

for i, chunk in enumerate(song[::1000]):
    if chunk.max >= threshold_frequency:
        note = frequency_to_note(chunk.max)
        print(f"Nota {note} rilevata nel chunk {i}")

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

        play(chunk)

# Atterra lo sciame alla fine
swarm.land()
