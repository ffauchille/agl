# -*- coding: utf-8 -*-

import tkFileDialog
import os


class JavaParser():

    def parse(self, from_file):

        if from_file == "":
            file_path_string = tkFileDialog.askopenfilename()
            file_path_string = file_path_string.replace("/", "\\")
        else:
            file_path_string = from_file
        sql_file = file_path_string.replace(".dia", ".sql")
        bashCommand = "perl C:\\PROGRA~2\\Parse-Dia-SQL-0.27\\Parse-Dia-SQL-0.27\\bin\\parsediasql --file {0} --db postgres > {1}".format(file_path_string, sql_file)
        os.system(bashCommand)



if __name__ == '__main__':
    jp = JavaParser()
    JavaParser.parse(jp, "")