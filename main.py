from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import csv
import time

###### Kategoriju istraukimas ###########

# url = 'https://rekvizitai.vz.lt/imones/'
# # url = 'https://rekvizitai.vz.lt/imones/transporto_paslaugos/siauliai/21/'
# driver = webdriver.Chrome("C:\\Users\Manta\Downloads\chromedriver_win32 (1)\chromedriver.exe")
# driver.get(url)
# time.sleep(5)
#
# kategorijos = driver.find_elements_by_id('catUrlKey')
#
# kat_list = []
# for i in kategorijos:
#     kat_list = i.text.split('\n')
#
# for i in kat_list:
#     print(i)

        ### nukopijavau ir su OpenOffice sutvarkiau formatavima


############## kategoriju surasymas

# kategorijos = list()
# with open('full_kategorijos.csv', 'r', encoding='utf-8') as kat:
#     sk = csv.reader(kat, delimiter='\t')
#     for i in kat:
#         kategorijos.append(i.rstrip().replace('"', ""))
# # for i in kategorijos:
# #     print(i)
#
#
# #### Istraukia linkus is svetaines pagal kiekviena kategorija  #########
#
# url = 'https://rekvizitai.vz.lt/imones/'
# # url = 'https://rekvizitai.vz.lt/imones/namu_savininku_bendrijos/21/'
# driver = webdriver.Chrome("C:\\Users\Manta\Downloads\chromedriver_win32 (1)\chromedriver.exe")
# driver.get(url)
# time.sleep(5)
#
# # kategorijos = ['Namų savininkų bendrijos'] #### pakeisti pagal reikiama kategorija
#
# for kategorija in kategorijos:
#     try:
#         driver.find_element_by_xpath('//*[@id="gsCookieDisclaimer-close"]').click()
#     except:
#         pass
#
# #### Ta uzkometuoti jei ieskau ne nuo pirmo puslapio
#     driver.find_element_by_xpath('//*[@id="city"]/option[5]').click()  # Option[miesto numeris]
#     time.sleep(5)
#     driver.find_element_by_id('catUrlKey').send_keys(kategorija)
#     driver.find_element_by_xpath('//*[@id="ok"]').click()
# ######
#
#     time.sleep(10)
#     del_miego = 0
#
#     try:
#         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "firmTitle")))
#         pavadinimai = driver.find_elements_by_class_name('firmTitle')
#         listoflinks = list()
#         # print('Ar veikia? 4')
#         with open('arab_project_linkai.csv', 'a', newline='', encoding='utf-8') as firmos:
#
#             irasymas = csv.writer(firmos)
#             # print('Ar veikia? 3')
#             pavadinimai = driver.find_elements_by_class_name('firmTitle')
#             for pavadinimas in pavadinimai:
#                 listoflinks.append(pavadinimas.get_attribute('href'))
#                 pav = pavadinimas.get_attribute('href')
#                 print(f'{kategorija} - {pav}')
#             time.sleep(5)
#             # print('Ar veikia? 1')
#             try:
#                 WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "prevnext")))
#                 tol = driver.find_elements_by_class_name('prevnext')
#                 # print('Ar veikia? 2')
#                 if len(tol) == 2: #Jei ieskai nuo toliau, tada reikia keisti i 4, jei nuo pirmo, tada 2
#                     tol[1].click()
#                     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "firmTitle")))
#                     pavadinimai = driver.find_elements_by_class_name('firmTitle')
#                     for pavadinimas in pavadinimai:
#                         listoflinks.append(pavadinimas.get_attribute('href'))
#                         pav = pavadinimas.get_attribute('href')
#                         print(f'{kategorija} - {pav}')
#                     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "prevnext")))
#                     tol = driver.find_elements_by_class_name('prevnext')
#                     time.sleep(5)
#                     while len(tol) == 4:
#                         tol[1].click()
#                         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "firmTitle")))
#                         pavadinimai = driver.find_elements_by_class_name('firmTitle')
#                         for pavadinimas in pavadinimai:
#                             listoflinks.append(pavadinimas.get_attribute('href'))
#                             pav = pavadinimas.get_attribute('href')
#                         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "prevnext")))
#                         tol = driver.find_elements_by_class_name('prevnext')
#                         print(f'{kategorija} - {pav}')
#                         time.sleep(5)
#             except:
#                 pass
#
#             if del_miego % 4 == 0:
#                 time.sleep(5)
#             del_miego += 1
#
#             for line in listoflinks:
#
#                 irasymas.writerow([kategorija, line])
#     except:
#         print(f'{kategorija} - firmų nerasta')


#### Patikrina, kiek kiekvienos kategorijos firmu rasta. Jei vienos katerogijos firmu skaicius yra 300, tiketina,
#### kad visu firmu neturiu

