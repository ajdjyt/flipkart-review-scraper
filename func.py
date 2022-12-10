from selenium import webdriver
from selenium.webdriver.common.by import By
import emoji
# Function to get rid of special characters which may cause issues in csv parsing
def clean(string):
    special_char='[@_!#$%^&*()<>?/\|}{~:].,"'
    # Remove new line characters
    string=string.strip().replace("\n"," ")
    # Remove all emojis
    string=emoji.replace_emoji(string, replace='')
    # Add all numbers,characters and special characters to string
    string=''.join(i for i in string if i.isnumeric() or i.isalpha() or i==" " or i in special_char)
    # Return cleaned string
    return string
# Function to get the reviews of the given url and return them
def seleniumrun(driver,link):
    driver.get(link)
    pgtitle=driver.title
    pgtitle=pgtitle[:pgtitle.find(":")]
    # Find all readmore elements on the page, where the review body is very long
    nreadmores=driver.find_elements(By.CLASS_NAME,'_1BWGvX')
    for i in range(len(nreadmores)):
        # Click all the readmore buttons to see the full text of the review
        nreadmores[i].click()
    reviews=[]
    # Find all review body elements
    reviewbodies=driver.find_elements(By.CLASS_NAME,'t-ZTKy')
    # Find all review title elements
    reviewheadings=driver.find_elements(By.CLASS_NAME,'_2-N8zT')
    # Find all review rating elements
    reviewratings=driver.find_elements(By.CSS_SELECTOR,'._3LWZlK._1BLPMq')
    # Get all the cleaned text and append it as a list to reviews
    for i in range(len(reviewbodies)):
        body=clean(reviewbodies[i].text)
        heading=clean(reviewheadings[i].text)
        rating=clean(reviewratings[i].text)
        reviews.append([int(rating),heading,body])
    # return the reviews list and the page title
    return [reviews,pgtitle]