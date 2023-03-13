import numpy as np
import pandas as pd
#1 - show_results.txt file is in my working project of VSCode
#2 
states = []
shows = []
viewers = []
#3
arr = np.genfromtxt('show_results.txt', dtype = 'str', delimiter=',')
#4
#print(arr)
#5
states = np.loadtxt("show_results.txt", usecols=0, dtype='str', delimiter = ",")
#removing duplicates
states = [*set(states)] 

shows = np.loadtxt("show_results.txt", usecols=1, dtype='str', delimiter= ',')
shows = [*set(shows)]

viewers = np.loadtxt("show_results.txt", usecols=2, dtype = 'str', delimiter=',')
#6
# for x in states:
#     print(x)
# for x in shows:
#     print (x)
# for x in viewers:
#     print(x)

#7

statesArr = np.array(states)
showsArr = np.array(shows)
viewersArr = np.array(viewers)

#8 
# print(statesArr)
# print(showsArr)
# print(viewersArr)

#9
statesArr = np.sort(statesArr)
showsArr = np.sort(showsArr)

# print(statesArr)
# print(showsArr)

#10
#using int64 to get rid of warning
viewersArr = viewersArr.astype(np.int64)
# print(viewersArr.dtype, viewersArr)

#11
viewersSum = np.sum(viewersArr)
#print(viewersSum)

#12
# print("Sorted array of states: ", statesArr, "\n\n Sorted array of shows: ", showsArr, "\n\nViewers list as ints ",viewersArr.dtype, 
#       "\n", viewersArr, "\n\n The total sum of viewers: " , viewersSum)

#13
show_raw_stats = pd.DataFrame(0, index = showsArr, columns= statesArr )
#print (show_raw_stats)

show_agg_stats = pd.DataFrame(0, index = showsArr, columns= ['Max', 'Min', 'Totals', 'Percent'])
#print (show_agg_stats)

