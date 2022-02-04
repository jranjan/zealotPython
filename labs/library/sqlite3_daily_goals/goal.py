from goal_manager import GoalManager


if __name__ == "__main__":
    gm = GoalManager('goal.db')
    gm.show_db_info()

    gm.drop_tables()
    gm.create_tables()

    gm.list_all_goals()

    print('--------------------------------------------')
    print('Fetching a specific person data in crude way...')
    gm.list_goals_crude_way('Jyoti')
    print('--------------------------------------------')
    print('Fetching a specific person data using parameterized query...')
    gm.list_goals_using_paramterized_query('Jyoti')
    print('--------------------------------------------')
    print('Backing up your data, see your exeuction directory')
    gm.backup_tables()
