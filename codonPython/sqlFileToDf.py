

def openSqlFile(path: str) -> str:
    '''
    Opens a SQL script stored at "path", and returns the contents as a string
    :param path: str - the path where the SQL script is located
    :return sql_string: str - the SQL code contained in the SQL script file, returned as a string.
        error: string - the error which occured during the reading of the SQL script
    '''

    with open(path, 'r') as query:
                sql_string = query.read()

    return sql_string