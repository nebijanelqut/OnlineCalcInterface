import inspect
from selenium import webdriver

# Path to the chrome webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"


# URL to load
url = "http://output.jsbin.com/hudape/1/"


def addition(operand1, operand2):
    """ Implimenting addition operation """
    operand1 = str(operand1)
    operand2 = str(operand2)
    driver = webdriver.Chrome(PATH)
    # Creation of web driver with url to connect to
    driver.get(url)

    # Locating output element to get the result of operation
    out_put = driver.find_element_by_id("output")
    # Button locator function
    button_to_click = lambda button: driver.find_element_by_xpath("//button[@value='{}']".format(button))

    for digit in operand1:
        # Step 1: Entering first opernad
        button_to_click(digit).click()

    # Step 2: Clicking on "PLUS" button
    button_to_click('+').click()

    for digit in operand2:
        # Step 3: Entering second operand
        button_to_click(digit).click()

    # Step 4: Cliking on "EQ" button
    button_to_click('=').click()

    # Step 5: Retrieving output
    result = out_put.text

    driver.quit()

    return result

def subtraction(operand1, operand2):
    """ Implementing subtraction operation """
    operand1 = str(operand1)
    operand2 = str(operand2)
    driver = webdriver.Chrome(PATH)
    # Creation of web driver with url to connect to
    driver.get(url)

    # Locating output element to get the result of operation
    out_put = driver.find_element_by_id("output")
    # Button locator function
    button_to_click = lambda button: driver.find_element_by_xpath("//button[@value='{}']".format(button))

    for digit in operand1:
        # Step 1: Entering first opernad
        button_to_click(digit).click()

    # Step 2: Clicking on "MINUS" button
    button_to_click('-').click()

    for digit in operand2:
        # Step 3: Entering second operand
        button_to_click(digit).click()

    # Step 4: Cliking on "EQ" button
    button_to_click('=').click()

    # Step 5: Retrieving output
    result = out_put.text

    driver.quit()

    return result

def multiplication(operand1, operand2):
    """ Implementing multiplication operation """
    operand1 = str(operand1)
    operand2 = str(operand2)
    driver = webdriver.Chrome(PATH)
    # Creation of web driver with url to connect to
    driver.get(url)

    # Locating output element to get the result of operation
    out_put = driver.find_element_by_id("output")
    # Button locator function
    button_to_click = lambda button: driver.find_element_by_xpath("//button[@value='{}']".format(button))

    for digit in operand1:
        # Step 1: Entering first opernad
        button_to_click(digit).click()

    try:
        # Step 2: Clicking on "MULT" button
        x = u'\u00d7'
        button_to_click(x.encode('utf-8')).click()

    except UnboundLocalError as e:
        # exception occurs while first operand is empty
        pass

    for digit in operand2:
        # Step 3: Entering second operand
        button_to_click(digit).click()

    # Step 4: Cliking on "EQ" button
    button_to_click('=').click()

    # Step 5: Retrieving output
    result = out_put.text

    driver.quit()

    return result

def division(operand1, operand2):
    """ Implementing division operation """
    operand1 = str(operand1)
    operand2 = str(operand2)
    driver = webdriver.Chrome(PATH)
    # Creation of web driver with url to connect to
    driver.get(url)

    # Locating output element to get the result of operation
    out_put = driver.find_element_by_id("output")
    # Button locator function
    button_to_click = lambda button: driver.find_element_by_xpath("//button[@value='{}']".format(button))

    for digit in operand1:
        # Step 1: Entering first opernad
        button_to_click(digit).click()

    # Step 2: Clicking on "DIV" button
    button_to_click('/').click()

    for digit in operand2:
        # Step 3: Entering second operand
        button_to_click(digit).click()

    # Step 4: Cliking on "EQ" button
    button_to_click('=').click()

    # Step 5: Retrieving output
    result = out_put.text

    driver.quit()

    return result

def delete_button(buttons):
    """ Implementing testing DEL button function """
    driver = webdriver.Chrome(PATH)
    # Creation of web driver with url to connect to
    driver.get(url)

    # Locating output element to get the result of operation
    out_put = driver.find_element_by_id("output")
    # Button locator function
    button_to_click = lambda button: driver.find_element_by_xpath("//button[@value='{}']".format(button))

    for button in buttons:
        # Step 1: Clicking on button times
        button_to_click(button).click()

    for i, _ in enumerate(buttons):
        # Step 1: Clicking on DEL button count times to clear the expression
        button_to_click("DEL").click()

    result = out_put.text

    driver.quit()

    return result



if __name__ == "__main__":
    result = addition('5', '5')
    print (result)

