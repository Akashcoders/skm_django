from django.db import models

class Tpr(models.Model):
    TPR_NO=models.CharField( max_length=50)
    segment=models.CharField( max_length=50)
    customer=models.CharField( max_length=50)
    pdf_file = models.FileField(upload_to='pdfs/')


def __str__(self):
        return self.title
