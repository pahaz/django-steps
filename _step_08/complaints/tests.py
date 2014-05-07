from django.shortcuts import resolve_url
from django.test import TestCase
from django.test import Client


class ComplaintsTest(TestCase):
    def test_index_url_status(self):
        c = Client()
        response = c.get(resolve_url('complaints_index'))
        self.assertEqual(response.status_code, 200, "bead complaints_index url status")

    def test_post_url_status(self):
        c = Client()
        response = c.get(resolve_url('complaints_post'))
        self.assertEqual(response.status_code, 302, "bead complaints_post url status")