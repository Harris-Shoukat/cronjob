from zoneinfo import ZoneInfo

from django.core.management.base import BaseCommand

from scheduler.models import DateRecord, ConversionState


class Command(BaseCommand):

    help = "Convert 10 records every 5 minutes"

    def handle(self, *args, **kwargs):

        state, _ = ConversionState.objects.get_or_create(id=1)

        batch_size = 10

        start = state.batch * batch_size
        end = start + batch_size

        records = DateRecord.objects.order_by("id")[start:end]

        if state.direction == "PST_TO_UTC":

            for record in records:
                record.datetime_value = record.datetime_value.astimezone(
                    ZoneInfo("UTC")
                )
                record.timezone = "UTC"
                record.save()

            self.stdout.write(
                self.style.SUCCESS(
                    f"Converted IDs {start+1}-{end} PST -> UTC"
                )
            )

        else:

            for record in records:
                record.datetime_value = record.datetime_value.astimezone(
                    ZoneInfo("Asia/Karachi")
                )
                record.timezone = "PST"
                record.save()

            self.stdout.write(
                self.style.SUCCESS(
                    f"Converted IDs {start+1}-{end} UTC -> PST"
                )
            )

        state.batch += 1

        if state.batch == 10:
            state.batch = 0

            if state.direction == "PST_TO_UTC":
                state.direction = "UTC_TO_PST"
            else:
                state.direction = "PST_TO_UTC"

        state.save()