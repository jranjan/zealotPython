CHECKPOINT_STATE = ['ZOMBIE', 'STARTED', 'DONE']

Checkpoint = [
    {
        'account_name': 'account_1',
        'state': 'ZOMBIE',
        'count': 0,
        'containers': [
            {
                'container_name': 'container_1',
                'state': 'ZOMBIE',
                'count': 0,
                'objects': [
                    {
                        'start_label': 'A',
                        'state': 'ZOMBIE',
                        'count': 0
                    },
                    {
                        'start_label': 'B',
                        'state': 'ZOMBIE',
                        'count': 0
                    },
                    {
                        'start_label': 'C',
                        'state': 'ZOMBIE',
                        'count': 0
                    }

                ]
            },
            {
                'container_name': 'container_1',
                'state': 'ZOMBIE',
                'count': 0,
                'objects': [
                    {
                        'start_label': 'X',
                        'state': 'ZOMBIE',
                        'count': 0
                    }
                ]
            }
        ]
    },
]


"""
Checkpoint = {
    'state': 'START',
    'state_reference_count': 1
}

AccountMark = {
    'name': 'myaccount',
    'checkpoint': Checkpoint()
}

Container = {
    'name': 'mycontainer',
    'parent_account': 'myaccount',
    'checkpoint': Checkpoint(),
    'object_checkpoints': list()
}

Objects = {
    'labels': 'A',
    'parent_container': 'mycontainer',
    'checkpoint': Checkpoint()
}
"""