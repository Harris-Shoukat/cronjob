from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from django.core.management.base import BaseCommand

from scheduler.models import DummyUser, DateRecord


class Command(BaseCommand):

    help = "Insert Dummy Users and Datetimes"

    def handle(self, *args, **kwargs):

        for i in range(100):

            DummyUser.objects.get_or_create(

                email=f"user{i}@gmail.com",

                defaults={

                    "name": f"User {i}"

                }

            )

        pst = ZoneInfo("Asia/Karachi")

        now = datetime.now(pst)

        for i in range(100):

            DateRecord.objects.create(

                datetime_value=now + timedelta(minutes=i),

                timezone="PST"

            )

        self.stdout.write(
            self.style.SUCCESS("Completed")
        )