from django.urls import path, include

from Car_Collection_App.web.views import index, catalogue, car_edit, car_create, \
    car_delete, car_details, profile_delete, profile_details, profile_edit, profile_create

urlpatterns = [
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('car/create', car_create, name='car create'),
    path('car/<int:pk>/', include([
        path('details/', car_details, name='car details'),
        path('edit/', car_edit, name='car edit'),
        path('delete/', car_delete, name='car delete')
    ])),
    path('profile/', include([
        path('create/', profile_create, name='profile create'),
        path('details/', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
    ])),
]
