from Tkinter import *
from controler.GenerateGraphsControler import GenerateGraphsContol


def buttonClick():
    root.destroy()
    GenerateGraphsContol(nbPairesGraphs.get(), nbNoeuds.get())




root = Tk()

root.title("Projet Applicatif")

label1 = Label(root, text="Generer des graphes")
label1.grid(row=0)

label2 = Label(root, text="Entrez le nombre de paires de graphes que vous souhaitez generer")
label2.grid(row=1)

nbPairesGraphs = IntVar()
entryNbPairesGraphs = Entry(root, textvariable=nbPairesGraphs)
entryNbPairesGraphs.grid(row=2)

label3 = Label(root, text="Entrez le nombres de noeud des graphes")
label3.grid(row=3)

nbNoeuds = IntVar()
entryNbNoeuds = Entry(root, textvariable=nbNoeuds)
entryNbNoeuds.grid(row=4)

button = Button(root, text="Generer",command=lambda: buttonClick())
button.grid(row=6)

root.mainloop()




