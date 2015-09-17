# -*- coding: utf-8 -*-
import xml.etree.cElementTree as etree

class UsecaseParser():

    @classmethod
    def parse(self, files_list):
        """
        Parse all files contained in the path_value and get the use-cases of the *.dia files
        :param path_value:
        :return: List of use-cases
        """

        files = files_list
        files2 = []
        for fil in files:
            files2.append(fil)
        for fil in files:
            if not fil.endswith(".dia"):
                files2.remove(fil)
        files = files2

        usecases = []

        dia = "{http://www.lysator.liu.se/~alla/dia/}"
        path = "{0}layer/{0}object[@type='UML - Usecase']/{0}attribute[@name='text']/{0}composite/{0}attribute[@name='string']/{0}string".format(dia)
        for fil in files:
            tree = etree.parse(fil)
            for diag in tree.findall(path):
                usecases.append(diag.text[1:len(diag.text)-1])
        return usecases
