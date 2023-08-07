class ValFormatError(Exception):
    def __str__(self):
        return f"Ошибка: Матрицы разных размеров нельзя сравнивать"