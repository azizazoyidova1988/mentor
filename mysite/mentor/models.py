from django.db import models


class About(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.CharField(max_length=650, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Trainer(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    job = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=650, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Courses(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.CharField(max_length=650, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    price = models.IntegerField(blank=False, null=False, default=0)
    trainer = models.ForeignKey(Trainer, blank=False, null=True, on_delete=models.SET_NULL)
    time = models.CharField(max_length=150, blank=True, null=True)
    available_seats = models.IntegerField(blank=False, null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Resources(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=650, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    author = models.CharField(max_length=250, blank=True, null=True)
    views = models.IntegerField(blank=True, null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Events(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.CharField(max_length=850, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    time = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment_Writers(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    job = models.CharField(max_length=100, blank=False, null=False)
    message = models.TextField(max_length=350, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Students(models.Model):
    full_name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    subject = models.CharField(max_length=150, blank=False, null=False)
    message = models.CharField(max_length=450, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
