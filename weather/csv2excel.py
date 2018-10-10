# -*- coding: utf-8 -*-
import os
import pandas as pd

def csv_to_xlsx_pd():
    csv = pd.read_csv('/Users/mengxiangyu/Downloads/weather.csv', encoding='utf-8')
    csv.to_excel('/Users/mengxiangyu/Downloads/weather.xlsx', sheet_name='data')

def listdir(path, list_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        elif os.path.splitext(file_path)[1] == '.jpeg':
            list_name.append(file_path)

def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.csv':
                L.append(os.path.join(root, file))
    return L

if __name__ == '__main__':
    csv_to_xlsx_pd()
'''
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.find_element_by_id('kw').send_keys('selenium')
    driver.find_element_by_id('su').click()
    # driver.quit()\

    with open('cities.txt', 'r') as f:
        cities = f.read().split(' ')
    print(cities)
    file_dir = ''
    L = file_name()
    for l in L:
        csv_to_xlsx_pd()

'''




