from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import Bill
from django.db.models import Q


class IndexView(ListView):
    template_name = 'index.html'
    model = Bill
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
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


class BillDetailView(DetailView):
    template_name = 'detail.html'
    model = Bill
