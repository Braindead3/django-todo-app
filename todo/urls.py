from django.urls import path
from .views import NoteList, NoteDetail,NoteCreate, NoteUpdate,NoteDelete

urlpatterns = [
    path('', NoteList.as_view(), name='todo-home'),
    path('<int:group_id>/', NoteList.as_view(), name='todo-home-group'),
    path('note/<int:pk>/', NoteDetail.as_view(), name='note'),
    path('note/create/', NoteCreate.as_view(), name='note-create'),
    path('note/update/<int:pk>/', NoteUpdate.as_view(), name='note-update'),
    path('note/delete/<int:pk>/', NoteDelete.as_view(), name='note-delete'),
]
