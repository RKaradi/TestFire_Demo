from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
	
def drive_application():
	port = 8091
	host = "127.0.0.1"
	profile = webdriver.FirefoxProfile()
	profile.set_preference("network.proxy.type", 1)
	profile.set_preference("network.proxy.http", host)
	profile.set_preference("network.proxy.http_port", port)
	profile.set_preference("network.proxy.https", host)
	profile.set_preference("network.proxy.https_port", port)
	profile.set_preference("network.proxy.ssl", host)
	profile.set_preference("network.proxy.ssl_port", port)
	profile.set_preference("network.proxy.ftp", host)
	profile.set_preference("network.proxy.ftp_port", port)
	
	profile.update_preferences()
	driver = webdriver.Firefox(firefox_profile=profile)
	# login
	driver.get("http://testfire.net/bank/login.aspx")
	element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "uid")))
	uid = driver.find_element_by_name('uid')
	uid.send_keys("admin")
	passw = driver.find_element_by_name('passw')
	passw.send_keys("admin")
	passw.send_keys(Keys.RETURN)
	element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Edit Users")))
	edit_users = driver.find_element_by_link_text("Edit Users")
	edit_users.click()
	# change password
	element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password1")))
	password1 = driver.find_element_by_name('password1')
	password1.send_keys("pass")
	password2 = driver.find_element_by_name('password2')
	password2.send_keys("pass")
	change = driver.find_element_by_name('change')
	change.click()
	element = WebDriverWait(driver, 10).until(EC.title_contains("Altoro Mutual"))
	# view recent transactions
	driver.get("http://testfire.net/bank/transaction.jsp")
	element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "startDate")))
	startDate = driver.find_element_by_name('startDate')
	startDate.send_keys("2020-07-10")
	endDate = driver.find_element_by_name('endDate')
	endDate.send_keys("2020-07-10")
	endDate.send_keys(Keys.RETURN)
	time.sleep(2)
	driver.quit()

drive_application()
