# spacetracking
"Choreography as music instrument"
Use a dancers position to make music. 
There are 2-4 proximity sensors above the stage. These can be used binary(turn soundeffect on/off) or linear(distort the sound).
Also the position of the dancer is tracked, and there are different zones on the stage. According to the position of the dancer,
which zone and sensor he is using, he can play together with the musician on the stage. 

My part is to build the Hardware that is needed and read the sensors. 

The proximity sensor values are read out over an ADC in an Arduino uno. It will send the raw data over seriell to a Raspbery Pi.
The Pi sends the data over MQTT in the Topic lasers/raw/..
Simultaneously there is a javascript which gets the postion from the dancer from the Decawave MDK1001 and compares it with a given .SVG
The javascript returns the zone in which the dancer is located also over MQTT in the topic track/.

After that there are python scripts that receive the raw values from MQTT and modify them with the desired functions(binary, linear).
Then they will be send over MQTT again and at the end another python script sends all values over OSC(so the music program Ableton live can map them to sound effects)
to the laptop of the musician in Ableton.

Ableton translates the given values to sound effects.
