import pygame
import random as rand
class Job():
    def __init__(self):

        self.happinessChange = 0
        self.hungerChange = 0

    def interactions(self):
        for i in range(3): #temp interactions
            event = rand.random(1,100)
            if (event >1 and event <50):
                self.happinessChange -=10
                self.hungerChange -=10
            else:
                self.happinessChange -=5
                self.happinessChange -=10
        
