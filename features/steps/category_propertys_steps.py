from behave import given, when, then, step  # pylint: disable=no-name-in-module


@when(u'я пишу текст задачи')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="project_text"]').send_keys('test')


@when(u'я нажимаю кнопку "ОК"')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="submit_add_todo"]/div').click()







@then(u'задача не должна появиться')
def step_impl(context):
    pass
