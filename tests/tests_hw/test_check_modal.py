from pages.modal_dialogs import ModalDialogs


def test_check_modal(browser):
    check_modal_page = ModalDialogs(browser)

    check_modal_page.visit()
    assert check_modal_page.btn_small_modal.exists()
    assert check_modal_page.btn_large_modal.exists()

    check_modal_page.btn_small_modal.click()
    assert check_modal_page.alert()
    check_modal_page.alert().btn_close_small_modal.click()
    assert not check_modal_page.alert()

    check_modal_page.btn_large_modal.click()
    assert check_modal_page.alert()
    check_modal_page.alert().btn_close_large_modal.click()
    assert not check_modal_page.alert()