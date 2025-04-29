from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

STATUS_WORKING = (
    ("working", "Working"),
    ("notworking", "Not Working"),
)

ROLE_CHOICES = (
    ("mentor", "Mentor"),
    ("mentee", "Mentee"),
)


class UserProfile(AbstractUser):
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="mentee")

    @property
    def mentorship_count(self):
        return self.mentorships.count()

    @property
    def mentees(self):
        return self.menteeships.all()  # Add this


class CoMentor(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("name", "user")

    def __str__(self):
        return self.name


# Image size validation function
def validate_image_size(image):
    max_size = 2 * 1024 * 1024  # 2 MB
    if image.size > max_size:
        raise ValidationError(
            "The image file is too large. Maximum size allowed is 5 MB."
        )


class Mentorship(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to="profile", null=True, blank=True)
    company = models.CharField(max_length=50)
    status = models.CharField(
        max_length=20,
        choices=STATUS_WORKING,
        default="working",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="mentorships",  # If mentor is deleted, set to NULL
    )  # If mentor is deleted, set to NULL
    comentor = models.ForeignKey(
        CoMentor, null=True, blank=True, on_delete=models.SET_NULL
    )  # If co-mentor is deleted, set to NULL
    content = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    mentees = models.ManyToManyField(  # Change to ManyToManyField
        settings.AUTH_USER_MODEL,  # ✅ Correct setting
        related_name="menteeships",  # related name for mentees
        blank=True,
    )
