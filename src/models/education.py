
from ..models import db, cursor
from ..models.parser import EntityParser
from ..models.constants import EDUCATION_PARSER_DICT

class Education:
    """
    SQL helper for the education table

    Args:
        **kwargs : dict : the values to be inserted into the database (optional : other than insert)
    
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
        sql_dict = EntityParser(**self.__dict__).sqlParse(TABLE_PARSER_DICT=EDUCATION_PARSER_DICT)
        filtered_sql_dict = {k: v for k, v in sql_dict.items() if v not in (None, "")}
        if not filtered_sql_dict:
            raise ValueError("No valid data to insert.")
        
        columns = ', '.join(filtered_sql_dict.keys())
        placeholders = ', '.join(['%s'] * len(filtered_sql_dict))
        sql = f"INSERT INTO education ({columns}) VALUES ({placeholders})"
        print(f"EDUCATION INSERT SQL: {sql}\n\nValues: {list(filtered_sql_dict.values())}")
        # insert the values to the database, if there is an error raise an exception
        try:
            cursor.execute(sql, list(filtered_sql_dict.values()))
            db.commit()
        except:
            db.rollback()
             # send the error to calling function
            raise

    def fetchone(self, query='SELECT * FROM education WHERE CSC_ID_No = %s', query_args=()):
        """
        Fetches one value from the database

        Args:
            query : str : the SQL query to be executed  

        Returns : dict : the fetched value
        """
        try:
            cursor.execute(query, query_args)
            return cursor.fetchone()
        except Exception as e:
            raise e
    
    def fetch(self, query='SELECT * FROM education', query_args=()):
        """
        Fetches all values from the database

        Args:
            query : str : the SQL query to be executed  

        Returns : dict : the fetched value
        """

        cursor.execute(query, query_args)
        fetched_rows = cursor.fetchall()
    
        parser = EntityParser()
        col_name = parser.get_column_names('education')
        return [EntityParser().sqlTupleToJson(col_name, row, TABLE_PARSER_DICT=EDUCATION_PARSER_DICT) for row in fetched_rows]
    
    def update(self, query_condition : str):
            """
            Updates value in the database.

            Args:
                query_condition : str : the SQL condition for updating specific rows (i.e., "CSC_ID_No = <value>")

            Returns : None
            """
            
            # Convert the value into SQL variable naming
            sql_dict = EntityParser(**self.__dict__).sqlParse(TABLE_PARSER_DICT=EDUCATION_PARSER_DICT)
            
            # Create the SET part of the SQL query, only include non-empty values
            set_clause = ', '.join([f"{key} = %s" for key, value in sql_dict.items() if value != ""])
            values = [value for value in sql_dict.values() if value != ""]

            # Formulate the final SQL query
            sql = f"UPDATE education SET {set_clause} WHERE {query_condition}"
            print(f"EDUCATION SET SQL: {sql}\n\nValues: {values}")
            # Update the values in the database, if there is an error raise an exception
            try:
                cursor.execute(sql, values)
                db.commit()
            except Exception as e:
                db.rollback()
                raise e
            
    def count(self):
        """
        Counts the number of rows in the database

        Returns : int : the number of rows
        """
        cursor.execute('SELECT COUNT(*) FROM education')
        return cursor.fetchone()[0]
    
    def delete(self, query_condition: str):
        """
        Deletes a row in the children table.

        Args:
            query_condition : str : the SQL condition for deleting specific rows (i.e., "Children_ID = <value>")

        Returns : None
        """
        sql = f"DELETE FROM education WHERE {query_condition}"
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
