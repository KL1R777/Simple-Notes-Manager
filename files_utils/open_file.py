import time

def open_file(file):
    try:
        with open(file, "r+", encoding='utf-8') as f:
            return f"{file} найден! Можете его использовать"
            
    except FileNotFoundError:
        print(f"{file} не найден, создаем новый...")
        time.sleep(1.5)
        with open(file, 'x') as f:
            return f"{file} создан успешно!"
            
            
        


