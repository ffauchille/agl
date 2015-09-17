import os
from referentiel.ref import Reference
from referentiel.passerelles.use_case import UsecaseParser
from referentiel.passerelles.class_diag import DiagParser
from referentiel.passerelles.class_method_java import JavaParser
from referentiel.passerelles.test_unitaire import JunitParser

class Project(object):
    """
        Represent a project
    """

    current_ref = None

    categories = ['referentiel',
                  'specification',
                  'conception',
                  'realisation',
                  'test_unitaire',
                  'test_fonctionnel']

    def __init__(self, **kwargs):
        self.name = kwargs.get('project_name', "New project")
        self.root_path = kwargs.get('root_path', './')
        self.absolute_path = os.path.join(self.root_path, self.name)
        self.create_folder()
        self.current_ref = Reference(self.absolute_path, self.name)

    def create_folder(self):
        """
        create the project's folder tree as follow
        project_name
            <categories_item1>
            <categories_item2>
            ...
        :return: void
        """
        project_path = os.path.join(self.root_path, self.name)
        if not os.path.exists(project_path):
            os.makedirs(project_path)
            print "project's folder {} has been created"
        # create a folder for each category
        for category in self.categories:
            cat_path = os.path.join(project_path, category)
            if not os.path.exists(cat_path):
                os.makedirs(cat_path)
                print "folder {} has been created".format(cat_path)
        os.chdir('C:\\AGL\\Projects\\' + self.name)

    def list_dir(self, dir_path):
        """
        List the content of the directory specified by dir_path
        :param dir_path: path of the directory
        :return: a list of filenames
        """
        files = os.listdir(dir_path)
        files2 = []
        for fil in files:
            fil = os.path.join(dir_path, fil)
            files2.append(fil)
        return files2

    def get_specification_files(self):
        """
        List the content of this project's specification
        :return: the files which are inside the specification folder
        """
        return self.list_dir(os.path.join(self.absolute_path, 'specification'))

    def get_conception_files(self):
        """
        List the content of this project's conception
        :return: the files which are inside the conception folder
        """
        return self.list_dir(os.path.join(self.absolute_path, 'conception'))

    def get_realisation_files(self):
        """
        List the content of this project's realisation
        :return: the files which are inside the realisation folder
        """
        return self.list_dir(os.path.join(self.absolute_path, 'realisation'))

    def get_test_u_files(self):
        return self.list_dir(os.path.join(self.absolute_path, 'test_unitaire'))

    def get_test_f_files(self):
        return self.list_dir(os.path.join(self.absolute_path, 'test_fonctionnel'))

    def get_referentiel_files(self):
        return self.list_dir(os.path.join(self.absolute_path, 'referentiel'))

    def set_referientiel(self, ref):
        self.current_ref = ref


    def update_specification(self):
        """
        Update the specifications inside the json
        :return:
        """
        files = self.get_specification_files()
        if files == []:
            print "Le dossier de specification est vide, impossible de continuer"
            return 0
        else:
            return self.current_ref.insert_use_cases(UsecaseParser.parse(files))

    def update_conception(self):
        """
        Update the conception inside the json
        :return:
        """
        files = self.get_conception_files()
        if files == []:
            print "Le dossier de conception est vide, impossible de continuer"
            return 0
        else:
            return self.current_ref.insert_diag_concept(DiagParser.parse(files))

    def update_realisation(self):
        """
        Update the conception inside the json
        :return:
        """
        files = self.get_realisation_files()
        if files == []:
            print "Le dossier de realisation est vide, impossible de continuer"
            return 0
        else:
            return self.current_ref.insert_rea(JavaParser.parse(files))

    def update_test_u(self):
        files = self.get_test_u_files()
        if files == []:
            print "Le dossier de realisation est vide, impossible de continuer"
            return 0
        else:
            self.current_ref.insert_test_u(JunitParser.parse(files))
            return 0

    def get_ref(self):
        return self.current_ref


