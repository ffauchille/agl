#!/usr/bin/env python
# -*- coding: latin-1 -*-

import ttk
import Tkinter


class GUI(Tkinter.Frame):
    """
        IHM de la plateforme d'exécution de l'AGL
    """

    def __init__(self, master=None):
        Tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


    def paramMaster(self):
        width = self.master.winfo_screenmmwidth()
        height = self.master.winfo_screenheight()
        self.master.geometry("{0}x{1}+{2}+{3}".format(800, 600, 300, 300))
        self.master.title("AGL execution plateform")


    def start(self):
        self.paramMaster()
        self.mainloop()
        self.master.destroy()

    def createWidgets(self):
        self.TREE = ttk.Treeview(master=self.master)
        spec = "spec"
        arch = "architecture-element"
        cls = "class-fonction"
        tst = "test"
        res = "result"
        err = "error"
        self.TREE["columns"] = (spec,
                                arch,
                                cls,
                                tst,
                                res,
                                err,)
        self.TREE.column(spec, width=100)
        self.TREE.column(arch, width=100)
        self.TREE.column(cls, width=100)
        self.TREE.column(tst, width=100)
        self.TREE.column(res, width=100)
        self.TREE.column(err, width=100)
        self.TREE.heading(err, text="besoin/exigence")
        self.TREE.heading(arch, text="Elément d'architecture")
        self.TREE.heading(cls, text="classe/fonction")
        self.TREE.heading(tst, text="Test")
        self.TREE.heading(res, text="Résultat")
        self.TREE.heading(err, text="Anomalie")
        self.TREE.pack()

        self.QUIT = Tkinter.Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack()

    def createFrame(self):
        pass


if __name__ == '__main__':
    gui = GUI(master=Tkinter.Tk())
    gui.start()