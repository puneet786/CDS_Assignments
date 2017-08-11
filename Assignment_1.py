#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 07:35:40 2017

@author: puneet
"""

import time
import random as rd
import csv

class PeakFinding():
        
    def input_random(self,n):
        randomlist=[]
        for i in range(0,n):
            rd.seed(rd.randint(-99999,99999))
            randomlist.append(rd.randint(-999,999))
        #randomlist=[-451, 255, 536, 636, 801,912,1234]
        rd.shuffle(randomlist)
        return (randomlist)
    
    def LinSearchPeak1D(self,inputarray):
        #print(inputarray)
        comparisons=0
        index=0
        flag=0
        list_len=len(inputarray)
        start_time=time.time()
        
        if(list_len==1):
            comparisons=comparisons+1
            #print("Peak Found at first location 1")
            flag=1
            #print('Linear Algorithm took time in milliseconds: %s and % comparisons' % (((time.time()-start_time)*1000),comparisons))
            return comparisons
        
        while(index<list_len):
            comparisons=comparisons+2
            if(index==0 and inputarray[0]>=inputarray[1]):
                #print("Peak Found at first location 1")
                flag=1
                break
            elif (index==list_len-1 and inputarray[list_len-1]>=inputarray[list_len-2]):
                #print("Peak Found at last location ",list_len)
                flag=1
                break
            elif(inputarray[index]>=inputarray[index-1] and inputarray[index]>=inputarray[index+1]):
                #print("Peak Found at location ",index+1)
                flag=1
                break
            index=index+1

        if(flag==0):
            print('Peak Not Found')
        #print('Linear Algorithm took time in milliseconds: %s and %s comparisons' % (((time.time()-start_time)*1000),comparisons))
        return (comparisons)

    def BinSearchPeak1D(self,inputarray):
        comparisons=0
        list_len=len(inputarray)
        start=0
        end=list_len-1
        mid=int((start+end+1)/2)
        flag=0
        start_time=time.time()
        
        if(list_len==1):
            comparisons=comparisons+1
            #print("Peak Found at first location 1")
            flag=1
            #print('Binary Algorithm took time in milliseconds: %s and %s comparisons' % (((time.time()-start_time)*1000),comparisons))
            return comparisons
        
        while(mid!=start or mid!=end):
            if(mid==end and end==list_len-1):
                comparisons=comparisons+2
                #print("Peak Found at last location ",end+1)
                flag=1
                break
            if(mid==end and end==1):
                comparisons=comparisons+2
                #print("Peak Found at first location ",1)
                flag=1
                break
            if(inputarray[mid]>=inputarray[mid-1] and inputarray[mid]>=inputarray[mid+1]):
                comparisons=comparisons+2
                #print("Peak Found at location ",mid+1)
                flag=1
                break
            elif(inputarray[mid]<inputarray[mid-1]):
                comparisons=comparisons+1
                end=mid
                mid=int((start+end+1)/2)
            else:
                start=mid
                mid=int((start+end+1)/2)

        if(flag==0):
            print('Peak Not Found')
        #print('Binary Algorithm took time in milliseconds: %s and %s comparisons' % (((time.time()-start_time)*1000),comparisons))      
        
        return (comparisons)
        
    
peakfindingobj=PeakFinding()

n =[int(x) for x in input('Enter the size of random list to be generated (between -999 to 999): ').split()]

while (1):
    peakmethod = input('Enter the method for finding the peak (Linear/Binary/Both): ')
    if (peakmethod=='Linear' or peakmethod=='Binary' or peakmethod=='Both'):
        break
    else:
        print ('Incorrect Option. Try Again')
                
while(1):
    if(peakmethod=='Linear'):
        iterations=0
        comparisonslist=[]
        while(iterations<1000):
            inputlist = peakfindingobj.input_random(n[0])
            comparisonslist.append(peakfindingobj.LinSearchPeak1D(inputlist))
            iterations=iterations+1
        with open("/home/puneet/Coding/CDSAssignments/1DPeakFinding_Files/output_linear_"+str(n[0])+"_.csv", "w") as f:
            writer = csv.writer(f)
            print("Writing")
            for val in comparisonslist:
                writer.writerow([val])
        break
    elif(peakmethod=='Binary'):
        iterations=0
        comparisonslist=[]
        while(iterations<1000):
            inputlist = peakfindingobj.input_random(n[0])
            comparisonslist.append(peakfindingobj.BinSearchPeak1D(inputlist))
            iterations=iterations+1
        with open("/home/puneet/Coding/CDSAssignments/1DPeakFinding_Files/output_binary_"+str(n[0])+"_.csv", "w") as f:
            writer = csv.writer(f)
            print("Writing")
            for val in comparisonslist:
                writer.writerow([val])
        break
    elif(peakmethod=='Both'):
        iterations=0
        comparisonslist=[]
        while(iterations<1000):
            inputlist = peakfindingobj.input_random(n[0])
            comparisonslist.append(peakfindingobj.LinSearchPeak1D(inputlist))
            iterations=iterations+1
        print(max(comparisonslist))
        with open("/home/puneet/Coding/CDSAssignments/1DPeakFinding_Files/output_linear_"+str(n[0])+"_.csv", "w") as f:
            writer = csv.writer(f)
            print("Writing")
            for val in comparisonslist:
                writer.writerow([val])
    
        iterations=0
        comparisonslist=[]
        while(iterations<1000):
            inputlist = peakfindingobj.input_random(n[0])
            comparisonslist.append(peakfindingobj.BinSearchPeak1D(inputlist))
            iterations=iterations+1
        with open("/home/puneet/Coding/CDSAssignments/1DPeakFinding_Files/output_binary_"+str(n[0])+"_.csv", "w") as f:
            writer = csv.writer(f)
            print("Writing")
            for val in comparisonslist:
                writer.writerow([val])
        break
    else:
        print("Incorrect Option Please Try Again")
