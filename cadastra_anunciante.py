# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import time
from datetime import datetime
from faker import Faker #Biblioteca de dados falsos

faker = Faker()

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
	l = 'admin@afil.io'
	p = 'P@ssw0rd!'
	driver = webdriver.Chrome(executable_path='/home/wellington/Documentos/v3/automatiza/chromedriver')
	
	driver.get('http://homolog.dashboard.afi.vc/advertiser/create')
	time.sleep(5)
	title = driver.title
	print title

	login = driver.find_element_by_id('login')
	login.click()
	login.send_keys(l)

	password = driver.find_element_by_id('password')
	password.click()
	password.send_keys(p)

	driver.find_elements_by_tag_name("button")[0].click()

	time.sleep(3)
	checkbox_anunciantes = driver.find_element_by_id('anunciante').click()

	nome_fantasia = driver.find_element_by_id('nomeFantasia')
	nome_fantasia.click()
	nome_fantasia.send_keys(faker.company())

	time.sleep(1)
	razao_social = driver.find_element_by_id('razaoSocial')
	razao_social.click()
	razao_social.send_keys(faker.company())

	time.sleep(1)
	cnpj = driver.find_element_by_id('cnpj')
	cnpj.click()
	cnpj.send_keys(faker.msisdn())

	time.sleep(1)
	codigo_postal = driver.find_element_by_id('codigoPostal')
	codigo_postal.click()
	codigo_postal.send_keys(faker.msisdn())

	time.sleep(1)
	endereco = driver.find_element_by_id('endereco')
	endereco.click()
	endereco.send_keys(faker.address())
	
	time.sleep(1)
	numero = driver.find_element_by_id('numero')
	numero.click()
	numero.send_keys('172')
	
	time.sleep(1)
	complemento = driver.find_element_by_id('complemento')
	complemento.click()
	complemento.send_keys('110')

	time.sleep(1)
	pais = driver.find_element_by_id('pais')
	pais.click()
	pais.send_keys(faker.country())

	time.sleep(1)
	estado = driver.find_element_by_id('estado')
	estado.click()
	estado.send_keys(faker.state())

	time.sleep(1)
	cidade = driver.find_element_by_id('cidade')
	cidade.click()
	cidade.send_keys(faker.city())

	time.sleep(1)
	driver.find_elements_by_tag_name("button")[1].click()
	time.sleep(1)

	time.sleep(1)
	cidade = driver.find_element_by_id('nomeComercial')
	cidade.click()
	cidade.send_keys(faker.first_name())

	time.sleep(2)
	email_comercial = driver.find_element_by_id('emailComercial')
	email_comercial.click()
	email_comercial.send_keys(faker.ascii_free_email())

	time.sleep(1)
	telefone_comercial = driver.find_element_by_id('telefoneComercial')
	telefone_comercial.click()
	telefone_comercial.send_keys(faker.msisdn())

	time.sleep(1)
	driver.find_elements_by_tag_name("button")[2].click()
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
	cnpj_faturamento = driver.find_element_by_id('cnpjFaturamento')
	cnpj_faturamento.click()
	cnpj_faturamento.send_keys(faker.msisdn())

	time.sleep(1)
	razaoSocial_faturamento = driver.find_element_by_id('razaoSocialFaturamento')
	razaoSocial_faturamento.click()
	razaoSocial_faturamento.send_keys(faker.first_name())

	time.sleep(1)
	inscricaoEstadual_faturamento = driver.find_element_by_id('inscricaoEstadualFaturamento')
	inscricaoEstadual_faturamento.click()
	inscricaoEstadual_faturamento.send_keys(faker.msisdn())

	time.sleep(1)
	inscricaoMunicipal_faturamento = driver.find_element_by_id('inscricaoMunicipalFaturamento')
	inscricaoMunicipal_faturamento.click()
	inscricaoMunicipal_faturamento.send_keys(faker.msisdn())

	time.sleep(1)
	cep_faturamento = driver.find_element_by_id('cepFaturamento')
	cep_faturamento.click()
	cep_faturamento.send_keys(faker.msisdn())

	time.sleep(1)
	endereco_faturamento = driver.find_element_by_id('enderecoFaturamento')
	endereco_faturamento.click()
	endereco_faturamento.send_keys(faker.address())

	time.sleep(1)
	cidade_faturamento = driver.find_element_by_id('cidadeFaturamento')
	cidade_faturamento.click()
	cidade_faturamento.send_keys(faker.city())

	time.sleep(1)
	estado_faturamento = driver.find_element_by_id('estadoFaturamento')
	estado_faturamento.click()
	estado_faturamento.send_keys(faker.state())

	time.sleep(1)
	ddd_faturamento = driver.find_element_by_id('dddFaturamento')
	ddd_faturamento.click()
	ddd_faturamento.send_keys('21')

	time.sleep(1)
	telefone_faturamento = driver.find_element_by_id('TelefoneFaturamento')
	telefone_faturamento.click()
	telefone_faturamento.send_keys(faker.msisdn())

	time.sleep(1)
	prazo_faturamento = driver.find_element_by_id('prazoFaturamento')
	prazo_faturamento.click()
	prazo_faturamento.send_keys('20')

	time.sleep(1)
	email1 = driver.find_element_by_id('email1')
	email1.click()
	email1.send_keys(faker.ascii_free_email())

	time.sleep(1)
	driver.find_elements_by_tag_name("button")[2].click()
	time.sleep(1)

	time.sleep(1)
	email_acesso = driver.find_element_by_id('emailAcesso')
	email_acesso.click()
	email_acesso.send_keys(faker.ascii_free_email())

	time.sleep(1)
	driver.find_elements_by_tag_name("button")[2].click()
	time.sleep(3)

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