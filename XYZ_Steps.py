from XYZ_User_Date import *
from XYZ_Pages import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Click_button(BasePage):


    def click_button_Customer_Login(self):
        return self.find_element_located((By.XPATH, '//button[@ng-click="customer()"]')).click()

    def click_button_Bunk_Manager_Login(self):
        return self.find_element_located((By.XPATH, '//button[contains(text(),"Bank Manager")]')).click()

    def click_button_Home(self):
        return self.find_element_located((By.XPATH, '//button[@ng-click="home()"]')).click()

    def click_button_Add_Customer(self):
        return self.find_element_located((By.XPATH, '//button[@ng-click="addCust()"]')).click()

    def click_button_Add_Customer_bottom(self):
        return self.find_element_located((By.XPATH, '//button[@type="submit"]')).click()

    def click_button_Open_Account(self):
        return self.find_element_located((By.XPATH, '//button[@ng-click="openAccount()"]')).click()

    def click_button_Process_bottom(self):
        return self.find_element_located((By.XPATH, '//button[@ng-click="showCust()"]')).click()

    def click_button_Customers(self):
        return self.find_element_located((By.XPATH, '//button[@ng-click="showCust()"]')).click()


class Work_Drop_Down_list(BasePage):

    # def __init__(self):
    #     self.xyz_main_drop = Drop_Down_List()

    def sortout_Drop_Down_list_customer_name(self, browser, x): # x - № элемента который нужно выбрать из выпадающего списка

        xyz_main_drop = Drop_Down_List(browser)
        drop_down_customer_name = xyz_main_drop.Drop_Down_List_Customer_Name()
        drop_down_customer_name.click()
        i = 0
        while i != x:
            drop_down_customer_name.send_keys(Keys.DOWN)
            i += 1
        drop_down_customer_name.send_keys(Keys.ENTER)


    def sortout_Drop_Down_list_currency(self, browser, x):

        xyz_main_drop = Drop_Down_List(browser)
        drop_down_currency = xyz_main_drop.Drop_Down_List_Currency()
        drop_down_currency.click()
        i = 0
        while i != x:
            drop_down_currency.send_keys(Keys.DOWN)
            i += 1
        drop_down_currency.send_keys(Keys.ENTER)





def Add_Customer(browser):
    First_Name = User1.First_Name(browser)
    Last_Name = User1.Last_Name(browser)
    Post_Code = User1.Post_Code(browser)
    ClickButton = Click_button(browser)
    ClickButton.click_button_Bunk_Manager_Login()
    ClickButton.click_button_Bunk_Manager_Login()
    ClickButton.click_button_Add_Customer()
    xyz_main_input = Input(browser)
    xyz_main_input.Add_Customer_First_Name().send_keys(First_Name)
    xyz_main_input.Add_Customer_Last_Name().send_keys(Last_Name)
    xyz_main_input.Add_Customer_Post_Code().send_keys(Post_Code)
    Click_button.click_button_Add_Customer_bottom(browser)
    browser.switch_to_alert().accept()  # нажимает OK в alert окно

#def Open_Account(self):
