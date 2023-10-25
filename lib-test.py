from djitellopy import TelloSwarm

swarm = TelloSwarm.fromIps([
    "192.168.1.101",
    "192.168.1.103"
])

swarm.connect()

print(swarm.get_battery())
swarm.takeoff()

swarm.move_up(100)

swarm.flip_forward()

swarm.land()
swarm.end()