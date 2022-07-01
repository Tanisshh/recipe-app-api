""" django command for waiting for database """

from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2Error
import time
from django.db.utils import OperationalError


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('waiting for database')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database Unavailable .wait 1 sec')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available'))

"""another Solution"""
# import time
# from django.db import connection
# from django.db.utils import OperationalError
# from django.core.management.base import BaseCommand
#
# class Command(BaseCommand):
#     """Django command that waits for database to be available"""
#
#     def handle(self, *args, **options):
#         """Handle the command"""
#         self.stdout.write('Waiting for database...')
#         db_conn = None
#         while not db_conn:
#             try:
#                 connection.ensure_connection()
#                 db_conn = True
#             except OperationalError:
#                 self.stdout.write('Database unavailable, waiting 1 second...')
#                 time.sleep(1)
#
#         self.stdout.write(self.style.SUCCESS('Database available!'))
