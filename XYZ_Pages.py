from XYZ_Base import BasePage
from selenium.webdriver.common.by import By
from XYZ_User_Date import *


class Common_elements(BasePage):

    def Serch_title(self):
        return self.driver.title

    def Table_Customer(self):
        return self.driver.find_elements_by_class_name('ng-scope')

    def Error_Withdrawl(self):
        return self.driver.find_elements_by_class_name('error ng-binding')

    def button_Customer_Login(self):
        return self.find_element_located((By.XPATH, '//button[@ng-click="customer()"]'))

    def button_Bunk_Manager_Login(self):
        return self.find_element_located((By.XPATH, '//button[contains(text(),"Bank Manager")]'))



class Input(BasePage):

    def Add_Customer_First_Name(self):
        return self.find_element_located((By.XPATH, '//input[@placeholder="First Name"]'), timeout=5)

    def Add_Customer_Last_Name(self):
        return self.find_element_located((By.XPATH, '//input[@placeholder="Last Name"]'), timeout=5)

    def Add_Customer_Post_Code(self):
        return self.find_element_located((By.XPATH, '//input[@placeholder="Post Code"]'), timeout=5)

    def Table_Customers_Serch_Customer(self):
        return self.find_element_located((By.XPATH, '//input[@placeholder="Search Customer"]'), timeout=5)

    def Money_amount(self):
        return self.find_element_located((By.XPATH, '/html/body//div[2]//div[4]//form//input'), timeout=5)


class Drop_Down_List(BasePage):


    def Name(self, browser):
        First_Name = User1.First_Name(browser)
        Last_Name = User1.Last_Name(browser)
        return f'{First_Name} {Last_Name}'


    def Drop_Down_List_Customer_Name(self):
        return self.find_element_located((By.ID, "userSelect"))

    def Drop_Down_List_Currency(self):
        return self.find_element_located((By.ID, "currency"))

    def Drop_Down_List_Customer_Name_Serch_Element(self):
        return self.sum_string("//*[@id='userSelect']/option")

    def Drop_Down_List_Customer_Name_Names_list(self):
        element = Drop_Down_List.Drop_Down_List_Customer_Name_Serch_Element(self)
        return self.names_list(element, "//*[@id='userSelect']/option")

    def Drop_Down_List_Customer_Name_Serch_Namber_Name(self, browser):
        flname = Drop_Down_List.Name(browser, browser)
        element = Drop_Down_List.Drop_Down_List_Customer_Name_Names_list(self)
        return self.serch_namber_name(element, flname)

    def Drop_Down_List_Currency_Serch_Element(self):
        return self.sum_string("//*[@id='currency']/option")

    def Drop_Down_List_Currency_Names_list(self):
        element = Drop_Down_List.Drop_Down_List_Currency_Serch_Element(self)
        return self.names_list(element, "//*[@id='currency']/option")

    def Drop_Down_List_Currency_Serch_Namber_Name(self):
        element = Drop_Down_List.Drop_Down_List_Currency_Names_list(self)
        return self.serch_namber_name(element, 'Rupee')

    def Drop_Down_Your_Name(self):
        return self.find_element_located((By.ID, "userSelect"))

    def Drop_Down_Your_Name_Serch_Element(self):
        return self.sum_string("//*[@id='userSelect']/option")

    def Drop_Down_Your_Name_Names_list(self):
        element = Drop_Down_List.Drop_Down_Your_Name_Serch_Element(self)
        return self.names_list(element, "//*[@id='userSelect']/option")

    def Drop_Down_Your_Name_Serch_Namber(self, browser):
        flname = Drop_Down_List.Name(browser, browser)
        element = Drop_Down_List.Drop_Down_Your_Name_Names_list(self)
        return self.serch_namber_name(element, flname)

    def Drop_Down_ID(self):
        return self.find_element_located((By.ID, "accountSelect"))

    def Drop_Down_ID_Serch_Element(self):
        return self.sum_string("//*[@id='accountSelect']/option")

    def Drop_Down_ID_Names_list(self):
        element = Drop_Down_List.Drop_Down_ID_Serch_Element(self)
        return self.names_list(element, "//*[@id='accountSelect']/option")





class Table_Check(BasePage):

    def Get_Name_list(self):
        return self.names_list_cycle_text('/html/body//table/tbody/tr/td')

    def Get_Name_ID(self):
        actual_value = Table_Check.Get_Name_list(self)
        lst = actual_value[3]
        lst = lst.split()
        return lst

    def Get_String_Quantity_in_Table_Users(self):
        x = self.names_list_cycle_text('/html/body//div[2]/div[2]//table/tbody')
        return len(x)

    def Get_Date_Transactions(self, i):
        line = f'//*[@id="anchor{i}"]/td'
        return self.names_list_cycle_text(line)

    def Get_String_Quantity_in_Table_Transactions(self):
        x = self.names_list_cycle_text('//*[@id="anchor0"]')
        return len(x)





class Account_Elements(BasePage):

    def Get_Welcome_Name(self):
        return self.names_cycle_text('/html/body//div[2]//div[1]/strong/span')

    def Get_Elements_list(self):
        return self.names_list_cycle_text('/html/body//div[2]//div[2]/strong')


