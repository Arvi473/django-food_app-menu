from . import views
from django.urls import path

app_name = 'food_app'
urlpatterns = [
    #/food_app/
    path('',views.IndexClassView.as_view(),name='index'),
    #/food_app/1
    path('<int:pk>/',views.Food_appDetail.as_view(),name='detail'),
    path('item/',views.item,name='item'),
    # add items
    path('add',views.CreateItem.as_view(),name='create_item'),
    # edit
    path('update/<int:id>/',views.update_item,name='update_item'),
    # delete
    path('delete/<int:id>,',views.delete_item,name='delete_item'),


    #path('recipe/',views.recipe,name='recipe'),
    #path('rating/',views.rating,name='rating'),
    #path('review/',views.review,name='review'),
]