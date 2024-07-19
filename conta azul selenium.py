import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
##
# Função para aguardar e clicar em um elemento
def wait_and_click(driver, xpath, wait_time=20):
    element = WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()

# Função para obter as coordenadas de um elemento
def get_coordinates(element):
    location = element.location
    size = element.size
    x = location['x'] + size['width'] / 2
    y = location['y'] + size['height'] / 2
    return x, y

# Função para obter texto usando pyautogui
def get_text_via_pyautogui(element):
    x, y = get_coordinates(element)
    pyautogui.click(x, y)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    return pyperclip.paste()

# Iniciar o WebDriver
driver = webdriver.Chrome()

try:
    # Navegar até a página de login
    driver.get('https://contabilidade.contaazul.com/login/login.html')

    # Preencher os campos de email e senha
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('ti2.controllersbr@gmail.com')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('cvrecife123')

    # Submeter o formulário de login (pressionar Enter)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(Keys.RETURN)

    # Aguardar até que a página do dashboard carregue
    wait = WebDriverWait(driver, 20)
    wait.until(EC.url_to_be('https://contabilidade.contaazul.com/#/dashboard-contador'))

    # Executar os cliques sequenciais na página do dashboard
    dashboard_steps = [
        '/html/body/div[1]/div[1]/div[2]/div[2]/section/div[3]/main/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div[1]/div[1]/div/h1/span',
        '/html/body/div[1]/div[1]/div[2]/div[2]/section/div[3]/main/div/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/table/tbody/tr[2]',
        '/html/body/div[1]/div[1]/div[2]/div[1]/aside/div/div/div/div/ul[2]/li[2]/div[2]/ul/li[2]/a/div/div'
    ]

    for xpath in dashboard_steps:
        wait_and_click(driver, xpath)
        time.sleep(2)  # Pequeno atraso para garantir que a página carregue corretamente

    # Navegar para a URL específica para a segunda parte dos cliques
    driver.get('https://app.contaazul.com/#/ca/visao-geral')

    # Adicionar um tempo de espera maior e um screenshot para verificar se a página está correta
    time.sleep(10)
    driver.save_screenshot('visao_geral_page.png')

    # Executar os cliques sequenciais na nova URL
    ca_visao_geral_steps = [
        '//*[@id="FINANCE"]/div[1]/div',
        '//*[@id="FINANCIAL_STATEMENT_VIEW"]/a/div/div[1]/div',
        '//*[@id="gateway"]/section/div[3]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div/div/div/div[1]/span/button',
        '//*[@id="gateway"]/section/div[3]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div/div/div/div[2]/div[7]',
        '//*[@id="gateway"]/section/div[3]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/ul/li[4]',
        '//*[@id="gateway"]/section/div[3]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div/div[1]/div/button/span[2]/span',
        '//*[@id="gateway"]/section/div[3]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div/div[1]/div/div/div/div/div[4]/button'
    ]

    for xpath in ca_visao_geral_steps:
        wait_and_click(driver, xpath, wait_time=30)
        time.sleep(5)  # Aumentar o atraso para garantir que a página carregue corretamente

    # Navegar para a URL de edição
    driver.get('https://app.contaazul.com/#/ca/financeiro/extrato?rollover=FinancialEventEditRollover')

    # Aguardar até que o tbody esteja presente
    tbody_xpath = '//*[@id="gateway"]/section/div[3]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/table/tbody'
    tbody = wait.until(EC.presence_of_element_located((By.XPATH, tbody_xpath)))

    # Encontrar todos os subelementos do tbody
    subelements = tbody.find_elements(By.TAG_NAME, 'tr')

    for i, subelement in enumerate(subelements, start=1):
        try:
            # Clicar no botão dentro de cada subelemento
            button_xpath = f'//*[@id="gateway"]/section/div[3]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr[{i}]/td[6]/div/div/div/div/div[1]/span/button'
            wait_and_click(driver, button_xpath)

            # Aguardar a nova classe aparecer
            new_button_xpath = f'//*[@id="gateway"]/section/div[3]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr[{i}]/td[6]/div/div/div/div/div[2]/div[2]'
            wait_and_click(driver, new_button_xpath)

            # Aguardar a nova página carregar
            input_xpath = '//*[@id="ng-app"]/body/div[16]/div[2]/div[2]/div/div/div/form/div/div/div[1]/div/div/div/div/fieldset/div[1]/div[3]/div/div/input'
            input_element = wait.until(EC.presence_of_element_located((By.XPATH, input_xpath)))

            # Use pyautogui para obter os textos necessários
            number_xpath = '//*[@id="ng-app"]/body/div[16]/div[2]/div[2]/div/div/div/form/div/div/div[1]/div/div/div/div/fieldset/div[2]/div/div/div[1]/div[4]/div/div/input'
            text1_xpath = '//*[@id="ng-app"]/body/div[16]/div[2]/div[2]/div/div/div/form/div/div/div[1]/div/div/div/div/fieldset/div[1]/div[1]/div/div/div/button'
            text2_xpath = '//*[@id="ng-app"]/body/div[16]/div[2]/div[2]/div/div/div/form/div/div/div[1]/div/div/div/div/fieldset/div[2]/div/div/div[1]/div[2]/div/div/div/button'

            number_element = driver.find_element(By.XPATH, number_xpath)
            text1_element = driver.find_element(By.XPATH, text1_xpath)
            text2_element = driver.find_element(By.XPATH, text2_xpath)

            # Usar pyautogui para copiar os textos
            number = get_text_via_pyautogui(number_element)
            text1 = get_text_via_pyautogui(text1_element)
            text2 = get_text_via_pyautogui(text2_element)

            # Editar o texto
            new_text = f"VL DE Nº {number} A {text1} REF A {text2}"
            input_element.clear()
            input_element.send_keys(new_text)

            # Salvar as alterações
            save_button_xpath = '//*[@id="ng-app"]/body/div[16]/div[2]/div[2]/div/div/div/form/div/div/div[3]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div/span/button'
            wait_and_click(driver, save_button_xpath)
        
        except Exception as e:
            print(f"Erro no elemento {i}: {e}")
            continue

finally:
    # Fechar o WebDriver
    driver.quit()
