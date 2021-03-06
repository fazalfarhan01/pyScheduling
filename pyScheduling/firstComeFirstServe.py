from terminaltables import SingleTable
from .common import clear, grab_inputs, sort_list_in_list, custom_print


class FirstComeFirstServe(object):
    def __init__(self, total_processes: int = None, processes: list = None, store_to_file:bool=False) -> None:
        self.total_processes, self.processes = grab_inputs(total_processes, processes)

        self.store_to_file = store_to_file

        self.first_run = True

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
            if arrival_time <= self.last_completed_time:
                completed_time = service_time + self.last_completed_time
            else:
                completed_time = arrival_time + service_time
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
        custom_print(self.store_to_file, table.table)

    def print_processes(self):
        table_data = [["Process ID", "Arrival Time", "Service Time"]]
        table_data += sort_list_in_list(0, self.processes)
        table = SingleTable(table_data)
        custom_print(self.store_to_file, table.table)

    def print_computed_processes(self):
        table_data = [["Process ID", "Arrival Time", "Service Time",
                       "Completed Time", "Turn Around Time", "Weighted TAT"]]
        table_data += sort_list_in_list(0, self.processes_computed)
        
        table_data += [["Total", "---", "---", "---", sum([single_process[4] for single_process in self.processes_computed]), sum([
            single_process[4] for single_process in self.processes_computed])]]
        table = SingleTable(table_data)
        custom_print(self.store_to_file, table.table)

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
        custom_print(self.store_to_file, table.table)


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
