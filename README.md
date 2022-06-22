# Тестовый проект telegram бота "MyBot"

MyBot - имеет большое разнообразие функций (присылать/распозновать/принимать и сохронть котиков, а также оценивать их и присылать рейтинг, встроенный калькулятор поможет быстро посчитать сложные выражения, функция visa - покажет ориентировочное время ожидания собеседования на неиммиграционную визу в посольстве или консульстве США, также Вы можете узнать расположенеи планет из предложенных в данный момент времени, сыграет с Вами в игру "Числа" и многое другое)
 
Бот написан на Windows, для других ОС, необходимо небольшое редактирование, также необходиму установить, настроить и подключить БД MongoDB и зарегистрироваться на Clarifai для распознования котиков на фото

## Установка

1. Клонируйте репозиторий с githab `git clone https://github.com/Alex-K3/MyBot`
2. Создайте и активируйте виртуальное окружение:
```
    python -m venv env
    env\Scripts\activate
```
3. Установите зависимости `pip install -r requirements.txt`
4. Создайте и настройте БД MongoDB
5. Создайте файл settings.py с переменными:
```
    API_KEY = "Ваш Api бота"
    USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']
    CLARIFAI_API_KEY = 'Ваш Api clarifai'
    MONGO_LINK = "Подключение к БД"
    MONGO_DB = "Имя Вашей таблицы"
```
8. Запустите Бота `python bot.py` и наслаждайтесь! 