import uuid
from django.core.management.base import BaseCommand
from django.db import models
from cms.models import Project


class ProjectPK(models.Model):
    """Temporary model to bypass UUID coercion during read."""
    id = models.CharField(max_length=36, primary_key=True)

    class Meta:
        managed = False
        db_table = Project._meta.db_table


class Command(BaseCommand):
    help = "Fix malformed project UUIDs in cms_project table"

    def handle(self, *args, **options):
        bad = []
        for pid in ProjectPK.objects.values_list("id", flat=True):
            try:
                uuid.UUID(pid)
            except (ValueError, TypeError):
                new_id = str(uuid.uuid4())  # Dashed UUID format
                ProjectPK.objects.filter(id=pid).update(id=new_id)
                bad.append((pid, new_id))
        
        if bad:
            self.stdout.write(
                self.style.SUCCESS(f'Fixed {len(bad)} bad project IDs:')
            )
            for old_id, new_id in bad:
                self.stdout.write(f'  {old_id} → {new_id}')
        else:
            self.stdout.write(
                self.style.SUCCESS('No bad project IDs found. All clear!')
            )
