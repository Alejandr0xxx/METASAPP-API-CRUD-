from django.db import models


class Objectives(models.Model):
    FREQUENCY_STATUS = [
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
        ('Yearly', 'Yearly'),
    ]

    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField(null=True)
    details = models.TextField()
    events = models.IntegerField()
    icon = models.TextField(null=True)
    objective_num = models.IntegerField(null=True)
    deadline = models.DateField()
    completed_times = models.IntegerField(default=0)
    completed_times_bef = models.IntegerField(default=0)
    is_completed_bef = models.BooleanField(default=False)
    frequency = models.CharField(max_length=7,choices=FREQUENCY_STATUS)

    class Meta:
        db_table = 'objectives'
