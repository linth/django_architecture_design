from django.shortcuts import render
from .models import Book


def index(request):
    template = 'index.html'

    # show all book.
    b = Book.objects\
        .get_all()

    # show less than 100 pages for book.
    less_100_page_book = Book.objects\
        .get_book_for_less_100_pages()

    context = {
        "all_book": b,
        "less_100_page_book": less_100_page_book,
    }
    return render(request, template, context)
