# Features included:
#    - Read log
#    - List exsiting log
#    - Write to log
#    - Automated get time of each log line
#    - Users can specify the log file's name
#    - Confirm before commit
from datetime import datetime
import os
import pathlib


while True:
    print('-----------------------------------------------------------')
    print("\t\tA simple program to write your log!")
    option = input('Press q to cancel or any key to continue. ').lower()
    if option == 'q':
        break

    dir_name = 'log_dir/'
    dir_exist = os.path.exists(dir_name)
    if dir_exist is False:
        os.makedirs(dir_name)

    print('Exist files: ', end='')
    file_in_dir = [f for f in os.listdir(dir_name) if os.path.isfile(os.path.join(dir_name, f))]
    if len(file_in_dir) == 0:
        print('None')
    else:
        for i in file_in_dir:
            print(i)

    print("\nPlease specify the log file name.")
    print("Otherwise, the default one will be used: log.txt")

    file_name = 'log.txt'
    name_change = input('> ').strip()
    if name_change:
        file_name = name_change
    file_exist = os.path.exists(f'log_dir/{file_name}')
    if file_exist is False:
        pathlib.Path(f'log_dir/{file_name}').touch()

    with open(f'log_dir/{file_name}', 'a+') as f_obj:

        while True:
            print('----------------------------------------------------')
            print('Options:')
            print('\t1. Read log')
            print('\t2. Write to log')
            print('Or press any other keys to go back')

            option = input('> ').strip()
            if option != '1' and option != '2':
                break
            elif option == '1':
                f_obj.seek(0)
                print('-------------------------------------------------')
                print('Options:')
                print('\t1. Read last log')
                print('\t2. Read all log')
                print('Or press any other keys to go back')
                option = input('> ').strip()
                if option != '1' and option != '2':
                    continue
                elif option == '1':
                    line_ls = f_obj.readlines()
                    if len(line_ls) == 0:
                        print('Log is empty!')
                        input("\nPress any key to continue")
                        continue
                    print(line_ls[-1])
                    input('\nPress any key to continue.')
                    continue
                elif option == '2':
                    all_log = f_obj.readlines()
                    if len(all_log) == 0:
                        print('Log is empty!')
                        input("\nPress any key to continue")
                        continue
                    for line in all_log:
                        print(line)
                    input("\nPress any key to continue")
                    continue
            elif option == '2':
                print('-----------------------------------------------')
                print("Write to log: ")
                to_log = input('> ').strip()
                if not to_log:
                    continue
                print(f"Confirm write to log: {file_name}\nLine: {to_log}")
                option = input('y/n: ').lower().strip()
                if option == 'y':
                    current_time = datetime.now().strftime('%d-%m-%Y %H:%M')
                    f_obj.write(f'{current_time}: {to_log}\n')
                    print('Log file written')
                    input("Press any key to continue")
                break
