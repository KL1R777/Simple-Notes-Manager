to_do_list = []
spin = True


def add_task():
    task = str(input("Добавьте задачу: "))

    to_do_list.append(task)



    

def remove_task():
    if to_do_list:
       num = int(input("Введите номер задачи для удаления: "))
       if(num >= 1 and num <= len(to_do_list)):
            removed = to_do_list.pop(num - 1)
            print("Задача успешно удалилась: ", removed)


       else:
           print(f"Не смогли найти задачу под номером: {num}, её, либо не существует либо вы не правильно ввели номер")
    else:
        print("В списке отсутствуют задачи!!! Удаление невозможно")


def check_lists():
    if to_do_list:
        print('Список задач: ')
        for index, name in enumerate(to_do_list, start=1):
            print(f'Задача № {index} : {name}')
    else:
        print("В списке ничего нету")

while spin:
    try:
        print("=" * 30 + " Менеджер задач " + "=" * 30)

        check_list = f"{1}. Посмотреть весь список задач"
        add_tasks = f"{2}. Добавить задачи"
        remove_tasks = f"{3}. Удалить задачи"
        remove_all_to_do_list = f"{4}. Удалить весь список задач"
        quit_in_to_do = f"{5}. Выйти из менеджера"
        print(check_list)
        print(add_tasks)
        print(remove_tasks)
        print(remove_all_to_do_list)
        print(quit_in_to_do)
        inp_manager = (int(input("Выберите пункт: ")))

        if inp_manager == 1:
            check_lists()


        elif inp_manager == 2:
            add_task()
            print("Задача добавилась успешно")
        elif inp_manager == 3:
            remove_task()

        elif inp_manager == 4:
            if to_do_list:
                to_do_list.clear()
            else:
                print("Список и так пустой!!! Удаление невозможно")

        elif inp_manager == 5:
            print("До свидания!")
            spin = False

        else:
            print("Выберите число от 1 до 5")
    except ValueError:
        print("Вы ввели не числовые данные")
        