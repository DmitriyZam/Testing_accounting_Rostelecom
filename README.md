# Module28_Final_Project_"Тестировщик-автоматизатор_на_Python"

Объект тестирования: 
https://b2c.passport.rt.ru

Ссылка на требования по проекту: 
https://docs.google.com/document/d/1xQ-zgYk4XS9Acw8nbp-oFM0gAXi2_Lsr/edit?usp=share_link&ouid=101500873532933086422&rtpof=true&sd=true


Заказчик передал вам следующее задание:

Протестировать требования.

Разработать тест-кейсы (не менее 15). Необходимо применить несколько техник тест-дизайна.

Провести автоматизированное тестирование продукта (не менее 15 автотестов). Заказчик ожидает по одному автотесту на каждый написанный тест-кейс. Оформите свой набор автотестов в GitHub.

Оформить описание обнаруженных дефектов. Во время обучения вы работали с разными сервисами и шаблонами, используйте их для оформления тест-кейсов и обнаруженных дефектов. (если дефекты не будут обнаружены, то составить описание трех дефектов)

Ссылка на тестирование требований, тест-кейсы, баг-репорты: 
https://docs.google.com/spreadsheets/d/1P_ZUNYFsSB7-bjEXu7adw0lcMu_JLiaG/edit?usp=share_link&ouid=101500873532933086422&rtpof=true&sd=true

Запуск тестов:

Установить все внешние зависимости командой pip install -r requirements.txt

Скачать версию Selenium WebDriver для Chrome 110 версии по ссылке: https://chromedriver.chromium.org/downloads

Команда для запуска тестов

python3 -m pytest -v --driver Chrome --driver-path autotests_rostelecom.py

Где driver-path путь к драйверу Selenium для текущей ОС
