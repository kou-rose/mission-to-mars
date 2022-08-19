#!/usr/bin/env python
# coding: utf-8

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

#pip install splinter

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

browser.quit()

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

html = browser.html
main_page = soup(html, 'html.parser')

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# find the HTML tag that holds all the links to the full resolution images or common CSS element
full_rez = main_page.find_all('div', class_='item')

# using a for loop, iterate through the tags or CSS element
for full_rez in range(4):

# create an empty dictionary hemisphere = {} inside the loop
    hemispheres = {}

# with the for loop: click on each hemisphere link, navigate to full resolution image,
    # retrieve full image resolution image url string and title,
    # use browser.back() to navigate to the beginning and get the next image

    full_image = main_page.find_all('div', class_='item')[0].a.get('href')
    browser.find_by_text(f'https://marshemispheres.com/{full_image}').click()
    
    html = browser.html
    sample_image = soup(html, 'html.parser')
    
    img_url = sample_image.find('div.downloads ul li a').get('href')
    img_title = sample_image.find('h2.title').get_text()
    
    hemispheres = {
        'img_url': img_url,
        'title': img_title}
    
    hemisphere_image_urls.append(hemispheres)
    
    browser.back()
# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()



