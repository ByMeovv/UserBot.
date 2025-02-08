from my_logger.logger import log

from io import BytesIO
from PIL import Image

import requests
import time


def download_image(url: str, output_file: str):
    start_time = time.time()

    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    # Создаем объект BytesIO
    img_byte_arr = BytesIO()
    img_byte_arr.seek(0)

    # Сохраняем изображение в объект BytesIO
    img.save(img_byte_arr, format='JPEG')

    # Получаем байты изображения
    img_byte_arr = img_byte_arr.getvalue()

    # Записываем байты изображения в файл
    with open(output_file, 'wb') as f:
        f.write(img_byte_arr)

    end_time = time.time()
    t = end_time - start_time
    return log.debug(f"Time: {t}")


