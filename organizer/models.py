import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
        default=None, null=True)
    project_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    done_flag = models.BooleanField(default=False)

    def __str__(self):
        return self.project_name

    def num_active_tasks(self):
        return self.task_set.filter(done_flag=False) \
                            .exclude(snooze_date__date=timezone.now().date()) \
                            .count()


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
        default=None, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
        default=None, null=True)
    task_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    done_flag = models.BooleanField(default=False)
    due_date = models.DateTimeField('date completed', default=None, null=True)
    repeat = models.CharField(max_length=200, default=None, null=True)
    snooze_date = models.DateTimeField('date snoozed', default=None, null=True)
    priority = models.CharField(
        'priority',
        max_length=1,
        choices = (('A', 'High'), ('B', 'Normal'), ('C', 'Low')),
        default = 'B'
    )

    def num_active_comments(self):
        return self.comment_set.filter(status_flag=True).count()

    def __str__(self):
        return self.task_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def overdue(self):
        return self.due_date < timezone.now() if self.due_date else False

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
        default=None, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    comment_text = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)
    status_flag = models.BooleanField(default=True) # True = active, False=hidden
    last_edit_date = models.DateTimeField('last edit date', default=None, null=True)
