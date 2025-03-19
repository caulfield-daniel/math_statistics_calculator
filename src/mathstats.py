class Statistics:
    """
    Класс для вычисления статистических показателей:
    математическое ожидание, дисперсия и среднее квадратичное отклонение.
    """

    @staticmethod
    def _validate_input(input_data: dict):
        """
        Проверяет корректность входных данных.

        Args:
            input_data (dict): Структура вида {value: probability}

        Raises:
            TypeError: Если `input_data` не является словарем.
            ValueError: Если вероятность не в допустимом диапазоне или если сумма вероятностей не равна 1.
        """
        if not isinstance(input_data, dict):
            raise TypeError(f"Неверный тип данных: {type(input_data)}")

        if not all(
            isinstance(key, (int, float)) and isinstance(value, (int, float))
            for key, value in input_data.items()
        ):
            raise ValueError("Ключи и значения должны быть числами (int или float).")

        if not all(value >= 0 for value in input_data.values()):
            raise ValueError(
                "Неверные статистические данные. Вероятность должна быть неотрицательной"
            )

        if not sum(input_data.values()) == 1:
            raise ValueError(
                "Неверные статистические данные. Сумма вероятностей должна быть равна 1"
            )

    @staticmethod
    def expectation(input_data: dict) -> float:
        """
        Вычисляет математическое ожидание.

        Args:
            input_data (dict): Структура вида {value: probability}.

        Returns:
            float: Математическое ожидание.

        Raises:
            ValueError: Если `input_data` не является словарем, если вероятность не в допустимом диапазоне
                        или если сумма вероятностей не равна 1.
        """
        Statistics._validate_input(input_data)

        return sum(x * p for x, p in input_data.items())

    @staticmethod
    def _expectation_of_square(input_data: dict) -> float:
        """
        Вычисляет математическое ожидание квадратов значений.

        Args:
            input_data (dict): Структура вида {value: probability}.

        Returns:
            float: Математическое ожидание квадратов.
        """
        return sum(x**2 * p for x, p in input_data.items())

    @staticmethod
    def dispersion(input_data: dict) -> float:
        """
        Вычисляет дисперсию.

        Args:
            input_data (dict): Структура вида {value: probability}.

        Returns:
            float: Дисперсия.

        Raises:
            ValueError: Если `input_data` не является словарем, если вероятность не в допустимом диапазоне
                        или если сумма вероятностей не равна 1.
        """
        Statistics._validate_input(input_data)

        return (
            Statistics._expectation_of_square(input_data)
            - Statistics.expectation(input_data) ** 2
        )

    @staticmethod
    def standard_deviation(input_data: dict) -> float:
        """
        Вычисляет среднее квадратичное отклонение.

        Args:
            input_data (dict): Структура вида {value: probability}.

        Returns:
            float: Среднее квадратичное отклонение.

        Raises:
            ValueError: Если `input_data` не является словарем, если вероятность не в допустимом диапазоне
                        или если сумма вероятностей не равна 1.
        """
        Statistics._validate_input(input_data)

        return Statistics.dispersion(input_data) ** 0.5
