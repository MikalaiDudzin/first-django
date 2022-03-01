import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from store.models import Book
from store.serializers import BooksSerializer


class BooksApiTestCase(APITestCase):
    # def setUP(self):
    #     self.book_1 = Book.objects.create(name='Test book 1', price=25.00, author_name='Author 1')
    #     self.book_2 = Book.objects.create(name='Test book 2', price=260.00, author_name='Author 5')
    #     self.book_3 = Book.objects.create(name='Test book 3 Author 1', price=100.00, author_name='Author 2')

    def test_get(self):
        book_1 = Book.objects.create(name='Test book 1', price=25.00, author_name='Author 1')
        book_2 = Book.objects.create(name='Test book 2', price=260.00, author_name='Author 5')
        book_3 = Book.objects.create(name='Test book 3 Author 1', price=100.00, author_name='Author 2')
        url = reverse('book-list')
        # print(url)
        response = self.client.get(url)
        serializer_data = BooksSerializer([book_1, book_2, book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        # print(response.data)
        # print(response)

    def test_create(self):
        self.assertEqual(0, Book.objects.all().count())
        url = reverse('book-list')
        data = {
            "name": "Programming in Python 3",
            "price": 150,
            "author_name": "Mark Summerfield"
        }
        json_data = json.dumps(data)
        self.client.force_login(User.objects.create(username='test_username'))
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(1, Book.objects.all().count())

    def test_update(self):
        self.book_4 = Book.objects.create(name='Test book 1', price=25.00, author_name='Author 1')
        url = reverse('book-detail', args=(self.book_4.id,))
        data = {
            "name": self.book_4,
            "price": 500,
            "author_name": self.book_4.author_name
        }
        json_data = json.dumps(data)
        self.client.force_login(User.objects.create(username='test_username'))
        response = self.client.put(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.book_4 = Book.object.get(id=self.book_4.id)
        self.assertEqual(500, self.book_4.price)
