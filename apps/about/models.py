from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class About(models.Model):
    our_mission = models.CharField(
        max_length=255,
        verbose_name='Заголовок о нас ',
        blank=True, null=True
    )
    mission_descriptions = models.CharField(
        max_length=255,
        verbose_name='Описание о нас',
        blank=True, null=True
    )
    vision = models.CharField(
        max_length=255,
        verbose_name='Заголовок о нас №2',
        blank=True, null=True
    )
    vision_descriptions = models.CharField(
        max_length=255,
        verbose_name='Описание о нас №2'
    )
    banner_image = models.ImageField(
        upload_to='image/',
        verbose_name="Фото баннера",
        blank=True, null=True
    )

    slug = models.SlugField( 
        max_length=255,
        unique=True,
        db_index=True,
        blank=True, null=True
    )

    def get_absolute_url(self):
        return reverse('settings',  kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.our_mission
    
    class Meta:
        verbose_name = 'Настройка страницы о нас'
        verbose_name_plural = 'Настройки страницы о нас'


class OurMission(models.Model):
    title = models.CharField(
        max_length=255, 
        verbose_name='Заголовок',
        blank=True, null=True

    )
    descriptions = models.TextField(
        verbose_name='Описание ',
        blank=True, null=True
    )
    descriptions2 = models.TextField(
        verbose_name='Описание №2',
        blank=True, null=True
    )
    numbers = models.CharField(
        max_length=10, 
        verbose_name='Номерация',
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Фото',
        blank=True, null=True
    )

    slug = models.SlugField( 
        max_length=255,
        unique=True,
        db_index=True,
        blank=True, null=True
    )

    def get_absolute_url(self):
        return reverse('settings',  kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.title) if self.title else ""
    
    class Meta:
        verbose_name = 'Наша миссия'
        verbose_name_plural = 'Наша миссия'
