from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from allure_commons.types import AttachmentType
import allure
from adat import *


class TestConduit1(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get("http://localhost:1667/#/")

    def teardown(self):
        self.driver.quit()

#01 TC01 HOMEPAGE

    def test_homepage(self):
        time.sleep(2)
        assert self.driver.find_element_by_xpath('//h1[@class="logo-font"]').text == "conduit"

#02 TC02 ACCEPTING COOKIES

    def test_accept_cookies(self):
        self.driver.find_element_by_xpath('//button[contains(@class, "accept")]').click()
        time.sleep(2)
        after_accept = self.driver.get_cookie("vue-cookie-accept-decline-cookie-policy-panel")
        assert after_accept['value'] == 'accept'

# REGISTRATION
#03 without data
#
    def test_bad_signup(self):
        self.test_accept_cookies()

        self.driver.find_element_by_xpath('//a[contains(text(),"Sign up")]').click()
        self.driver.find_element_by_xpath('//button[contains(@class,"pull-xs")]').click()
        time.sleep(2)
        alert_n_subtext = self.driver.find_element_by_xpath('//div[@class="swal-text"]')
        print(alert_n_subtext.text)
        # A felugróablak szövegének ellenőrzése
        reg_fail = "Username field required."
        time.sleep(3)
        assert alert_n_subtext.text == reg_fail
        self.driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]').click()

#04 -TC03
#registration with valid data
    def test_signup(self):
        self.driver.find_element_by_xpath('//a[contains(text(),"Sign up")]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"Username")]').send_keys(username)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"Email")]').send_keys(mail)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"Password")]').send_keys(password)
        self.driver.find_element_by_xpath('//button[contains(@class,"pull-xs")]').click()
        self.driver.implicitly_wait(8)
        alert_text = self.driver.find_element_by_xpath('//div[@class="swal-title"]')
        success = "Welcome!"
        time.sleep(4)
        assert alert_text.text == success
        time.sleep(2)
        self.driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]').click()
        time.sleep(4)
        # Annak ellenőrzése, hogy valóban megfelelő userrel léptünk-e be
        username_value = self.driver.find_element_by_xpath('//li/a[contains(@href, "#/@")]').text
        assert username_value == username

#05 -  SIGNIN

    def test_sign_in(self):
        self.driver.find_element_by_xpath('//a[contains(text(),"Sign in")]').click()
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"Email")]').send_keys(mail)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"Password")]').send_keys(password)

        self.driver.find_element_by_xpath('//button[contains(@class,"pull-xs")]').click()
        time.sleep(3)
        # A "Log out" link meglétének ellenőrzése
        exit = self.driver.find_element_by_xpath('//a[contains(text(),"Log out")]')
        assert exit.text == " Log out"
        # Annak ellenőrzése, hogy valóban megfelelő userrel léptünk-e be
        username_value = self.driver.find_element_by_xpath('//li/a[contains(@href, "#/@")]').text
        assert username_value == username

#06 - CREATING NEW ARTICLE

    def test_new_article(self):
        conduit_signin(self.driver)
        time.sleep(2)
        self.driver.find_element_by_xpath('//a[@href="#/editor"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"Article Title")]').send_keys(title)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"about")]').send_keys(about)

        self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"Write your")]').send_keys(write)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"tags")]').send_keys(tag + Keys.ENTER)
        self.driver.find_element_by_xpath('//button[contains(text(),"Publish")]').click()
        time.sleep(3)
        #A módosítás gomb jelenlétének ellenőrzése
        edit = self.driver.find_element_by_xpath('//span[contains(text(),"Edit")]')
        if edit.is_displayed():
            szoveg_down = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[1]/p')
            assert write == szoveg_down.text
        else:
            False

#07 - MODIFYING ARTICLE

    def test_modify_article(self):
        conduit_signin(self.driver)
        time.sleep(3)
        self.driver.find_element_by_xpath('//li/a[contains(@href, "#/@")]').click()
        time.sleep(2)
        sajat_cikk = self.driver.find_elements_by_xpath('//*[@id="app"]//a/h1')
        sajat_cikk[0].click()
        time.sleep(3)
        #módosítás megnyitása
        edit = self.driver.find_element_by_xpath('//span[contains(text(),"Edit")]')
        edit.click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"Article Title")]').clear()
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"Article Title")]').send_keys(title_mod)

        self.driver.find_element_by_xpath('//input[contains(@placeholder,"about")]').clear()
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"about")]').send_keys(about_mod)

        self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"Write your")]').clear()
        self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"Write your")]').send_keys(write_mod)

        self.driver.find_element_by_xpath('//*[@class ="ti-icon-close"]').click()
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"tags")]').send_keys(tag_mod)
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_xpath('//button[contains(text(),"Publish")]').click()
        time.sleep(4)
        #módosított szöveg ellenőrzése
        if self.driver.find_element_by_xpath('//span[contains(text(),"Edit")]').is_displayed():
            szoveg_down2 = self.driver.find_element_by_xpath('//div[@class="col-xs-12"]//div//p')
            assert write_mod == szoveg_down2.text
        else:
            False

