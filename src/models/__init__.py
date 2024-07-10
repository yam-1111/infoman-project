import mysql.connector as mysql
from os import getenv, path, listdir


def create_db():
     schema_folder = '/home/vee/personal/infoman-project/src/models/schemas'
     for filename in listdir(schema_folder):
        if filename.endswith('.sql'):
            sql_file_path = path.join(schema_folder, filename)
            with open(sql_file_path, 'r') as file:
                schema_sql = file.read()
            
            # Execute the SQL commands
            if schema_sql.strip():  # Check if the file content is not blank
                print(f'Executing SQL file: {sql_file_path}')
                for command in schema_sql.split(';'):
                    command = command.strip()
                    if command:  # Execute non-empty commands
                        cursor.execute(command)
                        



db = mysql.connect(
    host = getenv('DB_HOST'),
    user = getenv('DB_USERNAME'),
    password = getenv('DB_PASSWORD'),
    database = getenv('DB_NAME')
)

cursor = db.cursor(buffered=True)
create_db()
