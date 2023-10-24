from djitellopy import TelloSwarm

swarm = TelloSwarm.fromIps([
    "192.168.1.100",
    "192.168.1.102"
])

swarm.connect()
swarm.takeoff()

swarm.move_up(100)

swarm.sequential(lambda i, tello: tello.move_forward(i * 20 + 20))

swarm.parallel(lambda i, tello: tello.move_left(i * 100 + 20))

swarm.land()
swarm.end()