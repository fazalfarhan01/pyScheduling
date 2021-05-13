from terminaltables import SingleTable
from .common import clear, sort_list_in_list
import io

class FirstComeFirstServe(object):
    def __init__(self, total_processes: int = None, processes: list = None, store_to_file:bool=False) -> None:
        if total_processes == None:
            clear()
            total_processes = int(
                input("Enter the total number of processes: "))

        self.total_processed = total_processes

        if processes == None:
            processes = []
            for process_number in range(total_processes):
                process = []
                clear()
                process.append(process_number+1)
                process.append(
                    int(input("Enter the Arrival Time for P{}: ".format(process_number+1))))
                process.append(
                    int(input("Enter the Service/Burst Time for P{}: ".format(process_number+1))))
                processes.append(process)

        self.store_to_file = store_to_file

        self.first_run = True

        self.processes = processes
        self.processes_computed = []
        self.last_completed_time = 0
        self.start_time = 0

        self.gantt_chart_header = ["START"]
        self.gantt_chart_timing = [0]

        self.processes = sort_list_in_list(1, self.processes)
        self.__start_basic_calculations()
        # self.__create_gantt_chart()

    def __start_basic_calculations(self):
        clear()
        for process_index in range(len(self.processes)):
            single_process = self.processes[process_index]
            index = single_process[0]
            arrival_time = single_process[1]

            if self.last_completed_time < arrival_time:
                self.gantt_chart_header += ["--"]
                self.gantt_chart_timing += [arrival_time]

            # CORRECTION FOR INITIAL START TIME
            if self.first_run:
                self.last_completed_time = arrival_time
                self.start_time = arrival_time
                self.first_run = False
            
            service_time = single_process[2]
            completed_time = service_time + arrival_time
            self.last_completed_time = completed_time
            turn_around_time = completed_time - arrival_time
            weighted_turn_around_time = round(turn_around_time/service_time, 2)
            self.processes_computed.append(
                [index, arrival_time, service_time, completed_time, turn_around_time, weighted_turn_around_time])
            self.gantt_chart_header += ["P"+str(index)]
            self.gantt_chart_timing += [completed_time]

    def __create_gantt_chart(self):
        if self.start_time != 0:
            self.gantt_chart_header += ["--"]
            self.gantt_chart_timing += [self.start_time]
        self.gantt_chart_header += ["P"+str(single_process[0]) for single_process in self.processes]
        self.gantt_chart_timing += [single_process[3] for single_process in self.processes_computed]

    def print_gantt_chart(self):
        clear()
        table_data = [
            self.gantt_chart_header,
            self.gantt_chart_timing
        ]
        table = SingleTable(table_data, "Gantt Chart")
        self.__custom_print(table.table)

    def print_processes(self):
        table_data = [["Process ID", "Arrival Time", "Service Time"]]
        table_data += sort_list_in_list(0, self.processes)
        table = SingleTable(table_data)
        self.__custom_print(table.table)

    def print_computed_processes(self):
        table_data = [["Process ID", "Arrival Time", "Service Time",
                       "Completed Time", "Turn Around Time", "Weighted TAT"]]
        table_data += sort_list_in_list(0, self.processes_computed)
        
        table_data += [["Total", "---", "---", "---", sum([single_process[4] for single_process in self.processes_computed]), sum([
            single_process[4] for single_process in self.processes_computed])]]
        table = SingleTable(table_data)
        self.__custom_print(table.table)

    def print_final_averages(self):
        turn_around_times = [single_process[4]
                             for single_process in self.processes_computed]
        weighted_turn_around_times = [single_process[5]
                                      for single_process in self.processes_computed]

        average_turn_around_time = round(
            sum(turn_around_times)/len(turn_around_times), 2)
        average_weighted_turn_around_time = round(
            sum(weighted_turn_around_times)/len(weighted_turn_around_times), 2)

        table = SingleTable([["Avg. TAT", "Avg. W-TAT"],
                            [average_turn_around_time, average_weighted_turn_around_time]])
        self.__custom_print(table.table)

    def __custom_print(self, data_to_print):
        if self.store_to_file:
            with io.open("./solution.txt", "a", encoding="utf-8") as solution:
                solution.write(data_to_print+"\n")
        print(data_to_print)


if __name__ == "__main__":

    processes = [
        [1, 0, 3],
        [2, 2, 3],
        [3, 3, 5],
        [4, 4, 2],
        [5, 8, 3],
    ]

    fifs = FirstComeFirstServe(5, processes)
    fifs.print_gantt_chart()
    fifs.print_processes()
    fifs.print_computed_processes()
    fifs.print_final_averages()
