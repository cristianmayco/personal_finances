from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Bill


class IndexView(ListView):
    template_name = 'index.html'
    model = Bill

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bills'] = Bill.objects.order_by('-id')
        return context


class BillCreateView(CreateView):
    model = Bill
    template_name = 'create.html'
    fields = ['type', 'due_date', 'payday', 'amount', 'active', 'description']


class EditView(UpdateView):
    template_name = 'edit.html'
    model = Bill
    fields = ['type', 'due_date', 'payday', 'amount', 'active', 'description']
    context_object_name = 'bill'


class BillDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Bill
    success_url = reverse_lazy('index')
