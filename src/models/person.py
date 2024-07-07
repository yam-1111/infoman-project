
from ..models import db, cursor
from ..models.parser import EntityParser

class personalInformation:
    """class helper for the personal_information table

    Args:
        **kwargs : dict : key value pairs of the entity (optional)
    """
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def insert(self, query = None):
        """
        inserts value to the database

        Args:
            query : str : the sql query to be executed


        Returns : None
        """
        
        # convert the value into sql variable naming
        sql_dict = EntityParser(**self.__dict__).sqlParse()
        columns = ', '.join(sql_dict.keys())
        placeholders = ', '.join(['%s'] * len(sql_dict))
        sql = f"INSERT INTO personal_information ({columns}) VALUES ({placeholders})"

        # insert the values to the database, if there is an error raise an exception
        try:
            cursor.execute(sql, list(sql_dict.values()))
            db.commit()
        except:
            db.rollback()
             # send the error to calling function
            raise

    def update(self, query_condition : str):
        """
        Updates value in the database.

        Args:
            query : str : the SQL query to be executed (not used in this implementation)
            query_condition : str : the SQL condition for updating specific rows (i.e., "CSC_ID_No = <value>")

        Returns : None
        """
        
        # Convert the value into SQL variable naming
        sql_dict = EntityParser(**self.__dict__).sqlParse()
        
        # Create the SET part of the SQL query, only include non-empty values
        set_clause = ', '.join([f"{key} = %s" for key, value in sql_dict.items() if value != ""])
        values = [value for value in sql_dict.values() if value != ""]

        # Formulate the final SQL query
        sql = f"UPDATE personal_information SET {set_clause} WHERE {query_condition}"
        print(f"SQL: {sql}\n\nValues: {values}")
        # Update the values in the database, if there is an error raise an exception
        try:
            cursor.execute(sql, values)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e

    def fetchone(self, query = 'SELECT * FROM personal_information WHERE CSC_ID_No = %s', query_args = ()):
        """
        fetches one value from the database

        Args:
            query : str : the sql query to be executed  
            query_args : tuple : query value to pass to the query

        Returns: 
            json : fetched value as json with html format

        Usage:
            personalInformation().fetchone(
                query="SELECT * FROM personal_information WHERE Email_Address = %s OR Date_Of_Birth = %s",
                query_args= <email_address>, <date_of_birth>)
            )
        """
        try:
            # fetch one value from the personal_information table
            cursor.execute(query, query_args)
            fetched_row = cursor.fetchone()

            # return a html json formatted value
            parser = EntityParser()
            col_name = parser.get_column_names('personal_information')
            return EntityParser().sqlTupleToJson(col_name, fetched_row)
        except Exception as e:
            print(str(e))
            return {}
        

    def fetch(self, query = 'SELECT * FROM personal_information', query_args = (), query_limit=None):
        """
        fetches all values from the database

        Args:
            query : str : the sql query to be executed  
            query_args : tuple : the arguments to be passed to the query
            query_limit : int : the limit of the query (default : None)

        Returns : 
            json : fetched value as json with html format

        Usage:
            personalInformation().fetch(query_limit=<value>|None)
        """
        
        # fetch all the values from the personal_information table\
        try:
            if query_limit:
                query += f' LIMIT {query_limit}'
            cursor.execute(query, query_args)
            fetched_rows = cursor.fetchall()

            # return a html json formatted value
            parser = EntityParser()
            col_name = parser.get_column_names('personal_information')
            return [EntityParser().sqlTupleToJson(col_name, row) for row in fetched_rows]
        
        except Exception as e:
            print(str(e))
            return {}
