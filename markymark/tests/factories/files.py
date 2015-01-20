import factory

from filer.models.filemodels import File
from filer.models.imagemodels import Image


class FileFactory(factory.DjangoModelFactory):
    FACTORY_FOR = File

    original_filename = 'file.data'
    file = factory.django.FileField(filename='file.data')


class ImageFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Image

    original_filename = 'test.jpg'
    file = factory.django.ImageField(filename='test.jpg', color='blue')
    default_alt_text = 'test alt text'
    default_caption = 'test caption'
