from django.urls import path
from .views import *

urlpatterns = [
    path('', GetStartView.as_view(), name='base.html'),
    path('dic/', testShowData, name='dic_view'),
    path('chart/<int:year>/<int:month>',ChartsView.as_view(), name='charts'),
    path('chart/json/', LineChartJSONView.as_view(), name='line_chart_json'),

    path('load/', LoadView.as_view(), name='load_data'),


]
