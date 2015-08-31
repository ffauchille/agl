__author__ = 'flo'

class Project(object):
    '''
        Represent a project
    '''

    def __init__(self, **kwargs):
        self.name = kwargs.get('project_name', "New project")
        self.root_path = kwargs.get('root_path', './')

    def create_folder(self):
        """
        create the project's folder tree
        :return: void
        """
        pass