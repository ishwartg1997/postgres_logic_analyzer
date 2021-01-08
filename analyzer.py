import sys
from sql_regex_check import find_duplicate_assignment_line_nos, format_report


def main() -> None:
    if(len(sys.argv) < 2):
        raise ValueError("Run it as python3 analyzer.py {filename}")
    filename = sys.argv[1]
    line_nos = find_duplicate_assignment_line_nos(filename)
    format_report(line_nos)


if __name__ == "__main__":
    main()
