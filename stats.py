import pygame
from statInteractions import Interactions
class Stats():
    def __init__(self):
        self.happiness = 100
        self.hunger = 100
        self.jobUpdateArray = []
        
    def updatedstats(self):
        self.jobupdate = Interactions() #calls job from statInteractions 
        self.jobupdatearray = self.jobupdate.jobInteractions() #job from statInteractions returns an array, happiness and hunger

        self.happiness =self.happiness + self.jobupdatearray[0] # + whatever other interactions
        self.hunger=self.hunger + self.jobupdatearray[1]
        
