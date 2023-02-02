from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
#options = ChromeOptions()
#options.headless = True
driver.get('https://www.eliteprospects.com/draft/nhl-entry-draft/2015')
driver.implicitly_wait(10)

# Find the table containing the draft data
table = driver.find_element(By.CLASS_NAME, "draft")
# Find all of the rows in the table
rows = table.find_elements(By.TAG_NAME, "tr")
# Print the data for each row

data = {}
counter = 0
#data[1]="Connor McDavid"
for row in rows:
    # Find all of the cells in the row
    cells = row.find_elements(By.TAG_NAME, "td")
    # Print the data for each cell
    for cell in cells:
        print(counter,"Text",cell.text)
        if counter == 54:
            player = cell.text
            data[player]=[]
        elif counter == 55 or counter == 56 or counter == 57 or counter == 58 or counter == 59 or counter == 60: 
            data[player].append(cell.text)
        counter += 1
print(data)
# Close the browser
driver.quit()

#data = {"Connor McDavid": [1, 8, 537, 280]}