import os


class System(object):
    @staticmethod
    def is_directory_exist(d):
        return os.path.isdir(d)

    @staticmethod
    def create_dir(d):
        print(d)
        if not System.is_directory_exist(d):
            os.mkdir(d)

    @staticmethod
    def delete_dir(d):
        if System.is_directory_exist(d):
            os.rmdir(d)

    @staticmethod
    def is_file_exist(f):
        os.path.isfile(f)

    @staticmethod
    def create_file(f):
        if not System.is_file_exist(f):
            with open('f', 'w') as fp:
                pass

    @staticmethod
    def delete_file(f):
        if System.is_file_exist(f):
            os.remove(f)
