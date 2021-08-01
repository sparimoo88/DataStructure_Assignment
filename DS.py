#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
time_table_dict = {}
counter = 0
number_of_guards = 0
time_start = 0
time_end = 0
min_hours = 0
min_hours_guards = None
new_dict = {}
input_file = open('/Users/sukarmaparimoo/Documents/Studies/CMU/DataStructures/InputFiles/3.in')


# In[ ]:


number_of_guards = int(input_file.readline())
counter = counter + 1
#print(number_of_guards)
#print(counter)


# In[ ]:


for x in input_file:
    #print(x)
    time_start, time_end = x.split()
    time_start = int(time_start)
    time_end = int(time_end)
    #print(time_start, time_end)
    
    for start_time in range(time_start, time_end):
        if start_time in time_table_dict:
            time_table_dict[start_time] = [] 
        else :
            time_table_dict[start_time] = [counter]
        #print (time_table_dict[start_time])
    counter = counter + 1
#print(time_table_dict)


# In[ ]:


for time_start in time_table_dict:
    #print(time_start,time_table_dict[time_start])
    if len(time_table_dict[time_start]) == 1:
        value_in_new_dict = time_table_dict[time_start][0]
        if value_in_new_dict in new_dict:
            new_dict[value_in_new_dict] = new_dict[value_in_new_dict] + 1
        else :
            new_dict[value_in_new_dict] = 1
#print(new_dict)


# In[ ]:


for guards in range(1,(number_of_guards+1)):
    if guards not in new_dict:
        min_hours_guards = guards
        min_hours = 0
        break
    else:
        if new_dict[guards] < min_hours or min_hours_guards == None:
            min_hours = new_dict[guards]
            min_hours_guards = guards

total_coverage = len(time_table_dict)
max_coverage = total_coverage - min_hours
sys.stdout = open('/Users/sukarmaparimoo/Documents/Studies/CMU/DataStructures/OutputFiles/1.out','wt')
print("Guard no.%s"% min_hours_guards,"Solo min hours %s" % min_hours)
print("Fired %s" % min_hours_guards)
print(max_coverage)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




