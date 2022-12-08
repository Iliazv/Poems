from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from books.models import Poet, Poem, Comment
from django.template import loader
from django.db.models import Q
from django.utils import timezone
from django.urls import reverse
import datetime


def show_main(request):
    list_poets = Poet.objects.all().order_by('name')
    equal_slice = len(list_poets)
    list_poems = Poem.objects.all()[:equal_slice]
    temlate = loader.get_template('books/main.html')
    content_poets = {'list_poets': list_poets, 'list_poems': list_poems}
    return HttpResponse(temlate.render(content_poets, request))

def show_poets(request):
    list_poets = Poet.objects.all().order_by('name')
    equal_slice = len(list_poets)
    list_poems = Poem.objects.all()[:equal_slice]
    temlate = loader.get_template('books/list_poets.html')
    content_poets = {'list_poets': list_poets, 'list_poems': list_poems}
    return HttpResponse(temlate.render(content_poets, request))

def show_list_poems(request):
    list_poems = Poem.objects.all()
    temlate = loader.get_template('books/list_poems.html')
    content_poets = {'list_poems': list_poems}
    return HttpResponse(temlate.render(content_poets, request))

def show_poems(request, poet_id):
    poet = Poet.objects.get(id = poet_id)
    list_poems = poet.poem_set.all()
    poet_name = poet.name + ' '+ poet.lastname
    URL = poet.url
    template = loader.get_template('books/poems.html')
    content = {'list_poems': list_poems, 'poet': poet, 'poet_id': poet_id, 'poet_name': poet_name, 'URL': URL}
    return HttpResponse(template.render(content, request))

def display_poem(request, arg1):
    poem = Poem.objects.get(id = arg1)
    text = poem.poem_text
    poet_name = poem.connect_question.name + ' ' + poem.connect_question.lastname
    poem_name = poem.poem_name
    list_commentaries = poem.comment_set.order_by('-date')
    condition3 = 1
    poet_id = poem.connect_question.id
    if poem.rating != 0:
        poem.rank = '{:.2f}'.format((poem.rating / poem.votes))
    else: poem.rank = 0
    rank = poem.rank
    template = loader.get_template('books/poem_page.html')
    content = {'text': text, 'poem_name': poem_name, 'poet_name': poet_name, 
               'list_commentaries': list_commentaries,'arg1': arg1, 'rank': rank,
               'poet_id': poet_id, 'condition3': condition3}
    return HttpResponse(template.render(content, request))

def display_searched(request, arg1, arg2):
    poem = Poem.objects.get(id = arg1)
    text = poem.poem_text
    name_poem = poem.poem_name
    poet_name = poem.connect_question
    list_commentaries = poem.comment_set.order_by('-date')
    search_text = arg2
    condition4 = 1
    if poem.rating != 0:
        poem.rank = '{:.2f}'.format((poem.rating / poem.votes))
    else: poem.rank = 0
    poem.save()
    rank = poem.rank
    template = loader.get_template('books/text_poem.html')
    link = request.META.get('HTTP_REFERER')
    content = {'text': text, 'name_poem': name_poem, 'poet_name': poet_name,
               'list_commentaries': list_commentaries, 'arg1': arg1, 
               'rank': rank, 'condition4': condition4, 'link': link, 
               'search_text':search_text}

    return HttpResponse(template.render(content, request))

def display_popular(request, arg1):
    poem = Poem.objects.get(id = arg1)
    text = poem.poem_text
    name_poem = poem.poem_name
    poet_name = poem.connect_question
    list_commentaries = poem.comment_set.order_by('-date')
    poet_id = poem.connect_question.id
    condition1 = 1
    if poem.rating != 0:
        poem.rank = '{:.2f}'.format((poem.rating / poem.votes))
    else: poem.rank = 0
    poem.save()
    rank = poem.rank
    template = loader.get_template('books/text_poem.html')
    content = {'text': text, 'name_poem': name_poem, 'poet_name': poet_name,
               'list_commentaries': list_commentaries, 'arg1': arg1, 
               'rank': rank, 'condition1': condition1, 'poet_id': poet_id}
    return HttpResponse(template.render(content, request))

