import time
import random
import undetected_chromedriver.v2 as uc
m = 1

#Here we add the list of mails
mail_list = ['aliandabdelrahman', 'mahmopudnasser']
name1_list = ['Mahmoud', 'Ali', 'Ahmed']
name2_list = ['Nasser', 'omar', 'Zaki']
year_list = ['2000', '20001', '20001']
pas_list = ['Zhgffdgfdgfd']



accounts_numbers = int(input("Enter the number of accounts: "))

for i in range(accounts_numbers):
    web = uc.Chrome()
    mail = random.choice(mail_list)
    pas = random.choice(pas_list)
    name1 = random.choice(name1_list)
    name2 = random.choice(name2_list)
    year = random.choice(year_list)
    web.get("https://outlook.live.com/owa/?nlp=1&signup=1")
    web.find_element_by_xpath('//*[@id="MemberName"]').send_keys(mail,m)
    time.sleep(1)
    web.find_element_by_xpath('//*[@id="iSignupAction"]').click()
    time.sleep(2.2)
    web.find_element_by_xpath('//*[@id="PasswordInput"]').send_keys(pas)
    time.sleep(1)
    web.find_element_by_xpath('//*[@id="iSignupAction"]').click()
    time.sleep(1)
    web.find_element_by_xpath('//*[@id="FirstName"]').send_keys(name1)
    web.find_element_by_xpath('//*[@id="LastName"]').send_keys(name2)
    time.sleep(1)
    web.find_element_by_xpath('//*[@id="iSignupAction"]').click()
    time.sleep(2)
    web.find_element_by_xpath('//*[@id="BirthDay"]/option[16]').click()
    web.find_element_by_xpath('//*[@id="BirthMonth"]/option[10]').click()
    web.find_element_by_xpath('//*[@id="BirthYear"]').send_keys(year)
    web.find_element_by_xpath('//*[@id="iSignupAction"]').click()
    time.sleep(30)
    print("-----------------------------------------------------------------------------------")
    print(mail+str('@outlook.com'))
    print(pas)