# kiek_list = list()
# kiek = 0
# naujas = []
# with open('arab_project_linkai.csv', 'r', encoding='utf-8') as url:
#     sk = csv.reader(url, delimiter=',')
#     b = 0
#
#     for j in sk:
#         naujas.append(j)
#
#     paskutinis = len(naujas) - 1
#     for i in naujas:
#         # Tikrina ar elementas yra paskutinis
#         if naujas.index(i) == paskutinis:
#             if kiek >= 300:
#                 tekstas = f'{kiek} - {b} -  - -  -   -  -  - -   virsija 300!!!!!!!!!!'
#             else:
#                 tekstas = f'{kiek} - {b}'
#             kiek_list.append(tekstas)
#
#         if i[0] == b or b == 0:
#             kiek += 1
#             b = i[0]
#         else:
#             if kiek >= 300:
#                 tekstas = f'{kiek} - {b} -  - -  -   -  -  - -   virsija 300!!!!!!!!!!'
#             else:
#                 tekstas = f'{kiek} - {b}'
#             kiek_list.append(tekstas)
#             kiek = 1
#             b = i[0]
#
# for i in kiek_list:
#     print(i)


#### Pasalina pasikartojancius linkus ir sukuria nauja cvs sarasa, kuriame nera pasikartojimu

# sarasas_nerusiuotas = list()
# with open('arab_project_linkai.csv', 'r', encoding='utf-8') as url:
#     sk = csv.reader(url, delimiter=',')
#     for i in sk:
#         sarasas_nerusiuotas.append(i[1])
#
# unikalus_sarasas = set(sarasas_nerusiuotas)
#
# with open('unikalus_arabic_siauliai.csv', 'w', newline='', encoding='utf-8') as firmos:
#     irasymas1 = csv.writer(firmos, delimiter=',')
#     for i in unikalus_sarasas:
#         irasymas1.writerow([i])


#### Pagal unikalius linkus istraukia reikalinga informacija ir suraso i nauja cvs faila


# url_list = list()
#
# with open('unikalus_arabic_siauliai.csv', 'r', encoding='utf-8', newline= '') as url:
#     filtered = (line.replace('\r', '') for line in url) #pasalina entry (newline)
#     for i in csv.reader(filtered):
#         url_list.append(i[0])
#
# a = 1
#
# driver = webdriver.Chrome("C:\\Users\Manta\Downloads\chromedriver_win32 (1)\chromedriver.exe")
#
# for url in url_list:
#     print(url)
#
#     driver.get(url)
#
#     # time.sleep(2)
#     # del_miego = 0
#     listofirm = list()
#     try:
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "fn")))
#         pavadinimas = driver.find_element_by_class_name('fn')
#
#         listofirm.append(pavadinimas.text)
#
#         # time.sleep(1)
#
#         # if del_miego % 4 == 0:
#         #     time.sleep(2)
#         # del_miego += 1
#     except:
#         pass
#
#     try:
#         adresas = driver.find_elements_by_tag_name('td')
#         i = 0
#         for i in range(len(adresas)):
#             if adresas[i].text == "Vadovas":
#                 listofirm.append(adresas[i+1].text)
#             # else:
#             #     listofirm.append('')
#         j = 0
#         for j in range(len(adresas)):
#             if adresas[j].text == "Tinklalapis":
#                 listofirm.append(adresas[j + 1].text)
#             # else:
#             #     listofirm.append('')
#         time.sleep(1)
#
#
#         # if del_miego % 4 == 0:
#         #     time.sleep(2)
#         # del_miego += 1
#
#     except:
#         pass
#     print(f'{a} - {listofirm}')
#     # driver.quit()
#
#     with open('Siauliai_firmos.v.csv', 'a', newline='', encoding='utf-8') as firmos:
#         irasymas1 = csv.writer(firmos, delimiter=',')
#
#         if len(listofirm) == 3:
#             irasymas1.writerow([listofirm[0], listofirm[1], listofirm[2]])
#             print('Irasyta')
#             print('')
#             a += 1
#         elif len(listofirm) == 2:
#             irasymas1.writerow([listofirm[0], listofirm[1]])
#             print('Irasyta')
#             print('')
#             a += 1
#         else:
#             print('')


#### Istraukia vardu sarasa ###########

# url = 'https://www.horoskopai.lt/visi-vardai-pagal-abecele/'
# driver = webdriver.Chrome("C:\\Users\Manta\Downloads\chromedriver_win32 (1)\chromedriver.exe")
# driver.get(url)
#
# vardai = driver.find_elements_by_tag_name('a')
#
# # for i in vardai:
# #     print(i.text)
#
# with open('Vardu sarasas.csv', 'a', newline='', encoding='utf-8') as vardai1:
#     irasymas = csv.writer(vardai1, delimiter=',')
#
#     for vardas in vardai:
#         irasymas.writerow([vardas.text])

#### Istrina nereikalingas eilutes ############

vardu_sar = []
with open('Vardu sarasas.csv', 'r', encoding='utf-8') as be_lt:
    sk = csv.reader(be_lt, delimiter=',')
    for i in sk:
        vardu_sar.append(i[0])

be_lt_vardu = list()
with open('Siauliai_firmos.v.csv', 'r', encoding='utf-8') as be_lt:
    sk = csv.reader(be_lt, delimiter=',')
    for i in sk:
        vardas = i[1].split(' ')
        if vardas[0] not in vardu_sar and vardas[0][0].isupper():
            be_lt_vardu.append(i)




with open('Galutinis_arab.csv', 'w', newline='', encoding='utf-8') as sarasiukas:
        irasymas1 = csv.writer(sarasiukas, delimiter=',')

        for i in be_lt_vardu:

            if len(i) == 3:
                irasymas1.writerow([i[0], i[1], i[2]])

            elif len(i) == 2:
                irasymas1.writerow([i[0], i[1]])
