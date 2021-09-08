#!/usr/bin/env python
import matplotlib.pyplot as plt

f_attack = open("../../../buildlogs/ArduCopter-Rocking Drone Test.txt", 'r')

time_attack = []
rotors_attack = [[], [], [], []]

lines = f_attack.readlines()
rotor_num = 0
time_slice = 0

for line in lines:
    tokens = line.split()
    if len(tokens) == 5:
        if tokens[1] == "Rotor":
            if rotor_num == 0:
		if time_slice == 0:
		    time_attack.append(float(tokens[0][5:9]))
		    time_slice = time_slice + 1
		else:
		    time_attack.append(float(tokens[0][5:9]) + float(time_slice / 3))
		    time_slice = (time_slice + 1) % 3
            rotors_attack[rotor_num].append(int(tokens[4]))
            rotor_num = (rotor_num + 1) % 4

plt.subplot(2, 1, 1)
plt.plot(time_attack, rotors_attack[0], 'ro', label = 'Rotor1', markersize=1)
plt.plot(time_attack, rotors_attack[1], 'bo', label = 'Rotor2', markersize=1)
plt.plot(time_attack, rotors_attack[2], 'go', label = 'Rotor3', markersize=1)
plt.plot(time_attack, rotors_attack[3], 'mo', label = 'Rotor4', markersize=1)
plt.title('Rocking Drone Attack')
plt.xlabel('Time')
plt.ylabel('Rpm')
plt.legend(loc='best', ncol=4)

f_hover = open("../../../buildlogs/ArduCopter-Simple Hover Test.txt", 'r')

time_hover = []
rotors_hover = [[], [], [], []]

lines = f_hover.readlines()
rotor_num = 0
time_slice = 0

for line in lines:
    tokens = line.split()
    if len(tokens) == 5:
        if tokens[1] == "Rotor":
            if rotor_num == 0:
		if time_slice == 0:
		    time_hover.append(float(tokens[0][5:9]))
		    time_slice = time_slice + 1
		else:
		    time_hover.append(float(tokens[0][5:9]) + float(time_slice / 3))
		    time_slice = (time_slice + 1) % 3
            rotors_hover[rotor_num].append(int(tokens[4]))
            rotor_num = (rotor_num + 1) % 4

plt.subplot(2, 1, 2)
plt.plot(time_hover, rotors_hover[0], 'ro', label = 'Rotor1', markersize=1)
plt.plot(time_hover, rotors_hover[1], 'bo', label = 'Rotor2', markersize=1)
plt.plot(time_hover, rotors_hover[2], 'go', label = 'Rotor3', markersize=1)
plt.plot(time_hover, rotors_hover[3], 'mo', label = 'Rotor4', markersize=1)
plt.title('Simple Hover Test')
plt.xlabel('Time')
plt.ylabel('Rpm')
plt.legend(loc='best', ncol=4)
plt.savefig('../../../buildlogs/result.png')

f_attack.close()
f_hover.close()
