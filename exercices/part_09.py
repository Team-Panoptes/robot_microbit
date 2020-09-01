# Exercice 9
# Objectif: Faire en sorte que le robot, une fois sa cible trouvée, avance vers elle.
# La précision n'étant pas toujours extrême, le robot doit parfois tourner dans la direction opposée pour
# compenser sa déviation. Du coup, avant qu'il n'avance, on fait une seconde lecture de la distance, et le
# robot tourne pendant 0.1 secondes avant d'avancer.
# Lorsque le robot tourne, ses LEDs sont cyan (autrement, elles sont noires (éteintes)).

from robot_microbit import *

robot.speed = 50

while True:
    distance = robot.distance_from_obstacle()

    if distance > 50:
        robot.turn_left(25)
        robot.change_all_led_color(Color.cyan)
    else:
        if robot.distance_from_obstacle() > 50:
            robot.turn_right(25)
            robot.wait(0.1)
        robot.go_forward()
        robot.change_all_led_color(Color.black)