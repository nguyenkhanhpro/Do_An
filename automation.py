import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Kết nối đến cơ sở dữ liệu
db = mysql.connector.connect(
    host="localhost",     
    user="root",           
    password="120804",           
    database="ConsignmentTH"   
)
cursor = db.cursor()
cursor.execute("SELECT email, Password_User FROM th_user")
accounts = cursor.fetchall()

# Khởi tạo trình duyệt Chrome và WebDriverWait
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

for email, password in accounts:
    print(f"Đang đăng nhập với: {email} | {password}")
    
    # Mở trang Login
    driver.get("http://localhost:3008/login")
    sleep(1)

    # Đợi cho đến khi form đăng nhập load (các input phải có id tương ứng: "email" và "password")
    email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
    email_input.clear()
    email_input.send_keys(email)
    sleep(1)

    password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password_input.clear()
    password_input.send_keys(password)
    
    # Đợi nút đăng nhập (id="loginButton") có thể click được và click vào nó
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "loginButton")))
    login_button.click() 
    sleep(1)
    # Trên trang Home, click vào nút "Đăng nhập" để quay lại trang Login
    home_login_button = wait.until(EC.element_to_be_clickable((By.ID, "homeLoginButton")))
    home_login_button.click()
    
    # Tạm dừng ngắn trước khi chuyển sang tài khoản tiếp theo
    sleep(1)

# Đóng trình duyệt và giải phóng tài nguyên
driver.quit()
cursor.close()
db.close()
