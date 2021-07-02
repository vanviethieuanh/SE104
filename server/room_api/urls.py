from django.conf.urls import url
from django.urls import path,re_path
from . import views

urlpatterns = [
    url(r'^get_room/', views.RoomView.as_view()),
    url(r'^get_room_rental/', views.RoomRentalView.as_view()),
    url(r'^get_available_room/', views.AvailableRoomsView.as_view()),
    url(r'^get_client_by_phone/', views.ClientByPhoneView.as_view()),
    url(r'^get_dont_know_how_to_name/', views.DontNoHowToNameView.as_view()),
    path(r'client/<id>', views.ClientUpdateView.as_view()),
    path(r'room_category/<id>', views.CategoryUpdateView.as_view()),
    path(r'rent/<id>', views.RentUpdateView.as_view()),
    path(r'delete_room_catagory/<id>', views.CategoryDeleteView.as_view()),
    path(r'delete_rental/<id>', views.RentalsDeleteView.as_view()),
    path(r'delete_service/<id>', views.ServiceDeleteView.as_view()),
]
