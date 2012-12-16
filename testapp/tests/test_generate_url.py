# -*- coding: utf-8 -*-

from mock import patch
from unittest import TestCase
from django_thumbor import generate_url, crypto

# class TestGenerateURL(TestCase):
#     
#     def setUp(self):
#         super(TestGenerateURL, self).setUp()
#         self.mox.StubOutWithMock(crypto, 'generate')
# 
#         self.url = 'domain.com/path/image.jpg'
# 
#     def assertPassesArgsToCrypto(self, *args, **kwargs):
#         with patch('django_thumbor.crypto.generate') as mock:
#         # crypto.generate(image_url=self.url)
#         # self.mox.ReplayAll()
#         generate_url(self.url)
# 
#     def test_should_pass_url_arg_to_crypto(self):
#         crypto.generate(image_url=self.url)
#         self.mox.ReplayAll()
#         generate_url(self.url)
# 
#     def test_should_pass_url_kwarg_to_crypto(self):
#         crypto.generate(image_url=self.url)
#         self.mox.ReplayAll()
#         generate_url(image_url=self.url)
# 
#     def test_should_pass_kwargs_to_crypto(self):
#         crypto.generate(image_url=self.url, width=300, height=200)
#         self.mox.ReplayAll()
#         generate_url(image_url=self.url, width=300, height=200)
# 
#     def test_should_return_the_result(self):
#         encrypted_url = 'encrypted-url.jpg'
#         crypto.generate(image_url=self.url).AndReturn(encrypted_url)
# 
#         self.mox.ReplayAll()
# 
#         url = generate_url(image_url=self.url)
#         self.assertEqual(url, encrypted_url)

from mock import patch
from unittest import TestCase
from django_thumbor import crypto

class TestGenerateURL(TestCase):
    
    url = 'domain.com/path/image.jpg'

    def assertPassesArgsToCrypto(self, *args, **kwargs):
        with patch('django_thumbor.crypto.generate') as mock:
            generate_url(*args, **kwargs)
            mock.assert_called_with(*args, **kwargs)

    def test_should_pass_url_arg_to_crypto(self):
        with patch('django_thumbor.crypto.generate') as mock:
            generate_url(self.url)
            mock.assert_called_with(image_url=self.url)

    def test_should_pass_url_kwarg_to_crypto(self):
        self.assertPassesArgsToCrypto(image_url=self.url)

    def test_should_pass_extra_kwargs_to_crypto(self):
        self.assertPassesArgsToCrypto(image_url=self.url, width=300, height=200)

    def test_should_return_the_result(self):
        encrypted_url = 'encrypted-url.jpg'

        with patch('django_thumbor.crypto.generate') as mock:
            mock.return_value = encrypted_url
            url = generate_url(self.url)

        self.assertEqual(url, encrypted_url)
