from django.shortcuts import render, redirect
from .models import Book, Thread
from .forms import BookForm,ThreadForm
from .utils import (
    process_wikipedia_info,
    generate_author_gpt_info,
    generate_audio_script,
    create_tts_audio,
)
from django.contrib.auth.decorators import login_required

def index(request):
    books = Book.objects.all()
    context = {
        "books": books,
    }
    return render(request, "books/index.html", context)

@login_required
def create(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)

            wiki_summary = process_wikipedia_info(book)

            author_info, author_works = generate_author_gpt_info(
                book, wiki_summary
            )
            book.author_info = author_info
            book.author_works = author_works
            book.save()

            audio_script = generate_audio_script(book, wiki_summary)

            audio_file_path = create_tts_audio(book, audio_script)
            if audio_file_path:
                book.audio_file = audio_file_path
                book.save()

            return redirect("books:detail", book.pk)
    else:
        form = BookForm()
    context = {"form": form}
    return render(request, "books/create.html", context)

@login_required
def detail(request, pk):
    book = Book.objects.get(pk=pk)
    threadform= ThreadForm()
    thread = book.thread_set.all()
    context = {
        "book": book,
        "thread":thread,
        'threadform':threadform,
    }
    return render(request, "books/detail.html", context)

@login_required
def update(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("books:detail", pk)
    else:
        form = BookForm(instance=book)
    context = {
        "form": form,
        "book": book,
    }
    return render(request, "books/update.html", context)

@login_required
def delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect("books:index")

@login_required
def create_thread(request,pk):

    if request.method == "POST":
        book = Book.objects.get(pk=pk)
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("books:detail", pk)
    form = ThreadForm()
    context={
        'form':form,
        'pk':pk
    }
    return render(request,"books/create_thread.html",context)
def thread_detail(request, pk):
    thread= Thread.objects.get(pk=pk)
    context={
        'thread':thread,
    }
    return render(request,'books/thread_detail.html', context)

