from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import Bill
from django.db.models import Q


class HomeView(ListView):
    template_name = '../templates/home.html'
    model = Bill
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get('q')
        qs = super().get_queryset(*args, **kwargs)

        if query:
            return qs.filter(Q(description__icontains=query)).order_by('-id')
        else:
            return qs.order_by('-id')


class BillCreateView(CreateView):
    model = Bill
    template_name = '../templates/create.html'
    fields = ['type', 'due_date', 'payday', 'amount', 'active', 'description']


class EditView(UpdateView):
    template_name = '../templates/edit.html'
    model = Bill
    fields = ['type', 'due_date', 'payday', 'amount', 'active', 'description']
    context_object_name = 'bill'


class BillDeleteView(DeleteView):
    template_name = '../templates/delete.html'
    model = Bill
    success_url = reverse_lazy('home')


class BillDetailView(DetailView):
    template_name = '../templates/detail.html'
    model = Bill
