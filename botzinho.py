from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from danger import Pw
from danger import User


class IGbot:
    def __init__(self):
        self.driver = webdriver.Chrome()
       

    def login(self):
        driver = self.driver 
        url = 'https://instagram.com/'
        driver.get(url)
        time.sleep(5)

        #Usuario
        nome_usuario = driver.find_element_by_name('username')
        nome_usuario.click()

        time.sleep(1)

        nome_usuario.send_keys(User)

        #Senha
        senha_usuario = driver.find_element_by_name('password')
        senha_usuario.click()

        senha_usuario.send_keys(Pw)

        time.sleep(3)

        #Entrar
        senha_usuario.send_keys(Keys.ENTER)

        time.sleep(6)

    def ver_nao_seguidores(self):
        driver = self.driver
        #Ativar ou Não suas Informações de Login
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()

        #Acessando perfil
        url = 'https://www.instagram.com/gfsillva/'
        driver.get(url)
        time.sleep(3)

        #Estou seguindo
        seguindo = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        seguindo.click()
        
        estou_seguindo = self.listar_ig()

        time.sleep(5)

        #Meus Seguidores
        seguidores = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        seguidores.click()
        
        esta_me_seguindo = self.listar_ig()

        #Quem não me segue de volta

        quem_nao_me_segue = [ig for ig in estou_seguindo if ig not in esta_me_seguindo]

        print(quem_nao_me_segue)

        arquivo_txt = open('nao_me_segue.txt', 'w+')
        arquivo_txt.write(str(quem_nao_me_segue))
        


    def listar_ig(self):
        driver = self.driver

        time.sleep(5)

        popUp = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[3]')

        ult_tamanho, tamanho = 0, 1

        while ult_tamanho != tamanho:
            ult_tamanho = tamanho

            time.sleep(5)
            tamanho = driver.execute_script('''
                                        arguments[0].scrollTo(0, arguments[0].scrollHeight);
                                        return arguments[0].scrollHeight;
                                        ''', popUp)

        links = popUp.find_elements_by_tag_name('a')
        nomes = [nomes.text for nomes in links if nomes.text != '']

        time.sleep(3)

        botao_fechar = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/button')
        botao_fechar.click()

        return(nomes)

tarefa = IGbot()
tarefa.login()    
tarefa.ver_nao_seguidores()    
tarefa.listar_ig()