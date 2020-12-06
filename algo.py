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
perChange =  {'TSLA': 5.54, 'AAPL': 2.69, 'FB': 0.99, 'ZM': 14.29, 'ADBE': 1.57, 'ADI': 3.52, 'ADP': 0.52, 'ADSK': 0.8, 'ALGN': 8.4, 'ALXN': 1.31, 'AMAT': 7.71, 'AMD': 1.49, 'AMGN': 3.23, 'AMZN': 0.17, 'ANSS': 1.6, 'ASML': 6.09, 'ATVI': 1.76, 'AVGO': 2.52, 'BIDU': 3.65, 'BIIB': 2.37, 'BKNG': 4.76, 'BMRN': 1.16, 'CDNS': 1.75, 'CDW': 2.31, 'CERN': 0.73, 'CHKP': 2.16, 'CHTR': 2.88, 'CMCSA': 2.89, 'COST': 4.68, 'CPRT': 2.91, 'CSCO': 3.16, 'CSX': 2.0, 'CTAS': 2.3, 'CTSH': 3.75, 'CTXS': 5.33, 'DLTR': 2.99, 'DOCU': 6.73, 'DXCM': 8.87, 'EA': 0.74, 'EBAY': 1.07, 'EXC': 0.34, 'EXPE': 3.29, 'FAST': 2.83, 'FISV': 1.69, 'FOX': 3.08, 'GILD': 1.47, 'GOOGL': 3.95, 'IDXX': 0.83, 'ILMN': 8.87, 'INCY': 1.66, 'INTC': 7.53, 'INTU': 4.71, 'ISRG': 7.48, 'JD': 0.19, 'KDP': 0.26, 'KHC': 3.58, 'KLAC': 4.66, 'LBTYA': 11.1, 'LRCX': 10.45, 'LULU': 1.85, 'MAR': 6.89, 'MCHP': 7.33, 'MDLZ': 2.75, 'MELI': 0.26, 'MNST': 3.14, 'MRNA': 0.14, 'MSFT': 0.14, 'MU': 14.43, 'MXIM': 4.06, 'NFLX': 1.55, 'NTES': 3.31, 'NVDA': 1.17, 'NXPI': 3.52, 'ORLY': 1.71, 'PAYX': 1.42, 'PCAR': 0.41, 'PDD': 5.44, 'PEP': 1.12, 'PYPL': 1.7, 'QCOM': 7.1, 'REGN': 4.57, 'ROST': 7.18, 'SBUX': 4.35, 'SGEN': 5.24, 'SIRI': 2.31, 'SNPS': 4.12, 'SPLK': 21.11, 'SWKS': 6.38, 'TCOM': 4.38, 'TMUS': 0.86, 'TTWO': 0.12, 'TXN': 3.27, 'ULTA': 1.5, 'VRSK': 1.33, 'VRSN': 1.63, 'VRTX': 0.25, 'WBA': 14.21, 'WDAY': 1.16, 'XEL': 2.39, 'XLNX': 1.62}

ticker = []
for index, (key,value) in enumerate(perChange.items()):
    ticker.insert(index,(value,key))
print("")
print("Selection Sort")
startTime = process_time()
selectionSort(ticker)
endTime = process_time()
for i in range(len(ticker)):
    print(ticker[i][1], ":", ticker[i][0])
print("Time To Sort:", endTime-startTime)

#Heapsort

perChange = {'TSLA': 5.54, 'AAPL': 2.69, 'FB': 0.99, 'ZM': 14.29, 'ADBE': 1.57, 'ADI': 3.52, 'ADP': 0.52, 'ADSK': 0.8, 'ALGN': 8.4, 'ALXN': 1.31, 'AMAT': 7.71, 'AMD': 1.49, 'AMGN': 3.23, 'AMZN': 0.17, 'ANSS': 1.6, 'ASML': 6.09, 'ATVI': 1.76, 'AVGO': 2.52, 'BIDU': 3.65, 'BIIB': 2.37, 'BKNG': 4.76, 'BMRN': 1.16, 'CDNS': 1.75, 'CDW': 2.31, 'CERN': 0.73, 'CHKP': 2.16, 'CHTR': 2.88, 'CMCSA': 2.89, 'COST': 4.68, 'CPRT': 2.91, 'CSCO': 3.16, 'CSX': 2.0, 'CTAS': 2.3, 'CTSH': 3.75, 'CTXS': 5.33, 'DLTR': 2.99, 'DOCU': 6.73, 'DXCM': 8.87, 'EA': 0.74, 'EBAY': 1.07, 'EXC': 0.34, 'EXPE': 3.29, 'FAST': 2.83, 'FISV': 1.69, 'FOX': 3.08, 'GILD': 1.47, 'GOOGL': 3.95, 'IDXX': 0.83, 'ILMN': 8.87, 'INCY': 1.66, 'INTC': 7.53, 'INTU': 4.71, 'ISRG': 7.48, 'JD': 0.19, 'KDP': 0.26, 'KHC': 3.58, 'KLAC': 4.66, 'LBTYA': 11.1, 'LRCX': 10.45, 'LULU': 1.85, 'MAR': 6.89, 'MCHP': 7.33, 'MDLZ': 2.75, 'MELI': 0.26, 'MNST': 3.14, 'MRNA': 0.14, 'MSFT': 0.14, 'MU': 14.43, 'MXIM': 4.06, 'NFLX': 1.55, 'NTES': 3.31, 'NVDA': 1.17, 'NXPI': 3.52, 'ORLY': 1.71, 'PAYX': 1.42, 'PCAR': 0.41, 'PDD': 5.44, 'PEP': 1.12, 'PYPL': 1.7, 'QCOM': 7.1, 'REGN': 4.57, 'ROST': 7.18, 'SBUX': 4.35, 'SGEN': 5.24, 'SIRI': 2.31, 'SNPS': 4.12, 'SPLK': 21.11, 'SWKS': 6.38, 'TCOM': 4.38, 'TMUS': 0.86, 'TTWO': 0.12, 'TXN': 3.27, 'ULTA': 1.5, 'VRSK': 1.33, 'VRSN': 1.63, 'VRTX': 0.25, 'WBA': 14.21, 'WDAY': 1.16, 'XEL': 2.39, 'XLNX': 1.62}
ticker = []
for index, (key,value) in enumerate(perChange.items()):
    ticker.insert(index,(value,key)) 
startTime = process_time()
heapSort(ticker)
endTime = process_time()
print("")
print ("Heap Sort") 
n = len(ticker) 
for i in range(n): 
   print (ticker[i][1], ":",ticker[i][0])
print("Time To Sort:", endTime-startTime)
