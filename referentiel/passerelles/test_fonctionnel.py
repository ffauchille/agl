# -*- coding: utf-8 -*-

import tkFileDialog
import plyj.parser as plyj


class JavaParser():

    def parse(self):
        file_path_string = tkFileDialog.askopenfilename()
        files = [file_path_string]

        json = []

        for fil in files:
            parser = plyj.Parser()
            tree = parser.parse_file(file(fil))
            for type_decl in tree.type_declarations:
                json.append(type_decl.name)
            print json
        return json

if __name__ == '__main__':
    jp = JavaParser()
    JavaParser.parse(jp)