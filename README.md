# ArduPilot Rocking Drone

## Outline
This project mimics "Rocking Drones with Intentional Sound Noise on Gyroscopic Sensors(2005) Y Son et al."
In this project, a sinusoider error is added to gyro when the attack flag is 1(ON).
It adds this function to ardupilot project, simulates this attack, and analyzes the results.

## Develop

1. Add parameters

Go to ardupilot/libraries/SITL

In SITL.h, adds following parameters into the SITL class.
```C
    AP_Int8  attack_trigger;
    AP_Float attack_frequency_roll; 
    AP_Float attack_frequency_pitch;
    AP_Float attack_frequency_yaw;
    AP_Float attack_amplitude_roll;
    AP_Float attack_amplitude_pitch;
    AP_Float attack_amplitude_yaw;
```

attack trigger represents the attack status(ON/OFF).
Other paramters are for attack frequency and amplitude.

In SITL.cpp, adds extra table and parameters to the extended table.

Adding table is done by adding AP_SUBGROUPEXTENSION to the suitable table.
In my case, I added a subgroup to var_info2 by adding it to the table.

```AP_SUBGROUPEXTENSION("",     5, SITL,  var_attack)```

Use a contents number that is not in use(in my case 5).

Finally, fill in the extended table with ```AP_GROUPINFO```
The newly added params must be in the SITL group.

![Alt text](/image/parameter.jpg)

2. Modify gyro value

3. Add tests to arducopter.py

4. Set essential/useless tests in autotest.py

## Result
