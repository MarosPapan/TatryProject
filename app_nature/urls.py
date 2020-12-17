from django . urls import path
from . import views

urlpatterns = [
    path("", views.homepage,name="homepage"),
    path("peaks/<int:mountain_id>", views.all_peaks, name="all_peaks"),
    path("peak_inf/<int:peak_id>/", views.detail, name="detail"),
    path("profile/", views.profilePage, name="profile"),
    path("add_post/", views.AddPost, name="add_post"),
]