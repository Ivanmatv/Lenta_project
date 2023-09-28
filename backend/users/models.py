from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        UserManager)
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Имя пользователя',
        max_length=150,
        unique=True,
    )
    email = models.EmailField(
        'Электронная почта',
        max_length=254,
        unique=True,
    )
    first_name = models.CharField(
        'Имя',
        max_length=150,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
    )
    # Флаг, указывающий, активен ли пользователь.
    is_active = models.BooleanField(default=True)
    # Флаг, указывающий, является ли пользователь сотрудником.
    is_staff = models.BooleanField(default=False)
    # Флаг, указывающий, является ли пользователь администратором.
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.email