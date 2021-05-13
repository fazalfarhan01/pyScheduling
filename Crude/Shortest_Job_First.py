print('Enter number of processes')
total_number_of_process = int(input())
total_process, time = [], 0
for i in range(total_number_of_process):
    proc = []
    print('Enter Process Id')
    proc.append(input())
    print('Enter arrival time')
    proc.append(int(input()))
    print('Enter execution time')
    proc.append(int(input()))
    total_process.append(proc)
# total_process = [['1', 2, 3], ['2', 3, 4], ['3', 4, 5], ['4', 5, 3]]

total_process.sort(key = lambda total_process:total_process[1])
print(total_process)
proc_queue = []

arrange_eachprocess_on_Burst_time = []
i = 0
while (i < total_number_of_process):
    arrival_time = total_process[i][1]
    while( i < total_number_of_process and total_process[i][1] == arrival_time):
        arrange_eachprocess_on_Burst_time.append(total_process[i])
        i = i+1
    arrange_eachprocess_on_Burst_time.sort(key = lambda arrange_eachprocess_on_Burst_time:arrange_eachprocess_on_Burst_time[2])
    for proc in arrange_eachprocess_on_Burst_time:
        proc_queue.append(proc)
    arrange_eachprocess_on_Burst_time = []
    

for each_Process_List in proc_queue:
    Completed_Time = Completed_Time if Completed_Time > each_Process_List[1] else each_Process_List[1]
    Completed_Time = Completed_Time + each_Process_List[2]
    each_Process_List.append(Completed_Time)
    print(each_Process_List)
    each_Process_List.append(each_Process_List[3] - each_Process_List[2] - each_Process_List[1] if time > each_Process_List[1] else 0)
    each_Process_List.append(each_Process_List[3]-each_Process_List[1])
    each_Process_List.append(each_Process_List[5]/each_Process_List[2])

sum1,sum2 = 0,0
for each_Process_List in proc_queue:
    sum1 = sum1 +each_Process_List[5];
    sum2 = sum2+ each_Process_List[6];
avarage_TAT = sum1/float(total_number_of_process);
avarage_WT = sum2/float(total_number_of_process);
  
print ('\n')
print ('{:<4} {:<12} {:<20} {:<20} {:<20} {:<20} '.format(*'PID_Arrival Time_Burst Time_Current Time_Total Arrival time_Waiting turnaround'.split('_')))
for proc in proc_queue:
    print ('{:<4} {:<12} {:<20} {:<20} {:<20} {:<20} '.format(proc[0],proc[1],proc[2],proc[3],proc[5],proc[6]))
print('Total_Average TAT = {} Total Average Wt = {}'.format(avarage_TAT,avarage_WT))