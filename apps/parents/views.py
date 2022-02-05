from django.views.generic import DetailView, ListView

from .models import parents


class parentList(ListView):
    model = parents
    paginate_by = 3
    template_name = 'front/list.html'


class parentDetailView(DetailView):

    model = parents
    template_name = 'front/detail.html'

    def get_context_data(self, **kwargs):

        return {
            'parent': parents.get_by_pk(self.kwargs['pk'])
        }
