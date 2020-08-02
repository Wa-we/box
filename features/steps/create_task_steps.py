from behave import given, when, then, step  # pylint: disable=no-name-in-module
from selenium.webdriver.support.ui import Select


@given(u'я загружаю страницу "http://qa-assignment.oblakogroup.ru/board/:roman_shipilov"')
def step_impl(context):
    context.driver.get("http://qa-assignment.oblakogroup.ru/board/:roman_shipilov")


@when(u'я нажимаю кнопку добавления новой задачи')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="add_new_todo"]').click()


@then(u'должен появиться интерфейс создания новой задачи')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="create_div"][contains(@style,"display: block")]')


@then(u'должны появиться поля "Выбор категории" и "Название задачи"')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="select2-select_category-container"]')
    context.driver.find_element_by_xpath('//*[@id="project_text"]')


@when(u'я выбираю создание новой задачи в "Выборе категорий"')
def step_impl(context):
    select = Select(context.driver.find_element_by_xpath('//*[@id="select_category"]'))
    select.select_by_visible_text('Создать новый список')


@then(u'должно появиться поле "Заголовок"')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="project_title"]')
