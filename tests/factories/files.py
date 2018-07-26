import factory
from filer.models import File, Image


class FileFactory(factory.DjangoModelFactory):
    original_filename = 'file.data'
    file = factory.django.FileField(filename='file.data')

    class Meta:
        model = File


class ImageFactory(factory.DjangoModelFactory):
    original_filename = 'test.jpg'
    file = factory.django.ImageField(filename='test.jpg', color='blue')
    default_alt_text = 'test alt text'
    default_caption = 'test caption'

    class Meta:
        model = Image
