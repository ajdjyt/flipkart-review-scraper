from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import emoji,csv
def clean(string):
    return emoji.replace_emoji(string, replace='').strip()
#from selenium.webdriver.common.keys import keys
link="https://www.flipkart.com/hp-ink-tank-wireless-415-all-one-multi-function-wifi-color-printer-voice-activated-printing-google-assistant-alexa-color-page-cost-20-paise-black-10-paise/product-reviews/itm3d317b6a651a2?pid=PRNF6M6F8V9BPNQ5&lid=LSTPRNF6M6F8V9BPNQ59PCYJM&marketplace=FLIPKART"
driver=webdriver.Chrome()
pages=1
driver.get(link)
pgtitle=driver.title
pgtitle=pgtitle[:pgtitle.find(":")]
print(pgtitle)
nreadmores=driver.find_elements(By.CLASS_NAME,'_1BWGvX')
for page in range(pages):
    for i in range(len(nreadmores)):
        nreadmores[i].click()
    reviews=[]
    reviewbodies=driver.find_elements(By.CLASS_NAME,'t-ZTKy')
    reviewheadings=driver.find_elements(By.CLASS_NAME,'_2-N8zT')
    reviewratings=driver.find_elements(By.CSS_SELECTOR,'._3LWZlK._1BLPMq')
    for i in range(10):
        body=clean(reviewbodies[i].text)
        heading=clean(reviewheadings[i].text)
        rating=clean(reviewratings[i].text)
        reviews.append([rating,heading,body])
    #sleep(10)
with open(pgtitle+".csv","w") as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(reviews)
    csvfile.close()
with open(pgtitle+".csv","r") as csvfile:
    reader=csv.reader(csvfile)
    for i in reader:
        print(i)
driver.quit()
