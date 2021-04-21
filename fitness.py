'''
    To use this, create a folder within the main PhysiCell directory called Files 
    and place this script in that folder. (ie PhysiCell/Files/fitness.py)
'''
import xml.etree.ElementTree as ET
import pandas as pd
import os

from Parser import Parser
class Cell:
  def __init__(self, data, variables):
    self.data = data
    self.variables = variables 
  def getData(self):
    return self.data
  def getVariables(self):
    return self.variables
  def __str__(self):
    return "Cell Id: " + str(self.data[0]) + " Data index values: " + str(self.variables) 


def fitness():
    '''
        This function takes as input an array where each element is an array contianing 
        input parameters for a PhysiCell .xml config file. 
        The input will then be fed, one by one, into PhysiCell for simulation. 
        Each set of simulation data will then be 
    '''
    configFilePath = "./config/PhysiCell_settings.xml"   #Path to the xml config file within PhysiCell
    runSim()
    parser = Parser("./output/")                         #Parsing data into a Parser object
    frameCount = parser.getFrameCount()                  #Pulling frame count from data
    masterTable = {}                                     #Master array to store cell objects
    for frameNumber in range(*parser.getFrameRange()):   #Looping through frames
        curArray = [] 
        cells = parser.getFrame(frameNumber).cells       #Pulling cells from parser
        index = 0
        for i in range(len(cells.data[0])):              #Looping through Cell's
          curCellData = []                  
          for dataArray in cells.data:                   #Looping through master Data array aggregating the individual cell's data. 
            curCellData.append(dataArray[i])           
          newCell = Cell(curCellData, cells.variables)   #Creating Cell Object
          masterTable[newCell.getData()[0]] =  newCell

    VolumeFromInput = 0                                  #Summing healthy biomass within simulation output
    for cell in masterTable:
        curData = masterTable[cell].getData()            #Pulling individual cells data
        if curData[7] == 14:                             #Checking if cell is alive and healthy phase 14
            VolumeFromInput += curData[4]                #If cell is alive and healthy, add its volume to the current total 
    return VolumeFromInput


def runSim():
    print("-------------Running Simulation-------------")
    os.system("./cultured_meat") 
    print("-------------Simulation Finished-------------")
 
