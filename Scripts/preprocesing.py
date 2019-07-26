# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 13:39:41 2019

@author: valero
"""
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
        
import numpy as np
import os
import subprocess

class scenario:
    def __init__(self,id):
        self.id=id
        
    def videoScenario(self,x):
        dirName=File.createDirectory(self.id)
        vecttor=x.rstrip('\n')
        interval=vecttor.split(" ")
        #print (interval)
        i=0
        self.ids=str(i)
        os.system('ffmpeg -ss '+str(interval[0])+' -i video.mp4 -c copy -t '+str(interval[1])+' '+dirName+'/'+dirName+'.mp4')
        i+=1
        return print("Scenarios created...")

class File:
    def __init__(self,filename):
        self.filename = filename
    
    def lengthFile(self):
        f = open(self.filename, "r")
        length= sum(1 for line in f)
        f.close
        return length
    
    def createDirectory(dirName):
        # Create target Directory if don't exist
        dirName='Scenario'+str(dirName)
        if not os.path.exists(dirName):
            os.mkdir(dirName)
        return dirName
            
    

class Sumo:
    def __init__(self,background):
        self.ids=[]
        self.imageName= background
        
    def generateNetwork(self):
        worldImg = plt.imread(self.imageName)
        plt.ion()
        plt.figure()
        plt.imshow(worldImg)
        plt.tight_layout()
        nPoints=2
        videoPts = np.dot(0.1,np.array(plt.ginput(nPoints,timeout=300)))
        '''videoPts=np.array([[268.47708678, 181.94559384],
               [281.09693872, 159.86085295],
               [141.33207851, 106.54197851],
               [134.39115994, 129.5732083 ]])'''
        '''videoPts=np.array([[281.09693872, 159.86085295],
               [134.39115994, 129.5732083 ]])'''
        
        from xml.etree import ElementTree as ET
        
        root = ET.Element("nodes")
        
        rootEdge = ET.Element("edges")
        nodeAttributes = ["id", "x", "y"]
        edgeAttributes = ["from","id","to","numLanes"]
        
        for id in range(len(videoPts)):
            vType=ET.SubElement(root,"node")
            
            if id ==0:
                vTypeEdge=ET.SubElement(rootEdge,"edge")
                vTypeEdge.set(edgeAttributes[0],'Node_'+str(id))
            if id>0:
                vTypeEdge.set(edgeAttributes[1],"1to2")
                vTypeEdge.set(edgeAttributes[2],'Node_'+str(id)) 
                vTypeEdge.set(edgeAttributes[3],str(2)) 
            datos = np.append(['Node_'+str(id)],videoPts[id])
            k=0
            for x in nodeAttributes:
                vType.set(x,str(datos[k]))
                k+=1
        
        
        tree = ET.ElementTree(root)
        tree.write("nodes.nod.xml")
        tree = ET.ElementTree(rootEdge)
        tree.write("edge.edg.xml")
        
        os.system('netconvert --node-files=nodes.nod.xml --edge-files=edge.edg.xml --output-file=network.net.xml')
        os.system('sumo-gui network.net.xml')
                
        
        