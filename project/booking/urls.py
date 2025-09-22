
from django.urls import path 
from booking import views


app_name = 'booking' 
urlpatterns = [
    path('worker/<int:worker_id>/',views.BookingCreateView.as_view() , name="book_worker" )
]