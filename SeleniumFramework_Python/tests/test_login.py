from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("admin", "admin123")
    assert "Dashboard" in driver.title