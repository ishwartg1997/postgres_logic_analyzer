from sql_regex_check import find_duplicate_assignment_line_nos


def test_find_duplicate_assignment_line_nos() -> None:
    filename = "test_file.txt"
    line_nos = find_duplicate_assignment_line_nos(filename)
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert line_nos == expected