def display_new(request, arg1):
    link = request.META.get('HTTP_REFERER')
    poem = Poem.objects.get(id = arg1)
    text = poem.poem_text
    name_poem = poem.poem_name
    poet_name = poem.connect_question
    list_commentaries = poem.comment_set.order_by('-date')
    poet_id = poem.connect_question.id
    condition2 = 1
    if poem.rating != 0:
        poem.rank = '{:.2f}'.format((poem.rating / poem.votes))
    else: poem.rank = 0
    poem.save()
    rank = poem.rank
    template = loader.get_template('books/text_poem.html')
    content = {'text': text, 'name_poem': name_poem, 'poet_name': poet_name,
               'list_commentaries': list_commentaries, 'arg1': arg1, 
               'rank': rank, 'condition2': condition2, 'poet_id': poet_id,
               'link': link}
    return HttpResponse(template.render(content, request))

def show_searched(request, search_text=''):
    try:
        search_text = request.POST.get('text')
        search_text = search_text.capitalize()
    except: pass
    if search_text == '':
        return show_poets(request)
    searched_poems = []
    for e in Poem.objects.all():
        if search_text in e.poem_name:
            searched_poems.append((e.poem_name, e.id))
    data = Poem.objects.filter(Q(poem_name__istartswith=search_text))
    condition4 = 1
    template = loader.get_template('books/searched_poems.html')
    content = {'data': data, 'searched_poems': searched_poems, 'search_text': search_text, 
               'condition4': condition4}
    return HttpResponse(template.render(content, request))

def show_searched_again(request, arg1, search_text):
    if search_text == '':
        return show_poets(request)
    searched_poems = []
    for e in Poem.objects.all():
        if search_text in e.poem_name:
            searched_poems.append((e.poem_name, e.id))
    data = Poem.objects.filter(Q(poem_name__istartswith=search_text))
    condition4 = 1
    template = loader.get_template('books/searched_poems.html')
    content = {'data': data, 'searched_poems': searched_poems, 'search_text': search_text, 
               'condition4': condition4}
    return HttpResponse(template.render(content, request))
   

def create_comment(request, arg1):
    name_comment = request.POST.get('name_field')
    text_comment = request.POST.get('text_field')
    poem = Poem.objects.get(id = arg1)
    if name_comment == '' or text_comment == '':
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    poem.comment_set.create(name_author = name_comment, comment = text_comment, date = timezone.now())  
    if poem.rating != 0:
        poem.rank = '{:.2f}'.format((poem.rating / poem.votes))
    else: poem.rank = 0
    poem.save()
    rank = poem.rank
    poem = Poem.objects.get(id = arg1)
    text = poem.poem_text
    name_poem = poem.poem_name
    poet_name = poem.connect_question
    list_commentaries = poem.comment_set.order_by('-date')
    template = loader.get_template('books/poem_page.html')
    content = {'text': text, 'name_poem': name_poem, 'poet_name': poet_name,
               'list_commentaries': list_commentaries, 'arg1': arg1, 'rank': rank,
               }
    return HttpResponse(template.render(content, request))

def vote(request, arg1):
    data = request.POST.get('rating')
    data = int(data)
    poem = Poem.objects.get(id = arg1)
    
    poem.rating += data
    poem.votes += 1
    poem.save()
    if poem.rating != 0:
        poem.rank = '{:.2f}'.format((poem.rating / poem.votes))
    else: poem.rank = 0
    poem.save()
    rank = poem.rank
    text = poem.poem_text
    name_poem = poem.poem_name
    poet_name = poem.connect_question
    list_commentaries = poem.comment_set.order_by('-date')
    template = loader.get_template('books/poem_page.html')
    content = {'text': text, 'name_poem': name_poem, 'poet_name': poet_name,
               'list_commentaries': list_commentaries, 'arg1': arg1, 
               'rank': rank}
    return HttpResponse(template.render(content, request))



def show_new(request):
    new_poems = Poem.objects.all()
    new_poems = new_poems.filter(Q(old=False))
    template = loader.get_template('books/new_poems.html')
    content = {'new_poems': new_poems}
    return HttpResponse(template.render(content, request))

def show_popular(request):
    popular_poems = Poem.objects.all()
    popular_poems = popular_poems.exclude(rank=0).order_by('-rank')
    template = loader.get_template('books/popular_poems.html')
    content = {'popular_poems': popular_poems}
    return HttpResponse(template.render(content, request))

def golden_century(request):
    golden_poets = Poet.objects.all()
    golden_poets = golden_poets.filter(Q(century="golden"))
    
    template = loader.get_template('books/golden_century.html')
    content = {'golden_poets': golden_poets}
    return HttpResponse(template.render(content, request))

def silver_century(request):
    silver_poets = Poet.objects.all()
    silver_poets = silver_poets.filter(Q(century="silver"))

    template = loader.get_template('books/silver_century.html')
    content = {'silver_poets': silver_poets}
    return HttpResponse(template.render(content, request))
