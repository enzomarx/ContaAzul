import pyautogui
import time

# Função de espera padrão
def espera(segundos=2):
    time.sleep(segundos)

# Abrir navegador Edge com o link especificado
pyautogui.hotkey('win', 'r')
espera()
pyautogui.write('msedge https://mais.contaazul.com/#/dashboard-do-cliente/pro/')
pyautogui.press('enter')
espera(8)
pyautogui.click(591,317)
espera(3)

# Navegando para o menu de clientes
pyautogui.click(220,240)
espera(1)
pyautogui.click(206,244)
espera(3)

# Busca pelo cliente
pyautogui.click(533,546)
espera(1)
pyautogui.write('Medicalmais')
pyautogui.press('enter')
espera(3)

# Selecionar cliente e CA PRO
pyautogui.click(545,822)
espera(3)
pyautogui.click(200,367)
espera(3)
pyautogui.click(591,317)
espera(3)
pyautogui.click(1521,577)
espera(3)
pyautogui.click(1319,320)
espera(3)
pyautogui.click(1521,577)
espera(5)

# Navegar financeiro > visão de competência
pyautogui.click(197,550)
espera(2)
pyautogui.click(240,453)
espera(2)

# Seleção de período 'este ano'
pyautogui.click(671,372)
espera(1)
pyautogui.click(579,550)
espera(2)

# Ordenar por data (clicar duas vezes)
pyautogui.click(611,623)
espera(1)
pyautogui.click(608,620)
espera(2)

# Scroll para garantir visibilidade
pyautogui.scroll(-350)
espera(2)

# Automação principal (loop entre páginas)
for pagina in range(15):
    botoes = list(pyautogui.locateAllOnScreen(r'C:\Users\ema\Downloads\img1.png', confidence=0.8))

    if not botoes:
        # Posição inicial de busca caso nenhuma imagem tenha sido encontrada
        x_inicial, y_inicial = 600, 300  # ajuste conforme necessário
        pyautogui.moveTo(x_inicial, y_inicial)

        for tentativa in range(5):
            # Move para a direita, mantendo o mesmo Y
            x_atual, y_atual = pyautogui.position()
            pyautogui.moveTo(x_atual + 100, y_atual, duration=0.5)
            espera(1)
            botao_retry = pyautogui.locateOnScreen(r'C:\Users\ema\Downloads\img1.png', confidence=0.8)

            if botao_retry:
                botoes.append(botao_retry)
                break

    if not botoes:
        # Próxima página caso realmente não encontre o botão
        pyautogui.click(1856,252)
        espera(5)
        continue

    for botao in botoes:
        pyautogui.click(pyautogui.center(botao))
        espera(2)

        botao2 = pyautogui.locateOnScreen(r'C:\Users\ema\Downloads\img2.png', confidence=0.8)
        if botao2:
            pyautogui.click(pyautogui.center(botao2))
            espera(2)

            pyautogui.click(1523,333)
            espera()
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')
            pyautogui.write('PAGAMENTO')
            espera()

            pyautogui.moveTo(523,334)
            pyautogui.dragTo(640,337, duration=0.5)
            pyautogui.hotkey('ctrl','c')

            pyautogui.click(1523,333)
            pyautogui.press('space')
            pyautogui.hotkey('ctrl','v')

            pyautogui.moveTo(191,465)
            pyautogui.dragTo(564,494, duration=0.5)
            pyautogui.hotkey('ctrl','c')

            pyautogui.click(1523,333)
            pyautogui.press('space')
            pyautogui.write('REF A')
            pyautogui.press('space')
            pyautogui.hotkey('ctrl','v')

            pyautogui.moveTo(56,341)
            pyautogui.dragTo(434,358, duration=0.5)
            pyautogui.hotkey('ctrl','c')

            pyautogui.click(1523,333)
            pyautogui.press('space')
            pyautogui.write('A')
            pyautogui.press('space')
            pyautogui.hotkey('ctrl','v')
            espera(2)
            pyautogui.click(1742,974)
            espera(1)

    # Próxima página
    pyautogui.click(1856,252)
    espera(5)

print("Automação concluída com sucesso.")