import RPi.GPIO as GPIO
import time
 
buzzer_pin = 4
button1 = 17
button2 = 18
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
notes = {
	'B0' : 31,
	'C1' : 33, 'CS1' : 35,
	'D1' : 37, 'DS1' : 39,
	'EB1' : 39,
	'E1' : 41,
	'F1' : 44, 'FS1' : 46,
	'G1' : 49, 'GS1' : 52,
	'A1' : 55, 'AS1' : 58,
	'BB1' : 58,
	'B1' : 62,
	'C2' : 65, 'CS2' : 69,
	'D2' : 73, 'DS2' : 78,
	'EB2' : 78,
	'E2' : 82,
	'F2' : 87, 'FS2' : 93,
	'G2' : 98, 'GS2' : 104,
	'A2' : 110, 'AS2' : 117,
	'BB2' : 123,
	'B2' : 123,
	'C3' : 131, 'CS3' : 139,
	'D3' : 147, 'DS3' : 156,
	'EB3' : 156,
	'E3' : 165,
	'F3' : 175, 'FS3' : 185,
	'G3' : 196, 'GS3' : 208,
	'A3' : 220, 'AS3' : 233,
	'BB3' : 233,
	'B3' : 247,
	'C4' : 262, 'CS4' : 277,
	'D4' : 294, 'DS4' : 311,
	'EB4' : 311,
	'E4' : 330,
	'F4' : 349, 'FS4' : 370,
	'G4' : 392, 'GS4' : 415,
	'A4' : 440, 'AS4' : 466,
	'BB4' : 466,
	'B4' : 494,
	'C5' : 523, 'CS5' : 554,
	'D5' : 587, 'DS5' : 622,
	'EB5' : 622,
	'E5' : 659,
	'F5' : 698, 'FS5' : 740,
	'G5' : 784, 'GS5' : 831,
	'A5' : 880, 'AS5' : 932,
	'BB5' : 932,
	'B5' : 988,
	'C6' : 1047, 'CS6' : 1109,
	'D6' : 1175, 'DS6' : 1245,
	'EB6' : 1245,
	'E6' : 1319,
	'F6' : 1397, 'FS6' : 1480,
	'G6' : 1568, 'GS6' : 1661,
	'A6' : 1760, 'AS6' : 1865,
	'BB6' : 1865,
	'B6' : 1976,
	'C7' : 2093, 'CS7' : 2217,
	'D7' : 2349, 'DS7' : 2489,
	'EB7' : 2489,
	'E7' : 2637,
	'F7' : 2794, 'FS7' : 2960,
	'G7' : 3136, 'GS7' : 3322,
	'A7' : 3520, 'AS7' : 3729,
	'BB7' : 3729,
	'B7' : 3951,
	'C8' : 4186, 'CS8' : 4435,
	'D8' : 4699, 'DS8' : 4978
}
 
crazy_frog_melody = [
	notes['A4'], notes['C5'], notes['A4'], notes['A4'], notes['D5'], notes['A4'], notes['G4'], 
	notes['A4'], notes['E5'], notes['A4'], notes['A4'], notes['F5'], notes['E5'], notes['C5'],
	notes['A4'], notes['E5'], notes['A5'], notes['A4'], notes['G4'], notes['G4'], notes['E4'], notes['B4'], 
	notes['A4'],0,
	
	notes['A4'], notes['C5'], notes['A4'], notes['A4'], notes['D5'], notes['A4'], notes['G4'], 
	notes['A4'], notes['E5'], notes['A4'], notes['A4'], notes['F5'], notes['E5'], notes['C5'],
	notes['A4'], notes['E5'], notes['A5'], notes['A4'], notes['G4'], notes['G4'], notes['E4'], notes['B4'], 
	notes['A4'],0,
	
	
	notes['A3'], notes['G3'], notes['E3'], notes['D3'],
	
	notes['A4'], notes['C5'], notes['A4'], notes['A4'], notes['D5'], notes['A4'], notes['G4'], 
	notes['A4'], notes['E5'], notes['A4'], notes['A4'], notes['F5'], notes['E5'], notes['C5'],
	notes['A4'], notes['E5'], notes['A5'], notes['A4'], notes['G4'], notes['G4'], notes['E4'], notes['B4'], 
	notes['A4'],
]
 
crazy_frog_tempo = [
	2,4,4,8,4,4,4,
	2,4,4,8,4,4,4,
	4,4,4,8,4,8,4,4,
	1,4,
	
	2,4,4,8,4,4,4,
	2,4,4,8,4,4,4,
	4,4,4,8,4,8,4,4,
	1,4,
	
	8,4,4,4,
	
	2,4,4,8,4,4,4,
	2,4,4,8,4,4,4,
	4,4,4,8,4,8,4,4,
	1,
]
 
final_countdown_melody = [
	notes['A3'],notes['E5'],notes['D5'],notes['E5'],notes['A4'],
	notes['F3'],notes['F5'],notes['E5'],notes['F5'],notes['E5'],notes['D5'],
	notes['D3'],notes['F5'],notes['E5'],notes['F5'],notes['A4'],
	notes['G3'],0,notes['D5'],notes['C5'],notes['D5'],notes['C5'],notes['B4'],notes['D5'],
	notes['C5'],notes['A3'],notes['E5'],notes['D5'],notes['E5'],notes['A4'],
	notes['F3'],notes['F5'],notes['E5'],notes['F5'],notes['E5'],notes['D5'],
	notes['D3'],notes['F5'],notes['E5'],notes['F5'],notes['A4'],
	notes['G3'],0,notes['D5'],notes['C5'],notes['D5'],notes['C5'],notes['B4'],notes['D5'],
	notes['C5'],notes['B4'],notes['C5'],notes['D5'],notes['C5'],notes['D5'],
	notes['E5'],notes['D5'],notes['C5'],notes['B4'],notes['A4'],notes['F5'],
	notes['E5'],notes['E5'],notes['F5'],notes['E5'],notes['D5'],
	notes['E5'],
]
 
final_countdown_tempo = [
	1,16,16,4,4,
	1,16,16,8,8,4,
	1,16,16,4,4,
	2,4,16,16,8,8,8,8,
	4,4,16,16,4,4,
	1,16,16,8,8,4,
	1,16,16,4,4,
	2,4,16,16,8,8,8,8,
	4,16,16,4,16,16,
	8,8,8,8,4,4,
	2,8,4,16,16,
	1,
]
 
def buzz(frequency, length):
 
	if(frequency==0):
		time.sleep(length)
		return
	period = 1.0 / frequency
	delayValue = period / 2
	numCycles = int(length * frequency)
	
	for i in range(numCycles):
		GPIO.output(buzzer_pin, True)
		time.sleep(delayValue)
		GPIO.output(buzzer_pin, False)
		time.sleep(delayValue)
 
def play(melody,tempo,pause,pace=0.800):
	
	for i in range(0, len(melody)):
		
		noteDuration = pace/tempo[i]
		buzz(melody[i],noteDuration)
		
		pauseBetweenNotes = noteDuration * pause
		time.sleep(pauseBetweenNotes)
 
while True:
	if GPIO.input(button1) == 0:
		print "Crazy Frog (Axel F) Theme"
		play(crazy_frog_melody, crazy_frog_tempo, 0.30, 0.900)
		time.sleep(2)
	if GPIO.input(button2) == 0:
		print "The Final Countdown"
		play(final_countdown_melody, final_countdown_tempo, 0.30, 1.2000)
		time.sleep(2)
