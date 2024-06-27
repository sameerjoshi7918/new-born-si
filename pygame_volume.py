import pygame
pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("audios\Do_you_want_to_send_a_message_to_perticular_person.mp3")
sound.set_volume(0.1)
sound.play() 
