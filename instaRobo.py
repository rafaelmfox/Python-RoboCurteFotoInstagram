from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

usuario = "seu usuario"
senha = "sua senha"
hashtag = "conta que deseja dar o curtir"



class InstaBot:
    def __init__(self, usuario,senha):
        self.usuario = usuario
        self.senha = senha
        self.driver = webdriver.Firefox()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        login = driver.find_element_by_xpath("//input[@name='username']")
        login.clear()
        login.send_keys(usuario)
        login = driver.find_element_by_xpath("//input[@name='password']")
        login.clear()
        login.send_keys(senha)
        time.sleep(2)
        login.send_keys(Keys.ENTER)
        time.sleep(3)
        self.curtir_fotos(hashtag)



    def curtir_fotos(self,hashtag):
        time.sleep(5)
        driver = self.driver
        driver.get("https://www.instagram.com/"+hashtag+"/") # aqui pode por como hashtagtbm
        time.sleep(5)
        self.descer_pagina(200, 2) # quanto mais vc descer a pagina mais ele vai carregar as fotos
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' foto: '+ str(len(pic_hrefs)))

        for i in pic_hrefs:
            if "/p/" in i:
                print(str(i))
                driver.get(i)
                try:                                    #aqui pode dar erro no curtir devico que estamos pegando por classe que nao e o recomendado
                    #driver.find_element_by_class_name("//button[@class='wpO6b ']").click()
                    time.sleep(3)
                    driver.find_element_by_xpath("//*[@aria-label='Curtir']").click()
                    time.sleep(30)# tempo de cada curtir OBS: abaixo de 19 segundo o insta pega como bot
                except Exception as e:
                    print(e)
                    time.sleep(10)





    def descer_pagina(self,scrool_pagina,vezes):
        driver = self.driver
        pixel = scrool_pagina

        for i in range(1,vezes):
            print(str(pixel)+" - "+str(scrool_pagina))
            driver.execute_script("window.scrollTo(0,"+str(pixel)+");")
            time.sleep(2)
            pixel += scrool_pagina



meuBot =InstaBot(usuario,senha)
meuBot.login()





