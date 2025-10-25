from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_check_text(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    assert demo_qa_page.exist_text()
    demo_qa_page.btn_elements.click()
    assert elements_page.equal_url()
    assert elements_page.exist_text()