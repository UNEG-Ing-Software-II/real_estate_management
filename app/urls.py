from django.urls import path
from app.views.UserLogController import UserLogController
from app.views.UserController import UserController
from app.views.EstateController import EstateController
from app.views.AreaController import AreaController


urlpatterns = [

    # UserLogController
    path('',UserLogController.home,name='home'),
    path('login', UserLogController.sign_in, name = 'login'),
    path('sign_up', UserLogController.sign_up, name='sign_up'),
    path('sign_off', UserLogController.sign_off, name='sign_off'),
    path('my_account',UserLogController.my_account, name='my_account'),

    # #Estate
    path("estate/<int:estate_id>/", EstateController.read, name="estate"), #URL view to modify/eliminate property
    path("estate/create", EstateController.create, name="estate_create"),
    path("estate/update", EstateController.update, name="estate_update"),
    path("estate/delete", EstateController.delete, name="estate_delete"),

    #User
    path("save_owner", UserController.save_owner, name="save_owner"),
    path("unlink_owner", UserController.unlink_owner, name="unlink_owner"),
    path("search_owner", UserController.search_owner, name="search_owner"),
    path("validate_owner", UserController.validate_owner, name="validate_owner"),

    #Area
    path("area/create", AreaController.create, name="area_create"),
    path("area/delete", AreaController.delete, name="area_delete"),
    path("area/update", AreaController.update, name="area_update"),
]
