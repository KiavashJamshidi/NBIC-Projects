from selenium import webdriver
driver = webdriver.Chrome("""G:\program files\chromedriver.exe""")
driver.maximize_window()
driver.get("https://azure.microsoft.com/en-us/services/cognitive-services/speech-to-text/#overview")
driver.find_element_by_xpath("""//*[@id="uploadbtn"]""").send_keys("record.wav")
# s.send_keys("record.wav")