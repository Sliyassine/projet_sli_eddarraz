from django.urls import path
from . import views
from . import api
urlpatterns=[
path("api/",api.dhtser,name='json'),



path('charthu',views.charthu,name='charthu'),
path('chart_TEMP_jour',views.chart_TEMP_jour,name='charttem'),
path('chartHUM_jour',views.chart_hum_jour,name='chartHUM24'),
path('chartTEMP_semaine',views.chart_TEMP_semaine,name='chartTEMP2'),
path('chartHUM_semaine',views.chart_HUM_semaine,name='chartHUM4'),
path('chartTEMP_mois',views.chart_TEMP_mois,name='chartTEMPM'),
path('chartHUM_mois',views.chart_HUM_mois,name='chartHUMM'),
path('download_csv', views.download_csv, name='csv'),
path('csv_semaine',views.csv_semaine,name='csvS'),
path('csv_mois',views.csv_mois,name='csvM'),
path('csv_jour',views.csv_jour,name='csvJ'),
path('',views.index,name='index'),

path('temperature.html',views.table,name='temperature'),
path('humidite.html',views.humidite,name='humidite'),

]

