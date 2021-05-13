from common import clear, grab_inputs, sort_list_in_list


class HighestResponseRatioNext(object):
    def __init__(self, processes: list = None, total_processes: int = None,  store_to_file: bool = False) -> None:
        self.total_processes, self.processes = grab_inputs(
            total_processes, processes)

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
            data = [index, arrival_time, service_time, completed_time, turn_around_time, weighted_turn_around_time]
            self.processed_queue.append(data)
            # print(data)

            self.__update_to_be_processed_queue()

    def __update_to_be_processed_queue(self):
        print("B4: ", end="")
        print(self.to_be_processed_queue)
        del self.to_be_processed_queue[0]
        print("AF: ", end="")
        print(self.to_be_processed_queue)

        for process_index in range(self.added, self.last_completed_time):
            try:
                self.to_be_processed_queue.append(self.sorted_queue[process_index])
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


if __name__ == "__main__":
    hrrn = HighestResponseRatioNext(
        [
            [1, 0, 3],
            [2, 2, 6],
            [3, 4, 4],
            [4, 6, 5],
            [5, 8, 2],
        ])
    print(hrrn.processed_queue)
