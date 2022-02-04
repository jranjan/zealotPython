def diff_two_dict():
    print("---------------- Begin of %s -----------------" % (diff_two_dict))
    d1 = {
             'C01': '2014', 'C02': '2015', 'C03': '2016',
             'C04': '2017', 'C05': '2018', 'C06': '2019',
             'C07': '2020', 'C08': '2021', 'C09': '2022',
             'C10': '2023', 'C11': '2024', 'C12': '2025'
    }
    d2 = {
        'C01': '2014', 'C02': '2015', 'C03': '2016'
    }
    print d1
    diff = list(set(d1.keys())-set(d2.keys()))
    diff.sort()
    print('Upcoming classes...')
    for key in diff:
        print(d1[key])
    print("---------------- End of %s -----------------\n" % (diff_two_dict))

def zip_list_to_dict():
    print("---------------- Begin of %s -----------------" % (zip_list_to_dict))
    keys = [1,2,3]
    values = [1,4,9]
    d = dict(zip(keys, values)) # Note: convert tuple from zipped list() to dict()
    print d
    print("---------------- End of %s -----------------\n" % (zip_list_to_dict))


def main():
    diff_two_dict()
    zip_list_to_dict()

if __name__ ==  '__main__':
    main()
