
from django.test import TestCase

from django.core.urlresolvers import reverse

from mistypes.models import Mistype
from mistypes.forms import MistypeForm


class MistypeFormsTest(TestCase):

    def create_mistype(self, url='http://example.com', before='before', mistype='mistype',
                       after='after', comment='comment'):
        form_data = {
            'url': url,
            'before': before,
            'mistype': mistype,
            'after': after,
            'comment': comment,
        }
        return MistypeForm(data=form_data)

    def test_valid_form(self):
        form = self.create_mistype()
        self.assertTrue(form.is_valid())

    def test_comment_blank(self):
        form = self.create_mistype(comment='')
        self.assertTrue(form.is_valid())

    def test_big_data(self):
        form = self.create_mistype(before='*'*3000)
        self.assertFalse(form.is_valid())

    def test_invalid_form(self):
        form = self.create_mistype(after='')
        self.assertFalse(form.is_valid())


class MistypeModelsTest(TestCase):

    def create_mistype(self, type='O', ip='127.0.0.1', url='http://example.com', before='before', mistype='mistype',
                        after='after', comment='comment'):
        return Mistype.objects.create(type=type, ip=ip, url=url, before=before, mistype=mistype,
                                      after=after, comment=comment)

    def test_mistype_creation(self):
        w = self.create_mistype()
        self.assertTrue(isinstance(w, Mistype))

    def test_space_after_before(self):
        w = self.create_mistype(before='before ')
        self.assertTrue(w.before.endswith(' '))
        self.assertIn(' <span', w.full_text())


class MistypeViewsTest(TestCase):

    def test_nonajax_denied(self):
        url = reverse("mistypes:mistypes_submit")
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, 403)

    def test_get_denied(self):
        url = reverse("mistypes:mistypes_submit")
        resp = self.client.post(url, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(resp.status_code, 403)

    def test_spam_noreferer(self):
        data = dict(url='http://example.com', before='before', mistype='mistype',
                        after='after', comment='comment')
        url = reverse("mistypes:mistypes_submit")
        with self.settings(ALLOWED_HOSTS=['example.com', 'testserver']):
            resp = self.client.post(url, data=data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(resp.status_code, 403)

    def test_all_ok(self):
        data = dict(url='http://example.com', before='before', mistype='mistype',
                        after='after', comment='comment')
        url = reverse("mistypes:mistypes_submit")
        with self.settings(ALLOWED_HOSTS=['example.com', 'testserver']):
            resp = self.client.post(url, data=data, HTTP_X_REQUESTED_WITH='XMLHttpRequest',
                                    HTTP_REFERER='http://example.com')
        self.assertEqual(resp.status_code, 200)
        w = Mistype.objects.filter(url=data['url']).first()
        self.assertEqual(w.type, 'O')

    def test_space_trailing(self):
        data = dict(url='http://example.com', before='before ', mistype='mistype',
                        after='after', comment='comment')
        url = reverse("mistypes:mistypes_submit")
        with self.settings(ALLOWED_HOSTS=['example.com', 'testserver']):
            resp = self.client.post(url, data=data, HTTP_X_REQUESTED_WITH='XMLHttpRequest',
                                    HTTP_REFERER='http://example.com')
        self.assertEqual(resp.status_code, 200)
        w = Mistype.objects.filter(url=data['url']).first()
        self.assertEqual(w.before, 'before ')
