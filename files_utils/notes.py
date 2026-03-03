


def create_note(file):
    try:
        with open(file, "a") as f:
            note = input("Введите заметку: ")
            f.write(f"\n{note}")
            return "Заметка добавлена"
    except FileNotFoundError:
        return f'Файл не найден! (Чтобы проверить, откройте файл)'
    
    
def check_notes(file):
    try:
        with open(file, 'r') as f:
            return (f.read())
            
    except FileNotFoundError:
        return f"Файл не найден! (Откройте файл, для проверки)"
    
    
lines = []
      
def list_notes(file):
    try:
        
        with open(file, "r") as f:
            if f:
                for x in f:
                    
                    lines.append(x)
            else:
                return "Файл пустой, нумерация невозможно!"
                    
                    
            with open(file, "w") as f:
                for index, s in enumerate(lines, start=1):
                        f.write(f"{index}. {s}")
                    
                return f"Нумерация файла прошла успешно!"
                    
            
            
    except FileNotFoundError:
        return "Файл не найден!!!"
    
    
if __name__ == "__main__":
    print(list_notes("text.txt"))