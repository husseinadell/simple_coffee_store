from django.db import models


class CoffeeMachine(models.Model):
    COFFEE_MACHINE_SMALL = 'CM00'
    COFFEE_MACHINE_LARGE = 'CM10'
    ESPRESSO_MACHINE = 'EM00'
    MACHINE_TYPE_CHOICES = [
        (COFFEE_MACHINE_LARGE, 'Coffee Machine Large'),
        (COFFEE_MACHINE_SMALL, 'Coffee Machine Small'),
        (ESPRESSO_MACHINE, 'Espresso Machine'),
    ]

    BASE = '1'
    PREMIUM = '2'
    DELUX = '3'
    MODEL_CHOICES = [
        (BASE, 'Base'),
        (PREMIUM, 'Premium'),
        (DELUX, 'Delux')
    ]

    # name = models.CharField(max_length=30, default='')
    machine_type = models.CharField(
        max_length=4, choices=MACHINE_TYPE_CHOICES, default=COFFEE_MACHINE_SMALL)
    water_line_compatible = models.BooleanField(default=False)
    model = models.CharField(max_length=7, choices=MODEL_CHOICES, default=BASE)

    def __str__(self) -> str:
        return f'{self.machine_type}{self.model}'


class CoffeePod(models.Model):
    COFFEE_POD_SMALL = 'CP0'
    COFFEE_POD_LARGE = 'CP1'
    ESPRESSO_POD = 'EP0'
    POD_TYPE_CHOICES = [
        (COFFEE_POD_SMALL, 'Coffee Pod Small'),
        (COFFEE_POD_LARGE, 'Coffee Pod Large'),
        (ESPRESSO_POD, 'Espresso Pod'),
    ]

    FLAVOR_VANILLA = 'VANILLA'
    FLAVOR_CARAMEL = 'CARAMEL'
    FLAVOR_PSL = 'PSL'
    FLAVOR_MOCHA = 'MOCHA'
    FLAVOR_HAZELNUT = 'HAZELNUT'
    FLAVOR_CHOICES = [
        (FLAVOR_VANILLA, 'Flavor Vanilla'),
        (FLAVOR_CARAMEL, 'Flavor Caramel'),
        (FLAVOR_PSL, 'Flavor Psl'),
        (FLAVOR_MOCHA, 'Flavor Mocha'),
        (FLAVOR_HAZELNUT, 'Flavor Hazelnut')
    ]
    FLAVOR_IDS_CHOICES = [FLAVOR_VANILLA, FLAVOR_CARAMEL,
                          FLAVOR_PSL, FLAVOR_MOCHA, FLAVOR_HAZELNUT]

    SIZE_1_DOZEN = 1
    SIZE_3_DOZEN = 3
    SIZE_5_DOZEN = 5
    SIZE_7_DOZEN = 7
    PACKAGE_SIZE_CHOICES = [
        (SIZE_1_DOZEN, '1 Dozen'),
        (SIZE_3_DOZEN, '3 Dozen'),
        (SIZE_5_DOZEN, '5 Dozen'),
        (SIZE_7_DOZEN, '7 Dozen'),
    ]

    pod_type = models.CharField(
        max_length=3, choices=POD_TYPE_CHOICES, default=COFFEE_POD_SMALL)
    flavor = models.CharField(
        max_length=10, choices=FLAVOR_CHOICES, default=FLAVOR_VANILLA)
    package_size = models.IntegerField(
        choices=PACKAGE_SIZE_CHOICES, default=SIZE_1_DOZEN)

    def __str__(self) -> str:
        flavor_id = self.FLAVOR_IDS_CHOICES.index(self.flavor)
        return f'{self.pod_type}{flavor_id}{self.package_size}'
