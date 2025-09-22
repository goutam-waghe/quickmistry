from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Booking 
from users.models import User
from .forms import BookingForm
class BookingCreateView(LoginRequiredMixin , CreateView):
    login_url = 'users/login/'
    model = Booking
    template_name = "booking/booking_form.html"
    form_class = BookingForm
    # fields = ["scheduled_date" , "description"]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        worker = get_object_or_404(User, id=self.kwargs["worker_id"], role="worker")
        context['worker'] = worker
        return context

    def form_valid(self, form):
        form.instance.customer = self.request.user
        form.instance.worker_id = self.kwargs["worker_id"]
        # Get worker from URL (passed as worker_id)
        worker = get_object_or_404(User, id=self.kwargs["worker_id"], role="worker")
        print(worker)
        form.instance.worker = worker
        # Auto-assign category from worker
        form.instance.service_category = worker.serviceCategory
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("customer")