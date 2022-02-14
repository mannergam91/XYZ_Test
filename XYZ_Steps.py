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

    def click_button_Process(self):
        return self.find_element_located((By.XPATH, '//button[@type="submit"]')).click()

    def click_button_Customers(self):
        return self.find_element_located((By.XPATH, '//button[@ng-click="showCust()"]')).click()

    def click_button_Login(self):
        return self.find_element_located((By.XPATH, '/html/body//form/button')).click()

    def click_button_Transactions(self):
        return self.find_element_located((By.XPATH, '//button[@ng-click="transactions()"]')).click()

    def click_button_Deposit(self):
        return self.find_element_located((By.XPATH, '//button[@ng-click="deposit()"]')).click()

    def click_button_Deposit_bottom(self):
        return self.find_element_located((By.XPATH, '/html/body//div[2]//div[4]//form/button')).click()

    def click_button_Withdrawl(self):
        return self.find_element_located((By.XPATH, '//button[@ng-click="withdrawl()"]')).click()

    def click_button_Withdrawl_bottom(self):
        return self.find_element_located((By.XPATH, '/html/body//div[2]//div[4]//form/button')).click()

    def click_button_Back(self):
        return self.find_element_located((By.XPATH, '//button[@ng-click="back()"]')).click()

    def click_button_Reset(self):
        return self.find_element_located((By.XPATH, '//button[@ng-click="reset()"]')).click()

    def click_button_Logout(self):
        return self.find_element_located((By.XPATH, '/html/body//div[1]/button[2]')).click()

    def click_button_Delete(self):
        return self.find_element_located((By.XPATH, '//button[@ng-click="deleteCust(cust)"]')).click()


class Work_Drop_Down_list(BasePage):

    # def sortout_Drop_Down_list(self, browser, drop, x):  # x - № элемента который нужно выбрать из выпадающего списка
    #
    #     xyz_main_drop = Drop_Down_List(browser)
    #     drop.click()
    #     i = 0
    #     while i != x:
    #         drop.send_keys(Keys.DOWN)
    #         i += 1
    #     drop.send_keys(Keys.ENTER)


    def sortout_Drop_Down_list_customer_name(self, browser, x):  # x - № элемента который нужно выбрать из выпадающего списка

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


    def sortout_Drop_Down_Your_Name(self, browser, x):

        xyz_main_drop = Drop_Down_List(browser)
        drop_down_your = xyz_main_drop.Drop_Down_Your_Name()
        drop_down_your.click()
        i = 0
        while i != x:
            drop_down_your.send_keys(Keys.DOWN)
            i += 1
        drop_down_your.send_keys(Keys.ENTER)


    def sortout_Drop_Down_ID(self, browser, x):

        xyz_main_drop = Drop_Down_List(browser)
        drop_down_your = xyz_main_drop.Drop_Down_ID()
        drop_down_your.click()
        i = 0
        while i != x:
            drop_down_your.send_keys(Keys.DOWN)
            i += 1
        drop_down_your.send_keys(Keys.ENTER)



class Create_User(BasePage):


    def Add_Customer(self, browser):

        First_Name = User1.First_Name(browser)
        Last_Name = User1.Last_Name(browser)
        Post_Code = User1.Post_Code(browser)
        xyz_main_click = Click_button(browser)
        xyz_main_click.click_button_Bunk_Manager_Login()
        xyz_main_click.click_button_Add_Customer()
        xyz_main_input = Input(browser)
        xyz_main_input.Add_Customer_First_Name().send_keys(First_Name)
        xyz_main_input.Add_Customer_Last_Name().send_keys(Last_Name)
        xyz_main_input.Add_Customer_Post_Code().send_keys(Post_Code)
        xyz_main_click.click_button_Add_Customer_bottom()
        browser.switch_to_alert().accept()  # нажимает OK в alert окно


    def Open_Account(self, browser):

        xyz_main_click = Click_button(browser)
        xyz_main_click.click_button_Open_Account()
        xyz_main_Down = Drop_Down_List(browser)
        xyz_main_Down.Drop_Down_List_Customer_Name_Serch_Element()
        xyz_main_Down.Drop_Down_List_Customer_Name_Names_list()
        namber_name = xyz_main_Down.Drop_Down_List_Customer_Name_Serch_Namber_Name(browser)
        xyz_main_Work_Drop = Work_Drop_Down_list(browser)
        xyz_main_Work_Drop.sortout_Drop_Down_list_customer_name(browser, namber_name)
        xyz_main_Down.Drop_Down_List_Currency_Serch_Element()
        xyz_main_Down.Drop_Down_List_Currency_Names_list()
        currency = xyz_main_Down.Drop_Down_List_Currency_Serch_Namber_Name()
        xyz_main_Work_Drop.sortout_Drop_Down_list_currency(browser, currency)
        xyz_main_click.click_button_Process()
        browser.switch_to_alert().accept()  # нажимает OK в alert окно




def Customer_Login(browser):
    xyz_main_Work_Drop = Work_Drop_Down_list(browser)
    xyz_main_click = Click_button(browser)
    xyz_main_Down = Drop_Down_List(browser)
    xyz_main_Down.Drop_Down_Your_Name_Serch_Element()
    xyz_main_Down.Drop_Down_Your_Name_Names_list()
    currency = xyz_main_Down.Drop_Down_Your_Name_Serch_Namber(browser)
    xyz_main_Work_Drop.sortout_Drop_Down_Your_Name(browser, currency)
    xyz_main_click.click_button_Login()
