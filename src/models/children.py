from ..models import db, cursor
from ..models.parser import EntityParser
from ..models.constants import CHILDREN_PARSER_DICT 

class Children:
    """
    SQL helper for the children table
    
    Args:
        CSC_ID_No : int : the CSC_ID_No of the parent (optional : other than insert)
        fullName : str : the name of the children (optional : other than insert)
        birthDay : str : the date of birth of the children (optional : other than insert)
    """
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


    def insert(self, CSC_ID_No : int):
        """
        Inserts the children into the database.

        Args:
            CSC_ID_No : int : the CSC_ID_No of the parent
            
        Returns : None
        """
         # convert the value into sql variable naming
        sql_dict = EntityParser(**self.__dict__).sqlParse(TABLE_PARSER_DICT=CHILDREN_PARSER_DICT)
        columns = ', '.join(sql_dict.keys())
        placeholders = ', '.join(['%s'] * len(sql_dict))
        sql = f"INSERT INTO children ({columns}) VALUES ({placeholders})"

        # insert the values to the database, if there is an error raise an exception
        print(f"SQL: {sql}\n\nValues: {list(sql_dict.values())}")
        try:
            cursor.execute(sql, list(sql_dict.values()))
            db.commit()
        except:
            db.rollback()
             # send the error to calling function
            raise

    def update(self, query_condition: str):
        """
        Updates value in the database.

        Args:
            query_condition : str : the SQL condition for updating specific rows (i.e., "Children_ID = <value>")

        Returns : None
        """
        # Convert the value into SQL variable naming
        sql_dict = EntityParser(**self.__dict__).sqlParse(TABLE_PARSER_DICT=CHILDREN_PARSER_DICT)

        # Create the SET part of the SQL query, only include non-empty values
        set_clause = ', '.join([f"{key} = %s" for key, value in sql_dict.items() if value != ""])
        values = [value for value in sql_dict.values() if value != ""]

        # Formulate the final SQL query
        sql = f"UPDATE children SET {set_clause} WHERE {query_condition}"
        print(f"CHILDREN SQL: {sql}\n\nValues: {values}")
        # Update the values in the database, if there is an error raise an exception
        try:
            cursor.execute(sql, values)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e

    def fetchone(self, query='SELECT * FROM children WHERE CSC_ID_No = %s', query_args=()):
        """
        Fetches one value from the database

        Args:
            query : str : the SQL query to be executed  
            query_args : tuple : query value to pass to the query

        Returns: 
            json : fetched value as json with html format

        Usage:
            Children().fetchone(
                query="SELECT * FROM children WHERE fullName = %s",
                query_args= <fullName>
            )
        """
        try:
            # fetch one value from the children table
            cursor.execute(query, query_args)
            fetched_row = cursor.fetchone()

            # return a html json formatted value
            parser = EntityParser()
            col_name = parser.get_column_names('children')
            return EntityParser().sqlTupleToJson(col_name, fetched_row, TABLE_PARSER_DICT=CHILDREN_PARSER_DICT)
        except Exception as e:
            print(str(e))
            return {}

    def fetch(self, query='SELECT * FROM children', query_args=(), query_limit=None):
        """
        Fetches all values from the database

        Args:
            query : str : the SQL query to be executed  
            query_args : tuple : the arguments to be passed to the query
            query_limit : int : the limit of the query (default : None)

        Returns : 
            json : fetched value as json with html format

        Usage:
            Children().fetch(query_limit=<value>|None)
        """
        try:
            if query_limit:
                query += f' LIMIT {query_limit}'
            cursor.execute(query, query_args)
            fetched_rows = cursor.fetchall()

            # return a html json formatted value
            print(f"\n\n\nFETCHED ROWS: {fetched_rows}  \n\n\n")
            parser = EntityParser()
            col_name = parser.get_column_names('children')
            json_rows =  [EntityParser().sqlTupleToJson(col_name, row, TABLE_PARSER_DICT=CHILDREN_PARSER_DICT) for row in fetched_rows]
            return json_rows

        except Exception as e:
            print(str(e))
            return {}

    def count(self):
        """
        Counts the number of rows in the children table

        Returns: 
            int : the number of rows in the children table
        """
        cursor.execute('SELECT COUNT(*) FROM children')
        return cursor.fetchone()[0]

    def delete(self, query_condition: str):
        """
        Deletes a row in the children table.

        Args:
            query_condition : str : the SQL condition for deleting specific rows (i.e., "Children_ID = <value>")

        Returns : None
        """
        sql = f"DELETE FROM children WHERE {query_condition}"
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
        

    def count(self):
        """
        Counts the number of rows in the children table

        Returns: 
            int : the number of rows in the children table
        """
        cursor.execute('SELECT COUNT(*) FROM children')
        return cursor.fetchone()[0]
