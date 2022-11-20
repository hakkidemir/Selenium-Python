from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

browser = webdriver.Firefox()
url="https://twitter.com/i/flow/login"
browser.get(url)
username=browser.find_element(By.CSS_SELECTOR, '.r-1wzrnnt')
username.send_keys("hakki")
time.sleep(5)
nextButton=browser.find_element(By.CSS_SELECTOR,'div.css-18t94o4:nth-child(6) > div:nth-child(1)')
nextButton.click()
password=browser.find_element(By.CSS_SELECTOR,'.r-30o5oe')
password.send_keys('parola')
login=browser.find_element(By.CSS_SELECTOR ,'div.css-18t94o4:nth-child(6) > div:nth-child(1)')
login.click()
time.sleep(5)
searcArea=browser.find_element(By.XPATH ,'/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]/div')
searcArea.click()
search=browser.find_element(By.XPATH , '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
search.send_keys("yazılımbilimi")
search.click()
time.sleep(5)

####################################### scroll #######################
SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
tweets=[]
elements=browser.find_element(By.CSS_SELECTOR , '#id__4mf608lmm8n')
for element in elements:
    tweets.append(element.text)
hakkis=browser.find_elements(By.CSS_SELECTOR , '#id__57p69ln0l4x > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)')
for hakki in hakkis:
    try:
        hakki.click()
    except Exception:
        print("bir sorun oluştu")
    
tweetcount=0
with open("twitter.txt","w",encoding="utf-8") as file:
    for tweet in tweets:
        file.write(str(tweetcount) +" \n " +tweet "\n" )
        file.write("********************************")
        tweetcount+=1


  
   
browser.close()


