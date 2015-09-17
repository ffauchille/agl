import threading
import plyj.parser as plyj


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
        self.daemon = True

    def run(self):
        parser = plyj.Parser()
        _res = parser.parse_file(self.fil)
        return _res
