import threading
import plyj


class ThreadedFileParser(threading.Thread):
    """
    Threaded file parser using plyj.

    USAGE :
    parser = TreadedFileParser("file_path")
    parser.run()

    """

    def __init__(self, fil):
        threading.Thread.__init__(self)
        self.fil = fil

    def run(self):
        parser = plyj.Parser()
        print "ThreadedFileParser: parsing file {} started.".format(self.fil)
        _res = parser.parse_file(file(self.fil))
        print "ThreadedFileParser: parsing file {} done.".format(self.fil)
        return _res
