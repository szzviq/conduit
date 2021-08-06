from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from adat import *





class TestConduit1(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get("http://localhost:1667/#/")

    def teardown(self):
        self.driver.quit()

    # TC1 accepting cookies
    def test_accept_cookies(self):
        self.driver.find_element_by_xpath('//button[contains(@class, "accept")]').click()
        time.sleep(2)
        after_accept = self.driver.get_cookie("vue-cookie-accept-decline-cookie-policy-panel")
        assert after_accept['value'] == 'accept'

    # #TC2 registration
    #     #negative with too simple password
    #     def test_bad_signup(self):
    #         self.test_accept_cookies()

    #         self.driver.find_element_by_xpath('//a[contains(text(),"Sign up")]').click()
    #         self.driver.find_element_by_xpath('//input[contains(@placeholder,"Username")]').send_keys(username)
    #         self.driver.find_element_by_xpath('//input[contains(@placeholder,"Email")]').send_keys(mail)
    #         self.driver.find_element_by_xpath('//input[contains(@placeholder,"Password")]').send_keys(bad_password)
    #         self.driver.find_element_by_xpath('//button[contains(@class,"pull-xs")]').click()
    #         self.driver.implicitly_wait(8)
    #         # alert_n_text = self.driver.find_element_by_xpath('//div[@class="swal-title"]')
    #         alert_n_subtext = self.driver.find_element_by_xpath('//div[@class="swal-text"]')
    #         print(alert_n_subtext.text)
    #         reg_fail = "Password must be 8 characters long and include 1 number, 1 uppercase letter, and 1 lowercase letter. "
    #         time.sleep(3)
    #         assert alert_n_subtext.text == reg_fail
    #         self.driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]').click()

    #         #positive
    def test_signup(self):
        self.driver.find_element_by_xpath('//a[contains(text(),"Sign up")]').click()
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"Username")]').send_keys(username)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"Email")]').send_keys(mail_1)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"Password")]').send_keys(password)
        self.driver.find_element_by_xpath('//button[contains(@class,"pull-xs")]').click()
        self.driver.implicitly_wait(8)
        alert_text = self.driver.find_element_by_xpath('//div[@class="swal-title"]')
        success = "Welcome!"
        self.driver.implicitly_wait(2)
        assert alert_text.text == success
        time.sleep(2)
        self.driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]').click()

    # #TC3 signin
    def test_sign_in(self):
        conduit_registration(self.driver)
        self.driver.find_element_by_xpath('//a[contains(text(),"Sign in")]').click()
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"Email")]').send_keys(mail_1)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"Password")]').send_keys(password)
        self.driver.find_element_by_xpath('//button[contains(@class,"pull-xs")]').click()
        time.sleep(5)

        exit = self.driver.find_element_by_xpath('//a[contains(text(),"Log out")]')
        print(exit.text)
        assert exit.text == " Log out"

    # TC4 creating new blogpost
    def test_new_article(self):
        conduit_registration(self.driver)
        conduit_signin(self.driver)
        time.sleep(2)
        self.driver.find_element_by_xpath('//a[@href="#/editor"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"Article Title")]').send_keys(title)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"about")]').send_keys(about)

        self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"Write your")]').send_keys(write)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"tags")]').send_keys(tag + Keys.ENTER)
        self.driver.find_element_by_xpath('//button[contains(text(),"Publish")]').click()
        self.driver.implicitly_wait(8)
        edit = self.driver.find_element_by_xpath('//span[contains(text(),"Edit")]')
        if edit.is_displayed():
            szoveg_down = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[1]/p')
            assert write == szoveg_down.text
        else:
            False

    # #TC5 modifying blogpost, removing and adding new tag
    #     def test_modify_article(self):
    #         self.test_sign_in()

    #         self.driver.find_element_by_xpath('//*[@class="nav navbar-nav pull-xs-right"]//li[4]/a').click()
    #         time.sleep(5)
    #         sajat_cikk= self.driver.find_elements_by_xpath('//*[@id="app"]//a/h1')
    #         sajat_cikk[0].click()
    #         self.driver.implicitly_wait(4)
    #         edit = self.driver.find_element_by_xpath('//span[contains(text(),"Edit")]')
    #         edit.click()
    #         self.driver.implicitly_wait(2)
    #         self.driver.find_element_by_xpath('//input[contains(@placeholder,"Article Title")]').clear()
    #         self.driver.find_element_by_xpath('//input[contains(@placeholder,"Article Title")]').send_keys(title_mod)

    #         self.driver.find_element_by_xpath('//input[contains(@placeholder,"about")]').clear()
    #         self.driver.find_element_by_xpath('//input[contains(@placeholder,"about")]').send_keys(about_mod)

    #         self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"Write your")]').clear()
    #         self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"Write your")]').send_keys(write_mod)

    #         self.driver.find_element_by_xpath('//*[@class ="ti-icon-close"]').click()
    #         self.driver.find_element_by_xpath('//input[contains(@placeholder,"tags")]').send_keys(tag_mod + Keys.ENTER)
    #         self.driver.implicitly_wait(4)
    #         self.driver.find_element_by_xpath('//button[contains(text(),"Publish")]').click()
    #         time.sleep(4)
    #         if self.driver.find_element_by_xpath('//span[contains(text(),"Edit")]').is_displayed():
    #             szoveg_down2 = self.driver.find_element_by_xpath('//div[@class="col-xs-12"]//div//p')
    #             assert write_mod == szoveg_down2.text
    #         else:
    #             False

    # #TC6 profile modifying
    #     def test_modify_profile(self):
    #         self.test_sign_in()
    #         self.driver.find_element_by_xpath('//a[@href="#/settings"]').click()
    #         self.driver.implicitly_wait(2)
    #         self.driver.find_element_by_xpath('//input[@placeholder="URL of profile picture"]').clear()
    #         self.driver.find_element_by_xpath('//input[@placeholder="URL of profile picture"]').send_keys(pict)

    #         self.driver.find_element_by_xpath('//input[contains(@placeholder,"username")]').clear()
    #         self.driver.find_element_by_xpath('//input[contains(@placeholder,"username")]').send_keys(mod_username)

    #         self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"bio")]').clear()
    #         self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"bio")]').send_keys(bio)

    #         self.driver.find_element_by_xpath('//input[contains(@placeholder,"Email")]').clear()
    #         self.driver.find_element_by_xpath('//input[contains(@placeholder,"Email")]').send_keys(mod_mail)

    #         self.driver.find_element_by_xpath('//input[contains(@placeholder,"Password")]').clear()
    #         self.driver.find_element_by_xpath('//input[contains(@placeholder,"Password")]').send_keys(mod_password)
    #         self.driver.find_element_by_xpath('//button[contains(text(),"Update")]').click()
    #         self.driver.implicitly_wait(2)
    #         self.driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]').click()
    #         self.driver.implicitly_wait(2)

    #         self.driver.find_element_by_xpath('//*[@class="nav navbar-nav pull-xs-right"]//descendant::li[4]/a').click()
    #         self.driver.implicitly_wait(2)
    #         img = self.driver.find_element_by_xpath('//img[@class="user-img"]').get_attribute('src')
    #         motto = self.driver.find_element_by_xpath('//*[@class="user-img"]//following-sibling::p').text
    #         assert motto == bio
    #         assert img == pict
    #         self.driver.find_element_by_xpath('//a[contains(@class ,"btn-outline-secondary")]').click()
    #         time.sleep(5)
    #         #Visszaallitas
    #         self.driver.find_element_by_xpath('//input[@placeholder="URL of profile picture"]').clear()
    #         self.driver.find_element_by_xpath('//input[@placeholder="URL of profile picture"]').send_keys(pict2)
    #         self.driver.find_element_by_xpath('//input[contains(@placeholder,"username")]').clear()
    #         self.driver.find_element_by_xpath('//input[contains(@placeholder,"username")]').send_keys(username)
    #         self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"bio")]').clear()
    #         self.driver.find_element_by_xpath('//input[contains(@placeholder,"Password")]').send_keys(password)
    #         self.driver.find_element_by_xpath('//button[contains(text(),"Update")]').click()
    #         self.driver.implicitly_wait(2)
    #         self.driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]').click()

    # #TC7 deleting articles
    #     def test_delete_article(self):
    #         self.test_sign_in()
    #         self.driver.find_element_by_xpath('//*[@class="nav navbar-nav pull-xs-right"]//descendant::li[4]/a').click()
    #         time.sleep(5)
    #         sajat_cikk = self.driver.find_elements_by_xpath('//*[@id="app"]//a/h1')
    #         torles_elott=len(sajat_cikk)
    #         sajat_cikk[-1].click()
    #         self.driver.implicitly_wait(2)
    #         self.driver.find_element_by_xpath('//button[@class="btn btn-outline-danger btn-sm"]').click()
    #         self.driver.find_element_by_xpath('//*[@class="nav navbar-nav pull-xs-right"]//descendant::li[4]/a').click()
    #         time.sleep(5)
    #         torles_utan = len(self.driver.find_elements_by_xpath('//*[@id="app"]//a/h1'))
    #         assert torles_elott != torles_utan

    # #TC8 Writing blogposts from file
    #     def test_new_article_from_file(self):
    #         self.test_sign_in()
    #         self.driver.find_element_by_xpath('//*[@class="nav navbar-nav pull-xs-right"]//descendant::li[4]/a').click()
    #         time.sleep(5)
    #         sajat_cikk2 = self.driver.find_elements_by_xpath('//*[@id="app"]//a/h1')
    #         cikkek_szama=len(sajat_cikk2)
    #         self.driver.implicitly_wait(4)
    #         with open('article.csv', 'r', encoding="utf-8") as csv_in:  # mit nyitunk meg, milyen változó néveel
    #             csv_reader = csv.reader(csv_in, delimiter=',')  # mi a file és mi az elválasztó
    #             next(csv_reader)
    #             for row in csv_reader:
    #                 sor = [x.strip(' ') for x in row]  # soronként listába tesszük
    #                 print(row)
    #                 self.driver.find_element_by_xpath('//a[@href="#/editor"]').click()
    #                 time.sleep(3)
    #                 self.driver.find_element_by_xpath('//input[contains(@placeholder,"Article Title")]').send_keys(sor[0])
    #                 self.driver.find_element_by_xpath('//input[contains(@placeholder,"about")]').send_keys(sor[1])

    #                 self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"Write your")]').send_keys(sor[2])
    #                 self.driver.find_element_by_xpath('//input[contains(@placeholder,"tags")]').send_keys(sor[3])
    #                 self.driver.find_element_by_xpath('//button[contains(text(),"Publish")]').click()
    #                 time.sleep(3)
    #         self.driver.find_element_by_xpath('//*[@class="nav navbar-nav pull-xs-right"]//descendant::li[4]/a').click()
    #         time.sleep(7)
    #         cikkek_szama_iras_utan=len(self.driver.find_elements_by_xpath('//*[@id="app"]//a/h1'))
    #         assert cikkek_szama_iras_utan ==cikkek_szama + 6

    # #TC9 Saving posts
    #     def test_text_download(self):
    #         self.test_sign_in()
    #         blogger_name = "nulltunder"
    #         time.sleep(2)
    #         self.driver.find_element_by_xpath('//a[@href="#/my-feed"]').click()
    #         time.sleep(3)
    #         self.driver.find_element_by_xpath(f'//a[@href="#/@{blogger_name}/"]').click()
    #         time.sleep(3)
    #         # try:
    #         posztok = self.driver.find_elements_by_xpath('//a/h1')
    #         for i in range(len(posztok)):
    #             time.sleep(2)
    #             posztok = self.driver.find_elements_by_xpath('//a/h1')
    #             posztok[i].click()
    #             time.sleep(2)
    #             cim = self.driver.find_element_by_xpath('//div[@class="container"]/h1').text
    #             tartalom = self.driver.find_element_by_xpath('//div[@class="container"]/h1//following::p').text
    #             sorszam = i + 1
    #             with open('blogposzt.txt', 'a', encoding="utf-8") as f:
    #                 f.write(str(sorszam) + ". " + cim + " " + tartalom + "\n")
    #             time.sleep(2)
    #             self.driver.execute_script("window.history.go(-1)")
    #             time.sleep(2)

    # #TC10 Pagination
    #     def test_pagination(self):
    #         self.test_sign_in()
    #         lapozo_oldalak = self.driver.find_elements_by_xpath('//ul[@class="pagination"]/li/a')
    #         last_number=lapozo_oldalak[-1].text
    #         assert (len(lapozo_oldalak) > 0)
    #         for oldal in lapozo_oldalak:
    #             oldal.click()
    #             time.sleep(3)
    #             continue
    #         assert len(lapozo_oldalak) == int(last_number)

    # T11 list_faved_items

    # T12 logout'
    def test_logout(self):
        conduit_registration(self.driver)
        conduit_signin(self.driver)
        time.sleep(6)
        logout_btn=self.driver.find_element_by_xpath('//a[contains(text(),"Log out")]')
        logout_btn.click()
        time.sleep(2)
        navbar_osszes = self.driver.find_elements_by_xpath('//ul[contains(@class,"navbar-nav")]/li')
        assert navbar_osszes[-1].text == "Sign up"
