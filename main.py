from selenium import webdriver
from selenium.webdriver.common.by import By
from func import seleniumrun,clean
import emoji,csv
output=[]
try:
    pages=int(input("How many pages: "))
    lk=input("Link: ")
except:
    print("Enter whole numbers for number of pages and enter links without any escape characters.")
    quit()
lk=lk.split("/")
if lk[2]!='www.flipkart.com':
    print("Enter only links from flipkart")
    quit()
out=''
driver=webdriver.Chrome()
for i in range(1,5):
    out=out+lk[i]+"/"
out+=lk[5].split("&marketplace")[0]
out+="&marketplace=FLIPKART&page=1"
out="https:"+out
out=out.replace("/p/","/product-reviews/")
for i in range(1,pages+1):
    out=out[:-1]
    out+=str(i)
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
