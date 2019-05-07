# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:35:11 2019

@author: jasplund
"""

from selenium import webdriver


driver = webdriver.Chrome()
#Set the website
driver.get("https://daltonstate.gabest.usg.edu/B690/COM_F02_PKG.course_search")

#Select the item from the drop down menu.
driver.find_element_by_xpath("//select[@name='stvterm_code']/option[text()='201908 -- Fall 2019']").click()

#Click the button to go to the next webpage
button = driver.find_elements_by_xpath("//input[@name='cbutton' and @value='Submit Term']")[0]
button.click()

#Select the item from the drop down menu.
driver.find_element_by_xpath("//select[@name='stvptrm_code']/option[text()='1 -- Full Semester']").click()

#Click the button to go to the next webpage.
button = driver.find_elements_by_xpath("//input[@name='cbutton' and @value='Submit Part of Term']")[0]
button.click()

#Select the item from the drop down menu.
driver.find_element_by_xpath("//select[@name='stvcamp_code']/option[text()='A -- Main Campus']").click()

#Click the button to go to the next webpage.
button = driver.find_elements_by_xpath("//input[@name='cbutton' and @value='Search']")[0]
button.click()

##Set the class by which we want. 
#html_classes = driver.find_element_by_xpath("//div[@class='pagebodydiv']")
#html_classes_content = html_classes.get_attribute('innerHTML')

#Find the text for the class we want. 
txt = driver.find_element_by_class_name("pagebodydiv").text

with open('html_classes_content2.txt', 'a') as the_file:
    for line in txt.split('\n'):
        the_file.write(line)

##Write text to text file.
#text_file = open("html_classes_content.txt", "w")
#text_file.write(txt)
#text_file.close()
