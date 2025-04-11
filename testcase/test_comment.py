from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# Khởi tạo WebDriver (Chrome)
driver = webdriver.Chrome()

try:
    # 1. Mở trang đăng nhập (Sửa URL)
    driver.get("http://localhost:3000/login.php")
    print("Đã mở trang đăng nhập.")

    # 2. Nhập tên đăng nhập
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("lananh12")
    print("Đã nhập tên đăng nhập.")

    # 3. Nhập mật khẩu
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("123")
    print("Đã nhập mật khẩu.")

    # 4. Nhấn nút Đăng nhập
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    print("Đã nhấn nút đăng nhập.")

    # 5. Chờ tải trang và kiểm tra URL
    time.sleep(3)  # Chờ 3 giây để trang tải xong
    expected_url = "http://localhost:3000/index.php"
    if driver.current_url == expected_url:
        print("Đăng nhập thành công!")
    else:
        raise AssertionError("URL sau khi đăng nhập không đúng.")

except AssertionError as e:
    print(f"Lỗi kiểm tra: {e}")
except NoSuchElementException as e:
    print(f"Lỗi: Không tìm thấy phần tử - {e}")
except TimeoutException as e:
    print(f"Lỗi: Quá thời gian chờ - {e}")
finally:
    # Đóng trình duyệt
    driver.quit()
    print("Đã đóng trình duyệt.")
