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
counter2 = 0 #Once the couter gets to a certain number it terminates the program
#data[1]="Connor McDavid"
for row in rows:
    # Find all of the cells in the row
    cells = row.find_elements(By.TAG_NAME, "td")
    # Print the data for each cell
    for cell in cells:
        print(counter,"Text",cell.text)
        if counter == 64:
            player = cell.text
            data[player]=[]
        elif counter == 65 or counter == 66 or counter == 67 or counter == 68 or counter == 69 or counter == 70: 
            data[player].append(cell.text)
        elif counter == 73:
            counter = 63
        elif counter2 == 300:
            break
        elif "ROUND" in cell.text:
            counter += 1
        counter2 += 1
        counter += 1

print(data)
# Close the browser
driver.quit()

