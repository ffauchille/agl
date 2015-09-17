# -*- coding: utf-8 -*-

import tkFileDialog
import plyj.parser as plyj
import plyj.model as m


class JavaParser():

    @classmethod
    def parse(self, files_list):
        """
        :return: List of diagram names + file_name : [[f1,c1,c2],[f2,c1,c2,c3]
        """
        if files_list == "":
            file_path_string = tkFileDialog.askopenfilename()
            files = [file_path_string]
        else:
            files = files_list
            files2 = []
            for fil in files:
                files2.append(fil)
            for fil in files:
                if not fil.endswith(".java"):
                    files2.remove(fil)
            files = files2

        json = []
        data = []
        for fil in files:
            parser = plyj.Parser()
            tree = parser.parse_file(file(fil))
            if tree is not None:
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
    JavaParser.parse(jp, "")