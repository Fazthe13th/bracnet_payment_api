from django.db import models


class bKash_Onboarding(models.Model):
    onbording_res = models.JSONField()

    def __str__(self):
        return "Onboarding json string "+str(self.onbording_res)
