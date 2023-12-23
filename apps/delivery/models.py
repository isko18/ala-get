from django.db import models
from django.utils.text import slugify

from django.urls import reverse

# Create your models here.
class Delivery(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок доставки',
        blank=True, null=True
    )
    descriptions = models.TextField(
        verbose_name='Описание доставки',
        blank=True, null=True
    )
    banner_image = models.ImageField(
        upload_to='image/',
        verbose_name="Фото баннера",
        blank=True, null=True
    )
    trust_title = models.CharField(
        max_length=255,
        verbose_name='Заголовок доверие'
    )
    trust_descriptions = models.TextField(
        verbose_name='Описание доверие'
    )
    trust_descriptions2 = models.TextField(
        verbose_name='Описание доверие №2'
    )
    trust_image = models.ImageField(
        upload_to='image/',
        verbose_name='фото'
    )
    slug = models.SlugField( 
        max_length=255,
        unique=True,
        db_index=True,
        blank=True, null=True
        )

    def get_absolute_url(self):
        return reverse('index',  kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.title) if self.title else ""
    
    class Meta:
        verbose_name = 'Найстрока страницы доставка'
        verbose_name_plural = 'Найстрока страницы доставка'


class Favorabledelivery(models.Model):
    title_base = models.CharField(
        max_length=255,
        verbose_name="Заголовок Приложение для выгодной доставки",
        blank=True, null=True
    )
    title = models.CharField(
        max_length=255,
        verbose_name="заголовок",
        blank=True, null=True
    )
    descriptions = models.TextField(
        verbose_name="описание"
    )

    image = models.ImageField(
        upload_to="image/",
        blank= True, null=True
    )
    slug = models.SlugField( 
        max_length=255,
        unique=True,
        db_index=True,
        blank=True, null=True
        )

    def get_absolute_url(self):
        return reverse('index',  kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.title) if self.title else ""
    
    class Meta:
        verbose_name = 'Приложение для выгодной доставки'
        verbose_name_plural = 'Приложение для выгодной доставки'

