from django.contrib.auth.models import AbstractUser
from django.db import models

USER_ROLE_VALUE = 'user'
MODERATOR_ROLE_VALUE = 'moderator'
ADMIN_ROLE_VALUE = 'admin'

ROLE_CHOICES = [
    (USER_ROLE_VALUE, 'Пользователь'),
    (MODERATOR_ROLE_VALUE, 'Модератор'),
    (ADMIN_ROLE_VALUE, 'Администратор'),
]


class User(AbstractUser):
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Роль',
        choices=ROLE_CHOICES,
        max_length=50,
        default=USER_ROLE_VALUE,
    )
    email = models.EmailField(
        unique=True,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def is_moderator(self):
        return self.role == MODERATOR_ROLE_VALUE

    @property
    def is_admin(self):
        return self.role == ADMIN_ROLE_VALUE or self.is_superuser
