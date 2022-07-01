""" Test commands for waiting for database"""


from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):

    def test_wait_for_db_ready(self, patched_check):
        """ test waiting for database if database is ready"""
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """waiting for database when getting optioanalerror"""
        patched_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])

"""another Solution"""
# from unittest.mock import patch
# from django.core.management import call_command
# from django.db.utils import OperationalError
# from django.test import TestCase
#
# class CommandsTestCase(TestCase):
#
#     def test_wait_for_db_ready(self):
#         """Test waiting for db when db is available"""
#
#         with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
#             gi.return_value = True
#             call_command('wait_for_db')
#             self.assertEqual(gi.call_count, 1)
#
#     @patch('time.sleep', return_value=None)
#     def test_wait_for_db(self, ts):
#         """Test waiting for db"""
#
#         with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
#             gi.side_effect = [OperationalError] * 5 + [True]
#             call_command('wait_for_db')
#             self.assertEqual(gi.call_count, 6)
