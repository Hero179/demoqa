from pages.alerts import Alerts
import time


def test_check_alert(browser):
    check_alert_page = Alerts(browser)

    check_alert_page.visit()
    assert check_alert_page.timer_alert_btn.exist()

    check_alert_page.timer_alert_btn.click()
    time.sleep(5)
    assert check_alert_page.alert()