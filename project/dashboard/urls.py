
from django.urls import path 
from dashboard import views
urlpatterns = [
    path('worker/' , views.worker , name="worker" ) , 
    path("myprofile/" , views.profile , name="myprofile") ,
    path("worker-details/" , views.worker_deatil , name="workers Deatil") ,
    path("customer/" , views.customer , name="customer") ,
    path("customer/about" , views.customer_about , name="about") ,
    path("customer/service" , views.customer_service , name="service") ,
    path("search/workers" , views.worker_list ,name="workerList") ,
    path("customer/profile" , views.profile ,name="customerProfile" ) ,
    path("worker/profile" , views.profile ,name="workerProfile" ) ,
    path("workers/<int:pk>/", views.WorkerProfileView.as_view(), name="worker_profile"),
    path("worker/request" , views.worker_req , name="worker_request")  ,
    path("worker/ongoing-job" , views.worker_ongoing , name="worker_ongoing")  ,
    path("worker/complete-jobs" , views.worker_completed , name="worker_completed")  ,
    
]
  