def alter_dict(country_info=dict()):
    country_info['national_person'] = 'Tendulkar'


if __name__ == "__main__":
    india = dict()
    india['captial'] = 'Delhi'
    india['father_of_nation'] = 'Mahatama Gandhi'
    print('Dict before alteration..............')
    print india
    alter_dict(india)
    print('Dict after alteration..............')
    print india
