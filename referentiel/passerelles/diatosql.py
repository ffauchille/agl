# -*- coding: utf-8 -*-

import tkFileDialog
import os
from Tkinter import *


class JavaParserSQL():

    def parse(self, from_file):

        if from_file == "":
            try:
                root = Tk()
                root.withdraw()
                file_path_string = tkFileDialog.askopenfilename()
            except:
                return ""
            file_path_string = file_path_string.replace("/", "\\")
        else:
            file_path_string = from_file
        sql_file = file_path_string.replace(".dia", ".sql")
        bashCommand = "perl C:\\PROGRA~2\\Parse-Dia-SQL-0.27\\Parse-Dia-SQL-0.27\\bin\\parsediasql --file {0} --db postgres > {1}".format(file_path_string, sql_file)
        os.system(bashCommand)
        return sql_file


if __name__ == '__main__':
    jp = JavaParserSQL()
    JavaParserSQL.parse(jp, "")