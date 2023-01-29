import pygame


class Finance():
    def __init__(self):
        self.balance = 1000
        self.rent = 1000
        self.medicalExpenses = 1
        self.salary = 1
        self.randomEvent = 0
        self.debt = 0

    def payDay(self):
        self.balance +=self.salary
        self.salary = 1
    def salaryIncrease(self):
        self.salary +=1
    def returnValues(self):
        return self.balance,self.rent,self.medicalExpenses,self.salary,self.randomEvent,self.debt
