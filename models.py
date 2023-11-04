from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class PersonalinfoModel(models.Model):
    CHOICES = (
        ('可', '可'),
        ('不可', '不可'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             to_field='id', on_delete=models.CASCADE, null=True)
    item1 = models.CharField(
        max_length=2, choices=CHOICES, verbose_name='大学当直')
    item2 = models.CharField(
        max_length=2, choices=CHOICES, verbose_name='取手当直')
    item3 = models.CharField(
        max_length=2, choices=CHOICES, verbose_name='高萩当直')
    item4 = models.CharField(
        max_length=2, choices=CHOICES, verbose_name='日赤当直')
    item5 = models.CharField(
        max_length=2, choices=CHOICES, verbose_name='大学オンコール')
    item6 = models.CharField(
        max_length=2, choices=CHOICES, verbose_name='学園オンコール')
    item7 = models.CharField(
        max_length=2, choices=CHOICES, verbose_name='龍ヶ崎オンコール')
    item8 = models.CharField(
        max_length=2, choices=CHOICES, verbose_name='セントラルオンコール')

    def __str__(self):
        return f'PersonalinfoModel {self.id}'  # インスタンスの表示名を変更


class ShiftAvailability(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ユーザーと関連付け
    date = models.DateField()  # 日付
    on_call_available = models.BooleanField(
        default=False, verbose_name='当直可')  # 当直可否
    on_call_comments = models.TextField(
        blank=True, verbose_name='当直コメント')  # 当直のコメント
    on_call_external_hospital = models.BooleanField(
        default=False, verbose_name='外病院当直可')  # 外病院当直可否
    on_call_external_hospital_comments = models.TextField(
        blank=True, verbose_name='外病院当直コメント')  # 外病院当直のコメント

    class Meta:
        verbose_name = '当直可否入力'  # 管理画面で表示される名前
        verbose_name_plural = '当直可否入力一覧'  # 管理画面で表示される名前（複数形）

    def __str__(self):
        return f'{self.user.username} - {self.date} の当直情報'

class SurveyCalendar(models.Model):
    CHOICES = (
        ('可', '可'),
        ('不可', '不可'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                          to_field='id', on_delete=models.CASCADE, null=True)
    date = models.DateField()
    item1 = models.CharField(max_length=2, choices=CHOICES, verbose_name='大学当直')
    item2 = models.CharField(max_length=2, choices=CHOICES, verbose_name='取手当直')
    item3 = models.CharField(max_length=2, choices=CHOICES, verbose_name='高萩当直')
    item4 = models.CharField(max_length=2, choices=CHOICES, verbose_name='日赤当直')
    item5 = models.CharField(max_length=2, choices=CHOICES, verbose_name='大学オンコール')
    item6 = models.CharField(max_length=2, choices=CHOICES, verbose_name='学園オンコール')
    item7 = models.CharField(max_length=2, choices=CHOICES, verbose_name='龍ヶ崎オンコール')
    item8 = models.CharField(max_length=2, choices=CHOICES, verbose_name='セントラルオンコール')

    def __str__(self):
        return f'SurveyCalendar {self.id}'
