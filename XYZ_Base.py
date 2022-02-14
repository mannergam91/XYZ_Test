from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_located(self, link, timeout=5):
        WbDrW = WebDriverWait(self.driver, timeout)
        return WbDrW.until(EC.presence_of_element_located(link))

    def go_to_site(self):
        return self.driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    def sum_string(self, line):
        time.sleep(1)
        strings = self.driver.find_elements_by_xpath(line)
        sum_str = len(strings)
        return sum_str

    def names_list(self, sum_str, line):
        time.sleep(1)
        lst_names = list()
        x = 0
        while x < (sum_str - 1):
            x += 1
            list_names = self.driver.find_elements_by_xpath(line)
            scan_name = list_names[x].get_attribute('text')
            lst_names.extend([scan_name])
        return lst_names

    def serch_namber_name(self, lst_names, name):
        i = lst_names.index(name)
        return i + 1

    # def serch_namber_name(self, lst_names, name):
    #     x = 0
    #     while lst_names[x] != name:
    #         x += 1
    #     return x + 1

    def names_cycle_text(self, line):
        for element in self.driver.find_elements_by_xpath(line):
            return element.text

    def names_list_cycle_text(self, line):
        lst = list()
        for element in self.driver.find_elements_by_xpath(line):
            lst.append(element.text)
        return lst
