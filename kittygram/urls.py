# через generic view-класс:
from django.urls import path

from cats.views import CatList, CatDetail

urlpatterns = [
    path('cats/', CatList.as_view()),
    path('cats/<int:pk>/', CatDetail.as_view()),
]



# через view-класс:
# urls.py
# from django.urls import path

# from cats.views import APICat

# urlpatterns = [
#     path('cats/', APICat.as_view()),
# ]



# через view-функции:
# from django.urls import path

# from cats.views import cat_list

# urlpatterns = [
#    path('cats/', cat_list),
# ]


