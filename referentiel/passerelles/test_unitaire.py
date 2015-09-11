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
                # print(type_decl.name)
                json += '"Classe" : ' + type_decl.name + "{"
                # print('fields:')
                # for field_decl in [decl for decl in type_decl.body if type(decl) is m.FieldDeclaration]:
                #     for var_decl in field_decl.variable_declarators:
                #         if type(field_decl.type) is str:
                #             type_name = field_decl.type
                #         else:
                #             type_name = field_decl.type.name.value
                #         print('    ' + type_name + ' ' + var_decl.variable.name)
                # print
                # print('methods:')
                for method_decl in [decl for decl in type_decl.body if type(decl) is m.MethodDeclaration]:
                    # param_strings = []
                    # for param in method_decl.parameters:
                    #     if type(param.type) is str:
                    #         param_strings.append(param.type + ' ' + param.variable.name)
                    #     else:
                    #         param_strings.append(param.type.name.value + ' ' + param.variable.name)
                    # print(method_decl.name)
                    json += '"Méthode" : ' + method_decl.name + "{},"
                json = json[:-1]
                json += "},"
            json = json[:-1]
            if method_decl.body is not None:
                for statement in method_decl.body:
                    # note that this misses variables in inner blocks such as for loops
                    # see symbols_visitor.py for a better way of handling this
                    if type(statement) is m.VariableDeclaration:
                        for var_decl in statement.variable_declarators:
                            if type(statement.type) is str:
                                type_name = statement.type
                            else:
                                type_name = statement.type.name.value
                            print('        ' + type_name + ' ' + var_decl.variable.name)
                for st in method_decl.body:
                    print st
                print(method_decl.body)
            print json
        return json


if __name__ == '__main__':
    jp = JunitParser()
    JunitParser.parse(jp)