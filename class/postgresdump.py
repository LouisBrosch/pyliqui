import os
import subprocess
class postgresDump(object):

    def __init__(self):
        self.path = ""

    def find(self):
        print("Looking for pg_dump @ standard Path...")
        self.path = 'C:/PostgreSQL/pg10/bin/'
        print("Testing...")
        try:
            print(subprocess.check_output(self.path+"pg_dump.exe"))
        except subprocess.CalledProcessError:
            print("Found...")
        except FileNotFoundError:
            print("Not found...")
            self.path = ""

    def shema(self):
        if self.path != "":
            print("Dumping Shema only...")
            os.system(self.path+"pg_dump.exe --dbname=postgresql://postgres:test$@localhost:5432/postgres -s > test.sql")
            print("Done")
            return
        print("pg_dump not found")
        



a = postgresDump()
a.find()
a.shema()