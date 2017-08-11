import time
import random

class PeakFinding():
    
    step=0
    
    def input_random(self):
        return random.shuffle(list(range(0,9)))
   
    def input_list(self):

        a = [int(x) for x in input('Enter the List of integers space separated: ').split()]

        while (1):
            peakmethod = input('Enter the method for finding the peak (Linear/Binary/Both): ')
            if (peakmethod=='Linear' or peakmethod=='Binary' or peakmethod=='Both'):
                break
            else:
                print ('Incorrect Option. Try Again')

        return {'inputlist':a,'peakmethod':peakmethod}

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
        
    def Peakfinding_1d_Linear(self,inputarray):
        self.step=0
        index=0
        flag=0
        list_len=len(inputarray)
        start_time=time.time()
        
        if(list_len==1):
            self.step=self.step+1
            print("Peak Found at first location 1")
            flag=1
            print('Linear Algorithm took time in milliseconds: %s and % steps' % (((time.time()-start_time)*1000),self.step))
            return 1
        
        while(index<list_len):
            self.step=self.step+1
            if(index==0 and inputarray[0]>=inputarray[1]):
                print("Peak Found at first location 1")
                flag=1
                break
            elif (index==list_len-1 and inputarray[list_len-1]>=inputarray[list_len-2]):
                print("Peak Found at last location ",list_len)
                flag=1
                break
            elif(inputarray[index]>=inputarray[index-1] and inputarray[index]>=inputarray[index+1]):
                print("Peak Found at location ",index+1)
                flag=1
                break
            index=index+1

        if(flag==0):
            print('Peak Not Found')
        print('Linear Algorithm took time in milliseconds: %s and %s steps' % (((time.time()-start_time)*1000),self.step))

    def Peakfinding_1d_Binary(self,inputarray):
        self.step=0
        list_len=len(inputarray)
        start=0
        end=list_len-1
        mid=int((start+end+1)/2)
        flag=0
        start_time=time.time()
        
        if(list_len==1):
            self.step=self.step+1
            print("Peak Found at first location 1")
            flag=1
            print('Binary Algorithm took time in milliseconds: %s and %s steps' % (((time.time()-start_time)*1000),self.step))
            return 1
        
        while(mid!=start or mid!=end):
            self.step=self.step+1
            if(mid==end and end==list_len-1):
                print("Peak Found at last location ",end+1)
                flag=1
                break
            if(mid==end and end==1):
                print("Peak Found at first location ",1)
                flag=1
                break
            if(inputarray[mid]>=inputarray[mid-1] and inputarray[mid]>=inputarray[mid+1]):
                print("Peak Found at location ",mid+1)
                flag=1
                break
            elif(inputarray[mid]<inputarray[mid-1]):
                end=mid
                mid=int((start+end+1)/2)
            else:
                start=mid
                mid=int((start+end+1)/2)

        if(flag==0):
            print('Peak Not Found')
        print('Binary Algorithm took time in milliseconds: %s and %s steps' % (((time.time()-start_time)*1000),self.step))      
     
    def Peakfinding_2D_colmax(self,inputarray):   
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
            return (globalmaxindex)

    def Peakfinding_2D(self,matrix,colnum):
        #print("len",len(matrix))
        self.step=self.step+1
        if(len(matrix)==1):
            print("Peak at ",self.Peakfinding_2D_colmax(matrix[0])+1,",",colnum+1)
            print("Peak is ",matrix[0][self.Peakfinding_2D_colmax(matrix[0])])
            return(self.Peakfinding_2D_colmax(matrix[0]))
        else:
            midcol=int((len(matrix)-1)/2)
            maxcol=self.Peakfinding_2D_colmax(matrix[midcol])
            if(matrix[midcol][maxcol]<matrix[midcol-1][maxcol]):
                return (self.Peakfinding_2D(matrix[0:midcol+1],colnum+midcol))
            elif(matrix[midcol][maxcol]<matrix[midcol+1][maxcol]):
                return (self.Peakfinding_2D(matrix[midcol+1:],colnum+midcol))
            else:
                 print("Peak at ",maxcol+1,",",midcol+1)
                 print("Peak is ",matrix[midcol][maxcol])
                 return(1)    


peakfindingobj=PeakFinding()

choice = input('Enter the problem (1D/2D): ')
while(1):
    if (choice=='1D'):
        input_tuple = peakfindingobj.input_list()
        print('Input List: ',input_tuple)
        if(input_tuple['peakmethod']=='Linear'):
            peakfindingobj.Peakfinding_1d_Linear(input_tuple['inputlist'])
        if(input_tuple['peakmethod']=='Binary'):
            peakfindingobj.Peakfinding_1d_Binary(input_tuple['inputlist'])
        if(input_tuple['peakmethod']=='Both'):
            peakfindingobj.Peakfinding_1d_Linear(input_tuple['inputlist'])
            peakfindingobj.Peakfinding_1d_Binary(input_tuple['inputlist'])
        break
    elif(choice=='2D'): 
        #inputmatrix=peakfindingobj.input_matrix()
        inputmatrix=[[1, 2, 3,4,5], [50, 60,7,88,9], [9, 100, 11,12,12], [13, 174, 19,18,17],[3,7,6,5,15]]
        print('Input Matrix',inputmatrix)
        start_time=time.time()
        peakfindingobj.Peakfinding_2D(inputmatrix,0)
        print('Algorithm took time in milliseconds: %s and %s steps' % ( ((time.time()-start_time)*1000),peakfindingobj.step))
        break
    else:
        print ('Incorrect Option. Try Again')


