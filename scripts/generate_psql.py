import os
from dotenv import read_dotenv


env_paths = [".env", "../.env", "../../.env", "../../../.env"]

for env_path in env_paths:
    if os.path.exists(env_path):
        read_dotenv(env_path)

sql = """
CREATE USER {user} with password '{password}';
CREATE DATABASE {database} OWNER {user};
GRANT ALL PRIVILEGES ON DATABASE {database} to {user};
"""

print(
    sql.format(
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD"),
        database=os.environ.get("POSTGRES_DB"),
    )
)
