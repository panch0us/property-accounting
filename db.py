# Модуль для создания базы данных для учета имущества

def exist_db():
    """Проверяем существует база данных?"""
    pass


def create_db():
    """Создание базы данных"""
    pass


if __name__ == '__main__':
    if exist_db():
        print('База данных уже создана!')
    else:
        create_db()