from crispy_forms.bootstrap import PrependedText, Accordion, AccordionGroup, Tab, FieldWithButtons, StrictButton, PrependedAppendedText, TabHolder, FormActions, InlineField
from django import forms
from django.utils.translation import ugettext_lazy as _, ugettext
from crispy_forms import layout, bootstrap
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, MultiField, Div, Field, Button
from .models import Oferta

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ['imię', 'nazwisko', 'ulica', 'miasto', 'kod_pocztowy', 'wiadomość', 'telefon',
                  'email', 'NIP', 'kategoria', 'liczba_siedzień', 'pojemność_silnika',
                  'skrzynia_biegów', 'światła', 'kolor',
                  'Hak', 'Klima_Fabryczna_z_tyłu', 'Pakiet_Kierowcy', 'Bezpieczeństwo', 'Zima_1_MB', 'Boczne_Drzwi',
                  'Parkowanie', 'Góral', 'Pakiet_Zima_2_BP',
                  'Pakiet_Chrom', 'Pakiet_Optyczny', 'Pakiet_Przednia_Panorama', 'Pakiet_BP_Panorama_PRO',
                  'Pakiet_BP_Premium_Sound', 'Pakiet_Drzwi_Elektryczne', 'Pakiet_BP_Deska_rozdzielcza',
                  'Pakiet_BP_Full_Leather', 'Pakiet_Przedłużona_Gwarancja',
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
                  'Progi_boczne_spojlery']
        widgets = {
            'kategoria': forms.RadioSelect(),
            'liczba_siedzień': forms.RadioSelect(),
            'pojemność_silnika': forms.RadioSelect(),
            'dopuszczalna_masa_całkowita': forms.RadioSelect(),
            'skrzynia_biegów': forms.RadioSelect(),
            'światła': forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(form=self)

        self.helper[0:0].wrap_together(layout.Fieldset, 'Your name')
        self.helper.form_action = "."
        self.helper.form_method = "POST"
        self.helper.form_class = 'form-inline'
        self.helper.form_show_labels = False
        self.fields["kolor"].widget = forms.RadioSelect()
        self.helper.layout = layout.Layout(

            TabHolder(
                Tab(
                    '1. Model',
                    layout.HTML("""
                                <div class="row higg">
                                <div class="column hig col-sm-6">

                                <h3>Model</h3>
                                </div>

                                <div class="column  pp col-sm-6">

                                <button class="btn btn-primary nast continue" onclick="">Następny</button>
                                <button class="btn btn-primary poprz">Poprzedni</button>
                                </div>
                                </div>
                                     """),
                    Accordion(
                        AccordionGroup('Wybierz kategorie',
                                       # Field('kategoria', css_class="form-horizontal"),
                                       # active=True,
                                       Div(
                                           'kategoria',
                                           template='oferty/order/kategoria.html'
                                       ),
                                       ),
                        AccordionGroup('Liczba siedzień',
                                       # Field('liczba_siedzień', css_class="form-inline"),
                                       Div(
                                           'liczba_siedzień',
                                           template='oferty/order/siedzenia.html'
                                       ),
                                       ),
                        AccordionGroup('Pojemność silnika',
                                       # Field('pojemność_silnika', css_class="form-inline"),
                                       Div(
                                           'pojemność_silnika',
                                           template='oferty/order/silnik.html'
                                       ),
                                       ),
                        AccordionGroup('Skrzynia biegów',
                                       # Field('skrzynia_biegów', css_class="extra"),
                                       Div(
                                           'skrzynia_biegów',
                                           template='oferty/order/skrzynia.html'
                                       ),
                                       ),
                        AccordionGroup('Światła',
                                       # Field('światła', css_class="extra"),
                                       Div(
                                           'światła',
                                           template='oferty/order/swiatla.html'
                                       ),
                                       ),

                    )
                ),
                Tab('2. Wygląd',
                    layout.HTML("""
                                        <div class="row higg">
                                        <div class="column hig col-sm-6">

                                        <h3>Wygląd</h3>
                                        </div>

                                        <div class="column  pp col-sm-6">

                                        <button class="btn btn-primary nast continue" onclick="">Następny</button>
                                        <button class="btn btn-primary poprz">Poprzedni</button>
                                        </div>
                                        </div>
                                             """),
                    # Field("kolor")
                Div(
                    'kolor',
                    template='oferty/order/wyglad.html'
                ),
                    ),
                Tab('3. Wyposażenie fabryczne ',
                    layout.HTML("""
                                        <div class="row higg">
                                        <div class="column hig col-sm-6">

                                        <h3>Wyposażenie fabryczne</h3>
                                        </div>

                                        <div class="column  pp col-sm-6">

                                        <button class="btn btn-primary nast continue" onclick="">Następny</button>
                                        <button class="btn btn-primary poprz">Poprzedni</button>
                                        </div>
                                        </div>
                                             """),
                    Accordion(
                        AccordionGroup('Pakiety Mercedes',
                                         Div(
                                             'Hak', 'Klima_Fabryczna_z_tyłu', 'Pakiet_Kierowcy', 'Bezpieczeństwo', 'Zima_1_MB', 'Boczne_Drzwi', 'Parkowanie', 'Góral',
                                             template='oferty/order/pakiety_1.html'
                                         ),

                                       # Field('Hak', 'Klima_Fabryczna_z_tyłu', 'Pakiet_Kierowcy', 'Bezpieczeństwo',
                                       #       'Zima_1_MB', 'Boczne_Drzwi', 'Parkowanie', 'Góral',
                                       #       css_class="form-horizontal"),
                                       # active=True,

                                       ),
                        AccordionGroup('Pakiety test',
                                       Div(
                                           'Pakiet_Zima_2_BP', 'Pakiet_Chrom', 'Pakiet_Optyczny', 'Pakiet_Przednia_Panorama',
                                           'Pakiet_BP_Panorama_PRO', 'Pakiet_BP_Premium_Sound', 'Pakiet_Drzwi_Elektryczne', 'Pakiet_BP_Deska_rozdzielcza', 'Pakiet_BP_Full_Leather', 'Pakiet_Przedłużona_Gwarancja',
                                           template='oferty/order/pakiety_2.html'
                                       ),

                                       # Field('Pakiet_Zima_2_BP', 'Pakiet_Chrom', 'Pakiet_Optyczny',
                                       #       'Pakiet_Przednia_Panorama', 'Pakiet_BP_Panorama_PRO',
                                       #       'Pakiet_BP_Premium_Sound', 'Pakiet_Drzwi_Elektryczne',
                                       #       'Pakiet_BP_Deska_rozdzielcza', 'Pakiet_BP_Full_Leather',
                                       #       'Pakiet_Przedłużona_Gwarancja', css_class="extra"),

                                       ),

                    )
                    ),
                Tab('4. Opcje i Akcesoria',
                    layout.HTML("""
                                        <div class="row higg">
                                        <div class="column hig col-sm-6">

                                        <h3>Opcje i Akcesoria</h3>
                                        </div>

                                        <div class="column  pp col-sm-6">

                                        <button class="btn btn-primary nast continue" onclick="">Następny</button>
                                        <button class="btn btn-primary poprz">Poprzedni</button>
                                        </div>
                                        </div>
                                             """),
                    Accordion(
                        AccordionGroup('Opcje Mercedes',
                                       # Field('Dodatkowa_bateria', 'Opony_całoroczne', 'Spryskiwacze_reflektorów', 'Lampy_przeciwmgielne_z_funk_doświetlania_zakrętów', 'Ogrzewana_szyba_przednia', 'Siedzenie_kierowcy_komfortowe_hydrau_resorowane',
                                       #       'Pokrywa_schowka_na_środku_deski_rozdzielczej', 'Dodatkowe_ogrzewanie_wodne', 'Klimatyzacja_o_zwiększonej_wydajności', 'Dogrzewacz', 'Sygnalizator_cofania', 'Kierownica_wielofunkcyjna_z_komputerem_pokładowym', 'Alarm_antywłamaniowy_EDW', 'Pakiet_na_złe_drogi', 'Tempomat', 'Retarder',
                                       #       css_class="form-horizontal"),
                                       # active=True,
                                       Div(
                                           'Dodatkowa_bateria', 'Opony_całoroczne', 'Spryskiwacze_reflektorów', 'Lampy_przeciwmgielne_z_funk_doświetlania_zakrętów', 'Ogrzewana_szyba_przednia', 'Siedzenie_kierowcy_komfortowe_hydrau_resorowane',
                                           'Pokrywa_schowka_na_środku_deski_rozdzielczej', 'Dodatkowe_ogrzewanie_wodne', 'Klimatyzacja_o_zwiększonej_wydajności', 'Dogrzewacz', 'Sygnalizator_cofania', 'Kierownica_wielofunkcyjna_z_komputerem_pokładowym', 'Alarm_antywłamaniowy_EDW', 'Pakiet_na_złe_drogi', 'Tempomat', 'Retarder',
                                           template='oferty/order/opcje.html'
                                       ),


                                       ),
                        AccordionGroup('Opcje test',
                                       # Field('USB', 'DMC', 'Przedłużenie', 'WEBASTO_Suche_Part_No', 'WEBASTO_Mokre_Part_No', 'Drzwi_AutoCool', 'Rodzaj_bagażnika',
                                       #       'Ściana_separująca', 'Szyby_tylnie', 'Winda_załadunkowa','Jakie_półki','WiFi', 'DVBT', 'Lodówka','Lodówka_podschowkowa_TM', 'przyciski_STOP', 'Nietypowy_zderzak_przedni', 'Nietypowy_zderzak_tylni', 'Progi_boczne_spojlery',
                                       #        css_class="extra"),
                                       Div(
                                           'USB', 'DMC', 'Przedłużenie', 'WEBASTO_Suche_Part_No', 'WEBASTO_Mokre_Part_No', 'Drzwi_AutoCool', 'Rodzaj_bagażnika',
                                           'Ściana_separująca', 'Szyby_tylnie', 'Winda_załadunkowa','Jakie_półki','WiFi', 'DVBT', 'Lodówka','Lodówka_podschowkowa_TM', 'przyciski_STOP', 'Nietypowy_zderzak_przedni', 'Nietypowy_zderzak_tylni', 'Progi_boczne_spojlery',
                                           template='oferty/order/akcesoria.html'
                                       ),
                                       ),

                            )
                    ),
                Tab('5. Podumowanie',
                    layout.HTML("""
                                        <div class="row higg">
                                        <div class="column hig col-sm-6">

                                        <h3>Podsumowanie</h3>
                                        </div>

                                        <div class="column  pp col-sm-6">

                                        <button class="btn btn-primary nast continue" onclick="">Następny</button>
                                        <button class="btn btn-primary poprz">Poprzedni</button>
                                        </div>
                                        </div>
                                             """),
                    layout.HTML("""
                    <div class="column col-sm-6">
                     """),

                    layout.Fieldset(
                        _("Dane personalne"),
                        layout.Field("imię", placeholder="imię*", css_class="formpad"),
                        layout.Field("nazwisko", placeholder="nazwisko*", css_class="formpad"),
                        layout.HTML(u"""{% load i18n %}
                                  <br>
                          """),
                        layout.Field("ulica", placeholder="ulica", css_class="formpad"),
                        layout.Field("miasto", placeholder="miasto", css_class="formpad"),
                        layout.Field("kod_pocztowy", placeholder="kod pocztowy", css_class="formpad"),
                        # Div(
                        #     'kod_pocztowy',
                        #     template='oferty/order/my_div_template.html'
                        # ),
                        layout.HTML(u"""{% load i18n %}
                                          <br>
                                  """),
                        layout.Field("wiadomość", placeholder="wiadomość", css_class="formpad", rows="3"),
                    ),

                    layout.Fieldset(
                        _("Dane kontaktowe"),
                        layout.Field("NIP", placeholder="NIP/VAT*",
                                     css_class="formpad"),
                        layout.Div(
                            bootstrap.PrependedText("telefon",
                                                    """<span class="glyphicon glyphicon-earphone">
                                                    </span>""",
                                                    css_class="inputblock-level",
                                                    placeholder="+48700600500*"),
                            bootstrap.PrependedText("email", "@",
                                                    css_class="input-block-level",
                                                    placeholder="kontakt@example.com*"),
                            css_id="contact_info",
                        ),
                    ),
                    layout.HTML(u"""{% load i18n %}
                            <p class="help-block mar">{% trans "Załacznik zostanie automatycznie wysłany na wskazany adres email i można go wydrukować." %}</p>
                    """),

                    bootstrap.FormActions(
                        layout.Submit("submit", _("Wyślij Dane"),
                                      css_class="prawy"),
                    ),
                    layout.HTML("""
                            </div>
                             """),
                    layout.HTML("""
                            <div class="column col-sm-6">
                            <div style="padding-left:60px; padding-top:0px;">
                            <img src="/media/products/b43.png" style="width: 90%; border: 0px solid #999;"></div>
                             """),
                    )
            ),

        )
