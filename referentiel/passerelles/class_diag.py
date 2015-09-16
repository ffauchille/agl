# -*- coding: utf-8 -*-
import os
import xml.etree.cElementTree as etree

# Placeholder method to test the script with a dia file
import tkFileDialog


class DiagParser():

    @classmethod
    def parse(self, files_list):
        """

        :return: List of diagram names
        """
        files = files_list
        for fil in files:
            if not fil.endswith(".dia"):
                files.remove(fil)

        classes = []

        dia = "{http://www.lysator.liu.se/~alla/dia/}"
        path = "{0}layer/{0}object[@type='UML - Class']/{0}attribute[@name='name']/{0}string".format(dia)
        for fil in files:
            tree = etree.parse(fil)
            for cla in tree.findall(path):
                classes.append(cla.text[1:len(cla.text)-1])
        print classes
        return classes
        # usecases contains the name of the usecase that will be given to the json

if __name__ == '__main__':
    dp = DiagParser()
    DiagParser.parse(dp)