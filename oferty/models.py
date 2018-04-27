from django.db import models
from django.core.validators import RegexValidator
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

class Oferta(models.Model):
    Kategoria = [
        ('Basic', 'Basic'),
        ('Tourist', 'Tourist'),
        ('Exclusive', 'Exclusive')
    ]

    Liczba_siedzień = [
        ('Standard 16+1', 'Standard 16+1'),
        ('Przedłużka 16+1', 'Przedłużka 16+1'),
        ('Przedłużka 19+1', 'Przedłużka 19+1')
    ]

    Pojemność_silnika = [
        ('4 Cylindrów', '4 Cylindrów'),
        ('6 Cylindrów', '6 Cylindrów')
    ]

    Skrzynia_biegów = [
        ('Manulana', 'Manulana'),
        ('Automatyczna', 'Automatyczna')
    ]

    Światła = [
        ('Halogeny', 'Halogeny'),
        ('Ksenony', 'Ksenony')
    ]

    Kolor = [
        ('E1E3E4', 'E1E3E4'),
        ('354B6C', '354B6C'),
        ('6C4444', '6C4444'),
        ('0090FF', '0090FF'),
        ('ACA79C', 'ACA79C'),
        ('798790', '798790'),
        ('2E6668', '2E6668'),
        ('2F2F2F', '2F2F2F'),
        ('D4D0C6', 'D4D0C6'),
        ('9C9B93', '9C9B93'),
        ('595B57', '595B57'),
        ('EAC455', 'EAC455'),
        ('307098', '307098'),
        ('D32130', 'D32130'),
        ('D12235', 'D12235'),
        ('868D8F', '868D8F'),
        ('2A436C', '2A436C'),
        ('323437', '323437'),
        ('534642', '534642'),
        ('B7BCBF', 'B7BCBF'),
        ('464F55', '464F55'),
        ('525350', '525350'),
        ('999791', '999791'),
        ('4A4F68', '4A4F68'),
    ]

    imię = models.CharField(max_length=50)
    nazwisko = models.CharField(error_messages={'required': 'Prosze podaj swoje naziwsko!'}, max_length=50)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Numer telefonu należy wprowadzić w formacie: '+500500500'. Dopuszczalne do 15 cyfr")
    telefon = models.CharField(validators=[phone_regex], max_length=15)
    ulica = models.CharField(max_length=250, blank=True)
    kod_pocztowy = models.CharField(max_length=20, blank=True)
    miasto = models.CharField(max_length=100, blank=True)
    utworzony = models.DateTimeField(auto_now_add=True)
    aktualizowano = models.DateTimeField(auto_now=True)
    wiadomość = models.TextField(blank=True, null=True, max_length=400)
    nip_regex = RegexValidator(regex=r'^[0-9]{7,18}', message="Tylko cyfry. Dopuszczalne do 18 cyfr")
    NIP = models.CharField(validators=[nip_regex], max_length=18)
    wyceniono = models.BooleanField(default=False)
    kategoria = models.CharField(max_length=350, default='', choices=Kategoria)
    liczba_siedzień = models.CharField(max_length=350, default='', choices=Liczba_siedzień)
    pojemność_silnika = models.CharField(max_length=350, default='', choices=Pojemność_silnika)
    skrzynia_biegów = models.CharField(max_length=350, default='', choices=Skrzynia_biegów)
    światła = models.CharField(max_length=350, default='', choices=Światła)
    kolor = models.CharField(max_length=350, default=Kolor[0][0], choices=Kolor)

    Hak = models.BooleanField(default=False)
    Klima_Fabryczna_z_tyłu = models.BooleanField(default=False)
    Pakiet_Kierowcy = models.BooleanField(default=False)
    Bezpieczeństwo = models.BooleanField(default=False)
    Zima_1_MB = models.BooleanField(default=False)
    Boczne_Drzwi = models.BooleanField(default=False)
    Parkowanie = models.BooleanField(default=False)
    Góral = models.BooleanField(default=False)

    Pakiet_Zima_2_BP = models.BooleanField(default=False)
    Pakiet_Chrom = models.BooleanField(default=False)
    Pakiet_Optyczny = models.BooleanField(default=False)
    Pakiet_Przednia_Panorama = models.BooleanField(default=False)
    Pakiet_BP_Panorama_PRO = models.BooleanField(default=False)
    Pakiet_BP_Premium_Sound = models.BooleanField(default=False)
    Pakiet_Drzwi_Elektryczne = models.BooleanField(default=False)
    Pakiet_BP_Deska_rozdzielcza = models.BooleanField(default=False)
    Pakiet_BP_Full_Leather = models.BooleanField(default=False)
    Pakiet_Przedłużona_Gwarancja = models.BooleanField(default=False)

    Dodatkowa_bateria = models.BooleanField(default=False)
    Opony_całoroczne = models.BooleanField(default=False)
    Spryskiwacze_reflektorów = models.BooleanField(default=False)
    Lampy_przeciwmgielne_z_funk_doświetlania_zakrętów = models.BooleanField(default=False)
    Ogrzewana_szyba_przednia = models.BooleanField(default=False)
    Siedzenie_kierowcy_komfortowe_hydrau_resorowane = models.BooleanField(default=False)
    Pokrywa_schowka_na_środku_deski_rozdzielczej = models.BooleanField(default=False)
    Dodatkowe_ogrzewanie_wodne = models.BooleanField(default=False)
    Klimatyzacja_o_zwiększonej_wydajności = models.BooleanField(default=False)
    Dogrzewacz = models.BooleanField(default=False)
    Sygnalizator_cofania = models.BooleanField(default=False)
    Kierownica_wielofunkcyjna_z_komputerem_pokładowym = models.BooleanField(default=False)
    Alarm_antywłamaniowy_EDW = models.BooleanField(default=False)
    Pakiet_na_złe_drogi = models.BooleanField(default=False)
    Tempomat = models.BooleanField(default=False)
    Retarder = models.BooleanField(default=False)

    USB = models.BooleanField(default=False)
    DMC = models.BooleanField(default=False)
    Przedłużenie = models.BooleanField(default=False)
    WEBASTO_Suche_Part_No = models.BooleanField(default=False)
    WEBASTO_Mokre_Part_No = models.BooleanField(default=False)
    Drzwi_AutoCool = models.BooleanField(default=False)
    Rodzaj_bagażnika = models.BooleanField(default=False)
    Ściana_separująca = models.BooleanField(default=False)
    Szyby_tylnie = models.BooleanField(default=False)
    Winda_załadunkowa = models.BooleanField(default=False)
    Jakie_półki = models.BooleanField(default=False)
    WiFi = models.BooleanField(default=False)
    DVBT = models.BooleanField(default=False)
    Lodówka = models.BooleanField(default=False)
    Lodówka_podschowkowa_TM = models.BooleanField(default=False)
    przyciski_STOP = models.BooleanField(default=False)
    Nietypowy_zderzak_przedni = models.BooleanField(default=False)
    Nietypowy_zderzak_tylni = models.BooleanField(default=False)
    Progi_boczne_spojlery = models.BooleanField(default=False)

    class Meta:
        ordering = ('-utworzony',)
        verbose_name = 'Konfigurator'
        verbose_name_plural = 'Konfigurator'

    def __str__(self):
        return 'Oferta {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
