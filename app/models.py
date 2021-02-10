from django.db import models


class CommonData(models.Model):
    LEVEL_GAUGE_CHOICES = [
        ('50', 'УСК-ТЭ-50'),
        ('100', 'УСК-ТЭ-100'),
        ('150', 'УСК-ТЭ-150'),
        ('200', 'УСК-ТЭ-200'),
        ('2-50', 'УСК-ТЭ2-50'),
        ('2-100', 'УСК-ТЭ2-100  '),
        ('2-150', 'УСК-ТЭ2-150  '),
        ('2-200', 'УСК-ТЭ2-200  '),
        ('2-250', 'УСК-ТЭ2-250  '),
    ]
    LEVEL_GAUGE_YEAR_CHOICES = [
        ('2014', '2014'),
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021')
    ]
    performer = models.CharField(max_length=100)  # Исполнитель
    sector = models.CharField(max_length=100)  # Наименование участка
    well = models.CharField(max_length=100)  # Номер скважины
    altitude_mouth = models.DecimalField(max_digits=19, decimal_places=3)  # Абсолютная отметка устья (м)
    level_gauge = models.CharField(max_length=50, choices=LEVEL_GAUGE_CHOICES, default='50')  # Уровнемер
    level_gauge_year = models.CharField(max_length=50,
                                        choices=LEVEL_GAUGE_YEAR_CHOICES,
                                        default='2021')  # Год выпуска уровнемера
    level_gauge_correction = models.DecimalField(max_digits=19, decimal_places=3)  # Поправка на уровнемер (м)
    nozzle_height = models.DecimalField(max_digits=19, decimal_places=3)  # Высота патрубка (м)
    pump_at_depth = models.DecimalField(max_digits=19, decimal_places=3)  # Насос на глубине (м)
    static_level_mouth = models.DecimalField(max_digits=19, decimal_places=3)  # Статический уровень от устья замеренный (м)
    debit_counter = models.DecimalField(max_digits=19, decimal_places=3)  # Счетчик дебита (нач.значение)
    tank_volume = models.DecimalField(max_digits=19, decimal_places=3)  # Объем емкости (л)

    def __str__(self):
        return '{0}/{1}/{2}'.format(self.performer, self.sector, self.well)

