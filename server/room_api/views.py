from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
# Create your views here.

class RoomView(APIView):
    """docstring for RoomCategoryView."""

    def get(self, request):
        info = list(Rooms.objects.values())

        return Response(info)

class AvailableRoomsView(APIView):

    def get(self, request):
        c = Rooms.objects.filter(status__is_available='true')
        c = list(c.values()) # list(Status.objects.values())

        return Response(c)

class RoomRentalView(APIView):

    def get(self, request):
        a = list(RoomRentals.objects.values())

        return Response(a)


class ClientByPhoneView(APIView):

    def get(self, request, phone):
        res = list(Client.objects.filter(phone_no=phone).values())

        return Response(res)


class DontNoHowToNameView(APIView):

    def get(self, request):
        info = list(RoomRentals.objects.select_related().filter(room__status__is_available='false').values(name=F('client__fullname'), phone=F('client__phone_no'), floor=F('rooms__number'), start_at=F('start_at'), check_out_at=F('check_out_at')))

        return Response(info)




class ClientUpdateView(APIView): # update info client, bao gom  tat ca cac field trong bang client

    def patch(self,request,id):
        client_obj = Client.objects.get(id=id)
        client_obj.full_name = request.data["full_name"]
        client_obj.identify_card_no = request.data["identify_card_no"]
        client_obj.phone_no =  request.data["phone_no"]
        client_obj.email_address = request.data["email_address"]
        client_obj.post_number =  request.data["post_number"]
        client_obj.award_point =  request.data["award_point"]
        client_obj.notes =  request.data["notes"]
        client_obj.save()
        return Response({"Trang thai":" update thanh cong"})

class CategoryUpdateView(APIView):     #update a room category, bao gom tat ca cac field trong bang room categories

    def patch(self,request,id):
        res = RoomCategories.objects.get(id=id)
        res.name = request.data["name"]
        res.price = request.data["price"]
        res.note = request.data["note"]
        res.save()
        return Response({"Trang thai":" update thanh cong"})

class RentUpdateView(APIView):   # update rental, bao gom tat ca cac field trong bang room rental

    def patch(self,request,id):
        res = RoomRentals.objects.get(id=id)
        res.room = request.data["room"]
        res.client = request.data["client"]
        res.staff_create = request.data["staff_create"]
        res.create_at = request.data["create_at"]
        res.start_at = request.data["start_at"]
        res.check_out_at = request.data["check_out_at"]
        res.summary = request.data["summary"]
        res.save()
        return Response({"Trang thai":" update thanh cong"})


class CategoryDeleteView(APIView):   # delete a room category

    def detele(self,request,id):
        entry = RoomCategories.objects.get(id= id)
        entry.delete()
        return Response({"Trang thai":" delete thanh cong"})



class RentalsDeleteView(APIView):   # delete rentals

    def detele(self,request,id):
        entry = RoomRentals.objects.get(id= id)
        entry.delete()
        return Response({"Trang thai":" delete thanh cong"})

class ServiceDeleteView(APIView):   # delete service: chuyen is_canceled = true

    def patch(self,request,id):
        entry = RoomRentals.objects.get(client= id)
        entry1 = Services.objects.get(rental= entry.id)
        entry1.is_canceled = True
        entry1.save()
        return Response({"Trang thai":" delete thanh cong"})