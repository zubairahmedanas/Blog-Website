from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("User must be set")
        if not email:
            raise ValueError("email must be set")
        if not password:
            raise ValueError("password must be set")
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            password=password
                     ** extra_fields
        )
        user.set_password(password)
        user.save()

    def create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_super', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff will be true for superuser')
        if extra_fields.get('is_super') is not True:
            raise ValueError('is_super will be true for superuser')

        user = self.create_user(
            username = username,
            email=email,
            password=password,
            **extra_fields
        )
        return user
