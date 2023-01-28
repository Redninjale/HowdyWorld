import pygame
import random as rand
class Interactions():
    def __init__(self):

        self.jobHappiness = 0
        self.jobHunger = 0

    def jobInteractions(self):
        for i in range(3): #temp interactions
            event = rand.random(1,100)
            if (event >1 and event <50):
                self.jobHappiness -=10
                self.jobHunger -=10
            else:
                self.jobHappiness -=5
                self.jobHunger -=10
        return self.jobHappiness, self.jobHunger

        
