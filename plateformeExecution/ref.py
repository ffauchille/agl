import os
import json

class Reference(object):
    """
        Represent the reference document
    """

    def __init__(self, absolute_path=""):
        self.ref_path = os.path.join(absolute_path, 'referentiel', 'ref.json')

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
        pass

