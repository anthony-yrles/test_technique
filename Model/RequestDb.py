from Model.Db import Db
'''
RequestDb class is a class that is responsible for handling the requests to the database.
It has methods for creating, reading, updating, and deleting data from the database.
It uses the Db class to establish a connection to the database and execute queries.
'''

class RequestDb:
    def __init__(self):
        self.__db = Db(host="localhost", user="root", password="SKenan30mg/", database="test_technique")

    def create(self, table, data):
        '''
        Create a record in the database
        '''
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.__db.executeQuery(query, tuple(data.values()))


    def read(self, table, conditions=None):
        '''
        Read records from the database
        '''
        query = f"SELECT * FROM {table}"
        if conditions:
            query += f" WHERE {conditions}"
        print(query)
        return self.__db.fetch(query)


    def update(self, table, data, conditions=None):
        '''
        Update records in the database
        '''
        set_clause = ', '.join([f"{key} = %s" for key in data.keys()])
        query = f"UPDATE {table} SET {set_clause}"
        if conditions:
            query += f" WHERE {conditions}"
        self.__db.executeQuery(query, tuple(data.values()))


    def delete(self, table, conditions):
        '''
        Delete records from the database
        '''
        query = f"DELETE FROM {table} WHERE {conditions}"
        self.__db.executeQuery(query)