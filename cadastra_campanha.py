# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import time
from datetime import datetime
from faker import Faker 

faker = Faker(pt_BR)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def test_all():
	l = '#'
	p = '#'
	driver = webdriver.Chrome(executable_path='/home/wellington/Documentos/v3/automatiza/chromedriver')
	driver.get('http://0.0.0.0:8081/campaign/create')
	title = driver.title
	print title

	login = driver.find_element_by_id('login')
	login.click()
	login.send_keys(l)
	time.sleep(1)

	password = driver.find_element_by_id('password')
	password.click()
	password.send_keys(p)
	time.sleep(3)

	driver.find_elements_by_tag_name("button")[0].click()

	time.sleep(4)
	selecionar_anunciante = driver.find_element_by_id('anunciantesAgencias') 
	selecionar_anunciante.click()
	time.sleep(2)

	anunciante = driver.find_element_by_xpath('//*[@id="anunciantesAgencias"]/div/div[3]/ul/li[1]/span/span').click()
	time.sleep(1)

	selecionar_gerente = driver.find_element_by_id('gerentesCampanhas') 
	selecionar_gerente.click()
	time.sleep(1)

	gerente = driver.find_element_by_xpath('//*[@id="gerentesCampanhas"]/div/div[3]/ul/li[1]/span/span').click()
	time.sleep(1)

	time.sleep(1)
	campaign = driver.find_element_by_id('campaign')
	campaign.click()
	campaign.send_keys('Campanha Fict')

	time.sleep(1)
	campaign_description = driver.find_element_by_id('description')
	campaign_description.click()
	campaign_description.send_keys('Descript da campanha ficticia')

	protocolo = driver.find_element_by_id('protocolo') 
	protocolo.click()
	time.sleep(1)

	protocolo_select = driver.find_element_by_xpath('//*[@id="protocolo"]/div/div[3]/ul/li[1]/span').click()
	time.sleep(1)

	url = driver.find_element_by_id('url')
	url.click()
	url.send_keys('www.google.com.br')

	categoria = driver.find_element_by_id('categoria') 
	categoria.click()
	time.sleep(1)

	categoria_select = driver.find_element_by_xpath('//*[@id="categoria"]/div/div[3]/ul/li[1]/span').click()

	time.sleep(1)
	current_time = datetime.now()
	current_time2 = current_time.strftime('%m/%d/%Y')
	current_time3 = str(current_time2)
	print(current_time3)
	time.sleep(1)

	periodo = driver.find_element_by_xpath('//*[@id="Etapa1"]/section/div[7]/div[1]/span/div/div/div/input')
	periodo.click
	time.sleep(10)
	periodo.send_keys(current_time2)
	time.sleep(1)

	moeda = driver.find_element_by_id('moeda') 
	moeda.click()
	time.sleep(1)

	moeda_select = driver.find_element_by_xpath('//*[@id="moeda"]/div/div[3]/ul/li[1]/span').click()
	time.sleep(1)

	valor = driver.find_element_by_id('valor')
	valor.click()
	valor.send_keys('10')

	negocia = driver.find_element_by_xpath('//*[@id="Etapa1"]/section/div[9]/div/div/div[1]/a').click()
	time.sleep(1)

	categoria_comissao = driver.find_element_by_id('cpaCategoria1')
	categoria_comissao.click()
	categoria_comissao.send_keys('sale')

	valor_p = driver.find_element_by_xpath('//*[@id="Etapa1"]/section/div[9]/div/div/div[2]/div[2]/span/div/div[2]/input').click()
	time.sleep(1)

	valor_p1 = driver.find_element_by_xpath('//*[@id="Etapa1"]/section/div[9]/div/div/div[2]/div[2]/span/div/div[3]/ul/li[1]/span').click()
	time.sleep(1)

	moeda = driver.find_element_by_xpath('//*[@id="cpaMoeda1"]/div/div[2]/input').click()
	time.sleep(1)

	moeda_selected = driver.find_element_by_xpath('//*[@id="cpaMoeda1"]/div/div[3]/ul/li[1]/span').click()
	time.sleep(1)

	valor_comission = driver.find_element_by_id('cpaValor1')
	valor_comission.click()
	valor_comission.send_keys('10')

	step2 = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div/div[2]/div/div/div/div[3]/div[2]/span/button').click()
	time.sleep(1)



	time.sleep(1)
	driver.find_element_by_id('cnpjFaturamento').send_keys(u'\ue013')
	driver.find_element_by_id('cnpjFaturamento').send_keys(u'\ue013')
	driver.find_element_by_id('cnpjFaturamento').send_keys(u'\ue013')
	driver.find_element_by_id('cnpjFaturamento').send_keys(u'\ue013')
	driver.find_element_by_id('cnpjFaturamento').send_keys(u'\ue013')
	driver.find_element_by_id('cnpjFaturamento').send_keys(u'\ue013')
	driver.find_element_by_id('cnpjFaturamento').send_keys(u'\ue013')
	driver.find_element_by_id('cnpjFaturamento').send_keys(u'\ue013')


	time.sleep(1)
	email1 = driver.find_element_by_id('email1')
	email1.click()
	email1.send_keys('email1@gmail.com')

	time.sleep(1)
	driver.find_elements_by_tag_name("button")[2].click()
	time.sleep(1)

	time.sleep(1)
	email_acesso = driver.find_element_by_id('emailAcesso')
	email_acesso.click()
	email_acesso.send_keys('emailacesso@gmail.com')

	time.sleep(1)
	driver.find_elements_by_tag_name("button")[2].click()
	time.sleep(2)

	s = driver.find_element_by_class_name("success")
	if s:
		print bcolors.OKGREEN + "Cadastro de anunciante concluído"
		time.sleep(8)
		driver.close()
		quit()		
	print bcolors.WARNING + "Cadastro não realizado, popup de sucesso não encontrada" + bcolors.ENDC
	time.sleep(8)
	driver.close()
	quit()
test_all()