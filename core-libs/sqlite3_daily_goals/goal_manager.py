import sqlite3 as lite
import sys


Person = (
  ('Jyoti', 'Jyoti Ranjan', 40),
  ('Shivam', 'Shivam Jyoti', 9)
)

Goals = (
  ('Jyoti', 001, 'Awake before 06:00 AM'),
  ('Jyoti', 002, 'Sleep before 11:00 PM'),
  ('Jyoti', 003, 'Be a listner'),
  ('Jyoti', 004, 'Do not repeat yourself'),
  ('Jyoti', 005, 'Eat helathy food'),
  ('Jyoti', 006, 'Teach kids'),

  ('Shivam', 001, 'Awake before 06:30 AM'),
  ('Shivam', 002, 'Sleep before 10:30 PM')
)


class GoalManager(object):
    def __init__(self, db):
        self.db = db
        pass

    def show_db_info(self):
        self._show_sqlite3_component_info()
        print('----------------------------------------')
        self._show_db_version_info()

    def _show_sqlite3_component_info(self):
        print('sqlite3 components are:')
        print('1. SQLite database')
        print('2. pysqlite language binding')
        print('3. the sqlite3 command line tool: make sure it is installed')
        print('version details:')
        print('SQLite database:%s' % str(lite.sqlite_version))
        print('python binding of sqlite3:%s' % str(lite.version))

    def _show_db_version_info(self):
        con = None
        try:
            con = lite.connect(self.db)
            cur = con.cursor()
            cur.execute('SELECT SQLITE_VERSION()')
            data = cur.fetchone()
            print "SQLite version: %s" % data
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.close()

    def drop_tables(self):
        con = lite.connect(self.db)
        with con:
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS Person")
            cur.execute("DROP TABLE IF EXISTS Goal")

    def create_tables(self):
        con = lite.connect(self.db)
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE Person(firstname TEXT PRIMARY KEY, fullname TEXT, age INT NOT NULL)")
            cur.execute("CREATE TABLE Goal(person_firstname TEXT, "
                        "goal INT NOT NULL, "
                        "desc TEXT, "
                        "PRIMARY KEY(person_firstname, goal), "
                        "FOREIGN KEY(person_firstname) REFERENCES Person(firstname))")
            self._populate_tables(Person, Goals)

    def _populate_tables(self, person, goals):
        con = lite.connect(self.db)
        with con:
            cur = con.cursor()
            cur.executemany("INSERT INTO Person VALUES(?, ?, ?)", person)
            cur.executemany("INSERT INTO Goal VALUES(?, ?, ?)", goals)

    def add_person(self, name, age):
        pass

    def add_goal(self, name, goals):
        pass

    def delete_goal(self, name, goal):
        pass

    def delete_person(self, name):
        pass

    def list_all_goals(self):
        con = lite.connect(self.db)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM person")
            rows = cur.fetchall()
            for row in rows:
                print('------------  Person information --------------------')
                print('Name: %s' % row[0])
                print('Full name: %s' % row[1])
                print('Age: %s' % row[2])

                cur.execute("SELECT * FROM goal")
                goals = cur.fetchall()
                print('--------------')
                print('Goals of %s are:' %row[0])
                print('--------------')
                for g in goals:
                    if g[0] == row[0]:
                        print g

    def list_goals_crude_way(self, name):
        con = lite.connect(self.db)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Goal")
            rows = cur.fetchall()
            print('Goals of %s are:' % name)
            for row in rows:
                if row[0] == name:
                    print row

    def list_goals_using_paramterized_query(self, name):
        con = lite.connect(self.db)
        with con:
            con.row_factory = lite.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM Goal WHERE person_firstname=:name", {"name": name})
            con.commit()

            rows = cur.fetchall()
            print('Goals of %s are:' % name)
            for row in rows:
                print row

    def write_data(self, data, filename):
        f = open(filename, 'w')
        with f:
            f.write(data)

    def backup_tables(self):
        con = lite.connect(self.db)
        with con:
            cur = con.cursor()
            data = '\n'.join(con.iterdump())
            self.write_data(data, 'goaldb_backup.sql')

