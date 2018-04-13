import pygame
import subprocess
from pygame.locals import *

class App:
    def __init__(self):
        pygame.display.init()
        pygame.joystick.init()

        self.my_joystick = None
        self.joystick_names = []

        # Enumerate joysticks
        for i in range(0, pygame.joystick.get_count()):
            self.joystick_names.append(pygame.joystick.Joystick(i).get_name())

        # By default, load the first available joystick.
        if (len(self.joystick_names) > 0):
            self.my_joystick = pygame.joystick.Joystick(0)
            self.my_joystick.init()

    def check_buttons(self):
        for button_number in range(0, self.my_joystick.get_numbuttons()):
            if (self.my_joystick.get_button(button_number)):
                print "You just pressed button " + button_number
                if (button_number == 8):
                    print ("Die, PICO-8!")
                    subprocess.call(['killall','pico8'])
                    print ("Yey")
                    self.quit()

    def main(self):
        while (True):
            self.g_keys = pygame.event.get()
            check_buttons()

    def quit(self):
        pygame.quit()

app = App()
app.main()

