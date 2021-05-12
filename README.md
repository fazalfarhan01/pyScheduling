# pyScheduling
A python package with implementations of Preemptive and Non-Preemptive Scheduling


# Example Usage
```PYTHON
from pyScheduling import FirstComeFirstServe, clear

types = """1. First Come - First Serve

Select The Appropriate Scheduling Type: """


def start():
    clear()
    scheduling_type = input(types)
    if scheduling_type == "1":
        fifs = FirstComeFirstServe()
        fifs.print_gantt_chart()
        fifs.print_processes()
        fifs.print_computed_processes()
        fifs.print_final_averages()
        if input("Want to run again ? (Y/n): ").upper() == "Y":
            start()
        input("Press enter to exit: ")
    else:
        clear()
        print("Oops. You selected an unknown value.")
        if input("Want to retry ? (Y/n): ").upper() == "Y":
            start()
        else:
            quit()


if __name__ == "__main__":
    start()
```