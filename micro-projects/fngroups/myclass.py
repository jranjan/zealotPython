def start():
    print('start')


def stop():
    print('stop')


def status():
    print('status')

my_plays = {
    'start': start,
    'stop': stop,
    'status': status
}


def run_fns():
    for fn in my_plays.keys():
        print('Running %s' %fn)
        my_plays[fn]()
