def sendmail(from_mail,password,li,sub,msg):
    import time
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    driver.get('https://mail.google.com')
    try:
        box1 = driver.wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
        box1.send_keys(from_mail)
        btn= driver.wait.until(EC.presence_of_element_located((By.ID, "identifierNext")))
        btn.click() 
        time.sleep(5)           
        box1 = driver.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        box1.send_keys(password)
        btn1= driver.wait.until(EC.presence_of_element_located((By.ID, "passwordNext")))
        btn1.click()
        time.sleep(5)
        for x in range (0,len(li)):            
            driver.get('https://mail.google.com/mail/u/0/#inbox?compose=new')
            time.sleep(5)
            recip= driver.wait.until(EC.presence_of_element_located((By.NAME, "to")))
            recip.send_keys(li[x][0])
            subj= driver.wait.until(EC.presence_of_element_located((By.NAME, "subjectbox")))
            subj.send_keys(sub)
            cont= driver.find_element_by_class_name("Am.Al.editable.LW-avf")
            cont.send_keys('Hii '+li[x][1]+msg)
            btn =driver.find_element_by_class_name("T-I.J-J5-Ji.aoO.T-I-atl.L3")
            btn.click()
            time.sleep(3)
    except TimeoutException:
        print("Box or Button not found.")
    driver.quit()
# sendmail('ae16b111@smail.iitm.ac.in','joeydash',[['joydassudipta@gmaiil.com','joeydash'],['joydassudipta@gmaiil.com','joeydash']],'you are nice boy','you are going to be become an engineer!')

