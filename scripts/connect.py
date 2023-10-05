# standard library
from os import environ as env


# dependencies
from dotenv import load_dotenv
from notion_client import Client


def main() -> None:
    """Test connection to the database."""
    load_dotenv()
    client = Client(auth=env["NOTION_TOKEN"])
    client.databases.query(env["DATABASE_ID"])
    print("Connected.")


if __name__ == "__main__":
    main()
