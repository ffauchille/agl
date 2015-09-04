import os
import json
from passerrelles.use_case import UsecaseParser
from kivy.uix.treeview import TreeViewLabel, TreeView

class Reference(object):
    """
        Represent the reference document
    """

    referentiel_tree = TreeView

    ref_path = ""
    project_name = ""

    def __init__(self, absolute_path="", project_name="New project"):
        self.ref_path = os.path.join(absolute_path, 'referentiel', project_name + '.ref.json')
        self.project_name = project_name
        self.referentiel_tree = TreeView()
        if os.path.isfile(self.ref_path):
            self.load_json()
        else:
            self.create_json()

    def create_json(self):
        """
        Create the json file
        :return: void
        """
        ref = open(self.ref_path, 'a+')
        json.dump({"Use-case": "None"}, ref, sort_keys=True, indent=4, separators=(',', ': '))
        self.referentiel_tree.add_node({"Use-case": "None"})
        ref.close()

    def insert_use_cases(self, uc_list):
        """
        Insert all use cases given in parameter inside the ref.json
        :param uc_list: list of use_case which have to insert into the file
        :return: void
        """
        ref = open(self.ref_path, 'a+')

        for uc in uc_list:
            json.dump({"Use-case": uc}, ref, sort_keys=True, indent=4, separators=(',', ': '))

            ref.write('\n\n')

        ref.close()

    def load_json(self):
        """
        Load the ref.json on memory to make the print easier and improve the program speed
        :return:
        """
        ref = open(self.ref_path, 'r')
        data = json.load(ref)
        ref.close()
        print data


    def update_specs_json(self, specs_files):
        """
        :return:
        """
        use_cases = UsecaseParser.parse(specs_files)
        self.insert_use_cases(use_cases)

    def get_tree(self):
        return self.referentiel_tree