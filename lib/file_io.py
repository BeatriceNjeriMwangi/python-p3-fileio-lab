
from pathlib import Path
def write_file(file_name, file_content):
    file_path=f"{file_name}.txt"
    with open(file_path, mode='w',encoding='utf-8') as file:
        file.write(file_content)

    

def append_file(file_name, append_content):

    file_path=f"{file_name}.txt"
    with open(file_path, mode='a') as file:
        file.write(append_content)

def read_file(file_name):
    file_path=f"{file_name}.txt"
    with open(file_path, 'r') as f:
        return f.read()
write_file(file_name="logfile", file_content="Log 1: 5 bananas added" )
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

read_file(file_name="logfile")
   
