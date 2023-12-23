from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Settings(models.Model):
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

    banner_image2 = models.ImageField(
        upload_to='image/',
        verbose_name="Фото баннера2",
        blank=True, null=True
    )
    logo = models.ImageField(
        upload_to='image/',
        verbose_name='Лого фото',
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
    made_title = models.CharField(
        max_length=255,
        verbose_name='Где сделано?',
        blank=True, null=True
    )
    made_descriptions = models.CharField(
        max_length=255,
        verbose_name='Описание где сделано',
        blank=True, null=True
    )
    install = models.CharField(
        max_length=255,
        verbose_name='Установить приложение',
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
        verbose_name = 'Настройка страницы главная'
        verbose_name_plural = 'Настройки главная'


class Slider(models.Model):
    title_slider = models.CharField(
        max_length=255,
        verbose_name='Заголовок слайдера',
        blank=True, null=True
    )
    title_slider2 = models.CharField(
        max_length=255,
        verbose_name='Заголовок слайдера 2',
        blank=True, null=True
    )
    numbering = models.CharField(
        max_length=255, 
        verbose_name="Номерация слайдера",
        blank=True, null=True
    )
    descriptions = models.TextField(
        verbose_name='Описание слайлера',
        blank=True, null=True
    )
    image_slider = models.ImageField(
        upload_to='image/',
        verbose_name='Фото слайдера',
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
        return str(self.title_slider) if self.title_slider else ""

    class Meta:
        verbose_name = 'Настройка слайдера'
        verbose_name_plural = 'Настройки слайдера'

class Why(models.Model):
    why = models.CharField(
        max_length=255,
        verbose_name='Вопрос'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок',
        blank=True, null=True
    )
    descriptions = models.TextField(
        verbose_name='Описание',
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Иконка',
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
        verbose_name = 'Почему Alaget?'
        verbose_name_plural = 'Почему Alaget?'



class OrderСity(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок',
        blank=True, null=True
    )
    numbers = models.CharField(
        max_length=255, 
        verbose_name='Номерация',
        blank=True, null=True
    )
    descriptions = models.TextField(
        verbose_name='Описание',
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
        return reverse('index',  kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.title) if self.title else ""
    
    class Meta:
        verbose_name = 'Как заказать такси внутри города?'
        verbose_name_plural = 'Как заказать такси внутри города?'


class OrderIntercity(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок',
        blank=True, null=True
    )
    numbers = models.CharField(
        max_length=255, 
        verbose_name='Номерация',
        blank=True, null=True
    )
    descriptions = models.TextField(
        verbose_name='Описание',
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
        return reverse('index',  kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.title) if self.title else ""
    
    class Meta:
        verbose_name = 'Как заказать такси межгород?'
        verbose_name_plural = 'Как заказать такси внутри межгород?'


class Earn(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок',
        blank=True, null=True
    )
    descriptions = models.TextField(
        verbose_name='Описание',
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
        return reverse('index',  kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.title) if self.title else ""
    
    class Meta:
        verbose_name = 'С ALAGET зарабатывать легко!'
        verbose_name_plural = 'С ALAGET зарабатывать легко!'



class Base(models.Model):
    title1 = models.CharField(
        max_length=255,
        verbose_name='ГЛАВНАЯ',
        blank=True, null=True
    )
    title2 = models.CharField(
        max_length=255,
        verbose_name='ТАКСИ',
        blank=True, null=True
    )

    title3 = models.CharField(
        max_length=255,
        verbose_name='ГРУЗОПЕРЕВОЗКИ',
        blank=True, null=True
    )

    title4 = models.CharField(
        max_length=255,
        verbose_name='ДОСТАВКА',
        blank=True, null=True
    )

    title5 = models.CharField(
        max_length=255,
        verbose_name='О НАС',
        blank=True, null=True
    )

    title6 = models.CharField(
        max_length=255,
        verbose_name='КОНТАКТЫ',
        blank=True, null=True
    )
    title7 = models.CharField(
        max_length=255,
        verbose_name='Стать водителем',
        blank=True, null=True
    )

    title8 = models.CharField(
        max_length=255,
        verbose_name='РАБОТА В АЛАГЕТ',
        blank=True, null=True
    )
    title9 = models.CharField(
        max_length=255,
        verbose_name='ПАРТНЕРСТВО',
        blank=True, null=True
    )

    descriptions = models.CharField(
        max_length=255,
        verbose_name='Footer text',
        blank=True, null=True
    )

    req = models.CharField(
        max_length=255,
        verbose_name='Пользовательское соглашение',
        blank=True, null=True
    )
    req2 = models.CharField(
        max_length=255,
        verbose_name='Политика конфиденциальности',
        blank=True, null=True
    )
    req3 = models.CharField(
        max_length=255,
        verbose_name='Лицензионное соглашение',
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
        return str(self.title1) if self.title1 else ""
    
    class Meta:
        verbose_name = 'Страницы'
        verbose_name_plural = 'Страницы'


class Environment(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Текст',
        blank=True, null=True
    )

    descriptions = models.CharField(
        max_length=255,
        verbose_name='Текст',
        blank=True, null=True
    )
    descriptions2 = models.CharField(
        max_length=255,
        verbose_name='Текст',
        blank=True, null=True
    )

    descriptions3= models.CharField(
        max_length=255,
        verbose_name='Текст',
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
        return reverse('index',  kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.title) if self.title else ""
    
    class Meta:
        verbose_name = 'За экологию Кыргызстана'
        verbose_name_plural = 'За экологию Кыргызстана'