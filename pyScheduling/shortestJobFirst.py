from terminaltables import SingleTable
from .common import clear, sort_list_in_list, grab_inputs, custom_print

class ShortestJobFirst(object):
    def __init__(self, processes: list = None, total_processes: int = None,  store_to_file: bool = False) -> None:
        self.store_to_file = store_to_file
        self.total_number_of_process,self.total_process = grab_inputs(total_processes, processes)
        self.time = 0
        # print('Enter number of processes')
        # self.total_number_of_process = int(input())
        # self.total_process, self.time = [], 0
        # for i in range(self.total_number_of_process):
        #     self.proc = []
        #     print('Enter Process Id')
        #     self.proc.append(input())
        #     print('Enter arrival time')
        #     self.proc.append(int(input()))
        #     print('Enter execution time')
        #     self.proc.append(int(input()))
        #     self.total_process.append(self.proc)
        # print(self.total_process)
        self.total_process.sort(key = lambda total_process:total_process[1])
        # print(self.total_process)
        self.proc_queue = []
        self.arrival_time = 0
        self.arrange_eachprocess_on_Burst_time = []
        self.sum1 = 0 
        self.sum2 = 0
        self.avarage_TAT = 0
        self.avarage_WT = 0
        self.start_time = 0
        self.gantt_chart_header = ["START"]
        self.gantt_chart_timing = [0]
        self.store_to_file = False



    def calculateshortestJob(self):
    
        i = 0
        while (i < self.total_number_of_process):
            arrival_time = self.total_process[i][1]
            while( i < self.total_number_of_process and self.total_process[i][1] == arrival_time):
                self.arrange_eachprocess_on_Burst_time.append(self.total_process[i])
                i = i+1
            self.arrange_eachprocess_on_Burst_time.sort(key = lambda arrange_eachprocess_on_Burst_time:arrange_eachprocess_on_Burst_time[2])
            for proc in self.arrange_eachprocess_on_Burst_time:
                self.proc_queue.append(proc)
            self.arrange_eachprocess_on_Burst_time = []
            

        for each_Process_List in self.proc_queue:
            self.time = self.time if self.time > each_Process_List[1] else each_Process_List[1]
            self.time = self.time + each_Process_List[2]
            each_Process_List.append(self.time)
            # print(each_Process_List)
            each_Process_List.append(each_Process_List[3] - each_Process_List[2] - each_Process_List[1] if self.time > each_Process_List[1] else 0)
            each_Process_List.append(each_Process_List[3]-each_Process_List[1])
            each_Process_List.append(each_Process_List[5]/each_Process_List[2])

        
        for each_Process_List in self.proc_queue:
            self.sum1 = self.sum1 +each_Process_List[5];
            self.sum2 = self.sum2+ each_Process_List[6];
        self.avarage_TAT = self.sum1/float(self.total_number_of_process);
        self.avarage_WT = self.sum2/float(self.total_number_of_process);


        # print ('\n')
        # print ('{:<4} {:<12} {:<20} {:<20} {:<20} {:<20} '.format(*'PID_Arrival Time_Burst Time_Current Time_Total Arrival time_Waiting turnaround'.split('_')))
        # for proc in self.proc_queue:
        #     print ('{:<4} {:<12} {:<20} {:<20} {:<20} {:<20} '.format(proc[0],proc[1],proc[2],proc[3],proc[5],proc[6]))
        # print('Total_Average TAT = {} Total Average Wt = {}'.format(self.avarage_TAT,self.avarage_WT))

    def print_processes(self):
        table_data = [["Process ID", "Arrival Time", "Service Time"]]
        # print()
        table_data += sort_list_in_list(0, self.total_process)
        table = SingleTable(table_data)
        custom_print(self.store_to_file, table.table)
    
    def __create_gantt_chart(self):
        self.gantt_chart_header += ["--"]
        self.gantt_chart_timing += [self.start_time]
        self.gantt_chart_header += ["P"+str(single_process[0]) for single_process in self.proc_queue]
        self.gantt_chart_timing += [single_process[3] for single_process in self.proc_queue]

    def print_gantt_chart(self):
        clear()
        table_data = [
            self.gantt_chart_header,
            self.gantt_chart_timing
        ]
        table = SingleTable(table_data, "Gantt Chart")
        custom_print(self.store_to_file, table.table)

    def removeColumn4(self):
        # print(self.proc_queue)
        for i in range(self.total_number_of_process):
            try:
                # print(self.proc_queue[i][4])
                del self.proc_queue[i][4]
            except:
                pass

    def print_computed_processes(self):

        table_data = [["Process ID", "Arrival Time", "Service Time",
                       "Completed Time", "Turn Around Time", "Weighted TAT"]]
        self.removeColumn4()
        table_data += sort_list_in_list(0, self.proc_queue)
        table_data += [["Total", "---", "---", "---", sum([single_process[4] for single_process in self.proc_queue]), sum([
            single_process[5] for single_process in self.proc_queue])]]
        table = SingleTable(table_data)
        custom_print(self.store_to_file, table.table)

    def print_final_averages(self):
        turn_around_times = [single_process[4]
                             for single_process in self.proc_queue]
        weighted_turn_around_times = [single_process[5]
                                      for single_process in self.proc_queue]

        average_turn_around_time = round(
            sum(turn_around_times)/len(turn_around_times), 2)
        average_weighted_turn_around_time = round(
            sum(weighted_turn_around_times)/len(weighted_turn_around_times), 2)

        table = SingleTable([["Avg. TAT", "Avg. W-TAT"],
                            [average_turn_around_time, average_weighted_turn_around_time]])
        custom_print(self.store_to_file, table.table)


if __name__ == "__main__":

    # processes = [
    #     [1, 0, 3],
    #     [2, 2, 3],
    #     [3, 3, 5],
    #     [4, 4, 2],
    #     [5, 8, 3],
    # ]

    fifs = ShortestJobFirst()
    fifs.calculateshortestJob()
    fifs.print_gantt_chart()
    fifs.print_computed_processes()
    fifs.print_processes()
    fifs.print_final_averages()
    fifs.removeColumn4()
