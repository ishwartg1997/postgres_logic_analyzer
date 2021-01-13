import re
from typing import List


def find_duplicate_assignment_line_nos(filename: str) -> List[int]:
    line_no = 0
    line_nos = []
    exp = r"(\s)+(.+(\))?)(\s+)*[!><]?=(\s+)*\2(\s+)"
    pattern = re.compile(exp)
    with open(filename) as fp:
        Lines = fp.readlines()
        for line in Lines:
            line_no += 1
            if bool(pattern.search(line)):
                line_nos.append(line_no)
    return line_nos


def format_report(line_nos: List[int]) -> None:
    if(len(line_nos) == 0):
        SUCCESS = '\033[92m'
        print(f"{SUCCESS}Success: No duplicate assignments found")
    else:
        for line_no in line_nos:
            FAILURE = '\033[91m'
            print(f"{FAILURE}Line{str(line_no)}: Boolean LHS=RHS")
