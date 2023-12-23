from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Cargo(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок грузоперевозки',
        blank=True, null=True
    )
    descriptions = models.TextField(
        verbose_name='Описание грузоперевозки',
        blank=True, null=True
    )
    banner_image = models.ImageField(
        upload_to='image/',
        verbose_name="Фото баннера",
        blank=True, null=True
    )
    title2 = models.CharField(
        max_length=222, 
        verbose_name="Заголовок Как заказать услугу грузоперезки?",
        blank=True, null=True
    )

    descriptions2 = models.CharField(
        max_length=255,
        verbose_name="Описание Как заказать услугу грузоперезки?",
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
        verbose_name = 'Найстрока страницы грузоперевозки'
        verbose_name_plural = 'Найстрока страницы грузоперевозки'


class Profitable(models.Model):
    title2 = models.CharField(
        max_length=255, 
        verbose_name='Заголовок',
        blank=True, null=True
    )
    
    title = models.CharField(
        max_length=255, 
        verbose_name='Заголовок',
        blank=True, null=True
    )
    descriptions = models.TextField(
        verbose_name='Описание ',
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name="Фото ",
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
        verbose_name = 'Приложение для выгодных грузоперевозок'
        verbose_name_plural = 'Приложение для выгодных грузоперевозок'
