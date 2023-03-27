from selenium.webdriver.common.by import By
from .common import CommonOps

class Homepage(CommonOps):

    # elements
    navbar = (By.ID, "navbar")

    def verifyPageElements(self):
        self.wait_for(self.navbar)
