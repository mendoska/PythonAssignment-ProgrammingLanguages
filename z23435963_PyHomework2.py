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
print(arr, "\n")
#5
states = np.loadtxt("show_results.txt", usecols=0, dtype='str', delimiter = ",")
#removing duplicates
newStates = [*set(states)] 

shows = np.loadtxt("show_results.txt", usecols=1, dtype='str', delimiter= ',')
#removing duplicates
newShows = [*set(shows)]

viewers = np.loadtxt("show_results.txt", usecols=2, dtype = 'str', delimiter=',')
#6

for x in newStates:
    print(x)
print("\n")
for x in newShows:
    print (x)
print("\n")
for x in viewers:
    print(x)

#7

statesArr = np.array(newStates)
showsArr = np.array(newShows)
viewersArr = np.array(viewers)

#8 
print("\n")

print(statesArr)
print("\n")

print(showsArr)
print("\n")

print(viewersArr)

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
print("\n\nSorted array of states: ", statesArr, "\n\n Sorted array of shows: ", showsArr, "\n\nViewers list as ints ",viewersArr.dtype, 
     "\n", viewersArr, "\n\n The total sum of viewers: " , viewersSum)

#13
show_raw_stats = pd.DataFrame(0,index = showsArr, columns= statesArr )
#print (show_raw_stats)

show_agg_stats = pd.DataFrame(0,index = showsArr, columns= ['Max','Min','Totals','Percent'])
#print (show_agg_stats)

#print(show_raw_stats.index)

# states,shows,viewers are the original arrays

#14

# #will go through index
for ind in show_raw_stats.index:
    for s, st in enumerate(states):
       if (shows[s] == ind and states[s] == st):
        show_raw_stats.loc[ind,st] += np.int64(viewers[s]) 
      # print (show_raw_stats)
   


#15 
show_agg_stats['Max'] = show_raw_stats.max(axis=1)
show_agg_stats['Min'] = show_raw_stats.min(axis=1)
show_agg_stats['Totals'] = show_raw_stats.sum(axis=1)
show_agg_stats['Percent'] = round((show_agg_stats['Totals']/viewersSum) * 100,2)


# print("Percent total = " ,show_agg_stats['Percent'].sum())

#16
print("\n")
print(show_raw_stats)
print("\n")
print (show_agg_stats)

#17 

maxPercentName = show_agg_stats['Percent'].idxmax()
print("\nThe following show has the highest percentage: ", maxPercentName)
print(" with a percent of: ", show_agg_stats['Percent'].max(),"%")

minPercentName = show_agg_stats['Percent'].idxmin()
print("\nThe following show has the lowest percentage: ", minPercentName)
print(" with a percent of: ", show_agg_stats['Percent'].min(),"%")

print("\nMy favorite show is Better Call Saul")