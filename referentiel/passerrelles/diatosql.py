# -*- coding: utf-8 -*-

import tkFileDialog
import os


class JavaParser():

    def parse(self, from_file):
        file_path_string = tkFileDialog.askopenfilename()
        file_path_string = file_path_string.replace("/", "\\")
        sql_file = file_path_string.replace(".dia", ".sql")
        print file_path_string
        bashCommand = "perl C:\\PROGRA~2\\Parse-Dia-SQL-0.27\\Parse-Dia-SQL-0.27\\bin\\parsediasql --file {0} --db postgres > {1}".format(file_path_string, sql_file)
        print bashCommand
        os.system(bashCommand)



if __name__ == '__main__':
    jp = JavaParser()
    JavaParser.parse(jp, "")