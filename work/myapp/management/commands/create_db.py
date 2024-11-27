from django.core.management.base import BaseCommand
import psycopg
from django.conf import settings


class Command(BaseCommand):
    help = "Create a new database from scratch"

    def handle(self, *args, **kwargs):
        conn_params = {
            "host": settings.DATABASES["default"]["HOST"],
            "port": settings.DATABASES["default"]["PORT"],
            "user": settings.DATABASES["default"]["USER"],
            "password": settings.DATABASES["default"]["PASSWORD"],
        }
        database_name = settings.DATABASES["default"]["NAME"]

        try:
            # Подключаемся к базе 'postgres'
            with psycopg.connect(
                **conn_params, dbname="postgres", autocommit=True
            ) as conn:
                with conn.cursor() as cur:
                    # Удаляем существующую базу данных
                    cur.execute(
                        f"SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = '{database_name}'"
                    )
                    cur.execute(f"DROP DATABASE IF EXISTS {database_name}")

                    # Создаём новую базу данных
                    cur.execute(f"CREATE DATABASE {database_name}")
                    self.stdout.write(
                        self.style.SUCCESS(f"База данных '{database_name}' создана.")
                    )

            # Применяем миграции
            self.stdout.write("Применение миграций...")
            from django.core.management import call_command

            call_command("migrate")

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ошибка при создании базы данных: {e}"))
