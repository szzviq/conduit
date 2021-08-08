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

    # TC1 ACCEPTING COOKIES
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


    #TC2 REGISTRATION
    def test_signup(self):
        self.driver.find_element_by_xpath('//a[contains(text(),"Sign up")]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"Username")]').send_keys(username)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"Email")]').send_keys(mail_1)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"Password")]').send_keys(password)
        self.driver.find_element_by_xpath('//button[contains(@class,"pull-xs")]').click()
        self.driver.implicitly_wait(8)
        alert_text = self.driver.find_element_by_xpath('//div[@class="swal-title"]')
        print(alert_text)
        success = "Welcome!"
        time.sleep(4)
        assert alert_text.text == success
        time.sleep(2)
        self.driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]').click()
        time.sleep(4)
        # Annak ellenőrzése, hogy valóban megfelelő userrel léptünk-e be
        username_value = self.driver.find_element_by_xpath('//li/a[contains(@href, "#/@")]').text
        assert username_value == username


    #TC3 SIGNIN
    def test_sign_in(self):
        self.driver.find_element_by_xpath('//a[contains(text(),"Sign in")]').click()
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"Email")]').send_keys(mail_1)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"Password")]').send_keys(password)

        self.driver.find_element_by_xpath('//button[contains(@class,"pull-xs")]').click()
        time.sleep(3)
        # A Log out link meglétének ellenőrzése
        exit = self.driver.find_element_by_xpath('//a[contains(text(),"Log out")]')
        assert exit.text == " Log out"
        #Annak ellenőrzése, hogy valóban megfelelő userrel léptünk-e be
        username_value = self.driver.find_element_by_xpath('//li/a[contains(@href, "#/@")]').text
        assert username_value == username

    #TC4 CREATING NEW ARTICLE
    def test_new_article(self):
        # conduit_registration(self.driver)
        conduit_signin(self.driver)
        time.sleep(2)
        self.driver.find_element_by_xpath('//a[@href="#/editor"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"Article Title")]').send_keys(title)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"about")]').send_keys(about)

        self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"Write your")]').send_keys(write)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"tags")]').send_keys(tag + Keys.ENTER)
        self.driver.find_element_by_xpath('//button[contains(text(),"Publish")]').click()
        self.driver.implicitly_wait(6)
        edit = self.driver.find_element_by_xpath('//span[contains(text(),"Edit")]')
        if edit.is_displayed():
            szoveg_down = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[1]/p')
            assert write == szoveg_down.text
        else:
            False

