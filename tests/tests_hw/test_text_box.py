from pages.text_box import TextBox


def test_text_box(browser):
    text_box = TextBox(browser)
    text_box.visit()

    text_box.name.send_keys('Ded Moroz')
    text_box.current_address.send_keys('Veliky Ustyug')
    text_box.btn_submit.click()
    assert text_box.output_name.get_text == text_box.name.get_text
    assert text_box.output_current_address.get_text == text_box.current_address.get_text