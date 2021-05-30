from django.db import models


class About(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.CharField(blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Trainer(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Courses(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.CharField(blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    price = models.IntegerField(blank=False, null=False, default=0)
    trainer = models.ForeignKey(Trainer, blank=False, null=False, on_delete=models.SET_NULL)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    available_seats = models.IntegerField(blank=False, null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Events(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.CharField(blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Students(models.Model):
    full_name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    subject = models.CharField(blank=False, null=False)
    message = models.CharField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
