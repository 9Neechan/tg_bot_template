import os

from bot.db.requests.cathegory import (
    update_descr,
    get_descriptions,
    get_col_name
)

abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
example_photo_path = os.path.join(abs_path, 'content', 'screens', 'example.jpg')
sexes_photo_path = os.path.join(abs_path, 'content', 'screens', 'sexes_screen.jpg')
language_photo_path = os.path.join(abs_path, 'content', 'screens', 'language_screen.png')
upload_clohes_photo_path = os.path.join(abs_path, 'content', 'screens', 'upload_clothes_screen.png')
hello_photo_path = os.path.join(abs_path, 'content', 'screens', 'hello_screen.jpg')
looks_photo_path = os.path.join(abs_path, 'content', 'looks')
locales = os.path.join(abs_path, 'locales')
 



    
    