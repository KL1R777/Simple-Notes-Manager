import os





def create_files(file):
    try:

        with open(file, 'x') as f:
            print(f"Файл {file} успешно создан")

    except FileExistsError:
        print(f"Файл {file} уже создан")


def read_files(file):
    try:
        with open(file, 'r') as f:
            content = f.read()

            print(content)
    except FileNotFoundError:
        print(f"Файл {file} не найден")
        question = str(input("Хотите его создать (Y/N)? :"))
        print(question)

        if question.upper() == "Y":
            create_file(file)
        else:
            pass


def append_notes(file):
    try:
        note = str(input("Введите заметку которую хотите добавить: "))
        with open(file, 'a') as f:
            f.write(f'\n{note}')
            
           

            print(f"Заметка успешно добавлено в файл")
    except FileNotFoundError:
        print(f"Файл {file} не найден")


def delete_files(file):

    try:
        are_you_sure = str(input(f"Вы уверены что хотите удалить файл {file} (Y/N)?: "))

        if are_you_sure.upper() == "Y":
            os.remove(file)

            print(f"Файл успешно удален")
        else:
                print(f"По решению пользователя файл {file} не удален")

    except FileNotFoundError:
        print(f"Файл {file} был не найден либо был удален")


is_running = True


while is_running:
    try:
        print("-" * 15, end="")
        print("Менеджер заметок", end="")
        print("-" * 15)
        
        print("1. Создать файл")
        print("2. Прочитать файл")
        print("3. Добавить заметку в файл")
        print("4. Удалить файл")
        print("5. Выйти из менеджера")
        choice = int(input("Выберите опцию от 1-5: "))
        print(choice)

        if choice == 1:
            create_file = str(input("Введите название создания файла: "))
            print(create_file)

            create_files(create_file)

        elif choice == 2:
            read_file = str(input("Название файла: "))
            print(read_file)

            read_files(read_file)

        elif choice == 3:
            append_note_file = str(input("Название файла: "))
            print(append_note_file)
            append_notes(append_note_file)
        elif choice == 4:
            delete_file = str(input("Название файла: "))
            delete_files(delete_file)
        elif choice == 5:
            print("До свидания!")
            is_running = False
        else:
            print("Вы берите число в диапозоне от 1 до 5 (включительно)")

    except ValueError:
        print("Вы ввели не числовое значение!")