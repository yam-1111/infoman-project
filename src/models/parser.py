from ..models import db, cursor
from ..models.constants import (
    PERSONALINFO_PARSER_DICT,
    CHILDREN_PARSER_DICT,
    EDUCATION_PARSER_DICT,
)


class EntityParser:
    """
    helper class for parsing the entity

    Args:
        **kwargs : dict : key value pairs of the entity (optional)
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    # helper function for the entity parser
    def get_column_names(self, TABLE_NAME: str):
        """
        Helper function for the entity parser

        Args:
            TABLE_NAME : str : table name to get the columns from sql

        Returns:
            columns : list : list of columns in the table
        """
        cursor.execute(f"SHOW COLUMNS FROM {TABLE_NAME}")
        columns = [row[0] for row in cursor.fetchall()]
        print(columns)
        return columns

    # parser for the entity
    def jsonParse(self, TABLE_PARSER_DICT=PERSONALINFO_PARSER_DICT):
        """
        converts the given sql variable to the
        html json equivalent

        Returns:
            sql_dict : dict : json formatted in sql name variable
        """
        json_dict = {}

        # reversing the PERSONALINFO_PARSER_DICT to convert the sql variable to json variable
        json_to_sql = {v: k for k, v in TABLE_PARSER_DICT.items()}

        for key, value in self.__dict__.items():
            print(f"key: {key}, value: {value}")

            if key in json_to_sql:
                json_key = json_to_sql[key]
                json_dict[json_key] = value

        return json_dict

    def sqlParse(self, TABLE_PARSER_DICT=PERSONALINFO_PARSER_DICT):
        """
        converts the given json variable to sql variable naming

        Returns:
            sql_dict : dict : json formatted in sql name variable
        """
        sql_dict = {}
        for key, value in self.__dict__.items():
            if key in TABLE_PARSER_DICT:
                sql_key = TABLE_PARSER_DICT.get(key)
                sql_dict[sql_key] = value
        return sql_dict

    def sqlTupleToJson(
        self,
        sql_column_list: list,
        sql_tuple: tuple,
        TABLE_PARSER_DICT=PERSONALINFO_PARSER_DICT,
    ):
        """
        Converts the given SQL tuple to the
        HTML JSON equivalent.

        Args:
            sql_column_list : list : column names of the SQL table
            sql_tuple : tuple : tuple containing the SQL values

        Returns:
            json_dict : dict : JSON formatted in HTML JSON name variable
        """

        json_dict = {}
        json_to_sql = {v: k for k, v in TABLE_PARSER_DICT.items()}

        print(f"sql_column_list: {sql_column_list}\nsql_tuple: {sql_tuple}")

        for column, value in zip(sql_column_list, sql_tuple):
            if column in json_to_sql:

                # filter by date columns
                if column in [
                    "Date_Of_Birth",
                    "Education_Start",
                    "Education_End",
                    "Year_Graduated",
                    "Children_Date_of_Birth",
                ]:
                    json_dict[json_to_sql[column]] = (
                        str(value) if value is not None else ""
                    )
                else:
                    json_dict[json_to_sql[column]] = value if value is not None else ""

        return json_dict
