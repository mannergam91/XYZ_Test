from XYZ_Steps import *
from XYZ_User_Date import *
from datetime import *
import time


def test_xyz_check_title(browser):
    check_title = Common_elements(browser)
    check_title.go_to_site()
    assert 'XYZ Bank' in check_title.Serch_title()


def test_xyz_check_button(browser):
    xyz_main_botton = Common_elements(browser)
    xyz_main_click = Click_button(browser)
    xyz_main_click.go_to_site()
    xyz_main_click.click_button_Customer_Login()
    xyz_main_click.click_button_Home()
    xyz_main_click.click_button_Bunk_Manager_Login()
    xyz_main_botton.button_Customer_Login()
    xyz_main_botton.button_Bunk_Manager_Login()

def test_xyz_check_create_user_1(browser):
    first_name = User1.First_Name(browser)
    last_name = User1.Last_Name(browser)
    post_code = User1.Post_Code(browser)
    xyz_main_click = Click_button(browser)
    #Тест_1:
    xyz_main_click.go_to_site()
    xyz_main_create = Create_User(browser)
    Create_User.Add_Customer(xyz_main_create, browser)
    #Тест_2:
    xyz_main_click.click_button_Open_Account()
    Create_User.Open_Account(xyz_main_create, browser)
    #Тест_3:
    xyz_main_click.click_button_Customers()
    xyz_main_input = Input(browser)
    xyz_main_input.Table_Customers_Serch_Customer().send_keys(first_name)
    xyz_main_name = Table_Check(browser)
    actual_value = xyz_main_name.Get_Name_list()
    assert actual_value[0] == first_name
    assert actual_value[1] == last_name
    assert actual_value[2] == post_code


def test_xyz_check_create_user_2(browser):
    first_name = User1.First_Name(browser)
    xyz_main_click = Click_button(browser)
    #Тест_1:
    xyz_main_click.go_to_site()
    xyz_main_create = Create_User(browser)
    Create_User.Add_Customer(xyz_main_create, browser)
    #Тест_2:
    xyz_main_click.click_button_Open_Account()
    Create_User.Open_Account(xyz_main_create, browser)
    #Тест_3:
    xyz_main_click.click_button_Customers()
    xyz_main_input = Input(browser)
    xyz_main_input.Table_Customers_Serch_Customer().send_keys(first_name)
    xyz_main_name = Table_Check(browser)
    id_1 = xyz_main_name.Get_Name_ID()[0]
    id_2 = xyz_main_name.Get_Name_ID()[1]
    assert id_1 != id_2


def test_xyz_check_Customer_Login(browser):
    xyz_main_name = Table_Check(browser)
    id = xyz_main_name.Get_Name_ID()

    i = 0
    while i < 2:
        First_Name = User1.First_Name(browser)
        Last_Name = User1.Last_Name(browser)
        xyz_main_click = Click_button(browser)
        #Тест_1:
        xyz_main_click.go_to_site()
        xyz_main_click.click_button_Customer_Login()
        Customer_Login(browser)
        Work_Drop_Down_list(browser).sortout_Drop_Down_ID(browser, i)
        actual_name = Account_Elements(browser).Get_Welcome_Name()
        expected_name = f'{First_Name} {Last_Name}'
        assert actual_name == expected_name  # Проверяет что на экране приветствия указано имя созданного пользователя
        #Тест_2:
        actual_element_account = Account_Elements(browser).Get_Elements_list()
        assert actual_element_account[0] == id[i]
        assert actual_element_account[1] == '0'
        assert actual_element_account[2] == 'Rupee'
        #Тест_3:
        xyz_main_click.click_button_Deposit()
        xyz_main_input = Input(browser)
        xyz_main_input.Money_amount().send_keys('1000')
        actual_date_Deposit = datetime.today().strftime("%b %d, %Y %#I:%M:%S %p")
        xyz_main_click.click_button_Deposit_bottom()
        time.sleep(1)
        actual_element_account = Account_Elements(browser).Get_Elements_list()
        assert actual_element_account[1] == '1000'
        time.sleep(1)
        xyz_main_click.click_button_Transactions()
        time.sleep(1)
        expected_date_Deposit = xyz_main_name.Get_Date_Transactions(0)[0]
        expected_amount_Deposit = xyz_main_name.Get_Date_Transactions(0)[1]
        expected_type_Deposit = xyz_main_name.Get_Date_Transactions(0)[2]
        assert actual_date_Deposit == expected_date_Deposit
        assert expected_amount_Deposit == '1000'
        assert expected_type_Deposit == 'Credit'
        xyz_main_click.click_button_Back()
        xyz_main_click.click_button_Withdrawl()
        time.sleep(1)
        xyz_main_input.Money_amount().send_keys('1000')
        time.sleep(1)
        actual_date_Withdrawl = datetime.today().strftime("%b %d, %Y %#I:%M:%S %p")
        xyz_main_click.click_button_Withdrawl_bottom()
        time.sleep(1)
        actual_element_account = Account_Elements(browser).Get_Elements_list()
        assert actual_element_account[1] == '0'
        xyz_main_click.click_button_Transactions()
        expected_date_Withdrawl = xyz_main_name.Get_Date_Transactions(1)[0]
        expected_amount_Withdrawl = xyz_main_name.Get_Date_Transactions(1)[1]
        expected_type_Withdrawl = xyz_main_name.Get_Date_Transactions(1)[2]
        assert actual_date_Withdrawl == expected_date_Withdrawl
        assert expected_amount_Withdrawl == '1000'
        assert expected_type_Withdrawl == 'Debit'
        i += 1


