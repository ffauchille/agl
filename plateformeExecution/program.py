import threading
import subprocess

class Program(threading.Thread):
    """
    Class for running program using thread
    """

    def __init__(self, program_name=""):
        threading.Thread.__init__(self)
        self.name = program_name

    def run(self):
        subprocess.call([self.name])
