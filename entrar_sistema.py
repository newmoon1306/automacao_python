import pyautogui
import time
import pandas as pd #para abreviar o pandas para o apelido pd

pyautogui.PAUSE = 1  

pyautogui.press('win')
pyautogui.write('chrome')
time.sleep(3)

pyautogui.press('enter')

time.sleep(3)

pyautogui.click(x=984, y=698)

time.sleep(5)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press('enter')

time.sleep(1)   


#pyautogui.click(x=813, y=404)s
pyautogui.press('tab')
time.sleep(2)
pyautogui.write('lia10lisa@gmail.com')
pyautogui.press('tab')
time.sleep(4)   
pyautogui.write('lia10lisa')
time.sleep(1)
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)


# para ler e armazenar a base de dados
tabela = pd.read_csv('produtos.csv') 

for linha in tabela.index: #leio a linha da minha tabela por conta do index se for para colunas coloque tabela.colunms
#pegar a localização especifico nessa tabela pegando a linha e coluna nesse caso a linha e dinamico mas o codigo e o nome da coluna
   
    

    pyautogui.click(x=819, y=267)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab') #prox campo
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(10000) #rolar para cima a tela postivo para cima negativo para baixo

