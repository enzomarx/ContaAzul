import pyautogui
import time

pyautogui.PAUSE = 3
time.sleep(3)

# Número total de interações
num_iterations = 1000

# y inicial
initial_y = 222
increment_step = 50

# Contador de iterações
iteration_count = 0

while iteration_count < num_iterations:
    for i in range(10):
        # Cálculo da y-coordinate para cada iteração
        current_y = initial_y + (i * increment_step)

        # O clique no y inicial e no y incrementado
        pyautogui.click(x=820, y=current_y)
        time.sleep(2)
        
        # Performance drag
        pyautogui.moveTo(x=33, y=322)
        pyautogui.dragTo(x=243, y=335, duration=0.5, button='left')

        # Copy 1
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.PAUSE = 2  

        # The target location to paste t
        pyautogui.click(x=111, y=459)
        pyautogui.moveTo(x=1039, y=241)
        pyautogui.dragTo(x=549, y=237, duration=1.5, button='left')
        pyautogui.press('delete')

        # Fixed string
        pyautogui.write('VL DE N A ')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(' REF')

        # Save
        pyautogui.click(x=1196, y=692)

        # Second performance drag
        pyautogui.moveTo(x=648, y=328)
        pyautogui.dragTo(x=822, y=353, duration=0.5, button='left')

        pyautogui.hotkey('ctrl', 'c')
        pyautogui.PAUSE = 2  

        # The target location to paste 
        pyautogui.click(x=111, y=459)
        pyautogui.click(x=1039, y=241)
        time.sleep(3)
        pyautogui.press('space')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')

        # Save
        pyautogui.click(x=1196, y=692)
        time.sleep(1)
        
        # Go back
        pyautogui.click(x=43, y=692)
        time.sleep(1)
        
        time.sleep(5)

        iteration_count += 1
        if iteration_count >= num_iterations:
            break
    
    # Ações adicionais após cada 10 interações
    if iteration_count % 10 == 0:
        for _ in range(2):
            pyautogui.click(x=1305, y=712)
        pyautogui.click(x=878, y=698)
        time.sleep(1)
        for _ in range(9):
            pyautogui.click(x=1305, y=712)
        time.sleep(5)
    # Reiniciar o y inicial para a próxima iteração
    initial_y = 222
