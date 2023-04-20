from django.shortcuts import render
from .models import shopping_index, Shopping_detail
import plotly.graph_objs as go
from plotly.offline import plot

# Create your views here.

def shoppingindex(request):
    shopping_items = shopping_index.objects.all()
    return render(request, 'shopping/shopping_index.html', {'shopping_items':shopping_items})

def shoppingdetail(request):
    shopping_details = Shopping_detail.objects.all()
    return render(request, 'shopping/shopping_detail.html', {'shopping_details': shopping_details})

def product_by_name(request, value):
    produce_noorder = Shopping_detail.objects.filter(product_name=value)
    produces = produce_noorder.order_by('date')
    produce = produces.first()
    if produce.latitude.endswith('N'):
        produces_lat = float(produce.latitude[:-1])
    else:
        produces_lat = -float(produce.latitude[:-1])
    if produce.longitude.endswith('E'):
        produces_lng = float(produce.longitude[:-1])
    else:
        produces_lng = -float(produce.longitude[:-1])

    x_data = [produce.date for produce in produces]
    y_data = [float(produce.price) for produce in produces]
    trace = go.Scatter(x=x_data, y=y_data, mode='markers')
    data = [trace]
    layout = go.Layout(title='Price Trends ' + value, xaxis=dict(title='Date'), yaxis=dict(title='price'))
    fig = go.Figure(data=data, layout=layout)
    div = fig.to_html(full_html=False)
    context = {
        'produces': produces,
        'produces_lat': produces_lat,
        'produces_lng': produces_lng,
        'plot_div': div,
        'produce_noorder': produce_noorder,
    }
    return render(request, 'shopping/product_by_name.html', context)


def check_by_date(request, date):
    datesnoorder = Shopping_detail.objects.filter(date=date)
    dates = datesnoorder.order_by('price')
    x_data = [product.uniq_id for product in dates]
    y_data = [float(date.price) for date in dates]
    trace = go.Scatter(x=x_data, y=y_data, mode='markers')
    data = [trace]
    layout = go.Layout(title='Shopping Detail on ' + str(date), xaxis=dict(title='uniq_id'), yaxis=dict(title='price'))
    fig = go.Figure(data=data, layout=layout)
    div = fig.to_html(full_html=False)
    context = {
        'dates': dates,
        'plot_div': div,
    }
    return render(request, 'shopping/check_by_date.html', context)