#08  IMPORT DATA FROM FILE

    def test_new_article_from_file(self):
        conduit_signin(self.driver)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@class="nav navbar-nav pull-xs-right"]//li[4]/a').click()
        time.sleep(3)
        sajat_cikk2 = self.driver.find_elements_by_xpath('//*[@id="app"]//a/h1')
        cikkek_szama = len(sajat_cikk2)
        time.sleep(2)
        with open('article.csv', 'r', encoding="utf-8") as csv_in:
            csv_reader = csv.reader(csv_in, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                sor = [x.strip(' ') for x in row]
                self.driver.find_element_by_xpath('//a[@href="#/editor"]').click()
                time.sleep(3)
                self.driver.find_element_by_xpath('//input[contains(@placeholder,"Article Title")]').send_keys(sor[0])
                self.driver.find_element_by_xpath('//input[contains(@placeholder,"about")]').send_keys(sor[1])

                self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"Write your")]').send_keys(sor[2])
                self.driver.find_element_by_xpath('//input[contains(@placeholder,"tags")]').send_keys(sor[3])
                self.driver.find_element_by_xpath('//button[contains(text(),"Publish")]').click()
                time.sleep(3)
        time.sleep(5)
        self.driver.find_element_by_xpath('//nav/div/ul/li/a[starts-with(@href, "#/@")]').click()
        time.sleep(4)
        #ellenőrizzük, hogy mind a hat blogposzt megjelent-e
        cikkek_szama_iras_utan = len(self.driver.find_elements_by_xpath('//*[@id="app"]//a/h1'))
        assert cikkek_szama_iras_utan == cikkek_szama + 6

#09 - MODIFYING PROFILE

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
        # módosított profiladatok ellenőrzése
        self.driver.find_element_by_xpath('//li/a[contains(@href, "#/@")]').click()
        time.sleep(2)
        img = self.driver.find_element_by_xpath('//img[@class="user-img"]').get_attribute('src')
        motto = self.driver.find_element_by_xpath('//*[@class="user-img"]//following-sibling::p').text
        assert motto == bio
        assert img == pict
        self.driver.find_element_by_xpath('//a[contains(@class ,"btn-outline-secondary")]').click()
        time.sleep(3)
        # Visszaallitas
        self.driver.find_element_by_xpath('//input[@placeholder="URL of profile picture"]').clear()
        self.driver.find_element_by_xpath('//input[@placeholder="URL of profile picture"]').send_keys(pict2)
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"username")]').clear()
        self.driver.find_element_by_xpath('//input[contains(@placeholder,"username")]').send_keys(username)
        self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"bio")]').clear()
        self.driver.find_element_by_xpath('//button[contains(text(),"Update")]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]').click()

#10 - DELETING ARTICLES

    def test_delete_article(self):
        conduit_signin(self.driver)
        time.sleep(1)
        conduit_new_article(self.driver)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@class="nav navbar-nav pull-xs-right"]//li[4]/a').click()
        time.sleep(3)
        sajat_cikk = self.driver.find_elements_by_xpath('//*[@id="app"]//a/h1')
        torles_elott = len(sajat_cikk)
        #a listában utolsó saját cikk törlése
        sajat_cikk[-1].click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('//button[@class="btn btn-outline-danger btn-sm"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@class="nav navbar-nav pull-xs-right"]//li[4]/a').click()
        time.sleep(3)
        torles_utan = len(self.driver.find_elements_by_xpath('//*[@id="app"]//a/h1'))
        assert torles_elott != torles_utan

