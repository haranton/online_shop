from django.core.files.storage import FileSystemStorage

class MyCustomStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        # можно задать другую директорию для хранения
        kwargs['location'] = '/path/to/custom/folder'
        super().__init__(*args, **kwargs)