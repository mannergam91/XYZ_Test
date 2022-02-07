from XYZ_Pages import *
from XYZ_Steps import *
from XYZ_User_Date import *
from selenium.webdriver.common.keys import Keys
import time


# def test_xyz_check_title(browser):
#     check_title = Common_elements(browser)
#     check_title.go_to_site()
#     assert 'XYZ Bank' in check_title.serch_title()
#
#
# def test_xyz_check_button(browser):
#     xyz_main_page = Click_button(browser)
#     xyz_main_page.go_to_site()
#     xyz_main_page.click_button_Customer_Login()
#     xyz_main_page.click_button_Home()
#     xyz_main_page.click_button_Bunk_Manager_Login()


def test_xyz_check_create_user(browser):
    # First_Name = User1.First_Name(browser)
    # Last_Name = User1.Last_Name(browser)
    # Post_Code = User1.Post_Code(browser)
    xyz_main_click = Click_button(browser)
    xyz_main_click.go_to_site()
    Add_Customer(browser)
    # xyz_main_click.click_button_Bunk_Manager_Login()
    # xyz_main_click.click_button_Add_Customer()
    xyz_main_input = Input(browser)
    # xyz_main_input.Add_Customer_First_Name().send_keys(First_Name)
    # xyz_main_input.Add_Customer_Last_Name().send_keys(Last_Name)
    # xyz_main_input.Add_Customer_Post_Code().send_keys(Post_Code)
    # xyz_main_click.click_button_Add_Customer_bottom()
    # browser.switch_to_alert().accept() # нажимает OK в alert окно
    xyz_main_click.click_button_Open_Account()
    xyz_main_Down = Drop_Down_List(browser)
    xyz_main_Down.Drop_Down_List_Customer_Name_Serch_Element()
    xyz_main_Down.Drop_Down_List_Customer_Name_Names_list()
    namber_name = xyz_main_Down.Drop_Down_List_Customer_Name_Serch_Namber_Name()
    xyz_main_Drop = Work_Drop_Down_list(browser)
    xyz_main_Drop.sortout_Drop_Down_list_customer_name(browser, namber_name)
    xyz_main_Down1 = Drop_Down_List(browser)
    xyz_main_Down1.Drop_Down_List_Currency_Serch_Element()
    xyz_main_Down1.Drop_Down_List_Currency_Names_list()
    currency = xyz_main_Down1.Drop_Down_List_Currency_Serch_Namber_Name()
    xyz_main_Drop.sortout_Drop_Down_list_currency(browser, currency)
    xyz_main_click.click_button_Process_bottom()
    xyz_main_page = Click_button(browser)
    xyz_main_page.click_button_Customers()
    xyz_main_input.Table_Customers_Serch_Customer().send_keys('Sirius')
    xyz_main_table = Elements_Table(browser)
    xyz_main_table.Serch_User_in_Table('Sirius') # Проверка что в таблице присутствует созданный клиент
    xyz_main_table.Serch_User_in_Table('Black')
    xyz_main_table.Serch_User_in_Table('E77777')














