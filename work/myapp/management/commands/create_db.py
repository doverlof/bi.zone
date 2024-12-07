# from django.core.management.base import BaseCommand
# from django.core.management import call_command
# import psycopg2


# class Command(BaseCommand):
#     help = "Create a new database (and optionally a test database) and apply migrations"

#     def handle(self, *args, **kwargs):
#         # Main database details
#         main_database_name = "mydb"
#         test_database_name = "test_mydb"
#         conn_params = {
#             "user": "myuser",
#             "password": "mypassword",
#             "host": "localhost",  # Replace with "db" if using Docker
#             "port": "5432",
#         }

#         self._create_database(conn_params, main_database_name, is_test=False)
#         self._create_database(conn_params, test_database_name, is_test=True)

#         # Apply migrations to both databases
#         call_command("migrate", database="default")  # Main database
#         self.stdout.write("Applied migrations to the main database.")
#         call_command("migrate", database="test")  # Test database
#         self.stdout.write("Applied migrations to the test database.")

#     def _create_database(self, conn_params, database_name, is_test=False):
#         """Helper method to create the database."""
#         with psycopg2.connect(
#             **conn_params, dbname="postgres", autocommit=True
#         ) as conn:
#             with conn.cursor() as cur:
#                 # Drop existing database
#                 cur.execute(
#                     f"SELECT pg_terminate_backend(pid) "
#                     f"FROM pg_stat_activity WHERE datname = '{database_name}'"
#                 )
#                 cur.execute(f"DROP DATABASE IF EXISTS {database_name}")
#                 # Create a new database
#                 cur.execute(f"CREATE DATABASE {database_name}")
#                 self.stdout.write(
#                     self.style.SUCCESS(
#                         f"Database '{database_name}' created successfully!"
#                     )
#                 )
