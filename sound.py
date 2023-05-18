import pygame


def my_sound():

    pygame.mixer.init()

    try:
        pygame.mixer.music.load("funny-complete-sound.mp3")
        pygame.mixer.music.play()
        pygame.time.wait(1000)  # Wait for 1 seconds
        pygame.mixer.music.stop()
    finally:
        pygame.mixer.quit()



