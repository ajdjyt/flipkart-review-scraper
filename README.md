# Flipkart review scraper  
Scrapes the reviews of the given flipkart products link.  
## Dependencies:    
```
selenium,emoji  
```
Install these via  
```
python -m pip install -U selenium emoji  
```
Also for selenium the Chrome driver is used. To setup the Chrome driver for your platform follow this [link](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/ ).
## Running:   
Place main.py and func.py in the same directory  
run by  
```
python.exe main.py  
```
## Output:  
Output is in the format of a csv with the name of the website url, all newline characters,emojis are removed.  
The only accepted special characters are:  
```
[@_!#$%^&*()<>?/\|}{~:].,"  
```
The csv is formatted as [rating,heading,body]. If you find that the heading or body is empty,  
its probably because they contained only special characters outside of the above mentioned  
