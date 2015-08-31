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
