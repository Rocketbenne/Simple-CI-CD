import pytest
import csv

# Run this Script in Commandline with:
# python tests/test_program_executes.py
#
# Checks if the csv file named Test_Program.csv 
# has the same contents as the reference csv

def read_csv(filepath):
    with open(filepath, mode='r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def test_csv():
    reference_path = 'tests/reference.csv'
    program_output_path = 'Test_Program.csv'

    reference_content = read_csv(reference_path)
    program_output_content = read_csv(program_output_path)

    assert reference_content == program_output_content

if __name__ == '__main__':
    pytest.main()