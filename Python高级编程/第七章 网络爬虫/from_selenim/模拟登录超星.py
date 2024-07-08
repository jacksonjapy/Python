from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from re import search

if __name__ == '__main__':
    target_url = "https://passport2.chaoxing.com/login"
    driver = webdriver.Chrome()
    driver.get(target_url)

    fanyi_id = str()
    fanyi_pwd = str()
    user_name = str()
    with open("username", "r") as file1, open("password", "r") as file2, open("name", "r", encoding="utf-8") as file3:
        fanyi_id += file1.read()
        fanyi_pwd += file2.read()
        user_name += file3.read()

        # WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "showlogintext")))
    if WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CLASS_NAME, "lg-title"))):
        print("Page open successfully!")
    else:
        print("Page open failed!")
        exit(1)

    id_input = driver.find_element(By.CLASS_NAME, "ipt-tel")  # "//input[@class='ipt-tel']" # 登录框
    passwd_input = driver.find_element(By.CLASS_NAME, "ipt-pwd")  # "//input[@class='ipt-pwd']" # 密码框
    login_button = driver.find_element(By.ID, "loginBtn")  # "//button[@id='loginBtn']/text()" # 登录按钮
    id_input.send_keys(fanyi_id)    # 输入账号
    passwd_input.send_keys(fanyi_pwd)   # 输入密码
    login_button.click()

    personalName = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CLASS_NAME, "personalName"))).text
    if personalName == user_name:
        print(f"user:{user_name} Login successfully!")
    else:
        print(f"user:{user_name} Login failed!")
        exit(1)

    try:
        if WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CLASS_NAME, "err-tip"))).text:
            print("Login failed!")
            exit(1)
        else:
            print("Login failed!")
    except:
        print("error")

    course_url = str(driver.find_element(By.ID, "zne_kc_icon").get_attribute("href"))
    print(course_url)
    course_url = search(r"[^']*?\)", course_url)
    print(course_url)
    input("Press Enter to over...")
