from common import clear, grab_inputs


class HighestResponseRatioNext(object):
    def __init__(self, processes: list = None, total_processes: int = None,  store_to_file: bool = False) -> None:
        self.total_processes, self.processes = grab_inputs(
            total_processes, processes)


if __name__ == "__main__":
    hrrn = HighestResponseRatioNext(
        [
            [1, 0, 3],
            [2, 2, 6],
            [3, 4, 4],
            [4, 6, 5],
            [5, 8, 2],
        ])
    print(hrrn.total_processes)
    print(hrrn.processes)
