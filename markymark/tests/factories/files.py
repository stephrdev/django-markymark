import factory

from filer.models.filemodels import File


class FileFactory(factory.DjangoModelFactory):
    FACTORY_FOR = File

    original_filename = 'file.data'
    file = factory.django.FileField(filename='file.data')
