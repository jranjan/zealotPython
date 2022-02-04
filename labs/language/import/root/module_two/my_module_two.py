from root.module_one import my_module_one as m1

def test_module_two():
    print "module 2"

def use_module_two():
    m1.test_module_one()
