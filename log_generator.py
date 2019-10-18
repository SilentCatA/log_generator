# Features included:
#    - Write to log
#    - Automated get time of each log line
#    - Confirm before commit
from datetime import datetime
import os
import pathlib

dir_name = 'log_dir/'
dir_exist = os.path.exists(dir_name)
if dir_exist is False:
    os.makedirs(dir_name)

file_name = 'log.txt'
file_exist = os.path.exists(f'log_dir/{file_name}')
if file_exist is False:
    pathlib.Path(f'log_dir/{file_name}').touch()

with open(f'log_dir/{file_name}', 'a+') as f_obj:

    print("Write to log: ")
    to_log = input('> ').strip()
    print(f"Confirm write to log: {file_name}\nLine: {to_log}")
    option = input('y/n: ').lower().strip()
    if option == 'y':
        current_time = datetime.now().strftime('%d-%m-%Y %H:%M')
        f_obj.write(f'{current_time}: {to_log}\n')
        print('Log file written')
    else:
        print('Aborted!')
