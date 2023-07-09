class InstantiateCSVError(Exception):
    """
    Исключение, выбрасываемое при ошибке чтения CSV-файла.
    """

    def __init__(self, file_name: str):
        super().__init__(f"Файл {file_name.split('/')[-1]} поврежден")
