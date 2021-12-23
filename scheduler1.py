"""
1. Разработать структуру для хранения информации для отображения списка дел
в привязке к датам. Учитывайте, что к одной дате могут относиться сразу несколько дел.
Попробуйте поиграться с этим списком - программно добавьте новое дело или удалите его.
Программно попробуйте удалить все дела за выбранную дату.

2. Домашнее задание: на основе прошлого домашнего задания доработать скрипт таким образом,
чтобы запрашивать у пользователя информацию о списке дел. Пример:
Введите дату: 01-01-2011
Введите дело, которое нужно не забыть: помыть посуду
После этого на экран должно быть выведено:
Список дел на  01-01-2011:
- сходить на тренировку
- помыть посуду

3. Усовершенствуйте вашу программу-органайзер из прошлого ДЗ:
проведите рефакторинг кода и разбейте логически обособленные участки кода на функции и
предусмотрите обработку возможных возникающих исключений.

4. Усовершенствуйте вашу программу-органайзер из прошлого ДЗ:
добавьте подключение к json-файлу, который бы являлся хранилищем информации о делах (по сути аналогом базы данных).
Реализуйте вывод списка дел за выбранную дату на экран. Дату запрашивать у пользователя через консоль.
При добавлении нового дела предусмотрите, чтобы эта информация была зафиксирована в json-файле.

"""


import json
import codecs
from datetime import datetime
import pickle
# import heartrate
# heartrate.trace(browser=True)
# import snoop


#
# task_manager = {
#     '06.12.2021': [
#         {
#
#             'description': 'watch the video',
#             'status': 'done'
#         },
#         {
#
#             'description': 'Design a structure to store information for displaying a to-do list in relation to dates',
#             'status': 'not performed'
#         },
#         {
#
#             'description': 'bla-bla-bla',
#             'status': 'not performed'
#         }
#         ],
#     '07.12.2021': [
#         {
#             'description': 'watch the video',
#             'status': 'not performed'
#         },
#         {
#             'description': 'do your homework',
#             'status': 'not performed'
#         }
#     ]
#
# }
#
#
# new_date = '08.12.2021'
# new_task = [
#     {
#         'description': 'write to the mentor',
#         'status': 'not performed'
#     },
#     {
#
#        'description': 'parse type conversion',
#        'status': 'not performed'
#     }
#
# ]
#
# task_manager[new_date] = new_task





#print(task_manager)
#del task_manager['08.12.2021']
#task_manager['06.12.2021'].pop(1)
#print(task_manager)


# def write_read_file():
#     with open("data_content.json", "a", encoding="utf-8") as f:
#         json.dump(task_manager, f, ensure_ascii=False)
#     with open("data_content.json", "r", encoding="utf-8") as read_file:
#         data_task = json.load(read_file)
#     return data_task



def back():
    print('Продолжить?')
    continue_add = input('ДА или НЕТ:')
    if continue_add.casefold() == 'да'.casefold():
        menu()
    else:
       print("Выход из планировщика задач...")




def specific_to_do_list():
    while True:
        enter_date = input('Введите дату через точку:')
        try:
            datetime.strptime(enter_date, '%d.%m.%Y')
            break
        except ValueError:
            print('\u001b[1m', 'Некоректная дата ввода! ВВЕДИТЕ ДАТУ В ФОРМАТЕ ДЕНЬ.МЕСЯЦ.ГОД')
            continue
    if enter_date in task_manager:
        description = [desc['description'] for desc in task_manager[enter_date]]
        print('Все дела, которые нужно осилить в этот день:', '\n---'.join(map(str, description)), sep='\n---')
    else:
        print('Не найдено никаких дел')
        back()
    back()
#specific_to_do_list()



def add_to_do_list():
    while True:
        add_date = input('Введите дату через точку:')
        try:
            datetime.strptime(add_date, '%d.%m.%Y')
            break
        except ValueError:
            print('\u001b[1m', 'Некоректная дата ввода! ВВЕДИТЕ ДАТУ В',  'ФОРМАТЕ ДЕНЬ.МЕСЯЦ.ГОД')
            continue
    add_description = input("Введите дело, которое нужно не забыть сделать:")
    add_status = input('Поставьте метку, что дело сделано или не сделано:')
    if add_date not in  task_manager:
        new_task1 = [
            {
                'description': add_description,
                'status': add_status
            }
        ]
        task_manager[add_date] = new_task1

    elif add_date in task_manager:
        task_manager[add_date].append({'description': add_description, 'status': add_status})
    # with open("info.json", "a") as data:
    #         information = {add_date: {'description': add_description, 'status': add_status}}
    #         data.write(json.dumps(information))
    #         data.close()
    return  back()
#add_to_do_list()


def all_affairs():
    for all_date in task_manager:
        all_description = [all_desc['description'] for all_desc in task_manager[all_date]]
        print('\u270e', 'Дата:', all_date, '\u270d', 'Список дел:', *all_description, sep='\n')
    return  back()



def delete_affairs_date():
    while True:
        enter_date_affair = input('Введите дату через точку:')
        try:
            datetime.strptime(enter_date_affair, '%d.%m.%Y')
            break
        except ValueError:
            print('\u001b[1m', 'Некоректная дата ввода! ВВЕДИТЕ ДАТУ В ФОРМАТЕ ДЕНЬ.МЕСЯЦ.ГОД')
            continue
    if enter_date_affair in task_manager:
        del task_manager[enter_date_affair]
        print("Вы удалили все записи дел за", enter_date_affair)
    else:
        print("Данная дата не найдена")
    back()

# def delete_affairs_status():
#     #enter_affair = input('Введите дело, которое хотите удалить:')
#     for
#     for status_affair in task_manager:
#         if status_affair == 'done':
#             task_manager[status_affair].clear()
#             print("Вы удалили все сделанные дела")
#
#     back()

with open("info.json", "r") as tasks_json:
    task_manager = json.load(tasks_json)


def menu():
    answer = input("---> Просмотреть список дел на конкретную дату, нажмите 1\n"
                   "---> Добавить список новых дел на новый день или добавить на уже созданные дни, нажмите 2\n"
                    '---> Просмотреть все созданные дела, нажмите 3\n'
                    '---> Удалить все дела за выбраную дату, нажмите 4\n')
    if answer == '1':
        specific_to_do_list()
    elif answer == '2':
        add_to_do_list()
    elif answer == '3':
        all_affairs()
    elif answer == '4':
        delete_affairs_date()
    # elif answer == '5':
    #     delete_affairs_status()
    with open("info.json", "w", encoding="utf-8") as tasks_json:
        json.dump(task_manager, tasks_json, indent=4, ensure_ascii=False)

menu()
