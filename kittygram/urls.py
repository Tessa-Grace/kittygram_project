# через view-класс:
# urls.py
from django.urls import path

from cats.views import APICat

urlpatterns = [
    path('cats/', APICat.as_view()),
]



# через view-функции:
# from django.urls import path

# from cats.views import cat_list

# urlpatterns = [
#    path('cats/', cat_list),
# ]


