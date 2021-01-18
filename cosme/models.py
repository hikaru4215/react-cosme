from django.db import models
from django.conf import settings
from django.utils import timezone

class Category(models.Model):
	name = models.CharField("カテゴリ", max_length=50)

	def __str__(self):
		return self.name

class Price(models.Model):
	price = models.CharField("プライス", max_length=50)

	def __str__(self):
		return self.price

class SkinType(models.Model):
	skintype = models.CharField("肌タイプ", max_length=50)

	def __str__(self):
		return self.skintype

class Score(models.Model):
	scores = models.CharField("おすすめ度", max_length=50)

	def __str__(self):
		return self.scores


class Recommenditem(models.Model):
    brand = models.CharField("ブランド名", max_length=100)
    product = models.CharField("製品名", max_length=100)
    content = models.TextField("説明")
    image = models.ImageField(upload_to='images', verbose_name='イメージ画像')
    item = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.CharField("本体価格", max_length=100)
    price_data = models.ForeignKey(Price, on_delete=models.CASCADE)
    skintype = models.ForeignKey(SkinType, on_delete=models.CASCADE)
    acne_point = models.IntegerField("ニキビポイント", default=0)
    pores_point = models.IntegerField("毛穴ポイント", default=0)
    berd_point = models.IntegerField("髭剃り負けポインント", default=0)
    wrinkle_point = models.IntegerField("シワポイント", default=0)
    official_page = models.URLField("公式URL")
    rakuten_page = models.URLField("楽天URL")
    amazon_page = models.URLField("アマゾンURL")
    trouble_name1 =  models.CharField("ニキビ", max_length=100, blank=True)
    trouble_name2 =  models.CharField("毛穴", max_length=100, blank=True)
    trouble_name3 =  models.CharField("髭剃り負け", max_length=100, blank=True)
    trouble_name4 =  models.CharField("シワ", max_length=100, blank=True)
    capacity = models.CharField("容量", max_length=100)


    def __str__(self):
        return self.product


class Review(models.Model):
	# user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	brand = models.CharField("ブランド名", max_length=100, blank=True)
	product = models.CharField("製品名", max_length=100)
	category = models.ForeignKey(Category, verbose_name='カテゴリー', on_delete=models.CASCADE)
	price = models.ForeignKey(Price, verbose_name='プライス', on_delete=models.CASCADE, blank=True)
	score = models.ForeignKey(Score, verbose_name='おすすめ度', on_delete=models.CASCADE)
	comment = models.TextField("クチコミ")
	created = models.DateTimeField("作成日", default=timezone.now)
	image = models.ImageField(upload_to='images', verbose_name='イメージ画像', blank=True)


	def __str__(self):
		return self.product