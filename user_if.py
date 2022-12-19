from os.path import exists
from csv_file import creating
from list_import import writing_scv, writing_txt, get_info
from list_export import from_file

def view():
    print(from_file('Phonebook.txt'))

def record_info():
    info = get_info()
    writing_scv(info)
    writing_txt(info)

def user_choice():
    flag = input('Привет! Для начала работы со справочником нажмите \'+\', или просто нажмите Enter для завершения работы: ')
    while (flag == '+'):
        path = 'Phonebook.csv'
        valid = exists(path)
        if not valid:
            creating()
        choice_action = input('Введите \'+\', если хотите записать новые данные, или просто нажмите Enter, если хотите просмотреть справочник в консоли: ')
        if choice_action == '+':
            record_info()
        else:
            view()
        flag = input('Для продолжения работы нажмите \'+\', или просто нажмите Enter для завершения работы: ')
    print('Пока.')