#11 - SAVING DATA

    def test_sampletext_download(self):
        conduit_signin(self.driver)
        blogger_name = "testuser1"
        time.sleep(6)
        my_feed = self.driver.find_element_by_xpath('//a[contains(text(),"Your Feed")]')
        my_feed.click()
        time.sleep(2)
        self.driver.find_element_by_xpath(f'//a[@href="#/@{blogger_name}/"]').click()
        time.sleep(3)
        # a user posztjainak fileba írása
        posztok = self.driver.find_elements_by_xpath('//a/h1')
        for i in range(len(posztok)):
            time.sleep(1)
            post_title = self.driver.find_elements_by_xpath('//a/h1')[i].text
            post_about = self.driver.find_elements_by_xpath('//a/p')[i].text
            with open('blogposzt2.txt', 'a', encoding='UTF-8') as to_file:
                to_file.writelines(f'{post_title} \n{post_about} \n')
            time.sleep(1)
        # file tartalmának ellenőrzése (az about text egyezésének ellenőrzésével)
        with open('blogposzt2.txt', 'r', encoding='UTF-8') as from_file:
            content_list = from_file.readlines()
            titles_abouts = [line.rstrip(' \n') for line in content_list]

        time.sleep(1)
        self.driver.find_element_by_xpath(f'//a[@href="#/@{blogger_name}/"]').click()
        time.sleep(1)
        assert titles_abouts[1] == self.driver.find_elements_by_xpath('//a/p')[0].text
        assert titles_abouts[3] == self.driver.find_elements_by_xpath('//a/p')[1].text
        time.sleep(2)
        # testfile tartalmának törlése
        open("blogposzt2.txt", "w").close()

#12 PAGINATION

    def test_pagination(self):
        conduit_signin(self.driver)
        time.sleep(2)
        lapozo_oldalak = self.driver.find_elements_by_xpath('//ul[@class="pagination"]/li/a')
        last_number = lapozo_oldalak[-1].text
        # A lapozóoldalak számának ellenőrzése, amennyiben az nagyobb, mint 0
        assert (len(lapozo_oldalak) > 0)
        for oldal in lapozo_oldalak:
            oldal.click()
            time.sleep(3)
            continue
        assert len(lapozo_oldalak) == int(last_number)

#13 LIST FAVOURITED POSTS

    def test_list_faved_posts(self):
        global failed_ones
        conduit_signin(self.driver)
        time.sleep(4)
        fav_buttons = self.driver.find_elements_by_xpath('//div[@class="article-preview"]//button/i')
        counter = 0
        faved = 0
        # az első 10 blogposzt likeolása ellenőrzéssel
        for fav in fav_buttons[0:10]:
            fav.click()
            time.sleep(1)
            number_of_likes = self.driver.find_elements_by_xpath('//div[@class="article-preview"]//button/span')[
                counter]
            if int(number_of_likes.text) > 0:
                faved += 1
            else:
                # ha a klikkelés ellenére a likeok száma nulla marad az adott blogpsztnál:
                allure.attach(self.driver.get_screenshot_as_png(), name="Passwordfailure",attachment_type=AttachmentType.PNG)
                failed_ones = []
                failed_ones.append(counter)
                for i in failed_ones:
                    failed_title = self.driver.find_elements_by_xpath('//a/h1')[i].text
                    print(
                        f'Failure: an error occured during the like process of Article{i + 1}, which is called {failed_title}')
            counter += 1
        time.sleep(6)
        # a kedvencnek jelölt blogposztok számának ellenőrzése a Kedvencek aloldalon
        self.driver.find_element_by_xpath('//nav/div/ul/li/a[starts-with(@href, "#/@")]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//a[contains(text(), "Favorited")]').click()
        time.sleep(3)
        faved_links = self.driver.find_elements_by_xpath('//a/h1')
        # ellenőrizzük, hogy minden olyan bejegyzés, amelynél növekedett a likeok száma megjelent-e a Favorites aloldalon
        assert len(faved_links) == faved
        # ellenőrizzük, hogy nincs olyan bejegyzés, ahol nullán maradt a like számláló
        assert len(failed_ones) == 0, f"Test Failed: An error occured during liking {len(failed_ones)} article."

#14 LOGOUT

    def test_logout(self):
        conduit_signin(self.driver)
        time.sleep(3)
        logout_btn = self.driver.find_element_by_xpath('//a[contains(text(),"Log out")]')
        logout_btn.click()
        time.sleep(2)
        # A kilépés megtörténtének ellenőrzése
        navbar_all = self.driver.find_elements_by_xpath('//ul[contains(@class,"navbar-nav")]/li')
        assert navbar_all[-1].text == "Sign up"
