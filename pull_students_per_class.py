# -*- coding: utf-8 -*-
"""
Created on Wed May  1 12:57:03 2019

@author: jasplund
"""


import re
import copy
from Class import Class
from ClassList import ClassList
from Session import Session
from EquivalenceClassList import EquivalenceClassList
from selenium import webdriver
import sys
import csv

pattern1_str = "(?P<crn>\d{5})\s+(?P<dept>[A-Z]{4})\s+(?P<course_number>\d{4}[A-Z]*)\s+(?P<section>\d+[A-Z]*)"
pattern1 = re.compile(pattern1_str)

pattern2_str = "\s+(?P<start_date>\d{2}\-[A-Z]{3})-\d{4}\s+(?P<end_date>\d{2}-[A-Z]{3}-\d{4})\s+(?P<days>[MTWRF]+)\s+(?P<start_time>\d{2}:\d{2}[ap]m)-(?P<end_time>\d{2}:\d{2}[ap]m)\D+\d{4}[A-z]*"
pattern2 = re.compile(pattern2_str)

class_list = ClassList()

current_class = None

#with open('banner_course_schedule.py') as f:
with open('html_classes_content.txt') as f:

    for line in f:

        results1 = pattern1.match(line)
        results2 = pattern2.match(line)
        
        if results1 != None:
            if current_class != None:
                class_list.add_class(current_class)
            current_crn = results1.group('crn')
            current_dept = results1.group('dept')
            current_course_number = results1.group('course_number')
            current_section = results1.group('section')
            current_class = Class(current_crn, current_dept, current_course_number, current_section)
    
        elif results2 != None:
            
            new_session = Session(results2.group('days'), results2.group('start_time'), results2.group('end_time'), results2.group('start_date'), results2.group('end_date'))    
            current_class.add_session(new_session) 

# Don't forget to add the last class
class_list.add_class(current_class)
class_list.remove_no_sessions()
class_list.remove_specialized()
class_list.remove_a_session()



#def site_login():
#    driver = webdriver.Chrome()
#    #Set the website
#    driver.get('https://mydsccas.daltonstate.edu/cas/login?service=https://roadrunner.daltonstate.edu/index.cms')
#    driver.find_element_by_id('username').send_keys('jasplund')
#    driver.find_element_by_id ('password').send_keys('!Roadrunner141A')
#    driver.find_element_by_name('submit').click()
#    driver.get("https://daltonstate.gabest.usg.edu/ssomanager/c/SSB?pkg=twbkwbis.P_GenMenu?name=bmenu.P_FacMainMnu")


#site_login()
#crn = '80091'
#
#driver.get("https://daltonstate.gabest.usg.edu/B690/html_schedule2.html_class_listing?term=201908&crn="+crn)
#txt = driver.find_element_by_class_name("pagebodydiv").text
#print(txt)
    
usr_name = str(sys.argv[1])
pw = str(sys.argv[2])
    
pattern1_str = "(?P<std_id>\d{9})"
pattern1 = re.compile(pattern1_str)

driver = webdriver.Chrome()
driver.get('https://mydsccas.daltonstate.edu/cas/login?service=https://roadrunner.daltonstate.edu/index.cms')
driver.find_element_by_id('username').send_keys(usr_name)
driver.find_element_by_id ('password').send_keys(pw)
driver.find_element_by_name('submit').click()
driver.get("https://daltonstate.gabest.usg.edu/ssomanager/c/SSB?pkg=twbkwbis.P_GenMenu?name=bmenu.P_FacMainMnu")
d = {}
i=0
for cl in class_list.classes:
    crn = cl.crn
    driver.get("https://daltonstate.gabest.usg.edu/B690/html_schedule2.html_class_listing?term=201908&crn="+crn)
    txt = driver.find_element_by_class_name("pagebodydiv").text
    
    d[crn] = []
    
    for line in txt.split('\n'):
#        print(line)
        results1 = pattern1.match(line)
#        print(results1)
#        print(txt)
        if results1 != None:
            d[crn].append(results1.group('std_id'))

    print(i)
    i+=1    

w = csv.writer(open("students_to_classes.csv", "w"))
for key, val in d.items():
    w.writerow([key, val])

