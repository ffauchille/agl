__author__ = 'flo'
import os


class Project(object):
    '''
        Represent a project
    '''

    categories = ['referentiel',
                  'specification',
                  'conception',
                  'realisation',
                  'test', ]

    def __init__(self, **kwargs):
        self.name = kwargs.get('project_name', "New project")
        self.root_path = kwargs.get('root_path', './')
        self.absolute_path = os.path.join(self.root_path, self.name)

    def create_folder(self):
        """
        create the project's folder tree as follow
        project_name
            <categories_item1>
            <categories_item2>
            ...
        :return: void
        """
        print "project's name: {}".format(self.name)
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

    def list_dir(self, dir_path):
        """
        List the contend of the directory specified by dir_path
        :param dir_path: path of the directory
        :return: a list of filenames
        """
        return os.listdir(dir_path)

    def get_specification_files(self):
        """
        List the contend of this project's specification
        :return:
        """
        files = self.list_dir(os.path.join(self.absolute_path, 'specification'))
        print "spec files: {}".format(files)
        return files

    def get_specification_files(self):
        return self.list_dir(os.path.join(self.absolute_path, 'conception'))

    def get_conception_files(self):
        return self.list_dir(os.path.join(self.absolute_path, 'realisation'))

    def get_test_files(self):
        return self.list_dir(os.path.join(self.absolute_path, 'test'))

    def get_referentiel_files(self):
        return self.list_dir(os.path.join(self.absolute_path, 'referentiel'))
