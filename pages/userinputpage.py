from pages.spreadsheet import SpreadSheet
import time
from definitions.userinputdetails import InputDetails
import pytest 
def test_input_details(driver):
    sendmoney=InputDetails(driver)
       
    file_path = (Give_file_path)
    spreadsheets = SpreadSheet(file_path)
    desired_phone_number = ""
    result = {}

    result=spreadsheets.print_row_by_phone_number(desired_phone_number)
        # print(result["Remark"])

    sendmoney.transfer_optn()
    sendmoney.send_optn()
    sendmoney.receiver_phno(result["Receiver_Phone_No"])
    sendmoney.enter_amount(result["Amount"])
    sendmoney.purpose_click()
    sendmoney.purpose_dropdown()
    sendmoney.remarks_to(result["Remarks"])
    # sendmoney.remarks_to(FileHandle.result["Remarks"])
    time.sleep(10)
    sendmoney.send_to()
    time.sleep(5)