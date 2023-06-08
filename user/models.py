from django.db import models
from django.contrib.auth.models import (UserManager, AbstractBaseUser)
from utility.models import BaseModel
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.


class MyUserManager(BaseUserManager):
    """
    Inherits: BaseUserManager class
    """

    def create_user(self, email, password=None):
        """
        Create user with given email and password.
        :param email:
        :param password:
        :return:
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        # set_password is used set password in encrypted form.
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Create and save the super user with given email and password.
        :param email:
        :param password:
        :return: user
        """
        user = self.create_user(email, password=password)
        user.is_superuser = True
        user.username = ""
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class ActiveUserManager(UserManager):
    """
        ActiveUserManager class to filter the deleted user.
    """
    def get_queryset(self):
        return super(ActiveUserManager, self).get_queryset().filter(is_active=True, is_deleted=False)


class ActiveObjectsManager(UserManager):
    """
        ActiveObjectsManager class to filter the deleted objs
    """
    def get_queryset(self):
        return super(ActiveObjectsManager, self).get_queryset().filter(is_deleted=False)


class TopAnime(BaseModel):
    """
    """
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Name of Anime")
    total_seasons = models.IntegerField(blank=True, null=True, verbose_name="Total Seasons")
    total_likes = models.IntegerField(blank=True, null=True, verbose_name="Total Likes by Users")



class User(AbstractBaseUser, BaseModel):
    """
    MyUser models used for the authentication process and it contains basic
     fields.
     Inherit : AbstractBaseUser, PermissionMixin, BaseModel
    """

    username = models.CharField(max_length=50, blank=True, null=True, verbose_name='User Name')
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='First Name')
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Last Name')
    full_name = models.CharField(max_length=120, blank=True, null=True, verbose_name='Full Name')
    email = models.EmailField(max_length=80, unique=True, blank=False, null=False, verbose_name='Email')
    phone_number = models.CharField(max_length=25, unique=False, blank=True, null=True,
                                    verbose_name='Phone Number')
    no_of_anime_watched = models.IntegerField(null=True, blank=True, verbose_name="No of Animes watched")
    is_email_verified = models.BooleanField('Email Verified', default=False)
    is_active = models.BooleanField('Active', default=True)
    is_staff = models.BooleanField('Is Staff', default=False)
    is_superuser = models.BooleanField('SuperUser', default=False)


    objects = ActiveUserManager()
    all_objects = ActiveObjectsManager()
    all_delete_objects = UserManager()
    my_user_manager = MyUserManager()
    USERNAME_FIELD = 'email'

    def has_perm(self, perm, obj=None):
        """
        has_perm method used to give permission to the user.
        :param perm:
        :param obj:
        :return: is_staff
        """
        return self.is_staff

    def has_module_perms(self, app_label):
        """
        method to give module permission to the superuser.
        :param app_label:
        :return: is_superuser
        """
        return self.is_superuser

    def __str__(self):
        """
        :return: email
        """
        return self.email

    def get_short_name(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id']
        index_together = ["email", "phone_number", "updated_at"]