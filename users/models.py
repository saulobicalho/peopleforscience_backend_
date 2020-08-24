from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    ROLE = (
        ('Consultor', 'Consultor',),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def is_consultor(self):
        if self.role == 'Consultor':
            return True
        else:
            return False

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.mode != 'RGB':
            img = img.convert('RGB')

        if img.height > 100 or img.width > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)
