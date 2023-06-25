
from django.contrib.auth.models import (
    BaseUserManager
)
# TODO здесь должен быть менеджер для модели Юзера.
# TODO Поищите эту информацию в рекомендациях к проекту
class UserManager(BaseUserManager):
    pass
from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserRoles(models.TextChoices):

    USER = 'user'
    ADMIN = 'admin'


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone, role=UserRoles.USER, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role=role
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, phone, role=UserRoles.ADMIN, password=None):

        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            role=role
        )

        user.save(using=self._db)
        return user

# from django.contrib.auth.models import (
#     BaseUserManager
# )
# # TODO здесь должен быть менеджер для модели Юзера.
# # TODO Поищите эту информацию в рекомендациях к проекту
# class UserManager(BaseUserManager):
#     pass