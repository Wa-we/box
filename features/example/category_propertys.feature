#Feature: Свойства категории
#
#  Scenario: Заголовок категории не может быть пустым
#    Given я загружаю страницу "http://qa-assignment.oblakogroup.ru/board/:roman_shipilov"
#    When я нажимаю кнопку добавления новой задачи, оставляю пусытм строку ктегории, пишу текст задачи
#    Then должна появится ошибка
#
#  Scenario: Заголовоки категорий должны быть разными
#    Given я загружаю страницу "http://qa-assignment.oblakogroup.ru/board/:roman_shipilov"
#    When я нажимаю кнопку добавления новой задачи, пишу вместо новой ктегории существующую
#    Then должна появится ошибка
#
#  Scenario: Проверка добавления записи в новоую категорию с неуникальным названием
#    Given я загружаю страницу "http://qa-assignment.oblakogroup.ru/board/:roman_shipilov"
#    When я нажимаю кнопку добавления новой задачи, создаю новую категорию, пишу неуникальное название, пишу текст задачи
#    Then текст задачи должен добавиться в уже существующую категорию
