## Task 1: Read a File and Handle Errors

## Objective: 
Write a Python program that:

Opens and reads a text file named sample.txt.

Prints its content line by line with line numbers.

Handles errors gracefully if the file does not exist.

## Functionality:
The program tries to open sample.txt and displays its contents line by line. If the file is not found, it shows a user-friendly error message instead of crashing.

## Example Output (if file exists):
Reading file content:
Line 1: This is a sample text file.
Line 2: It contains multiple lines.

## Example Output (if file does not exist):
Error: The file 'sample.txt' was not found.


## Task 2: Write and Append Data to a File
Objective:
Write a Python program that:

1: Takes user input and writes it to a file named output.txt.

2: Appends additional input to the same file.

3: Reads and displays the final contents of the file.

## Functionality:
The user is prompted to enter some text, which is written to output.txt. Then, the user can enter more text to append. Finally, the program reads and prints the full content of output.txt.

## Example Output:
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.

Enter additional text to append: Learning file handling in Python.
Data successfully appended.

Final content of output.txt:
Hello, Python!
Learning file handling in Python.


## How to Run the Programs
Run each Python file separately using a Python interpreter (Python 3.x):
python task1_read_file.py
python task2_write_append_file.py


Make sure the required files (sample.txt) exist in the same directory before running Task 1.
