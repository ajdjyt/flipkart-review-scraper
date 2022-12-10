from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from func import seleniumrun,clean
import emoji,csv,selenium
from rich import print
output=[]
try:
    pages=int(input("How many pages: "))
    lk=input("Link: ")
except:
    print("Enter whole numbers for number of pages and enter links without any escape characters.")
    quit()

o=lk.split("/")
ifflipkart=[i for i in o if i=="www.flipkart.com"]
if len(ifflipkart)<1 or len(ifflipkart)>1:
    print("Enter only links from flipkart")
    quit()
options=Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# Ask the user to run chrome in the background or not5
isheadless=input("Run in the background? Yes or no: ")
if isheadless.lower() in ["yes","y"]:
    options.add_argument('headless')   
# Load strategy to speed up the program
print("Choose a load strategy")
print("1.Normal, If your computer or internet is slow")
print("2.Eager, If your computer and internet is fast")
print("If the program keeps failing pick Normal")
try:
    loadstrat=int(input(": "))
except ValueError:
    print("Enter a number")
    quit()
if loadstrat==1:
    driver=webdriver.Chrome(options=options)
elif loadstrat==2:
    options.page_load_strategy = 'eager'
    driver=webdriver.Chrome(options=options)
else:
    print("Enter a valid option")
    quit()
# Start the chrome engine
driver.get(lk) 
# Click The all reviews button
try:
    allreviews=driver.find_element(By.CSS_SELECTOR,'._3UAT2v._16PBlm')
    allreviews.click()
except selenium.common.exceptions.NoSuchElementException:
    print("Product has no reviews")
    quit()
# Get review page base url
reviewpage=driver.current_url
for i in range(1,pages+1):
    out=reviewpage+"&page="+str(i)
    selout=seleniumrun(driver,out)
    # Add the reviews to a list
    for i in selout[0]:
        output.append(i)
# Close chrome after finishing getting the reviews
driver.quit()
# Write the reviews to the csvfile with the name of the product
with open(selout[1]+".csv","w",newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(output)
    csvfile.close()
# Get best,low ratings and calculate avg
ratings=[int(i[0]) for i in output]
best=[i for i in output if int(i[0]>=4)]
low=[i for i in output if int(i[0]<=3)]
avg=sum(ratings)/len(ratings)
# While loop to give the user to data
while 1:
    print("0.Quit")
    print("1.Average rating")
    print("2.High rating reviews")
    print("3.Low rating reviews")
    print("4.All reviews")
    try:
        ch=int(input("Choose one of the above options: "))
    except ValueError:
        print("Enter a number")
    if ch==0:
        break
    elif ch==1:
        print("The average of review of",selout[1].split("Reviews")[0]+"is",avg,"stars.")
    elif ch==2:
        print(best)
    elif ch==3:
        print(low)
    elif ch==4:
        with open(selout[1]+".csv","r") as csvfile:
            reader=csv.reader(csvfile)
            for i in reader: print(i)
    else:
        print("Enter a valid option")
