from pyScheduling.firstComeFirstServe import FirstComeFirstServe, clear

types = """1. First Come - First Serve

Select The Appropriate Scheduling Type: """

def start():
    scheduling_type = int(input(types))
    if scheduling_type == 1:
        fifs = FirstComeFirstServe()
        fifs.print_gantt_chart()
        fifs.print_processes()
        fifs.print_computed_processes()
        fifs.print_final_averages()
        input("Press enter to exit: ")
    else:
        print("Oops. You selected an unknown value.")
        if input("Want to retry ? (Y/n): ").upper() == "Y":
            start()
        else:
            quit()


if __name__ == "__main__":
    clear()
    start()