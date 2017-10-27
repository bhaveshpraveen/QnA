from django.db import models


class QuestionAndAnswers(models.Model):
    user = models.CharField(max_length=125, help_text='Enter your User Name')
    answer = models.TextField(help_text='Your answer goes here')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {} - {}:{}:{}".format(self.user, self.answer, self.updated.hour, self.updated.minute, self.updated.second)