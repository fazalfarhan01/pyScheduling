from .common import clear, grab_inputs, sort_list_in_list, custom_print
from terminaltables import SingleTable


class HighestResponseRatioNext(object):
    def __init__(self, processes: list = None, total_processes: int = None,  store_to_file: bool = False) -> None:
        self.total_processes, self.processes = grab_inputs(
            total_processes, processes)

        self.store_to_file = store_to_file

        self.processed_queue = []
        self.start_time = 0
        self.last_completed_time = 0

        self.first_run = True
        self.added = 1

        self.__start_basic_calculations()

    def __start_basic_calculations(self):
        self.sorted_queue = sort_list_in_list(1, self.processes)
        self.start_time = self.sorted_queue[0][1]
        self.last_start_time = self.sorted_queue[-1][1]
        self.to_be_processed_queue = [self.sorted_queue[0]]
        while (len(self.processed_queue) <= self.total_processes) and len(self.to_be_processed_queue) is not 0:
            self.__update_response_ratio()

            # for process_index in range(1):
            # single_process = self.to_be_processed_queue[process_index]
            single_process = self.to_be_processed_queue[0]

            index = single_process[0]
            arrival_time = single_process[1]
            service_time = single_process[2]

            if self.first_run:
                self.last_completed_time = arrival_time
                self.start_time = arrival_time
                self.first_run = False

            if arrival_time <= self.last_completed_time:
                completed_time = service_time + self.last_completed_time
            else:
                completed_time = arrival_time + service_time
            self.last_completed_time = completed_time
            turn_around_time = completed_time - arrival_time
            weighted_turn_around_time = round(
                turn_around_time/service_time, 2)
            data = [index, arrival_time, service_time, completed_time,
                    turn_around_time, weighted_turn_around_time]
            self.processed_queue.append(data)
            # print(data)

            self.__update_to_be_processed_queue()

    def __update_to_be_processed_queue(self):
        del self.to_be_processed_queue[0]

        for process_index in range(self.added, self.last_completed_time):
            try:
                self.to_be_processed_queue.append(
                    self.sorted_queue[process_index])
                self.added += 1
            except:
                pass

    def __update_response_ratio(self):
        if len(self.to_be_processed_queue) == 1:
            pass
        else:
            for process_index in range(len(self.to_be_processed_queue)):
                single_process = self.to_be_processed_queue[process_index]
                index = single_process[0]
                arrival_time = single_process[1]
                service_time = single_process[2]
                response_ratio = (self.last_completed_time -
                                  arrival_time + service_time)/service_time

                self.to_be_processed_queue[process_index] = [
                    index, arrival_time, service_time, response_ratio]
            self.to_be_processed_queue = sort_list_in_list(
                3, self.to_be_processed_queue, reverse=True)

    def print_gantt_chart(self):
        pass

    def print_processes(self):
        table_data = [["Process ID", "Arrival Time", "Service Time"]]
        table_data += sort_list_in_list(0, self.processes)
        table = SingleTable(table_data)
        custom_print(self.store_to_file, table.table)

    def print_computed_processes(self):
        table_data = [["Process ID", "Arrival Time", "Service Time",
                       "Completed Time", "Turn Around Time", "Weighted TAT"]]
        table_data += sort_list_in_list(0, self.processed_queue)
        table_data += [["Total", "---", "---", "---", sum([single_process[4] for single_process in self.processed_queue]), round(sum([
            single_process[5] for single_process in self.processed_queue]), 2)]]
        table = SingleTable(table_data)
        custom_print(self.store_to_file, table.table)

    def print_final_averages(self):
        turn_around_times = [single_process[4]
                             for single_process in self.processed_queue]
        weighted_turn_around_times = [single_process[5]
                                      for single_process in self.processed_queue]

        average_turn_around_time = round(
            sum(turn_around_times)/len(turn_around_times), 2)
        average_weighted_turn_around_time = round(
            sum(weighted_turn_around_times)/len(weighted_turn_around_times), 2)

        table = SingleTable([["Avg. TAT", "Avg. W-TAT"],
                            [average_turn_around_time, average_weighted_turn_around_time]])
        custom_print(self.store_to_file, table.table)


if __name__ == "__main__":
    data = [
            [1, 0, 3],
            [2, 2, 6],
            [3, 4, 4],
            [4, 6, 5],
            [5, 8, 2],
        ]
    hrrn = HighestResponseRatioNext()
    # print(hrrn.processed_queue)
    hrrn.print_processes()
    hrrn.print_computed_processes()
    hrrn.print_final_averages()
