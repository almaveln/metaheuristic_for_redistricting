from entities import Unit
from typing import Iterable
import time
import csv


def verify_units_not_in_collection(units: Iterable[Unit], collection: Iterable[Unit]):
    for unit in units:
        if unit in collection:
            return False
    return True


class CumulativeTime:
    start = 0
    finish = 0

    @classmethod
    def initialize(cls):
        cls.start = time.time()

    @classmethod
    def get_cumtime(cls):
        return time.time() - cls.start


def get_current_time() -> str:
    return time.strftime("%Y-%m-%d_%H:%M:%S", time.gmtime())


def create_csv_file(file, csv_head: list):
    """Creates a CSV file"""

    with open(file, "a", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter="|", quoting=csv.QUOTE_NONE, lineterminator="\n")
        writer.writerow(csv_head)


def write_to_csv_file(file, csv_row: list):
    """Used to output information about the elite solution for further analysis"""

    with open(file, "a", newline="") as csvfile:
        # escapechar='\\' - not useful in DataFrame
        writer = csv.writer(csvfile, delimiter="|", quoting=csv.QUOTE_NONE, lineterminator="\n", quotechar='')
        writer.writerow(csv_row)
