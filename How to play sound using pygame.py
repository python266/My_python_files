from pygame import mixer

# Instantiate mixer
mixer.init()

# Load audio file
mixer.music.load('water.mp3')

print("music started playing....")

# Set preferred volume
mixer.music.set_volume(0.2)

# Play the music
mixer.music.play()

# Infinite loop
while True:
    print("------------------------------------------------------------------------------------")
    print("Press 'p' to pause the music")
    print("Press 'r' to resume the music")
    print("Press 'e' to exit the program")

    # take user input
    userInput = input(" ")

    if userInput == 'p':

        # Pause the music
        mixer.music.pause()
        print("music is paused....")
    elif userInput == 'r':

        # Resume the music
        mixer.music.unpause()
        print("music is resumed....")
    elif userInput == 'e':

        # Stop the music playback
        mixer.music.stop()
        print("music is stopped....")
        break

#----------------------------------------Notificatioin--------------------------------------------------------------

import time
from plyer import notification

if __name__=="__main__":
    m = input("Name")
    notification.notify(
        title="Hello",
        message=f"Hello sir {m}, Welcome to the new program.",
        app_icon="icon.ico",
        timeout=10
)
    time.sleep(60*60)

