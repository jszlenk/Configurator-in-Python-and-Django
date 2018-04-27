from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Oferta
from django.db import models
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
import csv
import datetime
from django.http import HttpResponse
from django.core.urlresolvers import reverse

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; \
        filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response

export_to_csv.short_description = 'Eksport do CSV'

def order_pdf(obj):
    return '<a href="{}">PDF</a>'.format(
        reverse('oferty:admin_order_pdf', args=[obj.id]))

order_pdf.allow_tags = True
order_pdf.short_description = 'Oferty PDF'


class FlatPageAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

    fieldsets = (
        (None, {'fields': ('imię', 'nazwisko', 'email',
                           'telefon', 'ulica', 'kod_pocztowy', 'miasto', 'wiadomość', 'NIP', 'wyceniono')}),
        (_('Model'), {
            'classes': ('collapse',),
            'fields': (
                'kategoria', 'liczba_siedzień', 'pojemność_silnika', 'skrzynia_biegów', 'światła'
            ),
        }),

        (_('Kolor'), {
            'classes': ('collapse', 'extrapretty'),
            'fields': (
                'kolor',
            ),
        }),

        (_('Wyposażenie fabryczne '), {
            'classes': ('collapse', 'extrapretty'),
            'fields': (
                'p_k', (
                    'Hak', 'Klima_Fabryczna_z_tyłu', 'Pakiet_Kierowcy', 'Bezpieczeństwo', 'Zima_1_MB', 'Boczne_Drzwi',
                    'Parkowanie', 'Góral'), 's_p',
                ('Pakiet_Zima_2_BP', 'Pakiet_Chrom', 'Pakiet_Optyczny', 'Pakiet_Przednia_Panorama',
                 'Pakiet_BP_Panorama_PRO', 'Pakiet_BP_Premium_Sound', 'Pakiet_Drzwi_Elektryczne',
                 'Pakiet_BP_Deska_rozdzielcza', 'Pakiet_BP_Full_Leather', 'Pakiet_Przedłużona_Gwarancja')
            ),
        }),

        (_('Opcje i Akcesoria'), {
            'classes': ('collapse', 'extrapretty'),
            'fields': (
                'opcje', (
                    'Dodatkowa_bateria', 'Opony_całoroczne', 'Spryskiwacze_reflektorów',
                    'Lampy_przeciwmgielne_z_funk_doświetlania_zakrętów', 'Ogrzewana_szyba_przednia',
                    'Siedzenie_kierowcy_komfortowe_hydrau_resorowane',
                    'Pokrywa_schowka_na_środku_deski_rozdzielczej', 'Dodatkowe_ogrzewanie_wodne',
                    'Klimatyzacja_o_zwiększonej_wydajności', 'Dogrzewacz', 'Sygnalizator_cofania',
                    'Kierownica_wielofunkcyjna_z_komputerem_pokładowym', 'Alarm_antywłamaniowy_EDW',
                    'Pakiet_na_złe_drogi', 'Tempomat', 'Retarder'),
                'akcesoria', (
                    'USB', 'DMC', 'Przedłużenie', 'WEBASTO_Suche_Part_No', 'WEBASTO_Mokre_Part_No', 'Drzwi_AutoCool',
                    'Rodzaj_bagażnika',
                    'Ściana_separująca', 'Szyby_tylnie', 'Winda_załadunkowa', 'Jakie_półki', 'WiFi', 'DVBT', 'Lodówka',
                    'Lodówka_podschowkowa_TM', 'przyciski_STOP', 'Nietypowy_zderzak_przedni', 'Nietypowy_zderzak_tylni',
                    'Progi_boczne_spojlery')
            ),
        }),
    )
    list_display = ['id', 'imię', 'nazwisko', 'email',
                    'telefon',
                    'utworzony', 'aktualizowano', order_pdf]
    list_filter = ['wyceniono', 'utworzony', 'aktualizowano']
    search_fields = ('nazwisko', 'email', 'kod_pocztowy', 'miasto', 'kategoria', 'NIP',)

    readonly_fields = (
        's_p', 'p_k', 'akcesoria', 'opcje', 'kategoria', 'liczba_siedzień', 'pojemność_silnika', 'skrzynia_biegów',
        'światła', 'kolor',
        'Hak', 'Klima_Fabryczna_z_tyłu', 'Pakiet_Kierowcy', 'Bezpieczeństwo', 'Zima_1_MB',
        'Boczne_Drzwi', 'Parkowanie', 'Góral', 'Pakiet_Zima_2_BP', 'Pakiet_Chrom', 'Pakiet_Optyczny',
        'Pakiet_Przednia_Panorama', 'Pakiet_BP_Panorama_PRO', 'Pakiet_BP_Premium_Sound', 'Pakiet_Drzwi_Elektryczne',
        'Pakiet_BP_Deska_rozdzielcza', 'Pakiet_BP_Full_Leather', 'Pakiet_Przedłużona_Gwarancja',
        'Dodatkowa_bateria', 'Opony_całoroczne', 'Spryskiwacze_reflektorów',
        'Lampy_przeciwmgielne_z_funk_doświetlania_zakrętów', 'Ogrzewana_szyba_przednia',
        'Siedzenie_kierowcy_komfortowe_hydrau_resorowane',
        'Pokrywa_schowka_na_środku_deski_rozdzielczej', 'Dodatkowe_ogrzewanie_wodne',
        'Klimatyzacja_o_zwiększonej_wydajności', 'Dogrzewacz', 'Sygnalizator_cofania',
        'Kierownica_wielofunkcyjna_z_komputerem_pokładowym', 'Alarm_antywłamaniowy_EDW',
        'Pakiet_na_złe_drogi', 'Tempomat', 'Retarder', 'USB', 'DMC', 'Przedłużenie', 'WEBASTO_Suche_Part_No',
        'WEBASTO_Mokre_Part_No', 'Drzwi_AutoCool', 'Rodzaj_bagażnika',
        'Ściana_separująca', 'Szyby_tylnie', 'Winda_załadunkowa', 'Jakie_półki', 'WiFi', 'DVBT', 'Lodówka',
        'Lodówka_podschowkowa_TM', 'przyciski_STOP', 'Nietypowy_zderzak_przedni', 'Nietypowy_zderzak_tylni',
        'Progi_boczne_spojlery'
    )

    def s_p(self, instance):
        return mark_safe('<br/>')

    s_p.short_description = "Specjalistyczne pakiety"

    def p_k(self, instance):
        return mark_safe('<br/>')

    p_k.short_description = "Klienckie pakiety"

    def opcje(self, instance):
        return mark_safe('<br/>')

    opcje.short_description = "Opcje"

    def akcesoria(self, instance):
        return mark_safe('<br/>')

    akcesoria.short_description = "Akcesoria"

admin.site.register(Oferta, FlatPageAdmin)
