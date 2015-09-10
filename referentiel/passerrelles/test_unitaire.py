# -*- coding: utf-8 -*-

import tkFileDialog
import plyj.parser as plyj
import plyj.model as m


class JunitParser():

    def parse(self):
        file_path_string = tkFileDialog.askopenfilename()
        files = [file_path_string]

        json = ""

        for fil in files:
            parser = plyj.Parser()
            tree = parser.parse_file(file(fil))
            for type_decl in tree.type_declarations:
                # json += '"Classe" : ' + type_decl.name + "{"
                print ("toto")
                print type_decl.body
                print("toto")
                for method_decl in [decl for decl in type_decl.body]:
                    print method_decl
                    if type(method_decl) == m.MethodDeclaration:
                        for met in method_decl.body:
                            print "  #####  "
                            print met
                            if type(met) == m.MethodInvocation:
                                    print met.name


if __name__ == '__main__':
    jp = JunitParser()
    JunitParser.parse(jp)