import time
import random

class PeakFinding():
    
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


    def Peakfinding_1d_Linear(self,inputarray):
        index=0
        flag=0
        list_len=len(inputarray)
        start_time=time.time()
        while(index<list_len):
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
        print('Linear Algorithm took time in milliseconds: %s' % ((time.time()-start_time)*1000))

    def Peakfinding_1d_Binary(self,inputarray):
        list_len=len(inputarray)
        start=0
        end=list_len-1
        mid=int((start+end+1)/2)

        start_time=time.time()

        while(mid!=start or mid!=end):
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
        print('Binary Algorithm took time in milliseconds: %s' % ((time.time()-start_time)*1000))      
        

    def Peakfinding_2D_Linear(self,matrix):
        return (1)


peakfindingobj=PeakFinding()
#x=peakfindingobj.input_random()
#print(x)
input_tuple = peakfindingobj.input_list()
print('Input List: ',input_tuple)
if(input_tuple['peakmethod']=='Linear'):
    peakfindingobj.Peakfinding_1d_Linear(input_tuple['inputlist'])
if(input_tuple['peakmethod']=='Binary'):
    peakfindingobj.Peakfinding_1d_Binary(input_tuple['inputlist'])
if(input_tuple['peakmethod']=='Both'):
    peakfindingobj.Peakfinding_1d_Linear(input_tuple['inputlist'])
    peakfindingobj.Peakfinding_1d_Binary(input_tuple['inputlist'])

