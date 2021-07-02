# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Client(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    full_name = models.CharField(max_length=29)
    identify_card_no = models.CharField(max_length=19)
    award_point = models.IntegerField()
    phone_no = models.CharField(max_length=12)
    email_address = models.CharField(max_length=34)
    post_number = models.IntegerField()
    notes = models.CharField(max_length=560)

    class Meta:

        db_table = 'client'


class RoomCategories(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    name = models.CharField(max_length=33)
    price = models.IntegerField()
    notes = models.CharField(max_length=568)

    class Meta:

        db_table = 'room_categories'


class RoomRentals(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    room = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='room')
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client')
    staff_create = models.ForeignKey('Staff', models.DO_NOTHING, db_column='staff_create')
    create_at = models.DateField()
    start_at = models.DateField()
    check_out_at = models.CharField(max_length=19)
    summary = models.CharField(max_length=487)

    class Meta:

        db_table = 'room_rentals'


class Rooms(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    category = models.ForeignKey(RoomCategories, models.DO_NOTHING, db_column='category')
    status = models.ForeignKey('Status', models.DO_NOTHING, db_column='status')
    floors = models.IntegerField()
    number = models.IntegerField()

    class Meta:

        db_table = 'rooms'


class ServiceTypes(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=568)
    unit_price = models.CharField(max_length=86)

    class Meta:

        db_table = 'service_types'


class Services(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    type = models.ForeignKey(ServiceTypes, models.DO_NOTHING, db_column='type')
    rental = models.ForeignKey(RoomRentals, models.DO_NOTHING, db_column='rental')
    created_at = models.DateField()
    is_canceled = models.CharField(max_length=5)
    quantity = models.IntegerField()
    sub_total = models.IntegerField()
    detail = models.CharField(max_length=557)

    class Meta:

        db_table = 'services'


class Staff(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    full_name = models.CharField(max_length=34)
    post_number = models.IntegerField()
    email_address = models.CharField(max_length=32)
    phone_no = models.CharField(max_length=12)
    identity_card_no = models.CharField(max_length=19)
    address = models.CharField(max_length=42)
    is_manager = models.CharField(max_length=5)

    class Meta:

        db_table = 'staff'


class Status(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    title = models.CharField(max_length=36)
    descriptions = models.CharField(max_length=548)
    is_available = models.CharField(max_length=5)

    class Meta:

        db_table = 'status'
