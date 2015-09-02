# -*- coding: utf-8 -*-
import os
import xml.etree.cElementTree as etree
from plateformeExecution.project import Project

class UsecaseParser():

    def parse(self, path_value):

        # Get only the files to parse, could be used for the project

        files = path_value
        for fil in files:
            if not fil.endswith(".dia"):
                files.remove(fil)

        print "test"
        print files
        usecases = []

        dia = "{http://www.lysator.liu.se/~alla/dia/}"
        path = "{0}layer/{0}object[@type='UML - Activity']/{0}attribute[@name='text']/{0}composite/{0}attribute[@name='string']/{0}string".format(dia)
        for fil in files:
            print fil
            tree = etree.parse(fil)
            for diag in tree.findall(path):
                usecases.append(diag.text[1:len(diag.text)-1])
        print usecases
        return usecases
        # usecases contains the name of the usecase that will be given to the json

if __name__ == '__main__':
    up = UsecaseParser()
    UsecaseParser.parse(up)