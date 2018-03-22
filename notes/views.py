from django.shortcuts import render, redirect, get_object_or_404

from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions

from . import models
from .models import Notes
from .forms import NoteForm, DeleteNote

from . import serializers


def index(request):
    all_notes = Notes.objects.all().order_by('-date')
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('notes:detail', note.id)
    else:
        form = NoteForm()
    number = Notes.objects.all().count()
    modulus = number % 10
    return render(request, 'notes/index.html', {'all_notes' : all_notes, 'form' : form, 'number':number, 'modulus':modulus})

def detail(request, note_id):
    note = Notes.objects.get(pk=note_id)
    form = DeleteNote()
    return render(request, 'notes/detail.html', {'note' : note, 'form' : form})

def delete_note(request, note_id):
    note_to_delete = get_object_or_404(Notes, pk=note_id)
    if request.method == 'POST':
        form = DeleteNote(request.POST, instance=note_to_delete)
        if form.is_valid():
            note_to_delete.delete()
            return redirect('notes:index')
    else:
        return render(request, 'notes/if_delete.html')
    return render(request, 'notes/index.html', {'form' : form})

def note_edit(request, note_id):
    note = get_object_or_404(Notes, pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('notes:detail', note_id)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/edit.html', {'form':form})

class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        else:
            if request.method == 'DELETE':
                return False
            else:
                return True

class ListCreateNote(generics.ListCreateAPIView):
    queryset = models.Notes.objects.all()
    serializer_class = serializers.NoteSerializer

class RetrieveUpdateDestroyNote(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Notes.objects.all()
    serializer_class = serializers.NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsSuperUser,
        permissions.DjangoModelPermissions,
    )
    queryset = models.Notes.objects.all()
    serializer_class = serializers.NoteSerializer