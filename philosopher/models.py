#! coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone
# Create your models here.

class UserProfile(models.Model):
	ROLE_CHOICES = (
		('s', u"学生"),		
		('o', u"组织者"),	
		('a', u"管理员"),
	)
	SEX_CHOICES = (
		('f', u"女"),
		('m', u"男"),
		('o', u"其他"),
	)
	STATUS_CHOICES = (
		('n', u'正常'),
		('b', u'被拉黑'),
		('w', u'待批准'),
	)
	user = models.OneToOneField(User)
	role = models.CharField(u'角色', max_length=1, choices=ROLE_CHOICES, default=ROLE_CHOICES[0][0])
	gender = models.CharField(u'性别', max_length=1, choices=SEX_CHOICES, default=SEX_CHOICES[0][0])
	status = models.CharField(u'状态', max_length=1, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
	schoolID = models.CharField(u'学号', max_length=20, default="000")
	phone = models.CharField(u'手机号码', max_length=25, default="000")
	attimes = models.IntegerField(u'公益时长', default = 0)
	intro = models.TextField(u'自我介绍', blank = True)
	avatar = models.ImageField(u'头像', upload_to = "image/UserAvatar", blank = True)
	def getAvatar(self):
		if self.avatar and hasattr(self.avatar, 'url'):
			return self.avatar.url
		else:
			return '/media/image/UserAvatar/default.jpg'
	def save(self, *args, **kwargs):
		if not self.pk:
			try:
				p = UserProfile.objects.get(user = self.user)
				self.pk = p.pk
			except UserProfile.DoesNotExist:
				pass

		super(UserProfile, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

class Activity(models.Model):
	atorganizer = models.ForeignKey(User)
	#0:pass; 1:reject; 2: wait
	atstatus = models.IntegerField(u'状态', default = 2)
	atname = models.CharField(u'活动名称', max_length=50)
	atcontent = models.TextField(u'活动内容')
	numlimit = models.IntegerField(u'人数限制', default=99999)
	athours = models.IntegerField(u'公益时长', default=0)
	feedback = models.TextField(u'备注')
	createdate = models.DateTimeField(u'创建日期', default = timezone.now, editable=False)
	publishdate = models.DateTimeField(u'发布日期', blank=True, null=True)
	applystart = models.DateTimeField(u'申请开始日期', default = timezone.now)
	applyend = models.DateTimeField(u'申请结束日期')
	doingstart = models.DateTimeField(u'活动开始日期')
	doingend = models.DateTimeField(u'活动结束日期')
	poster = models.ImageField(u'海报', upload_to = "image/ActivityPoster", blank = True)
	def getPoster(self):
		if self.poster and hasattr(self.poster, 'url'):
			return self.poster.url
		else:
			return '/media/image/ActivityPoster/default.jpg'
	def __unicode__(self):
		return self.atname

class Application(models.Model):
	GRADE_CHOICES = (
		('a', '大一'),
		('b', '大二'),
		('c', '大三'),
		('d', '大四'),
		('e', '研究生'),
		('f', '博士生'),
	)
	activity = models.ForeignKey(Activity)
	student = models.ForeignKey(User)
	activityid = models.IntegerField()
	#0:pass; 1:reject; 2: wait; 3: finish; 4: failed
	apstatus = models.IntegerField(u'状态', default = 2)
	grade = models.CharField(u'年级', max_length=1, choices=GRADE_CHOICES, default=GRADE_CHOICES[0][0])
	phone = models.CharField(u'手机号码', max_length=25)
	applyreason = models.TextField(u'申请原因')
	feedback = models.TextField(u'反馈')
	def __unicode__(self):
		return self.activity.atname