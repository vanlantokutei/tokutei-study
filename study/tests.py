from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Exam, PremiumPlan, PremiumProfile, PremiumRequest


class PremiumFlowTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='premium-test', email='premium@example.com', password='Test-pass-123!'
        )
        self.exam = Exam.objects.create(title='Đề Premium', is_free=False)
        self.plan = PremiumPlan.objects.create(
            name='1 tháng', slug='test-1-thang', duration_days=30,
            original_price_vnd=59000, sale_price_vnd=29000,
        )

    def test_premium_exam_redirects_free_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('exam_intro', args=[self.exam.id]))
        self.assertRedirects(response, reverse('premium'))

    def test_premium_user_can_open_premium_exam(self):
        PremiumProfile.objects.create(user=self.user, is_premium=True)
        self.client.force_login(self.user)
        response = self.client.get(reverse('exam_intro', args=[self.exam.id]))
        self.assertEqual(response.status_code, 200)

    def test_user_can_submit_transfer_request(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('premium'), {
            'plan': self.plan.id,
            'transfer_name': 'Nguyen Van A',
            'transfer_date': '2026-08-16',
            'reference': 'TOKUTEI123',
            'note': '',
        })
        self.assertRedirects(response, reverse('premium'))
        self.assertTrue(PremiumRequest.objects.filter(user=self.user, status='pending').exists())

    def test_premium_page_displays_sale_prices_and_discount(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('premium'))
        self.assertContains(response, '59.000đ')
        self.assertContains(response, '29.000')
        self.assertContains(response, 'Giảm 51%')
from django.urls import reverse

from .models import LearningCategory, Lesson, QuickQuestion, ServiceSituation, VocabularyEntry


class LibraryTests(TestCase):
    def setUp(self):
        self.category = LearningCategory.objects.create(
            slug='hygiene', title_jp='衛生管理', title_vi='Quản lý vệ sinh', order=1
        )
        self.lesson = Lesson.objects.create(
            category=self.category, slug='washing', title_jp='手洗い',
            title_furigana='てあらい', title_vi='Rửa tay', content_jp='手を洗います。',
            content_furigana='てを あらいます。', content_vi='Rửa tay.',
            exam_notes_vi='Nhớ rửa đủ các vị trí.',
        )
        QuickQuestion.objects.create(
            lesson=self.lesson, question_jp='いつ？', question_vi='Khi nào?',
            option_a='Trước chế biến', option_b='Không bao giờ', option_c='Tùy ý',
            correct_answer='A', explanation_vi='Phải rửa trước khi chế biến.',
        )

    def test_library_and_lesson_pages_render(self):
        library_response = self.client.get(reverse('library'))
        self.assertEqual(library_response.status_code, 200)
        self.assertContains(library_response, 'Quản lý vệ sinh')
        lesson_response = self.client.get(reverse('lesson_detail', args=['hygiene', 'washing']))
        self.assertEqual(lesson_response.status_code, 200)
        self.assertContains(lesson_response, 'Điểm cần nhớ khi thi')
        self.assertContains(lesson_response, 'Câu luyện nhanh')

    def test_progress_is_saved_in_session(self):
        response = self.client.post(reverse('toggle_lesson_progress', args=[self.lesson.id]))
        self.assertRedirects(response, reverse('lesson_detail', args=['hygiene', 'washing']))
        self.assertIn(self.lesson.id, self.client.session['completed_lesson_ids'])
        self.client.post(reverse('toggle_lesson_progress', args=[self.lesson.id]))
        self.assertNotIn(self.lesson.id, self.client.session['completed_lesson_ids'])

    def test_existing_core_pages_are_still_available(self):
        for name in ('home', 'tokutei1', 'practice1', 'exam_list'):
            self.assertEqual(self.client.get(reverse(name)).status_code, 200)


class VocabularyTests(TestCase):
    def setUp(self):
        self.word = VocabularyEntry.objects.create(
            category='hygiene', topic='food_poisoning', word_jp='衛生', furigana='えいせい',
            meaning_vi='vệ sinh', example_jp='衛生管理をします。',
            example_vi='Thực hiện quản lý vệ sinh.',
        )
        VocabularyEntry.objects.create(
            category='service', topic='communication', word_jp='注文', furigana='ちゅうもん',
            meaning_vi='gọi món',
        )

    def test_search_and_category_filter(self):
        response = self.client.get(reverse('vocabulary'), {'q': 'vệ sinh'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '衛生')
        self.assertNotContains(response, '注文')
        filtered = self.client.get(reverse('vocabulary'), {'category': 'service'})
        self.assertContains(filtered, '注文')
        self.assertNotContains(filtered, '衛生管理をします。')
        topic_filtered = self.client.get(reverse('vocabulary'), {'topic': 'communication'})
        self.assertContains(topic_filtered, '注文')
        self.assertNotContains(topic_filtered, '衛生管理をします。')

    def test_vocabulary_progress_is_saved_in_session(self):
        response = self.client.post(
            reverse('toggle_vocabulary_progress', args=[self.word.id]),
            {'next': reverse('vocabulary')},
        )
        self.assertRedirects(response, reverse('vocabulary'))
        self.assertIn(self.word.id, self.client.session['learned_vocabulary_ids'])


class ServiceSituationTests(TestCase):
    def setUp(self):
        self.situation = ServiceSituation.objects.create(
            category='complaint', slug='wrong-dish-test',
            title_jp='料理を間違えた', title_vi='Phục vụ sai món',
            situation_jp='違う料理を出しました。', situation_vi='Đã mang nhầm món.',
            response_jp='申し訳ございません。', response_vi='Thành thật xin lỗi.',
            handling_steps_vi='Xin lỗi và kiểm tra lại đơn.',
        )

    def test_situation_page_filter_and_content(self):
        response = self.client.get(reverse('service_situations'), {'category': 'complaint'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Phục vụ sai món')
        self.assertContains(response, 'Xem cách xử lý đúng')
        short_url_response = self.client.get(reverse('service_situations_short'))
        self.assertEqual(short_url_response.status_code, 200)
        self.assertContains(short_url_response, 'Phục vụ sai món')

    def test_situation_progress_is_saved(self):
        response = self.client.post(
            reverse('toggle_situation_progress', args=[self.situation.id]),
            {'next': reverse('service_situations')},
        )
        self.assertRedirects(response, reverse('service_situations'))
        self.assertIn(self.situation.id, self.client.session['completed_situation_ids'])
