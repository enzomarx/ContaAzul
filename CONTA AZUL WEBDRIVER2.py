import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Func para aguardar e clicar em um elemento
def wait_and_click(driver, xpath, wait_time=20):
    element = WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()

driver = webdriver.Chrome()

try:
    driver.get('https://contabilidade.contaazul.com/login/login.html')

    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('ti2.controllersbr@gmail.com')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('cvrecife123')

    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(Keys.RETURN)

    wait = WebDriverWait(driver, 20)
    wait.until(EC.url_to_be('https://contabilidade.contaazul.com/#/dashboard-contador'))

    # Exe os cliques sequenciais na página do dashboard
    dashboard_steps = [
        '/html/body/div[1]/div[1]/div[2]/div[2]/section/div[3]/main/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div[1]/div[1]/div/h1/span',
        '/html/body/div[1]/div[1]/div[2]/div[2]/section/div[3]/main/div/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/table/tbody/tr[2]',
        '/html/body/div[1]/div[1]/div[2]/div[1]/aside/div/div/div/div/ul[2]/li[2]/div[2]/ul/li[2]/a/div/div'
    ]

    for xpath in dashboard_steps:
        wait_and_click(driver, xpath)
        time.sleep(2)  

    driver.get('https://app.contaazul.com/#/ca/visao-geral')

    time.sleep(10)
    driver.save_screenshot('visao_geral_page.png')

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
        time.sleep(5)  


    #driver.get('https://app.contaazul.com/#/ca/financeiro/extrato')

    #tbody_xpath = '//*[@id="gateway"]/section/div[3]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/table/tbody'
    #tbody = wait.until(EC.presence_of_element_located((By.XPATH, tbody_xpath)))
    # primeiro elemento da tabela
    first_row_xpath = '//*[@id="gateway"]/section/div[3]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr[1]'
    wait_and_click(driver, first_row_xpath)

    edit_button_xpath = '//*[@id="ng-app"]/body/div[16]/div[2]/div[2]/div/form/div/div/div[2]/div/div/fieldset/div[2]/div[3]/div/span/span/svg/path'
    wait_and_click(driver, edit_button_xpath)


    
except Exception as e:
    print(f"Erro: {e}")

finally:
    driver.quit()
