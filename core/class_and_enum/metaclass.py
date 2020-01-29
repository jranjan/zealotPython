class HPEMetaClass(type):
    pass


class Base(object):
    __metaclass__ = HPEMetaClass

if __name__ == '__main__':
    print(type(Base))

