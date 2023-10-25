from djitellopy import TelloSwarm

swarm = TelloSwarm.fromFile("ips.txt")

swarm.connect()

print(swarm.get_battery())
swarm.takeoff()

swarm.move_up(100)

swarm.flip_forward()

swarm.land()
swarm.end()