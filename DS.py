import sys
input_file = open("/Users/sukarmaparimoo/Documents/Studies/CMU/DataStructures/InputFiles/10.in")
number_of_guards = input_file.readline()
number_of_guards = int(number_of_guards)
#print(number_of_guards)
guard_timestamps = []

for x in input_file:
    #print(x)
    (start_time, end_time) = x.split()
    start_time = int(start_time)
    end_time = int(end_time)
    list1 = [start_time,end_time]
    guard_timestamps.append(list1)

guard_timestamps.sort()
#print(guard_timestamps[:11])
#print(len(guard_timestamps))
total_coverage = 0
alone_time = {}
previous = None
previous_index = 0
for index,time_range in enumerate(guard_timestamps):
    if index == 0:
        coverage = int((time_range[1]) - time_range[0])
        #print(coverage)
        total_coverage = coverage
        alone_time[index] = coverage
    else:
        #previous = guard_timestamps[index-1]
        #print(time_range,guard_timestamps[index-1])
        if alone_time[index-1] > 0:
            previous = guard_timestamps[index-1]
            previous_index = index-1
        if (previous[1] > time_range[0]) and (time_range[1] > previous[1]):
            coverage = int((time_range[1]) - previous[1])
            #print(time_range[1])
            #print(previous[1])
            #print(coverage)
            total_coverage = total_coverage + coverage
            overlap = int(previous[1]-time_range[0])
            alone_time[index] = coverage
            if overlap <= alone_time[previous_index]:
                alone_time[previous_index] = int(alone_time[previous_index] - overlap)
            else:
                print(time_range,previous,alone_time[previous_index],overlap,coverage)
        elif (previous[1] > time_range[0]) and (time_range[1] < previous[1]):
            overlap = int(time_range[1] - time_range[0])
            alone_time[index] = 0
            #if alone_time[index-1]:
                #alone_time[index - 1] = int(alone_time[index - 1] - overlap)
        else:
            coverage = int((time_range[1]) - time_range[0])
            total_coverage = total_coverage + coverage
            alone_time[index] = coverage

#print(total_coverage)
#print(alone_time)
min_alone_time = min(alone_time.values())
#print(min_alone_time)
max_coverage = total_coverage - min_alone_time
sys.stdout = open('/Users/sukarmaparimoo/Documents/Studies/CMU/DataStructures/OutputFiles/10.out','wt')
print(max_coverage)
