import os


class FileSystemError(Exception):
    ''' Class for errors in filesystem module '''
    pass


class FSItem(object):
    ''' Common class for OS items OS: Files and Directories '''

    def __init__(self, path):
        ''' Creates new FSItem instance by given path to file '''
        self.path = path
        self.name = os.path.split(path)[1]

    def rename(self, newname):
        ''' Renames current item
                raise FileSystemError if item does not exist
                raise FileSystemError if item "newname" already exists '''
        if os.path.exists(self.path) and self.name != self.newname:
            os.rename(self.name, self.newname)
        else:
            raise FileSystemError(
                "Can't rename file: {0} already exist".format(self.getname()))

    def create(self):
        ''' Creates new item in OS
                raise FileSystemError if item with such path already exists '''
        if os.path.exists(self.path):
            if os.path.isfile(self.path):
                with open(self.path, 'a'):
                    pass
            elif os.path.isdir(self.path):
                os.mkdir(self.path)
        else:
            raise FileSystemError(
                "Can't create file/directory: path {0} already exist".format(self.get_path_name()))

    def getname(self):
        ''' Returns name of current item '''
        return self.name

    def get_path_name(self):
        return self.path

    def isfile(self):
        ''' Returns True if current item exists and current item is file, False otherwise '''
        return os.path.isfile(self.path)

    def isdirectory(self):
        ''' Returns True if current item exists and current item is directory, False otherwise '''
        return os.path.isdir(self.path)


class File(FSItem):
    ''' Class for working with files '''

    def __init__(self, path):
        ''' Creates new File instance by given path to file
                raise FileSystemError if there exists directory with the same path '''
        if os.path.exists(self.path):
            raise FileSystemError(
                "Can't create file: {0} already exist".format(self.getname()))
        else:
            self.path = path

    def __len__(self):
        ''' Returns size of file in bytes
                raise FileSystemError if file does not exist '''
        if isfile(self.path) and os.path.exists(self.path):
            return os.stat(path).st_size
        else:
            raise FileSystemError(
                "Can't show size: file {0} does not exist".format(self.get_path_name()))

    def getcontent(self):
        ''' Returns list of lines in file (without trailing end-of-line)
                raise FileSystemError if file does not exist '''
        if isfile(self.path) and os.path.exists(self.path):
            with open(path, 'r') as file:
                return ([line.rstrip() for line in file])
        else:
            raise FileSystemError(
                "Can't show content: file {0} does not exist".format(self.get_path_name()))

    def __iter__(self):
        ''' Returns iterator for lines of this file
                raise FileSystemError if file does not exist '''
        with open(path, 'r') as file:
            return iter(list(map(lambda line: line.rstrip(), file)))


class Directory(FSItem):
    ''' Class for working with directories '''

    def __init__(self, path):
        ''' Creates new Directory instance by given path
                raise FileSystemError if there exists file with the same path '''
        if os.path.exists(self.path):
            raise FileSystemError(
                "Can't create directory: {0} already exist".format(self.get_path_name()))
        else:
            self.path = path

    def items(self):
        ''' Yields FSItem instances of items inside of current directory
                raise FileSystemError if current directory does not exists '''
        if os.path.exists(self.path) == False:
            raise FileSystemError(
                "Can't show instances inside of directory: {0} already exist".format(self.get_path_name()))
        else:
            yield os.listdir(self.path)

    def files(self):
        ''' Yields File instances of files inside of current directory
                raise FileSystemError if current directory does not exists '''
        if os.path.exists(self.path) == False and isdirectory(self.path) == False:
            raise FileSystemError()
        else:
            for i in filter(lambda file: isfile(os.path.join(path, file)), list(os.listdir(path))):
                yield i

    def subdirectories(self):
        ''' Yields Directory instances of directories inside of current directory
                raise FileSystemError if current directory does not exists '''
        if os.path.exists(self.path) == False:
            raise FileSystemError()
        else:
            for i in filter(lambda file: isdirectory(os.path.join(self.path, file)), list(os.listdir(self.path))):
                yield i

    def filesrecursive(self):
        ''' Yields File instances of files inside of this directory,
                inside of subdirectories of this directory and so on...
                raise FileSystemError if directory does not exist '''
        if os.path.exists(self.path) == False and isdirectory(self.path) == False:
            raise FileSystemError()
        else:
            if os.listdir(path) == []:
                return
            else:
                for i in filter(lambda file: isdirectory(os.path.join(self.path, file)), list(os.listdir(self.path))):
                    self.new_path = os.path.join(self.path, i)
                    yield list(files(self.path)), list(filesrecursive(self.new_path))

    def getsubdirectory(self, name):
        ''' Returns Directory instance with subdirectory of current directory with name "name"
                raise FileSystemError if item "name" already exists and item "name" is not directory '''
        if os.path.exists(self.path) == False and isdirectory(self.path) == False:
            raise FileSystemError(
                "Can't create directory: {0} already exist".format(self.get_path_name()))
        else:
            if os.listdir(self.path) == []:
                return
            else:
                for i in filter(lambda file: isdirectory(os.path.join(self.path, file)), list(os.listdir(self.path))):
                    self.new_path = os.path.join(self.path, i)
                    yield list(subdirectories(self.path)), list(filesrecursive(self.new_path))
