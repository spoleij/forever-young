from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:

blocks = 7
for movement in range (blocks):
    robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
times = 7
blocks = 2
for blocktimes in range(times):
    for movement in range (blocks):
        robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()