from page_objects.homepage import Homepage

def test_homepage(driver):
    page = Homepage(driver)
    page.verifyPageElements()

