from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, ListView
from .utils import *
from django.db.models import Q

from chartjs.views.lines import BaseLineChartView

URL = 'https://minfin.com.ua/currency/mb/archive/usd/20-09-2005/23-04-2020/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

YEAR=2006
MONTH=1

def get_year():
    return YEAR


class ChartsView(View):
    template_name = 'chart1.html'
    mon = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct',
           11: 'Nov', 12: 'Dec'}

    def get(self, request, year=YEAR, month=MONTH):
        global YEAR
        global MONTH
        YEAR=year
        MONTH=month
        return render(request, template_name=self.template_name,
                      context=({'mon': self.mon,'year':YEAR}))


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        qset = Usd.objects.filter(Q(date__year=YEAR) & Q(date__month=MONTH))
        xAxis = []
        for item in qset:
            xAxis.append(item.date)
        return xAxis

    def get_providers(self):
        """Return names of datasets."""
        return ["Buying", "sell"]

    def get_data(self, year=YEAR, month=MONTH):
        """Return 2 datasets to plot."""
        queryset = Usd.objects.filter(Q(date__year=YEAR) & Q(date__month=MONTH))
        aList = []
        bList = []
        for item in queryset:
            aList.append(item.buy)
            bList.append(item.sale)
        return ([aList, bList])


class GetStartView(View):
    def get(self, request):
        return render(request, template_name='base.html')


def testShowData(request):
    html = get_html(URL, HEADERS)
    rows = get_content(html.text)
    saveToDB(rows)

    return HttpResponse('OK')


class LoadView(View):
    template_name = 'load.html'
    context_object_name = 'cont'

    def get(self, request):
        years = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
        return render(request, template_name=self.template_name,
                      context={'cont': years})

