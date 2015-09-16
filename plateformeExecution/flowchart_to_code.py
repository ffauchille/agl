# -*- coding: utf-8 -*-

from Tkinter import *
import tkFileDialog
import os


class FlowchartToCode():

    def parse(self):
        try:
            root = Tk()
            root.withdraw()
            fil = tkFileDialog.askopenfilename()
        except:
            pass
        count = 0
        body = ""
        array = []
        if fil:
            with open(fil) as f:
                stream = f.read()
            for ch in stream:
                if ch == "{":
                    count += 1
                elif ch == "}":
                    count -= 1
                if count > 0:
                    body += ch
            body = body[1:]
            array = [os.path.basename(fil), body]
            # print array
        return array

    def implement(self, files):
        array = self.parse()
        try:
            name = array[0].split("-")
        except:
            pass
        if len(name) != 2:
            print "Wrong file name"
            return -1
        class_meth = False
        for fil in files:
            if not fil.endswith(".java"):
                files.remove(fil)
        for fil in files:
            body = ""
            with open(fil, "r+") as f:
                lines = f.readlines()
            for line in lines:
                if line.find(" " + name[0] + " ") != -1:
                    class_meth = True
                if line.find(" " + name[1] + " ") != -1 and class_meth:
                    i = 0
                    for ch in line:
                        if ch == "{":
                            line = line[:i+1] + array[1] + line[i+1:]
                            class_meth = False
                            break
                        i += 1
                body += line
            with open(fil, "w") as f:
                if body:
                    f.write(body)
            class_meth = False
        return 0

if __name__ == '__main__':
    jp = FlowchartToCode()
    FlowchartToCode.implement(jp, "")