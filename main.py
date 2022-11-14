from selenium import webdriver
from selenium.webdriver.common.by import By
from func import seleniumrun,clean
import emoji,csv,selenium
output=[]
try:
    pages=int(input("How many pages: "))
    lk=input("Link: ")
except:
    print("Enter whole numbers for number of pages and enter links without any escape characters.")
    quit()

o=lk.split("/")
if o[2]!='www.flipkart.com':
    print("Enter only links from flipkart")
    quit()
driver=webdriver.Chrome()
driver.get(lk)
try:
    allreviews=driver.find_element(By.CSS_SELECTOR,'._3UAT2v._16PBlm')
    allreviews.click()
except selenium.common.exceptions.NoSuchElementException:
    print("Product has no reviews")
    quit()
'''
for i in range(1,5):
    out=out+lk[i]+"/"
out+=lk[5].split("&marketplace")[0]
out+="&marketplace=FLIPKART&page=1"
out="https:"+out
out=out.replace("/p/","/product-reviews/")
'''
for i in range(1,pages+1):
    out=driver.current_url
    out+="?page="+str(i)
    selout=seleniumrun(driver,out)
    for i in selout[0]:
        output.append(i)
driver.quit()
with open(selout[1]+".csv","w",newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(output)
    csvfile.close()
read=input("Read csv data? ")
if read.lower() in ["y","yes"]:
    with open(selout[1]+".csv","r") as csvfile:
        reader=csv.reader(csvfile)
        for i in reader: print(i)
