#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 01:31:14 2017

@author: puneet
"""

import time

class PeakFinding():

    def input_matrix(self):
        m = int(input('Enter the number of rows: '))
        n = int(input('Enter the number of columns: '))
        
        cnt=0
        collist=[]
        while(cnt<n):
            print('Enter the column: ',cnt+1)
            templist=[int(x) for x in input().split()]
            if(len(templist)!=m):
                print("Incorrect Input length of column. Please try again")
                return self.input_matrix()
            collist.append(templist)
            cnt=cnt+1
        return collist
    
    def list_globalmax(self,inputarray):   
            print(inputarray)
            list_len=len(inputarray)
            index=0
            globalmax=inputarray[0]
            globalmaxindex=0
            while(index<list_len):
                if(inputarray[index]>globalmax):
                    globalmaxindex=index
                    globalmax=inputarray[index]
                index=index+1
            print(globalmaxindex)
            return {'index':globalmaxindex,'value':globalmax}    
    
    def Peakfinding_2D_globalmax(self,matrix):   
            return 1

    def Peakfinding_2D(self,matrix,startrow,startcol,maxrow,maxcol):
     
        flag=0
        step=0
        while(flag==0):
            step=step+1
            midrow=int((startrow+maxrow)/2)
            midcol=int((startcol+maxcol)/2)
            
            print(midrow,midcol)
                        
            templist=[val for idx,val in enumerate(matrix[startcol]) if(idx>=startrow and idx<=maxrow)]
            max_left_border=self.list_globalmax(templist)
            templist=[val for idx,val in enumerate(matrix[startcol+1]) if(idx>=startrow and idx<=maxrow)]
            if(max_left_border['value']>=templist[max_left_border['index']]):
                print("Peak Found Left Boundary",max_left_border['value'])
                flag=1
                break
            
            templ=[temp[startrow] for temp in matrix]
            templist=[val for idx,val in enumerate(templ) if(idx>=startcol and idx<=maxcol)]
            max_top_border=self.list_globalmax(templist)
            templ=[temp[startrow+1] for temp in matrix]
            templist=[val for idx,val in enumerate(templ) if(idx>=startcol and idx<=maxcol)]
            if(max_top_border['value']>=templist[max_top_border['index']]):
                print("Peak Found Top Boundary",max_top_border['value'])
                flag=1
                break
            
            templist=[val for idx,val in enumerate(matrix[maxcol]) if(idx>=startrow and idx<=maxrow)]
            max_right_border=self.list_globalmax(templist)
            templist=[val for idx,val in enumerate(matrix[maxcol-1]) if(idx>=startrow and idx<=maxrow)]
            if(max_right_border['value']>=templist[max_right_border['index']]):
                print("Peak Found Right Boundary",max_right_border['value'])
                flag=1
                break
            
            templ=[temp[maxrow] for temp in matrix]
            templist=[val for idx,val in enumerate(templ) if(idx>=startcol and idx<=maxcol)]
            max_bottom_border=self.list_globalmax(templist)
            templ=[temp[maxrow-1] for temp in matrix]
            templist=[val for idx,val in enumerate(templ) if(idx>=startcol and idx<=maxcol)]
            if(max_bottom_border['value']>=templist[max_bottom_border['index']]):
                print("Peak Found Bottom Boundary",max_bottom_border['value'])
                flag=1
                break
                
            templist=[item[midrow] for item in matrix]
            max_mid_row=self.list_globalmax(templist)
            
            max_mid_col=self.list_globalmax(matrix[midcol])
            
            
            max_global_list=[max_left_border['value'],max_top_border['value'],max_right_border['value'],
                             max_bottom_border['value'],max_mid_row['value'],max_mid_col['value']]
            print(max_global_list)
            max_global=self.list_globalmax(max_global_list)
            print(max_global)
            
            if(max_global['index']==4):
                if(matrix[max_mid_row['index']][midrow-1]<=max_mid_row['value'] and matrix[max_mid_row['index']][midrow+1]<=max_mid_row['value']):
                    print("Peak Found ",max_mid_row['value'])
                    flag=1
                elif(matrix[max_mid_row['index']][midrow-1]>max_mid_row['value']):
                    if(max_mid_row['index']<midrow):
                        maxrow=midrow
                        maxcol=midcol
                    else:
                        startcol=midcol
                        maxrow=midrow
                else:
                    if(max_mid_row['index']<midrow):
                        startrow=midrow
                        maxcol=midcol
                    else:
                        startrow=midrow
                        startcol=midcol
                        
            elif(max_global['index']==5):
                if(matrix[midcol-1][max_mid_col['index']]<=max_mid_col['value'] and matrix[midcol+1][max_mid_col['index']]<=max_mid_col['value']):
                    print("Peak Found ",max_mid_col['value'])
                    flag=1
                elif(matrix[midcol-1][max_mid_col['index']]>max_mid_col['value']):
                    if(max_mid_col['index']<midcol):
                        maxrow=midrow
                        maxcol=midcol
                    else:
                        startrow=midrow
                        maxcol=midcol
                else:
                    if(max_mid_col['index']<midcol):
                        startcol=midcol
                        maxrow=midrow
                    else:
                        startrow=midrow
                        startcol=midcol
    
            elif(max_global['index']==0):
                if(max_left_border['index']<midrow):
                    maxrow=midrow
                    maxcol=midcol
                else:
                    startrow=midrow
                    maxcol=midcol
            elif(max_global['index']==1):
                if(max_top_border['index']<midcol):
                    maxrow=midrow
                    maxcol=midcol
                else:
                    startcol=midcol
                    maxrow=midrow
            elif(max_global['index']==2):
                if(max_right_border['index']<midrow):
                    startcol=midcol
                    maxrow=midrow
                else:
                    startrow=midrow
                    startcol=midcol
            elif(max_global['index']==3):
                if(max_bottom_border['index']<midcol):
                    startrow=midrow
                    maxcol=midcol
                else:
                    startrow=midrow
                    startrow=midcol
                
            print(startrow,startcol,maxrow,maxcol)
        return(step)
        
peakfindingobj=PeakFinding()
#inputmatrix=peakfindingobj.input_matrix()
#print('Input Matrix',inputmatrix)
inputmatrix=[[1, 2, 3,4,5], [50, 60,7,88,9], [9, 100, 11,12,12], [13, 174, 19,18,17],[3,7,6,5,15]]
print(inputmatrix)
start_time=time.time()
steps=peakfindingobj.Peakfinding_2D(inputmatrix,0,0,len(inputmatrix[0])-1,len(inputmatrix)-1)
print('Algorithm took time in milliseconds: %s and % s steps' % (((time.time()-start_time)*1000),steps))
    


