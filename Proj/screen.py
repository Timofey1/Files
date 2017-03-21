from selenium import webdriver
from PIL import Image

fox = webdriver.Chrome()
fox.get('https://www.artlebedev.ru/kovodstvo/business-lynch/2016/12/23/')

# now that we have the preliminary stuff out of the way time to get that image :D
element = fox.find_element_by_id('ToggleCommented') # find part of the page you want image of
element.click()
element = fox.find_element_by_id('LynchComments')
location = element.location
size = element.size
fox.save_screenshot('screenshot.png') # saves screenshot of entire page
fox.quit()
#
# im = Image.open('screenshot.png') # uses PIL library to open image in memory
#
# left = location['x']
# top = location['y']
# right = location['x'] + size['width']
# bottom = location['y'] + size['height']
#
#
# im = im.crop((left, top, right, bottom)) # defines crop points
# im.save('screenshot.png') # saves new cropped image