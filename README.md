## Postgres Logic Analyzer

Have you ever had annoying Postgres stuff where you've checked for a boolean involving the same variable on both sides when you didn't intend to do so?

This package is born from that as an additional means of sanity check and detects duplicate variable condition checks. The plan is to extend this and catch the errors that wouldn't be caught by a compiler

### How to Run

python3 analyzer.py {filename}.txt

There's a sample test_file.txt you can run it on right away!

### Dependencies

The package is currently super lightweight and uses everything that comes with a default Python installation


### Future

This was born out of a HackDay project
