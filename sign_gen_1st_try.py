from PIL import Image, ImageDraw, ImageFont
import random

def generate_signature(name):
    # Настройка параметров изображения
    width, height = 400, 100
    background_color = (255, 255, 255)  # Белый фон
    text_color = (0, 0, 0)  # Черный цвет текста

    # Создание изображения
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Загрузка шрифта (путь к файлу шрифта .ttf)
    font_path = "fonts/Purisa.ttf"
    font_size = 40
    font = ImageFont.truetype(font_path, font_size)

    # Генерация случайного смещения для создания эффекта рукописного текста
    x_offset = random.randint(5, 15)
    y_offset = random.randint(-5, 5)

    # Рисование текста на изображении
    draw.text((x_offset, height // 4 + y_offset), name, fill=text_color, font=font)

    # Сохранение изображения
    image.save('signature.png')

# Пример использования
generate_signature("Poueb Angpeu")
