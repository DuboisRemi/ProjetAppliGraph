from Tkinter import *



def init(listePairesGraphs):
    root = Tk()
    root.title("Projet Applicatif")
    label1 = Label(root, text=str(len(listePairesGraphs)))
    label1.grid(column=0 ,row= 0)
    label2 = Label(root, text=" Paires de Graphes Isomorphes 2 a 2")
    label2.grid(column=1 ,row= 0)