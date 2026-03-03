

lines = []
def delete_notes(file, index):
    try:
        with open(file, "r+") as f:
            if f:
                for x in f:
                    lines.append(x)
                
                lines.pop(index - 1)
                
                
            
            else:
                return "Файл пустой"
            
        with open(file, "w") as f:
            for x in lines:
                f.write(x)
                
            lines.clear()
                
            return "Заметка успешно удалена!"
            
    except FileNotFoundError:
        return f"Файл не найден!"
    
    
    
if __name__ == "__main__":
    delete_notes("text.txt", 1)
    print(lines)
    

        
        