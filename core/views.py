from django.db.models import Min, Sum
from .models import *

import pandas as pd
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render



def viewData(request):
    context = {
        "overall_sale_by_country": Data.objects.all().order_by("year"),
    }
    return render(request, "index.html", context)


def AllSale(request):
    context = {
        "result": Data.objects.filter(sale__gt=0)
        .values("country", "product")
        .annotate(Sum("sale"))
        .order_by("country")
    }
    return render(request, "AllSale.html", context)


def avg_sale_of_2years(request):
    data = Data.objects.all().values("year", "sale", "country", "product")
    data = pd.DataFrame(list(data))

    data["year"] = pd.to_datetime(data["year"], format="%Y")
    final_df = (
        data.groupby(["product", pd.Grouper(key="year", freq="2Y", closed="left")])
        .agg(
            {
                "year": lambda x: "-".join((str(min(x.dt.year)), str(max(x.dt.year)))),
                "sale": "mean",
            },
            data["sale"],
        )
        .reset_index(level=0)
        .reset_index(drop=True)
    )

    html = final_df.to_html(border=1, table_id="design", col_space=125)
    context = {
        "result": html,
    }
    return render(request, "avgSale.html", context)


def least_sale_list(request):
    data = (
        Data.objects.filter(sale__gt=0).values("product").annotate(min_sale=Min("sale"))
    )
    final_data = Data.objects.filter(sale__in=data.values("min_sale"))
    context = {
        "result": final_data,
    }
    return render(request, "leastSale.html", context)


class Find:
    def getData(self, request):
        if request.method == "GET":
            year = request.GET.get("years")
            product = request.GET.get("products")
            country = request.GET.get("countries")

            data = get_object_or_404(
                Data, year=year, product=product, country=country
            )

            return data
        else:
            pass
years = [2007,2008,2009,2010,2011,2012,2013,2014]
countries = ['Isereal','Russia','Saudi Arabia','Isereal']
products = ['Light Diesel Oil','LPG in MT','Mineral Turpentine Oil','Furnace Oil','Diesel','Kerosene','Aviation Turbine Fuel','Petrol']



def landing(request):
    if request.method == "GET":
        if 'getData' in request.GET:
            try:
                s = Find()
                result = s.getData(request)
                context = {
                    "result": result,
                    "year":years,
                    "country":countries,
                    "product":products,
                }
            except Http404 as e:
                err = e
                context = {
                    "error": err,
                    "year":years,
                    "country":countries,
                    "product":products,
                }
        else:
            context={
                "result":False,
                "error":False,
                "year":years,
                "country":countries,
                "product":products,
            }  
    return render(request, "land.html", context)
