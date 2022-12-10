# Flipkart review scraper  
Scrapes the reviews of the given flipkart products link.  
## Dependencies:    
```
selenium,emoji,rich
```
Install these via  
```
python -m pip install -U selenium emoji rich  
```
Or  
```
python -m pip install -r requirements.txt  
```  
Also for selenium the Chrome driver is used. To setup the Chrome driver for your platform follow this [link](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/ ).  
Any Chromium based browser should work Edge,Google Chrome etc.  
If you do not have any chrome based browser installed i recommend [Ungoogled Chromium](https://ungoogled-software.github.io/ungoogled-chromium-binaries/) [(Github)](https://github.com/  ungoogled-software/ungoogled-chromium).  
## Running:   
Place main.py and func.py in the same directory  
run by  
```
python main.py  
```
## Output:  
Output is in the format of a csv with the name of the website url, all newline characters,emojis are removed.  
The only accepted special characters are:  
```
[@_!#$%^&*()<>?/\|}{~:].,"  
```
The csv is formatted as [rating,heading,body]. If you find that the heading or body is empty,  
its probably because they contained only special characters outside of the above mentioned  

Also checkout my image-rescaler project at this [link](https://github.com/ajdjyt/image-rescaler)  
