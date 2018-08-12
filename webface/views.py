from django.views.generic import TemplateView

from webface.forms import NoteForm


class IndexView(TemplateView):
    template_name = 'webface/notes_list.html'

    def get_context_data(self, **kwargs):
        form = NoteForm()
        context = super().get_context_data(**kwargs)
        context['form'] = form
        context['title'] = 'Заметки'
        return context
