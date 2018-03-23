from Tkinter import *
from controler.MenuControler import umeyama,jouili


def umeyamaClick(listePairesGraphs):
    umeyama(listePairesGraphs)

def jouiliClick(listePairesGraphs):
    jouili(listePairesGraphs)


def init(listePairesGraphs):
    root = Tk()
    root.title("Projet Applicatif")
    label1 = Label(root, text=str(len(listePairesGraphs)))
    label1.grid(column=0, row=0)
    label2 = Label(root, text=" Paires de Graphes Isomorphes 2 a 2")
    label2.grid(column=1, row=0)

    button_umeyama = Button(root, text="Umeyama", command=lambda: umeyamaClick(listePairesGraphs))
    button_jouili = Button(root, text="Jouili", command=lambda: jouiliClick(listePairesGraphs))
    button_umeyama.grid(column=1, row=1)
    button_jouili.grid(column=2,row=1)

    root.mainloop()

