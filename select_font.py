import os
import random

def get_random_font():
    font_directory = 'fonts/'
    
    # Получаем список всех файлов с расширением .ttf в директории
    font_files = [f for f in os.listdir(font_directory) if f.endswith('.ttf')]
    
    if not font_files:
        return "Нет доступных шрифтов."
    
    # Случайным образом выбираем один файл
    selected_font = random.choice(font_files)
 
    return f"Выбранный шрифт: {selected_font}"

# Пример использования
print(get_random_font())
