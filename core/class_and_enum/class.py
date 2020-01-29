class Base:

    def __special_method__(self):
        pass

    def normal_method(self):
        pass

class AnotherBase(object):

    def __special_method__(self):
        print('Did it get included in __dict__?')

def print_about_class(cls):
    print('--------------------------------------------------------------')
    print('Information about %s' %cls)
    print('--------------------------------------------------------------')

    print('Name: %s' %cls)
    print('Type: %s' %type(cls))
    print(cls.__dict__)


if __name__ ==  '__main__':
    print_about_class(Base)
    print_about_class(AnotherBase)