def test_xyz_check_negative_Withdrawals(browser):
    xyz_main_input = Input(browser)
    xyz_main_click = Click_button(browser)
    xyz_main_click.go_to_site()
    xyz_main_click.click_button_Customer_Login()
    Customer_Login(browser)
    time.sleep(1)
    xyz_main_click.click_button_Logout()
    Customer_Login(browser)
    time.sleep(1)
    actual_element_account = Account_Elements(browser).Get_Elements_list()
    assert actual_element_account[1] == '0'
    xyz_main_click.click_button_Withdrawl()
    xyz_main_input.Money_amount().send_keys('1000')
    xyz_main_click.click_button_Withdrawl_bottom()
    time.sleep(1)
    Common_elements(browser).Error_Withdrawl()
    assert actual_element_account[1] == '0'


def test_xyz_check_Clear_Report_Transactions(browser):
    xyz_main_click = Click_button(browser)
    xyz_main_click.go_to_site()
    xyz_main_click.click_button_Customer_Login()
    Customer_Login(browser)
    xyz_main_click.click_button_Deposit()
    xyz_main_input = Input(browser)
    xyz_main_input.Money_amount().send_keys('1000')
    xyz_main_click.click_button_Deposit_bottom()
    xyz_main_click.click_button_Withdrawl()
    xyz_main_input.Money_amount().send_keys('1000')
    xyz_main_click.click_button_Withdrawl_bottom()
    xyz_main_click.click_button_Transactions()
    xyz_main_click.click_button_Reset()
    quantity_line_table = Table_Check(browser).Get_String_Quantity_in_Table_Transactions()
    assert quantity_line_table == 0


def test_xyz_check_Delete_User(browser):
    first_name = User1.First_Name(browser)
    xyz_main_click = Click_button(browser)
    xyz_main_click.go_to_site()
    xyz_main_create = Create_User(browser)
    Create_User.Add_Customer(xyz_main_create, browser)
    xyz_main_click.click_button_Open_Account()
    Create_User.Open_Account(xyz_main_create, browser)
    xyz_main_click.click_button_Customers()
    xyz_main_input = Input(browser)
    xyz_main_input.Table_Customers_Serch_Customer().send_keys(first_name)
    xyz_main_click.click_button_Delete()
    xyz_main_click.click_button_Home()
    Create_User.Add_Customer(xyz_main_create, browser)
    xyz_main_click.click_button_Open_Account()
    Create_User.Open_Account(xyz_main_create, browser)
    xyz_main_click.click_button_Customers()
    xyz_main_input.Table_Customers_Serch_Customer().send_keys(first_name)
    quantity_line_table = Table_Check(browser).Get_String_Quantity_in_Table_Users()
    assert quantity_line_table == 0












