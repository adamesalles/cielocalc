from tkinter import *


class Application:
    def __init__(self, master=None):
        print("Mãe, se tiver lendo n liga pra aqui não")
        self.mainfont = ("Arial", "10")
        self.firstCont = Frame(master)
        self.firstCont["pady"] = 10
        self.firstCont.pack()

        self.secondCont = Frame(master)
        self.secondCont["padx"] = 20
        self.secondCont.pack()

        self.thirdCont = Frame(master)
        self.thirdCont["pady"] = 20
        self.thirdCont.pack()

        self.fourthCont = Frame(master)
        self.fourthCont["pady"] = 20
        self.fourthCont.pack()

        self.title = Label(self.firstCont, text="Entre com os dados")
        self.title["font"] = ("Arial", "10", "bold")
        self.title.pack()

        self.parcelvLabel = Label(self.secondCont,
                                  text="Valor: ", font=self.mainfont, anchor=W, justify=LEFT)
        self.parcelvLabel.pack()

        self.parcelv = Entry(self.secondCont)
        self.parcelv["width"] = 30
        self.parcelv["font"] = self.mainfont
        self.parcelv.pack(side=LEFT)

        self.parcelqLabel = Label(self.thirdCont,
                                  text="Quantidade de Parcelas: ", font=self.mainfont, anchor=W, justify=LEFT)
        self.parcelqLabel.pack()

        self.parcelq = Entry(self.thirdCont)
        self.parcelq["width"] = 30
        self.parcelq["font"] = self.mainfont
        self.parcelq.pack(side=LEFT)

        self.calculate = Button(self.fourthCont)
        self.calculate["text"] = "Calcular"
        self.calculate["font"] = ("Calibri", "8")
        self.calculate["width"] = 12
        self.calculate["command"] = self.mesure
        self.calculate.pack()

        self.messageLabel = Label(self.fourthCont,
                                  text="", font=self.mainfont)
        self.messageLabel.pack()

    def mesure(self):
        x = float(self.parcelv.get())
        tfx = float(3.49)
        tpp = float(1.99)
        y = int(self.parcelq.get())
        tff = tfx + (y * tpp)
        a = x * (tff/100)
        varr = x - a
        ppy = x * (1 + (tff/200))
        print(round(tff, 2), "%")
        self.messageLabel["text"] = "Parcelas: {} \n Taxa Total: R${} ({} %) \n Valor a receber: R${} \n Valor a cobrar (dividindo os custos): R${}".format(
            y, round(a, 2), round(tff, 2), round(varr, 2), round(ppy, 2))


root = Tk()
root.title('Cálculo CIELO')
Application(root)
root.mainloop()
