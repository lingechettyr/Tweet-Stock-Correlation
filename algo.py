from time import process_time
def heapify(ticker, n, index): 
    smallest = index  
    left = 2 * index + 1      
    right = 2 * index + 2     
  
    if left < n and ticker[left][0] < ticker[smallest][0]: 
        smallest = left
  
    if right < n and ticker[right][0] < ticker[smallest][0]: 
        smallest = right
  
    if smallest != index: 
        ticker[index],ticker[smallest] = ticker[smallest],ticker[index]  # swap 
  
       
        heapify(ticker, n, smallest) 
  
def heapSort(ticker): 
    length = len(ticker) 
    for index in range(length // 2 - 1, -1, -1): 
        heapify(ticker, length, index) 

    for index in range( length-1, 0, -1): 
        ticker[index], ticker[0] = ticker[0], ticker[index]    
        heapify(ticker, index, 0) 

def selectionSort (ticker):
    length = len(ticker)
    for index in range(length): 
        largest = index 
        for select in range(index+1, length): 
            if ticker[largest][0] < ticker[select][0]: 
                largest = select         
        ticker[index], ticker[largest] = ticker[largest], ticker[index] 

#Selection
ticker = [ (2,"TESLA"), (3,"APPLE"), (5,"FORD"), (4,"GM"), (1,"MSFT"), (0,"NIO")] 
print("")
print("Selection Sort")
startTime = process_time()
selectionSort(ticker)
endTime = process_time()
for i in range(len(ticker)):
    print(ticker[i][1], ":", ticker[i][0])
print("Time To Sort:", endTime-startTime)

#Heapsort
ticker = [ (2,"TESLA"), (3,"APPLE"), (5,"FORD"), (4,"GM"), (1,"MSFT"), (0,"NIO")] 
startTime = process_time()
heapSort(ticker)
endTime = process_time()
print("")
print ("Heap Sort") 
n = len(ticker) 
for i in range(n): 
   print (ticker[i][1], ":",ticker[i][0])
print("Time To Sort:", endTime-startTime)
