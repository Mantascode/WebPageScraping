from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import csv
import time

###### Kategoriju istraukimas ###########

url = '???'
driver = webdriver.Chrome("C:\\Users\Manta\Downloads\chromedriver_win32\chromedriver.exe")
driver.get(url)
time.sleep(5)

kategorijos = driver.find_elements_by_id('catUrlKey')

kat_list = []
for i in kategorijos:
    kat_list = i.text.split('\n')

for i in kat_list:
    print(i)


############## kategoriju surasymas

kategorijos = list()
with open('full_kategorijos.csv', 'r', encoding='utf-8') as kat:
    sk = csv.reader(kat, delimiter='\t')
    for i in kat:
        kategorijos.append(i.rstrip().replace('"', ""))


#### Istraukia linkus is svetaines pagal kiekviena kategorija  #########

url = '???'

driver = webdriver.Chrome("C:\\Users\Manta\Downloads\chromedriver_win32\chromedriver.exe")
driver.get(url)
time.sleep(5)


for kategorija in kategorijos:
    try:
        driver.find_element_by_xpath('//*[@id="gsCookieDisclaimer-close"]').click()
    except:
        pass

#### Ta uzkometuoti jei ieskau ne nuo pirmo puslapio
    driver.find_element_by_xpath('//*[@id="city"]/option[5]').click()
    time.sleep(5)
    driver.find_element_by_id('catUrlKey').send_keys(kategorija)
    driver.find_element_by_xpath('//*[@id="ok"]').click()
######

    time.sleep(10)
    del_miego = 0

    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "firmTitle")))
        pavadinimai = driver.find_elements_by_class_name('firmTitle')
        listoflinks = list()

        with open('names.csv', 'a', newline='', encoding='utf-8') as firmos:

            irasymas = csv.writer(firmos)

            pavadinimai = driver.find_elements_by_class_name('firmTitle')
            for pavadinimas in pavadinimai:
                listoflinks.append(pavadinimas.get_attribute('href'))
                pav = pavadinimas.get_attribute('href')
                print(f'{kategorija} - {pav}')
            time.sleep(5)

            try:
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "prevnext")))
                tol = driver.find_elements_by_class_name('prevnext')

                if len(tol) == 2:
                    tol[1].click()
                    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "firmTitle")))
                    pavadinimai = driver.find_elements_by_class_name('firmTitle')
                    for pavadinimas in pavadinimai:
                        listoflinks.append(pavadinimas.get_attribute('href'))
                        pav = pavadinimas.get_attribute('href')
                        print(f'{kategorija} - {pav}')
                    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "prevnext")))
                    tol = driver.find_elements_by_class_name('prevnext')
                    time.sleep(5)
                    while len(tol) == 4:
                        tol[1].click()
                        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "firmTitle")))
                        pavadinimai = driver.find_elements_by_class_name('firmTitle')
                        for pavadinimas in pavadinimai:
                            listoflinks.append(pavadinimas.get_attribute('href'))
                            pav = pavadinimas.get_attribute('href')
                        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "prevnext")))
                        tol = driver.find_elements_by_class_name('prevnext')
                        print(f'{kategorija} - {pav}')
                        time.sleep(5)
            except:
                pass

            if del_miego % 4 == 0:
                time.sleep(5)
            del_miego += 1

            for line in listoflinks:

                irasymas.writerow([kategorija, line])
    except:
        print(f'{kategorija} - nerasta')



#### Pasalina pasikartojancius linkus ir sukuria nauja cvs sarasa, kuriame nera pasikartojimu

sarasas_nerusiuotas = list()
with open('names.csv', 'r', encoding='utf-8') as url:
    sk = csv.reader(url, delimiter=',')
    for i in sk:
        sarasas_nerusiuotas.append(i[1])

unikalus_sarasas = set(sarasas_nerusiuotas)

with open('names_unique.csv', 'w', newline='', encoding='utf-8') as firmos:
    irasymas1 = csv.writer(firmos, delimiter=',')
    for i in unikalus_sarasas:
        irasymas1.writerow([i])


#### Pagal unikalius linkus istraukia reikalinga informacija ir suraso i nauja cvs faila


url_list = list()

with open('names_unique.csv', 'r', encoding='utf-8', newline= '') as url:
    filtered = (line.replace('\r', '') for line in url) #pasalina entry (newline)
    for i in csv.reader(filtered):
        url_list.append(i[0])

a = 1

driver = webdriver.Chrome("C:\\Users\Manta\Downloads\chromedriver_win32\chromedriver.exe")

for url in url_list:
    print(url)

    driver.get(url)


    listofirm = list()
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "fn")))
        pavadinimas = driver.find_element_by_class_name('fn')

        listofirm.append(pavadinimas.text)

    except:
        pass

    try:
        adresas = driver.find_elements_by_tag_name('td')
        i = 0
        for i in range(len(adresas)):
            if adresas[i].text == "Vadovas":
                listofirm.append(adresas[i+1].text)

        j = 0
        for j in range(len(adresas)):
            if adresas[j].text == "Tinklalapis":
                listofirm.append(adresas[j + 1].text)

        time.sleep(1)


    except:
        pass
    print(f'{a} - {listofirm}')

    with open('names.v.csv', 'a', newline='', encoding='utf-8') as firmos:
        irasymas1 = csv.writer(firmos, delimiter=',')

        if len(listofirm) == 3:
            irasymas1.writerow([listofirm[0], listofirm[1], listofirm[2]])
            print('Irasyta')
            print('')
            a += 1
        elif len(listofirm) == 2:
            irasymas1.writerow([listofirm[0], listofirm[1]])
            print('Irasyta')
            print('')
            a += 1
        else:
            print('')

