from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from harakiri.core.models import BaseModel
from harakiri.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField("Email", unique=True, max_length=256)
    is_active = models.BooleanField("Is Active", default=True)
    is_staff = models.BooleanField("Is Staff", default=False, db_index=True)
    is_superuser = models.BooleanField("Is Superuser", default=False, db_index=True)

    # metadata
    first_name = models.CharField("First Name", max_length=64, default="", blank=True)
    last_name = models.CharField("Last Name", max_length=64, default="", blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list[str] = []

    class Meta:
        app_label = "users"
        verbose_name_plural = "Users"
        ordering = ["-modified"]

    def __str__(self) -> str:
        return f"{self.get_full_name()} (user {self.id})"

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self) -> str:
        return self.email

    def has_perm(self, perm, obj=None) -> bool:
        return self.is_superuser

    def has_module_perms(self, app_label) -> bool:
        return self.is_superuser
