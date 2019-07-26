# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 14:08:28 2019

@author: valero
"""
from Scripts import preprocesing

fileName="scenarios.txt"
fileScenarios=preprocesing.File(fileName)
#f = open("scenarios.txt", "r")
Scenarios = [preprocesing.scenario(x) for x in range(fileScenarios.lengthFile())]

f = open(fileName, "r")
k=0
for x in f:
    Scenarios[k].videoScenario(x)
    k+=1



sumoScenario = preprocesing.Sumo()

sumoScenario.generateNetwork()
