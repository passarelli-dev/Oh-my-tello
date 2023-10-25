from djitellopy import TelLo, Swarm

swarm = TelloSwarm.fromFile("ips.txt")

swarm.connect() # Connettiti allo swarm (Gruppo)

swarm.enable_mission_pads() # Attiva detection pads

swarm.set_mission_pad_detection_direction(1) # il parametro può essere: 0: lo cerca solo quando scende, 1: lo cerca in avanti e indietro, 2: lo cerca in tutte le direzioni

swarm.takeoff() # Fai volare lo sciame

pad = swarm.get_mission_pad_id()

while pad != 1: # Non fa nulla fin quando non identifica il pad
    if pad == 3: #Se è il pad di ID 3
        swarm.move_back(30) # Vai indietro di 30 centimetri
        tello.rotate_clockwise(90) # Gira in senso orario di 90 gradi
    
    if pad == 4: # Se è il pad di ID 4
        swarm.move_up(30)
        swarm.flip_forward()
    
    pad = swarm.get_mission_pad_id()

swarm.disable_mission_pads() # Disattiva riconoscimento pad

swarm.land() # Atterra

swarm.end() # Spegniti