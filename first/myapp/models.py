from django.db import models
from django.utils import timezone


class Studio(models.Model):
    """レッスンスタジオ"""
    name = models.CharField('名前', max_length=200)
    address = models.CharField('住所', max_length=200)
    # 設備、器具なども記載予定


class Trainer(models.Model):
    name = models.CharField('名前', max_length=200)
    introduction = models.TextField('紹介文')
    price30 = models.IntegerField('30分価格')
    price60 = models.IntegerField('60分価格')
    price90 = models.IntegerField('90分価格')
    nomination = models.IntegerField('指名料')
    # 指導可能なレッスン、資格なども記載予定


class Customer(models.Model):
    customerId = models.IntegerField('顧客管理番号', unique=True)
    name = models.CharField('名前', max_length=200)
    memo = models.TextField('備考')
    thisMonthRemainingTicket = models.IntegerField('今月の残チケット数', default=0)
    lastMonthRemainingTicket = models.IntegerField('先月の残チケット数', default=0)
    twoMonthsBeforeRemainingTicket = models.IntegerField('先々月の残チケット数', default=0)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)
    mainTrainer = models.ForeignKey(Trainer, on_delete=models.PROTECT)
    phone = models.CharField('連絡先', max_length=20)


class ReserveUnit(models.Model):
    startTime = models.DateTimeField('開始時間', default=timezone.now)
    duration = models.DurationField('レッスン時間')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)

