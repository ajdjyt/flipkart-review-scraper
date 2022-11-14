from selenium import webdriver
from selenium.webdriver.common.by import By
import emoji
def clean(string):
    special_char='[@_!#$%^&*()<>?/\|}{~:].,"'
    string=string.strip().replace("\n"," ")
    string=emoji.replace_emoji(string, replace='')
    string=''.join(i for i in string if i.isnumeric() or i.isalpha() or i==" " or i in special_char)
    return string
def seleniumrun(driver,link):
    driver.get(link)
    pgtitle=driver.title
    pgtitle=pgtitle[:pgtitle.find(":")]
    nreadmores=driver.find_elements(By.CLASS_NAME,'_1BWGvX')
    for i in range(len(nreadmores)):
        nreadmores[i].click()
    reviews=[]
    reviewbodies=driver.find_elements(By.CLASS_NAME,'t-ZTKy')
    reviewheadings=driver.find_elements(By.CLASS_NAME,'_2-N8zT')
    reviewratings=driver.find_elements(By.CSS_SELECTOR,'._3LWZlK._1BLPMq')
    for i in range(len(reviewbodies)):
        body=clean(reviewbodies[i].text)
        heading=clean(reviewheadings[i].text)
        rating=clean(reviewratings[i].text)
        reviews.append([rating,heading,body])
    return [reviews,pgtitle]