#TC5 modifying blogpost, removing and adding new tag
    def test_modify_article(self):
        conduit_signin(self.driver)
        time.sleep(2)
        self.driver.find_element_by_xpath('//li/a[contains(@href, "#/@")]').click()
        time.sleep(2)
        sajat_cikk= self.driver.find_elements_by_xpath('//*[@id="app"]//a/h1')
        sajat_cikk[0].click()
        self.driver.implicitly_wait(4)
        edit = self.driver.find_element_by_xpath('//span[contains(text(),"Edit")]')
        edit.click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"Article Title")]').clear()
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"Article Title")]').send_keys(title_mod)

        self.driver.find_element_by_xpath('//input[contains(@placeholder,"about")]').clear()
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"about")]').send_keys(about_mod)

        self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"Write your")]').clear()
        self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"Write your")]').send_keys(write_mod)

        self.driver.find_element_by_xpath('//*[@class ="ti-icon-close"]').click()
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"tags")]').send_keys(tag_mod + Keys.ENTER)
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_xpath('//button[contains(text(),"Publish")]').click()
        time.sleep(4)
        if self.driver.find_element_by_xpath('//span[contains(text(),"Edit")]').is_displayed():
            szoveg_down2 = self.driver.find_element_by_xpath('//div[@class="col-xs-12"]//div//p')
            assert write_mod == szoveg_down2.text
        else:
            False

    # #TC5 IMPORT DATA FROM FILE
    def test_new_article_from_file(self):
        conduit_signin(self.driver)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@class="nav navbar-nav pull-xs-right"]//li[4]/a').click()
        time.sleep(3)
        sajat_cikk2 = self.driver.find_elements_by_xpath('//*[@id="app"]//a/h1')
        cikkek_szama = len(sajat_cikk2)
        self.driver.implicitly_wait(4)
        with open('article.csv', 'r', encoding="utf-8") as csv_in:
            csv_reader = csv.reader(csv_in, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                sor = [x.strip(' ') for x in row]
                print(row)
                self.driver.find_element_by_xpath('//a[@href="#/editor"]').click()
                time.sleep(3)
                self.driver.find_element_by_xpath('//input[contains(@placeholder,"Article Title")]').send_keys(sor[0])
                self.driver.find_element_by_xpath('//input[contains(@placeholder,"about")]').send_keys(sor[1])

                self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"Write your")]').send_keys(sor[2])
                self.driver.find_element_by_xpath('//input[contains(@placeholder,"tags")]').send_keys(sor[3])
                self.driver.find_element_by_xpath('//button[contains(text(),"Publish")]').click()
                time.sleep(3)
        self.driver.find_element_by_xpath('//li/a[contains(@href, "#/@")]').click()
        time.sleep(6)
        cikkek_szama_iras_utan = len(self.driver.find_elements_by_xpath('//*[@id="app"]//a/h1'))
        assert cikkek_szama_iras_utan == cikkek_szama + 6

    #TC6 MODIFYING PROFILE
    def test_modify_profile(self):
        conduit_signin(self.driver)
        time.sleep(2)
        self.driver.find_element_by_xpath('//a[@href="#/settings"]').click()
        self.driver.implicitly_wait(2)
        # kép módosítása
        self.driver.find_element_by_xpath('//input[@placeholder="URL of profile picture"]').clear()
        self.driver.find_element_by_xpath('//input[@placeholder="URL of profile picture"]').send_keys(pict)
        # username módosítása
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"username")]').clear()
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"username")]').send_keys(mod_username)
        # bio módosítása
        self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"bio")]').clear()
        self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"bio")]').send_keys(bio)
        self.driver.find_element_by_xpath('//button[contains(text(),"Update")]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]').click()
        time.sleep(4)

        self.driver.find_element_by_xpath('//li/a[contains(@href, "#/@")]').click()
        self.driver.implicitly_wait(2)
        img = self.driver.find_element_by_xpath('//img[@class="user-img"]').get_attribute('src')
        motto = self.driver.find_element_by_xpath('//*[@class="user-img"]//following-sibling::p').text
        assert motto == bio
        assert img == pict
        self.driver.find_element_by_xpath('//a[contains(@class ,"btn-outline-secondary")]').click()
        time.sleep(5)
        # Visszaallitas
        # self.driver.find_element_by_xpath('//input[@placeholder="URL of profile picture"]').clear()
        # self.driver.find_element_by_xpath('//input[@placeholder="URL of profile picture"]').send_keys(pict2)
        # self.driver.find_element_by_xpath('//input[contains(@placeholder,"username")]').clear()
        # self.driver.find_element_by_xpath('//input[contains(@placeholder,"username")]').send_keys(username)
        # self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"bio")]').clear()
        # self.driver.find_element_by_xpath('//button[contains(text(),"Update")]').click()
        # self.driver.implicitly_wait(2)
        # self.driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]').click()

    #TC7 DELETING ARTICLES
    def test_delete_article(self):
        conduit_signin(self.driver)
        time.sleep(1)
        conduit_new_article(self.driver)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@class="nav navbar-nav pull-xs-right"]//li[4]/a').click()
        time.sleep(3)
        sajat_cikk = self.driver.find_elements_by_xpath('//*[@id="app"]//a/h1')
        torles_elott = len(sajat_cikk)
        sajat_cikk[-1].click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('//button[@class="btn btn-outline-danger btn-sm"]').click()
        self.driver.find_element_by_xpath('//*[@class="nav navbar-nav pull-xs-right"]//li[4]/a').click()
        time.sleep(3)
        torles_utan = len(self.driver.find_elements_by_xpath('//*[@id="app"]//a/h1'))
        assert torles_elott != torles_utan

    #TC9 SAVING DATA

    def test_sampletext_download(self):
        conduit_signin(self.driver)
        blogger_name = "testuser1"
        time.sleep(4)
        my_feed = self.driver.find_element_by_xpath('//a[contains(text(),"Your Feed")]')
        my_feed.click()
        time.sleep(2)
        self.driver.find_element_by_xpath(f'//a[@href="#/@{blogger_name}/"]').click()
        time.sleep(3)
        #a user posztjainak fileba írása
        posztok = self.driver.find_elements_by_xpath('//a/h1')
        print(self.driver.find_elements_by_xpath('//a/p')[0].text)
        for i in range(len(posztok)):
            time.sleep(1)
            post_title = self.driver.find_elements_by_xpath('//a/h1')[i].text
            post_about = self.driver.find_elements_by_xpath('//a/p')[i].text
            with open('blogposzt2.txt', 'a', encoding='UTF-8') as to_file:
                to_file.write(f'{post_title};{post_about}; \n')
                time.sleep(2)
        # file tartalmának ellenőrzése (az about text egyezésének ellenőrzésével)
        with open('blogposzt2.txt', 'r', encoding='UTF-8') as from_file:
            first_line = from_file.readline()
            text_list = first_line.split(";")

        self.driver.find_element_by_xpath(f'//a[@href="#/@{blogger_name}/"]').click()
        time.sleep(1)
        post_about_1 = self.driver.find_elements_by_xpath('//a/p')[0].text
        time.sleep(3)
        assert post_about_1 == text_list[1]
        time.sleep(2)
        #testfile törlése
        open("blogposzt2.txt", "w").close()


#TC10 PAGINATION

    def test_pagination(self):
        conduit_signin(self.driver)
        time.sleep(2)
        lapozo_oldalak = self.driver.find_elements_by_xpath('//ul[@class="pagination"]/li/a')
        last_number=lapozo_oldalak[-1].text
        assert (len(lapozo_oldalak) > 0)
        for oldal in lapozo_oldalak:
            oldal.click()
            time.sleep(3)
            continue
        assert len(lapozo_oldalak) == int(last_number)

# T11 LIST FAVOURITED POSTS
    def test_list_faved_posts(self):
        time.sleep(4)
        fav_buttons = self.driver.find_elements_by_xpath('//div[@class="article-preview"]//button/i')
        for fav in fav_buttons[0:3]:
            fav.click()
            time.sleep(1)
        time.sleep(1)
        self.driver.find_element_by_xpath('//li/a[contains(@href, "#/@")]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//a[contains(text(), "Favorited")]').click()
        time.sleep(3)
        faved_links = self.driver.find_elements_by_xpath('//a/h1')
        assert len(faved_links) == 3


#TC12 LOGOUT
    def test_logout(self):
        conduit_signin(self.driver)
        time.sleep(3)
        logout_btn = self.driver.find_element_by_xpath('//a[contains(text(),"Log out")]')
        logout_btn.click()
        time.sleep(2)
        navbar_all = self.driver.find_elements_by_xpath('//ul[contains(@class,"navbar-nav")]/li')
        assert navbar_all[-1].text == "Sign up"