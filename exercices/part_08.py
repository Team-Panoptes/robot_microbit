# Exercice 8
# Objectif: Le robot va tourner sur lui-même. Si un objet est placé près de lui (par exemple, à moins de 50 cm),
# le robot doit s'arrêter en faisant plus ou moins face à l'obstacle.
# En jouant sur la vitesse, on peut essayer de rendre le robot plus précis (ex: donner une vitesse de 25 pendant qu'il tourne).

from robot_microbit import *

robot.speed = 50

while True:
    distance = robot.distance_from_obstacle()

    if distance > 50:
        robot.turn_left(25)
    else:
        robot.stop()
