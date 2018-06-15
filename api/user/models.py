from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=UserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):

        user = self.create_user(username, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):
    username = models.CharField(max_length=18, verbose_name=u'用户名', unique=True)
    email = models.EmailField(verbose_name=u'邮箱')
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'用户名字')
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name
