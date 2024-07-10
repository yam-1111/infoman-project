from ..models import db, cursor
from ..models.parser import EntityParser


class Children:
    """
    SQL helper for the children table
    
    Args:
        CSC_ID_No : int : the CSC_ID_No of the parent (optional : other than insert)
        Name_Of_Children : str : the name of the children (optional : other than insert)
        Children_Date_Of_Birth : str : the date of birth of the children (optional : other than insert)
    """
    def __init__(self, CSC_ID_No=None, Name_Of_Children=None, Children_Date_Of_Birth=None):
        self.CSC_ID_No = CSC_ID_No
        self.Name_Of_Children = Name_Of_Children
        self.Children_Date_Of_Birth = Children_Date_Of_Birth

    def insert(self, CSC_ID_No : int):
        """
        Inserts the children into the database.

        Args:
            CSC_ID_No : int : the CSC_ID_No of the parent
            
        Returns : None
        """
        sql = (
            "INSERT INTO children (CSC_ID_No, Name_of_Children, Children_Date_of_Birth) "
            "VALUES (%s, %s, %s)"
        )
        values = (CSC_ID_No, self.Name_Of_Children, self.Children_Date_Of_Birth)
        cursor.execute(sql, values)
        db.commit()

    def update(self, query_condition: str):
        """
        Updates value in the database.

        Args:
            query_condition : str : the SQL condition for updating specific rows (i.e., "Children_ID = <value>")

        Returns : None
        """
        # Convert the value into SQL variable naming
        sql_dict = EntityParser(**self.__dict__).sqlParse()

        # Create the SET part of the SQL query, only include non-empty values
        set_clause = ', '.join([f"{key} = %s" for key, value in sql_dict.items() if value != ""])
        values = [value for value in sql_dict.values() if value != ""]

        # Formulate the final SQL query
        sql = f"UPDATE children SET {set_clause} WHERE {query_condition}"
        print(f"SQL: {sql}\n\nValues: {values}")
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
                query="SELECT * FROM children WHERE Name_of_Children = %s",
                query_args= <name_of_children>
            )
        """
        try:
            # fetch one value from the children table
            cursor.execute(query, query_args)
            fetched_row = cursor.fetchone()

            # return a html json formatted value
            parser = EntityParser()
            col_name = parser.get_column_names('children')
            return EntityParser().sqlTupleToJson(col_name, fetched_row)
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
            parser = EntityParser()
            col_name = parser.get_column_names('children')
            return [EntityParser().sqlTupleToJson(col_name, row) for row in fetched_rows]

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
