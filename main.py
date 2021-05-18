from pyScheduling import FirstComeFirstServe, clear, HighestResponseRatioNext, ShortestJobFirst

types = """1. First Come - First Serve
2. Highest Response Ratio First
3. Shortest Job First

Select The Appropriate Scheduling Type: """

def re_run():
    if input("Want to run again ? (Y/n): ").upper() == "Y":
            start()
    input("Press enter to exit: ")
    quit()

def run_fifs(store_to_file):
    fifs = FirstComeFirstServe(store_to_file=store_to_file)
    fifs.print_gantt_chart()
    fifs.print_processes()
    fifs.print_computed_processes()
    fifs.print_final_averages()

def run_hrrn(store_to_file):
    hrrn = HighestResponseRatioNext(store_to_file=store_to_file)
    hrrn.print_gantt_chart()
    hrrn.print_processes()
    hrrn.print_computed_processes()
    hrrn.print_final_averages()

def run_sjn(store_to_file):
    sjf = ShortestJobFirst(store_to_file = store_to_file)
    sjf.calculateshortestJob()
    sjf.print_gantt_chart()
    sjf.print_computed_processes()
    sjf.print_processes()
    sjf.print_final_averages()
    sjf.removeColumn4()

def start(store_to_file: bool = False):
    clear()
    scheduling_type = input(types)
    if scheduling_type == "1":
        run_fifs(store_to_file)
        re_run()
    elif scheduling_type == "2":
        run_hrrn(store_to_file)
        re_run()
    elif scheduling_type == "3":
        run_sjn(store_to_file)
        re_run()
    else:
        clear()
        print("Oops. You selected an unknown value.")
        if input("Want to retry ? (Y/n): ").upper() == "Y":
            start()
        else:
            quit()


if __name__ == "__main__":
    clear()
    start(True if input("Want to store data to a file: (Y/n)").upper()
          == "Y" else False)
