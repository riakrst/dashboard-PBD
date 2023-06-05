import pymongo
import pandas as pd
from django.shortcuts import render

# MongoDB Connection
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['datakelahiranDB']

# Collection Names
collection1 = db['dashboard_data2018']
collection2 = db['dashboard_data2019']
collection3 = db['dashboard_data2020']



def show_data(request):
    collections1 = collection1.find()
    collections2 = collection2.find()
    collections3 = collection3.find()
    context = {
        'collections1': collections1,
        'collections2': collections2,
        'collections3': collections3,
    }
    return render(request, 'tables-data.html', context)

def search(request):
    query = request.GET.get('query', '')  # Retrieve the search query from the request
    if query.isnumeric():
        query = int(query)
        query_filter = {'$eq': query}
    else:
        query_filter = {'$regex': query, '$options': 'i'}
    # Perform the search query on collection1
    results1 = collection1.find({
        '$or': [
            {'tahun': query_filter},
            {'wilayah': query_filter},
            {'jumlah_bayi_lahir': query_filter},
            {'kondisi_bayi': query_filter},
            {'jumlah': query_filter}
        ]
    })

    # Perform the search query on collection2
    results2 = collection2.find({
        '$or': [
            {'tahun': query_filter},
            {'wilayah': query_filter},
            {'jumlah_bayi_lahir': query_filter},
            {'kondisi_bayi': query_filter},
            {'jumlah': query_filter}
        ]
    })

    # Perform the search query on collection3
    results3 = collection3.find({
        '$or': [
            {'tahun': query_filter},
            {'wilayah': query_filter},
            {'jumlah_bayi_lahir': query_filter},
            {'kondisi_bayi': query_filter},
            {'jumlah': query_filter}
        ]
    })

    context = {
        'results1': results1,
        'results2': results2,
        'results3': results3,
        'query': query,
    }

    return render(request, 'search_results.html', context)
