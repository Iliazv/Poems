import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Poet, Poem, Comment
    
def create_comment(connect_question, name_author, comment, date):
    return Comment.objects.create(connect_question=connect_question, name_author=name_author, 
                                  comment=comment, date=date)

def create_poet(name, lastname, url):
    return Poet.objects.create(name=name, lastname=lastname, url=url)

def create_poem(connect_question, poem_name, poem_text, rating, votes, rank, old):
    return Poem.objects.create(connect_question=connect_question, poem_name=poem_name, 
                               poem_text=poem_text, rating=rating, votes=votes, rank=rank, old=old)
        
class MainPageTests(TestCase):
    def test_menu_empty(self):
        response = self.client.get(reverse('poets'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Список поэтов пуст')
        self.assertQuerysetEqual(response.context['list_poets'], [])
    
    def test_menu_content(self):
        poet = create_poet('Ilia', 'Zhelenkov', '')
        response = self.client.get(reverse('poets'))
        self.assertQuerysetEqual(response.context['list_poets'], [poet])
    
    def test_footer(self):
        response = self.client.get(reverse('poets'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Оффициальные группы сайта:')
 
    
class NewPageTests(TestCase):
    def test_new_empty(self):
        response = self.client.get(reverse('show_new'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Список современных стихотворений пуст')
        self.assertQuerysetEqual(response.context['new_poems'], [])
        
    def test_view_new(self):
        poet = create_poet('Ilia', 'Zhelenkov', '')
        poem = create_poem(poet, 'Clouds', 'abc', 0, 0, 0, False)
        response = self.client.get(reverse('show_new'))
        self.assertQuerysetEqual(response.context['new_poems'], [poem])
        
    def test_view_old(self):
        poet = create_poet('Ilia', 'Zhelenkov', '')
        poem = create_poem(poet, 'Clouds', 'abc', 0, 0, 0, True)
        response = self.client.get(reverse('show_new'))
        self.assertQuerysetEqual(response.context['new_poems'], [])
    
    def test_footer(self):
        response = self.client.get(reverse('show_new'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Оффициальные группы сайта:')
        
                    
class PopularPageTests(TestCase):
    def test_popular_empty(self):
        response = self.client.get(reverse('show_popular'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Список популярных стихотворений пуст')
        self.assertQuerysetEqual(response.context['popular_poems'], [])
    
    def test_view_popular(self):
        poet = create_poet('Ilia', 'Zhelenkov', '')
        poem = create_poem(poet, 'Clouds', 'abc', 5, 1, 5, True)
        response = self.client.get(reverse('show_popular'))
        self.assertQuerysetEqual(response.context['popular_poems'], [poem])
        
    def test_view_unpopular(self):
        poet = create_poet('Ilia', 'Zhelenkov', '')
        poem = create_poem(poet, 'Clouds', 'abc', 0, 0, 0, True)
        response = self.client.get(reverse('show_popular'))
        self.assertQuerysetEqual(response.context['popular_poems'], [])
        
    def test_footer(self):
        response = self.client.get(reverse('show_popular'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Оффициальные группы сайта:')    
        

class ListPoemsTests(TestCase):
    def test_no_poems(self):
        poet = create_poet('Ilia', 'Zhelenkov', '')
        response = self.client.get(reverse('poems', kwargs={'poet_id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Список стихотворений пуст')
        self.assertQuerysetEqual(response.context['list_poems'], [])
    
class CommentTests(TestCase):
    def test_future_comment(self):
        poet = create_poet('Ilia', 'Zhelenkov', '')
        poem = create_poem(poet, 'Clouds', 'abc', 0, 0, 0, True)
        time = timezone.now() + datetime.timedelta(days = 10)
        future_comment = create_comment(poem, 'Ilia', 'It is commentary', date=time)
        self.assertIs(future_comment.new_comment(), False)
    
    def test_comment_not_exist(self):
        poet = create_poet('Ilia', 'Zhelenkov', '')
        poem = create_poem(poet, 'Clouds', 'abc', 0, 0, 0, True)
        response = self.client.get(reverse('display_poem', kwargs = {'arg1': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Оставьте комментарий первым')
        
    def test_comment_with_content(self):
        poet = create_poet('Ilia', 'Zhelenkov', '')
        poem = create_poem(poet, 'Clouds', 'abc', 0, 0, 0, True)
        now = timezone.now()
        comment = create_comment(poem, 'text', 'text', now)
        response = self.client.get(reverse('display_poem', kwargs = {'arg1': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['list_commentaries'], [comment])
        
        
        
class RatingTests(TestCase):
    def test_rating_0(self):
        poet = create_poet('Ilia', 'Zhelenkov', '')
        poem = create_poem(poet, 'Clouds', 'abc', 0, 0, 0, True)
        response = self.client.get(reverse('display_poem', kwargs = {'arg1': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Средняя оценка - 0')
    
        
        
         
    
"""class MainPoemTests(TestCase):
    def test_searched(self):
        response = self.client.post('/all_poems/', {'search_text': 'Вечер'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'По вашему запросу ничего не найдено')
        self.assertQuerysetEqual(response.context['data'], [])"""
  

"""class CommentTests(TestCase):
    def test_time(self):
        time = timezone.now() + datetime.timedelta(days = 30)
        future_comment = Comment(date = time)
        self.assertIs(future_comment.new_comment(), False)
        
    def test_commentary(self):
        response = self.client.get(reverse('poems:14:7'))
        self.assertEqual(response.status_code, 200)
        self.assertContaints(response, 'Оставьте комментарий первым')
        self.assertQuerysetEqual(response.context['list_commentaries'], [])
        
    def test_past_commentary(self):
        comment = create_comment('Ilia', 'Simple example', -5)
        response = self.client.get('poems:14:7')
        self.assertQuerysetEqual(response.context['list_commentaries'], [comment])"""
        
        