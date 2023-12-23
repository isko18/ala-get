from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Taxi(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок сайта №1',
        blank=True, null=True
    )
    title2 = models.CharField(
        max_length=255,
        verbose_name='Заголовок сайта №2',
        blank=True, null=True
    )
    descriptions = models.TextField(
        verbose_name='Описание сайта',
        blank=True, null=True
    )
    banner_image = models.ImageField(
        upload_to='image/',
        verbose_name="Фото баннера",
        blank=True, null=True
    )
    advantage1 = models.CharField(
        max_length=255,
        verbose_name='Преимущества №1',
        blank=True, null=True
    )
    advantage2 = models.CharField(
        max_length=255, 
        verbose_name='преимущества №2',
        blank=True, null=True
    )
    advantage3 = models.CharField(
        max_length=255,
        verbose_name='преимущества №3',
        blank=True, null=True
    )
    title_order = models.CharField(
        max_length=255,
        verbose_name='Как заказать такси внутри города?',
        blank=True, null=True
    )
    title_order2 = models.CharField(
        max_length=255,
        verbose_name='Как заказать такси межгород?',
        blank=True, null=True
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
        verbose_name = 'Настройка страницы такси'
        verbose_name_plural = 'Настройки такси'


class TypesTaxi(models.Model):
    slide_title = models.CharField(
        max_length=255,
        verbose_name='Заголовок слайдера',
        blank=True, null=True
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок типов такси №1',
        blank=True, null=True
    )
        
    descriptions = models.TextField(
        verbose_name='Описание типов такси №1',
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Фото типов такси  №1',
        blank=True, null=True
    )
    title2 = models.CharField(
        max_length=255,
        verbose_name='Заголовок типов такси  №2',
        blank=True, null=True
    )
        
    descriptions2 = models.TextField(
        verbose_name='Описание типов такси№2',
        blank=True, null=True
    )
    image2 = models.ImageField(
        upload_to='image/',
        verbose_name='Фото типов такси №2',
        blank=True, null=True
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
        verbose_name = 'Типы такси'
        verbose_name_plural = 'Типы такси'

