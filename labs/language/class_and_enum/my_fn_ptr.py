
class  Provider:
    def help(self, **kwargs):
        print("help...")
        for k, v in kwargs.iteritems():
            print "%s = %s" % (k, v)

    def how_do_you_do(self, **kwargs):
        print("I am fine...")
        for k, v in kwargs.iteritems():
            print "%s = %s" % (k, v)

def hello_world():
    print('hello')

callers = {
    'c1': Provider.help,
    'c2': Provider.how_do_you_do,
}



if __name__ == "__main__":
    mp = Provider()
    for k in callers.keys():
        if callers[k] == Provider.how_do_you_do:
            callers[k](mp, a=3)
        else:
            callers[k](mp, a=3, b=99)
