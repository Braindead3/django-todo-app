from .models import Note, Group
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class NoteList(ListView):
    model = Note
    template_name = 'todo/home.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Note.objects.filter(user=self.request.user).order_by('-creation_time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            if context['object_list']:
                context['object_list'] = context['object_list'].filter(title__icontains=search_input)

        group = self.kwargs.get('group_id') or ''
        if group:
            if context['object_list']:
                context['object_list'] = context['object_list'].filter(group=group)

        context['all_groups'] = Group.objects.all()
        context['selected_group'] = context['all_groups'].filter(id=group).first()
        context['search_input'] = search_input

        return context


class NoteDetail(LoginRequiredMixin, DetailView):
    model = Note


class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'content', 'complete', 'group']
    success_url = reverse_lazy('todo-home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NoteCreate, self).form_valid(form)


class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'content', 'complete']
    success_url = reverse_lazy('todo-home')


class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('todo-home')


class GroupCreate(LoginRequiredMixin, CreateView):
    model = Group
    fields = ['title']
    success_url = reverse_lazy('todo-home')


class GroupUpdate(LoginRequiredMixin, UpdateView):
    model = Group
    fields = ['title']
    success_url = reverse_lazy('todo-home')


class GroupDelete(LoginRequiredMixin, DeleteView):
    model = Group
    success_url = reverse_lazy('todo-home')
