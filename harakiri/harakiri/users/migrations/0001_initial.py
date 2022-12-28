# Generated by Django 4.1.3 on 2022-11-24 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified", models.DateTimeField(auto_now=True, db_index=True)),
                ("email", models.EmailField(max_length=256, unique=True, verbose_name="Email")),
                ("is_active", models.BooleanField(default=True, verbose_name="Is Active")),
                ("is_staff", models.BooleanField(db_index=True, default=False, verbose_name="Is Staff")),
                ("is_superuser", models.BooleanField(db_index=True, default=False, verbose_name="Is Superuser")),
                ("first_name", models.CharField(blank=True, default="", max_length=64, verbose_name="First Name")),
                ("last_name", models.CharField(blank=True, default="", max_length=64, verbose_name="Last Name")),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Users",
                "ordering": ["-modified"],
            },
        ),
    ]
