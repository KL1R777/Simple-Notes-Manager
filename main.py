from files_utils.open_file import *
from files_utils.notes import *
from files_utils.delete_notes import *

print("=" * 16)
print("Менеджер заметок")
print("=" * 16)

is_running = True
   
   
while is_running:
    try:
        print("1. Проверка файла")
        print("2. Добавить заметку")
        print("3. Просмотреть заметки")
        print("4. Пронумеровать заметки")
        print("5. Удалить заметку")
        print("0. Выйти из менеджера")
        
        
        choice = int(input("Выберите пункт: "))
        
        if choice == 1:
            file = str(input("Название файла: "))
            
            print(open_file(file))
            
        elif choice == 2:
            file = str(input("Название файла: "))
            print(create_note(file))
            
        elif choice == 3:
            file = str(input("Название файла: "))
            print(check_notes(file))
            
        elif choice == 4:
            file = str(input("Название файла: "))
            print(list_notes(file))
        elif choice == 5:
            file = str(input("Название файла: "))
            index = int(input("Какую строку хотите удалить: "))
            print(delete_notes(file, index))
            
        elif choice == 0:
            print("До свидания!")
            is_running = False
        
        else:
            
            print("Введите число от 0 до 5 !!!")
            
    except Exception:
        print("Вы ввели нечисловые данные!!!")
         
    
         