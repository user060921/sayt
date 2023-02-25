from django.db import models


class About(models.Model):
    description = models.TextField(null=True)

class ContactUs(models.Model):
    fullname=models.CharField(max_length=100, verbose_name='F.I.O')
    email=models.EmailField()
    subject=models.TextField(max_length=250)

class  Clients(models.Model):
    cover_img=models.ImageField(upload_to='clients',blank=True,null=True)
    description=models.TextField(null=True)
    title = models.CharField(max_length=255)


class Studio(models.Model):
    title = models.CharField(max_length=255)

    def str(self):
        return f"{self.title}"