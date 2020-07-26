from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("about",views.about,name="About"),
    path("contact",views.contact,name="ContactUs"),
    path("tracker",views.track,name="TrackingStatus"),
    path("search",views.search,name="Search"),
    path("products",views.products,name="ProductViews"),
    path("checkout",views.checkout,name="CheckOut"),


]
