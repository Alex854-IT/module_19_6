from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['username']

    def __str__(self):
        return self.email

class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=2, max_digits=9)
    size = models.DecimalField(decimal_places=2, max_digits=5)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    user = models.ManyToManyField(User, related_name='games')

    def __str__(self):
        return self.title



class mydatabase(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


#python manage.py makemigrations
#python manage.py migrate