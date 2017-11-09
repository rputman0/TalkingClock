#A talking clock takes a 24-hour time and translates it into words.
##Input: An hour (0-23) followed by a colon followed by the minute (0-59).
##Output: The time in words, using 12-hour format followed by am or pm.

import datetime,pyglet,pygame

today = datetime.datetime.today()
hour = today.hour
minute = today.minute

print("%s:%s"%(hour,minute))

def play(song):
    pyglet.resource.media(song+'.wav').play()
    pygame.time.wait(1000)

play('its')

soundsHour = ['1','2','3','4','5','6','7','8','9','10','11','12']
if(hour >= 1 and hour <= 11):
    play(soundsHour[hour-1])
elif(hour > 13):
    play(soundsHour[hour-13])
elif(hour == 0 or hour == 12):
    play('12')

if(minute > 11 and minute < 60):
    if(minute == 11):
        play('11')
    elif(minute == 12):
        play('12')
    elif(minute == 13):
        play('thir')
        play('teen')
    elif(minute == 14):
        play('for')
        play('teen')
    elif(minute == 15):
        play('fif')
        play('teen')
    elif(minute == 16):
        play('six')
        play('teen')
    elif(minute == 17):
        play('seven')
        play('teen')
    elif(minute == 18):
        play('eight')
        play('teen')
    elif(minute == 19):
        play('nine')
        play('teen')
           
    elif(minute > 20 and minute < 30):
        play('twen')
        play('ty')
        minute -= 20
    elif(minute >= 30 and minute < 40):
        play('thir')
        play('ty')
        minute -= 30
    elif(minute >= 40 and minute < 50):
        play('for')
        play('ty')
        minute -= 40
    elif(minute >= 50 and minute < 60):
        play('fif')
        play('ty')
        minute -= 50
        
    soundsMinute = ['1','2','3','4','5','6','7','8','9','10']
    if(minute >= 1 and minute <= 11):
        play(soundsMinute[minute-1])
else:
    soundsMinute = ['1','2','3','4','5','6','7','8','9','10']
    if(minute >= 1 and minute <= 11):
        play('o')
        play(soundsMinute[minute-1])
    
if(hour >= 0 and hour <= 11):
    play('am')
elif(hour >= 12):
    play('pm')

pyglet.app.run()
