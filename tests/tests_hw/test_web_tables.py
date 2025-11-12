from pages.web_tables import WebTables

def test_web_tables(browser):
    web_tables = WebTables(browser)

    web_tables.visit()
    web_tables.btn_add.click()
    assert web_tables.modal_dialog.exist()
    web_tables.btn_submit.click()
    assert web_tables.user_form.get_dom_attribute('class') == 'was-validated'
    web_tables.first_name.send_keys('Ivan')
    web_tables.last_name.send_keys('Ivanov')
    web_tables.email.send_keys('ivan@ivanov.com')
    web_tables.age.send_keys('30')
    web_tables.salary.send_keys('100')
    web_tables.department.send_keys('Test')
    web_tables.btn_submit.click()
    assert not web_tables.modal_dialog.exist()
    assert web_tables.record4.exist()
    web_tables.btn_edit_record4.click()
    assert web_tables.modal_dialog.exist()
    web_tables.first_name.send_keys('Vova')
    web_tables.btn_submit.click()
    assert web_tables.first_name_record4.get_text() == web_tables.first_name.get_text()
    web_tables.btn_delete_record4.click()
    assert not web_tables.record4.exist()
















