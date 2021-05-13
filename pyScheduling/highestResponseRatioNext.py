from common import clear

class HighestResponseRatioNext(object):
    def __init__(self, total_processes: int = None, processes: list = None, store_to_file:bool=False) -> None:
        if total_processes == None:
            if processes == None:
                clear()
                self.total_processes = int(
                    input("Enter the total number of processes: "))
                processes = []
                for process_number in range(self.total_processes):
                    process = []
                    clear()
                    process.append(process_number+1)
                    process.append(
                        int(input("Enter the Arrival Time for P{}: ".format(process_number+1))))
                    process.append(
                        int(input("Enter the Service/Burst Time for P{}: ".format(process_number+1))))
                    processes.append(process)
                self.processes = processes
            else:
                self.total_processes = len(processes)

if __name__ == "__main__":
    hrrn = HighestResponseRatioNext()
    print(hrrn.total_processes)
    print(hrrn.processes)