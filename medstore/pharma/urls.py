from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),

    path('dealerform/', views.dealerform, name="dealerform"),
    path('dealerforminsert/', views.dealerforminsert, name="dealerforminsert"),
    path('dealerformupdate/<int:idlink>/', views.dealerformupdate, name="dealerforminsert"),
    path('dealerformview/<int:idlink>/', views.dealerformview, name="dealerformview"),
    path('dealerformdelete/<int:ididlink>/', views.dealerformdelete, name="dealerformdelete"),
    path('dealertable/', views.dealertable, name='dealertable'),

    path('medform/', views.medform, name="medform"),
    path('medforminsert/', views.medforminsert, name="medforminsert"),
    path('medformupdate/<int:id>/', views.medformupdate, name="medformupdate"),
    path('medformview/<int:id>/', views.medformview, name="medformview"),
    path('medformdelete/<int:id>/', views.medformdelete, name="medformdelete"),
    path('medtable/', views.medtable, name='medtable'),

    path('empform/', views.empform, name="empform"),
    path('empforminsert/', views.empforminsert, name="empforminsert"),
    path('empformupdate/<int:id>/', views.empformupdate, name="empformupdate"),
    path('empformview/<int:id>/', views.empformview, name="empformview"),
    path('empformdelete/<int:id>/', views.empformdelete, name="empformdelete"),
    path('emptable/', views.emptable, name='emptable'),

    path('custform/', views.custform, name="custform"),
    path('custforminsert/', views.custforminsert, name="custforminsert"),
    path('custformupdate/<int:id>/', views.custformupdate, name="custformupdate"),
    path('custformview/<int:id>/', views.custformview, name="custformview"),
    path('custformdelete/<int:id>/', views.custformdelete, name="custformdelete"),
    path('custtable/', views.custtable, name='custtable'),

    path('purchaseform/', views.purchaseform, name="purchaseform"),
    path('purchaseforminsert/', views.purchaseforminsert, name="purchaseforminsert"),
    path('purchaseformupdate/<int:id>/', views.purchaseformupdate, name="purchaseformupdate"),
    path('purchaseformview/<int:id>/', views.purchaseformview, name="purchaseformview"),
    path('purchaseformdelete/<int:id>/', views.purchaseformdelete, name="purchaseformdelete"),
    path('purchasetable/', views.purchasetable, name='purchasetable')
]