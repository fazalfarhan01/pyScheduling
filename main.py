from pyScheduling import FirstComeFirstServe, clear

types = """1. First Come - First Serve

Select The Appropriate Scheduling Type: """

def run_fifs(store_to_file):
    fifs = FirstComeFirstServe(store_to_file=store_to_file)
    fifs.print_gantt_chart()
    fifs.print_processes()
    fifs.print_computed_processes()
    fifs.print_final_averages()

def start(store_to_file: bool = False):
    clear()
    scheduling_type = input(types)
    if scheduling_type == "1":
        run_fifs(store_to_file)
        if input("Want to run again ? (Y/n): ").upper() == "Y":
            start()
        input("Press enter to exit: ")
        quit()

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
