import pyautogui
import time

pyautogui.PAUSE = 3
time.sleep(3)
# número de interações
num_iterations = 15 

# y inicial
initial_y = 222
increment_step = 50

for i in range(num_iterations):
    # cálculo da y-coordinate para cada iteração
    current_y = initial_y + (i * increment_step)
    
    # o clique no y inicial e no y incrementado
    pyautogui.click(x=820, y=current_y)
    time.sleep(2)
    # performance drag
    pyautogui.moveTo(32, 338)
    pyautogui.dragTo(140, 337, duration=0.5, button='left')

    # Copy 1
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.PAUSE = 2  

    # the target location to paste t
    pyautogui.click(x=111, y=459)
    pyautogui.moveTo(x=1039, y=241)
    pyautogui.dragTo(x=549, y=237, duration=1.5, button='left')
    pyautogui.press('delete')

    # fixed string
    pyautogui.write('VL DE N A ')
    
    pyautogui.hotkey('ctrl', 'v')

    # rest of fixed string
    pyautogui.write(' REF')
    #save
    pyautogui.click(x=1196, y=692)

    # second performance drag
    pyautogui.moveTo(651, 341)
    pyautogui.dragTo(800, 348, duration=0.5, button='left')

    pyautogui.hotkey('ctrl', 'c')
    pyautogui.PAUSE = 2  

    #  the target location to paste 
    pyautogui.click(x=111, y=459)
    pyautogui.click(x=1039, y=241)
    time.sleep(3)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')

    #save
    pyautogui.click(x=1196, y=692)
    time.sleep(1)
    # go back
    pyautogui.click(x=43, y=692)
    time.sleep(1)

    time.sleep(5)

    # Executa o clique 12 vezes a cada 10 interações
    if (i + 1) % 10 == 0:
        for _ in range(12):
            pyautogui.click(x=1305, y=712)
        initial_y = 222