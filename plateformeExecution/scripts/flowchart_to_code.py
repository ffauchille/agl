# -*- coding: utf-8 -*-

import tkFileDialog
import os
from plateformeExecution.project import Project


class FlowchartToCode():

    def parse(self):
        fil = tkFileDialog.askopenfilename()
        count = 0
        body = ""
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

    def implement(self, files, array):
        files = ["C:\\AGL\\Diagramme1.java"]
        for fil in files:
            body = ""
            with open(fil, "r+") as f:
                lines = f.readlines()
            for line in lines:
                if line.find(array[0]) != -1:
                    i = 0
                    for ch in line:
                        if ch == "{":
                            line = line[:i+1] + array[1] + line[i+1:]
                            break
                        i += 1
                body += line
            with open(fil, "w") as f:
                f.write(body)
        return

if __name__ == '__main__':
    jp = FlowchartToCode()
    FlowchartToCode.implement(jp, "", jp.parse())