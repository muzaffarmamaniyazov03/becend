from django.db import models
from ckeditor.fields import RichTextField


class Management(models.Model):
    text_ru = RichTextField(verbose_name='Об управлени РУС')
    text_uz = RichTextField(verbose_name='Об управлени УЗБ')
    publish = models.BooleanField(default=True, verbose_name='Опубликовать?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменено')

    def __str__(self):
        return f"{self.text_ru}\n{self.text_uz}"

    class Meta:
        verbose_name = 'Управление'
        verbose_name_plural = 'Управления'
        ordering = ['-updated_at']


class Regional(models.Model):
    title_uz = models.CharField(max_length=150, verbose_name='Наименование УЗБ')
    title_ru = models.CharField(max_length=150, verbose_name='Наименование РУС')
    image = models.ImageField(upload_to='institution/', blank=True, null=True)
    numbers = RichTextField(verbose_name='Телефоны')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    publish = models.BooleanField(default=True, verbose_name='Опубликовать?')

    def __str__(self):
        return f"{self.title_ru}\n{self.title_uz}"

    class Meta:
        verbose_name = 'Региональное учреждение'
        verbose_name_plural = 'Региональные учреждения'
        ordering = ['-updated_at']


class Guide(models.Model):
    post_ru = models.CharField(max_length=255, verbose_name='Должность РУС')
    post_uz = models.CharField(max_length=255, verbose_name='Должность УЗБ')
    name_ru = models.CharField(max_length=255, verbose_name='Польное имя РУС')
    name_uz = models.CharField(max_length=255, verbose_name='Польное имя УЗБ')
    work_time_ru = RichTextField(verbose_name='Время работы РУС')
    work_time_uz = RichTextField(verbose_name='Время работы УЗБ')
    contact = models.CharField(max_length=20, verbose_name='Личный тел')
    work_contact = models.CharField(max_length=20, verbose_name='Гос тел')
    photo = models.ImageField(upload_to='guide/', blank=True, verbose_name='Фото')
    publish = models.BooleanField(default=True, verbose_name='Опубликовать?')

    def __str__(self):
        return f"{self.name_ru}\n{self.name_uz}"

    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = 'Руководство'


class About(models.Model):
    text_ru = RichTextField(verbose_name='О нас РУС')
    text_uz = RichTextField(verbose_name='О нас УЗБ')

    class Meta:
        verbose_name = 'О Себе'
        verbose_name_plural = 'О Себе'


class Organization(models.Model):
    title_ru = models.CharField(max_length=250, verbose_name='Организация РУС')
    title_uz = models.CharField(max_length=250, verbose_name='Организация УЗБ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=True, verbose_name='Опубликовать?')

    def __str__(self):
        return f"{self.title_ru}\n{self.title_uz}"

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ['-updated_at']


class Director(models.Model):
    post_ru = models.CharField(max_length=250, verbose_name='Должность РУС')
    post_uz = models.CharField(max_length=250, verbose_name='Должность УЗБ')
    name_ru = models.CharField(max_length=255, verbose_name='Польное имя РУС')
    name_uz = models.CharField(max_length=255, verbose_name='Польное имя УЗБ')
    photo = models.ImageField(upload_to='directors/', blank=True, verbose_name='Фото')
    text_ru = RichTextField(verbose_name='Текст РУС')
    text_uz = RichTextField(verbose_name='Текст УЗБ')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name="Организация")

    def __str__(self):
        return f"{self.name_ru}\n{self.name_uz}"

    class Meta:
        verbose_name = 'Директор'
        verbose_name_plural = 'Директоры'


class News(models.Model):
    title_uz = models.CharField(max_length=150, verbose_name='Наименование УЗБ')
    title_ru = models.CharField(max_length=150, verbose_name='Наименование РУС')
    text_ru = RichTextField(verbose_name='Текст РУС')
    text_uz = RichTextField(verbose_name='Текст УЗБ')
    publish = models.BooleanField(default=True, verbose_name='Опубликовать?')

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Documents(models.Model):
    title_ru = models.CharField(max_length=255, verbose_name='Наименование РУС')
    title_uz = models.CharField(max_length=255, verbose_name='Наименование УЗБ')
    pdf_ru = models.FileField(upload_to='documents/', blank=True, null=True, verbose_name='PDF РУС')
    pdf_uz = models.FileField(upload_to='documents/', blank=True, null=True, verbose_name='PDF УЗБ')
    publish = models.BooleanField(default=True, verbose_name='Опубликовать?')

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class OpenData(models.Model):
    title_ru = models.CharField(max_length=255, verbose_name='Наименование РУС')
    title_uz = models.CharField(max_length=255, verbose_name='Наименование УЗБ')
    pdf_ru = models.FileField(upload_to='open_data/', blank=True, null=True, verbose_name='PDF РУС')
    pdf_uz = models.FileField(upload_to='open_data/', blank=True, null=True, verbose_name='PDF УЗБ')
    publish = models.BooleanField(default=True, verbose_name='Опубликовать?')

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Открытые данные'
        verbose_name_plural = 'Открытые данные'


