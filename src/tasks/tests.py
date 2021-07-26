from django.test import TestCase
from .models import Task
import datetime
import pytz
# Create your tests here.


class TaskTestCase(TestCase):

    def setUp(self):
        user = 1
        # unaware = datetime.datetime(2011, 8, 15, 8, 15, 12, 0)
        # aware = datetime.datetime(2011, 8, 15, 8, 15, 12, 0, pytz.UTC)
        # a = datetime.datetime('2006-10-25 14:30')
        t1 = Task.objects.create(availability='2006-10-25 14:30', name_id=user)
        # t1 = Task.objects.create(availability=a, name_id=user)

    def test_task(self):

        no_user = 0
        # task = Task.objects.get(pk=self.t1.id)
        t = Task.objects.filter(pk=self.t1.id).count()
        # self.assertNotEqual(task.pk, no_user)
        self.assertNotEqual(t, no_user)


