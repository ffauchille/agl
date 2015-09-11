# -*- coding: utf-8 -*-

import tkFileDialog
import plyj.parser as plyj
import plyj.model as m


class JavaParser():

    def parse(self):
        file_path_string = tkFileDialog.askopenfilename()
        files = [file_path_string]

        json = []
        data = []
        for fil in files:
            parser = plyj.Parser()
            tree = parser.parse_file(file(fil))
            for type_decl in tree.type_declarations:
                data.append(type_decl.name)
                for method_decl in [decl for decl in type_decl.body if type(decl) is m.MethodDeclaration]:
                    data.append(method_decl.name)
                json.append(data)
                data = []
            print json
        return json

if __name__ == '__main__':
    jp = JavaParser()
    JavaParser.parse(jp)