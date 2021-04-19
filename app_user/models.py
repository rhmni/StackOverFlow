from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from app_tag.models import Tag


class MyUserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not email:
            raise ValueError('Users must have a name')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(
            email=email,
            password=password,
            name=name,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=250, unique=True)
    name = models.CharField(max_length=200)
    skills = models.ManyToManyField(Tag, related_name='users', blank=True)
    join_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser
