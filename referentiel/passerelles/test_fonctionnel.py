# -*- coding: utf-8 -*-

import tkFileDialog
import plyj.parser as plyj
import os

class JavaParser():

    def parse(self, path_value):

        if path_value == "":
            file_path_string = tkFileDialog.askopenfilename()
            files = [file_path_string]
        else:
            files = path_value
            files2 = []
            for fil in files:
                files2.append(fil)
            for fil in files:
                if not fil.endswith(".java"):
                    files2.remove(fil)
            files = files2

        classes = []
        json = []

        for fil in files:
            parser = plyj.Parser()
            tree = parser.parse_file(file(fil))
            classes.append(os.path.basename(fil)[:-5])
            for type_decl in tree.type_declarations:
                classes.append(type_decl.name)
            json.append(classes)
            classes = []
        print json
        return json

if __name__ == '__main__':
    jp = JavaParser()
    JavaParser.parse(jp, "")