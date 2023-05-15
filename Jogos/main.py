'''import tkinter
import random

root = tkinter.Tk()
root.geometry('300x300')
root.title('Jogar Dado')

# display do dado
label = tkinter.Label(root, text='', font=('Arial', 260))

# função ativada por botão
def jogar_dados():
    dado = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dado)}')
    label.pack()

# botão
botao = tkinter.Button(root, text='Jogar Dado', foreground='black', command=jogar_dados)

botao.pack()

# mantem a janela aberta
root.mainloop()'''

'''s1 = {1,2,3,4,5,6}
s2 ={6,7,8,9}
print(s1&s2)'''

arquivo = open('arquivo.txt','a')

lista = (0,3,2,1,5,6,10,23)



arquivo.write(lista)