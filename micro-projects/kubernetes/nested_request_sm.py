class Request(object):
    def __init__(self, parent, receiver, callback):
        self.current_state = None
        self.prev_state = None
        self.child = None
        self.parent = parent
        self.receiver = receiver
        self.callback = callback

    def set_child_request(self, r):
        print("child = %s" % (r))
        self.child = r

    def execute(self, r):
        r.receiver.set_start_state(r)
        r.receiver.start_sm(r)


class HttpAuthorizeNode(Request):
    def __init__(self, parent, receiver, callback):
        super(HttpAuthorizeNode, self).__init__(parent, receiver, callback)


class PF9AuthorizeNode(Request):
    def __init__(self, parent, receiver, callback):
        super(PF9AuthorizeNode, self).__init__(parent, receiver, callback)


class Receiver(object):
    def __init__(self, next_r):
        self.next_r = next_r

    def set_start_state(self, r):
        pass

    def start_sm(self, r):
        while (r.current_state != None):
            response = r.current_state(r)
            if response == 1 and r.child != None:
                r.child.execute(r.child)


class HttpServiceReceiver(Receiver):
    def __init__(self, next_r):
        super(HttpServiceReceiver, self).__init__(next_r)

    def set_start_state(self, r):
        r.prev_state = None
        r.current_state = self.s1

    def s1(self, r):
        print("s1")
        r.prev_state = r.current_state
        r.current_state = self.s2

    def s2(self, r):
        print("s2")
        print("." * 79)
        print("Steps:")
        print("Create child request")
        print("Set next state as callback when child request gets completed")
        print("Wait for child request to processed")
        print("Change prev_state and current_state accordingly")
        print("Callback:%s" % (self.s3))
        pf9_r = PF9AuthorizeNode(r, r.receiver.next_r, self.s3)
        print("pf9_r = %s" % (pf9_r))
        print("Child request callback:%s" % (pf9_r.callback))
        r.set_child_request(pf9_r)
        r.prev_state = r.current_state
        r.current_state = self.s3
        return 1

    def s3(self, r):
        print("s3")
        print("Child request %s is done" % (r.child))
        r.prev_state = r.current_state
        r.current_state = None
        print("Calling callback of %s=" % (r))
        print("-" * 79)
        r.callback(r)


class PF9Receiver(Receiver):
    def __init__(self, next_r):
        super(PF9Receiver, self).__init__(next_r)

    def set_start_state(self, r):
        r.prev_state = None
        r.current_state = self.p1

    def p1(self, r):
        print("p1")
        r.prev_state = r.current_state
        r.current_state = self.p2

    def p2(self, r):
        print("p2")
        r.prev_state = r.current_state
        r.current_state = self.p3

    def p3(self, r):
        print("p3")
        r.prev_state = r.current_state
        r.current_state = self.p4

    def p4(self, r):
        print("p4")
        r.prev_state = r.current_state
        r.current_state = self.p5

    def p5(self, r):
        print("p5")
        r.prev_state = r.current_state
        r.current_state = self.p6

    def p6(self, r):
        print("p6")
        r.prev_state = r.current_state
        r.current_state = None
        print("r = %s" % (r))

        print("." * 79)
        if r.parent != None:
            print("Calling parent callback. %s" % (r.callback))
            print("parent = %s" % (r.parent))
            r.callback(r.parent)


def dummy_callback(r):
    print("Manager callback is here!")


if __name__ == "__main__":
    R2 = PF9Receiver(None)
    R1 = HttpServiceReceiver(R2)
    r = HttpAuthorizeNode(None, R1, dummy_callback)
    r.execute(r)