from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

s = Service("./drivers/geckodriver")
options = ChromeOptions()
options.headless = True
driver = webdriver.Chrome(service=s,options = options)

#options = ChromeOptions()
#options.headless = True
driver.get('https://www.eliteprospects.com/draft/nhl-entry-draft/2015')
driver.implicitly_wait(10)

# Find the table containing the draft data
table = driver.find_element(By.CLASS_NAME, "draft")
# Find all of the rows in the table
rows = table.find_elements(By.TAG_NAME, "tr")
print(rows)
# Print the data for each row
click = rows[0].find_elements(By.CLASS_NAME, "player")
click2 = rows[0].find_elements(By.TAG_NAME, "td")
click3 = rows[0].find_elements(By.XPATH, '//td[@class="player"]//a[@href]')
print(click2)
print(click3)
for i in click3:
    print(i.text)
    i = i.get_attribute('href')
    print(i.click())
    print(i.text)
data = {}
counter = 0
counter2 = 0 #Once the couter gets to a certain number it terminates the program
#data[1]="Connor McDavid"
for row in rows:
    # Find all of the cells in the row
    cells = row.find_elements(By.TAG_NAME, "td")
    # Print the data for each cell
    for cell in cells:
        print(counter,"Text",cell.text)
        if counter == 65:
            player = cell.text
            data[player]=[]
        elif counter == 66 or counter == 67 or counter == 68 or counter == 69 or counter == 70 or counter == 71: 
            data[player].append(cell.text)
        elif counter == 74:
            counter = 64
        elif counter2 == 300:
            print(data)
            break
        elif "ROUND 1" in cell.text:
            counter += 1
        elif "ROUND" in cell.text:
            counter -= 1
        counter2 += 1
        counter += 1

print(data)
# Close the browser
driver.quit()
