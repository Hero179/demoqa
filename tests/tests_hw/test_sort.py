from pages.web_tables import WebTables


def test_sort(browser):
    test_sort_page = WebTables(browser)
    test_sort_page.visit()

    test_sort_page.btn_first_name_table.click()
    assert test_sort_page.btn_first_name_table.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    test_sort_page.btn_first_name_table.click()
    assert test_sort_page.btn_first_name_table.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    test_sort_page.btn_last_name_table.click()
    assert test_sort_page.btn_first_name_table.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    test_sort_page.btn_first_name_table.click()
    assert test_sort_page.btn_first_name_table.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    test_sort_page.btn_age_table.click()
    assert test_sort_page.btn_age_table.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    test_sort_page.btn_first_name_table.click()
    assert test_sort_page.btn_age_table.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    test_sort_page.btn_email_table.click()
    assert test_sort_page.btn_email_table.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    test_sort_page.btn_email_table.click()
    assert test_sort_page.btn_email_table.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    test_sort_page.btn_salary_table.click()
    assert test_sort_page.btn_salary_table.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    test_sort_page.btn_salary_table.click()
    assert test_sort_page.btn_salary_table.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    test_sort_page.btn_department_table.click()
    assert test_sort_page.btn_department_table.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    test_sort_page.btn_department_table.click()
    assert test_sort_page.btn_department_table.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    test_sort_page.btn_action_table.click()
    assert test_sort_page.btn_action_table.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    test_sort_page.btn_action_table.click()
    assert test_sort_page.btn_action_table.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'