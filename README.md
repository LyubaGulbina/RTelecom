# RTelecom

В данном репозитории содержатся тесты для проведения тестирования сайта Ростелеком (https://b2c.passport.rt.ru) в соответствии с представленной заказчиком документацией.  

Проект выполнен с помощью библиотеки Pytest и Selenium.  

При тестировании использовались различные техники тест-дизайна: эквивалентное разделение, предугадывание ошибок, исследовательское тестирование.  

Репозиторий состоит из следующих файлов:  

settings.py  - данные для автотестов    

tests.auth_page.py – тесты для страницы авторизации
 
tests.registration.py – тесты для страницы регистрации

pages/base_page.py  - реализация шаблона PageObject для Python  

pages/auth_page.py  – вспомогательные данные для тестов страницы авторизации  

pages/reg_page.py – вспомогательные данные для тестов страницы регистрации  

conftest.py  - вспомогательные данные для работы с ошибками  

elements.py – вспомогательный код для класса WebElement  




Для запуска тестов необходимо загрузить файл с требованиями командой pip install -r requirements.txt
