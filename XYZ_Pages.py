from XYZ_Base import BasePage
from selenium.webdriver.common.by import By


class Common_elements(BasePage):


    def serch_title(self):
        return self.driver.title

    def table_Customer(self):
        return self.driver.find_elements_by_class_name('ng-scope')


class Input(BasePage):


    def Add_Customer_First_Name(self):
        return self.find_element_located((By.XPATH, '//input[@ng-model="fName"]'), timeout=5)

    def Add_Customer_Last_Name(self):
        return self.find_element_located((By.XPATH, '//input[@placeholder="Last Name"]'), timeout=5)

    def Add_Customer_Post_Code(self):
        return self.find_element_located((By.XPATH, '//input[@placeholder="Post Code"]'), timeout=5)

    def Table_Customers_Serch_Customer(self):
        return self.find_element_located((By.XPATH, '//input[@placeholder="Search Customer"]'), timeout=5)


class Drop_Down_List(BasePage):


    def Drop_Down_List_Customer_Name(self):
        return self.find_element_located((By.ID, "userSelect"))

    def Drop_Down_List_Currency(self):
        return self.find_element_located((By.ID, "currency"))


    def Drop_Down_List_Customer_Name_Serch_Element(self):
        return self.sum_string_drop_down("//*[@id='userSelect']/option")

    def Drop_Down_List_Customer_Name_Names_list(self):
        element = Drop_Down_List.Drop_Down_List_Customer_Name_Serch_Element(self)
        return self.names_list_drop_down(element, "//*[@id='userSelect']/option")

    def Drop_Down_List_Customer_Name_Serch_Namber_Name(self):
        element = Drop_Down_List.Drop_Down_List_Customer_Name_Names_list(self)
        return self.serch_namber_name(element, 'Sirius Black')


    def Drop_Down_List_Currency_Serch_Element(self):
        return self.sum_string_drop_down("//*[@id='currency']/option")

    def Drop_Down_List_Currency_Names_list(self):
        element = Drop_Down_List.Drop_Down_List_Currency_Serch_Element(self)
        return self.names_list_drop_down(element, "//*[@id='currency']/option")

    def Drop_Down_List_Currency_Serch_Namber_Name(self):
        element = Drop_Down_List.Drop_Down_List_Currency_Names_list(self)
        return self.serch_namber_name(element, 'Rupee')



class Elements_Table(BasePage):


    def Serch_User_in_Table(self, nameelement):
        return self.find_element_located((By.XPATH, f'//td[contains(text(),"{nameelement}")]'))


