from django.db import models


class CategoryManager(models.Manager):
    def all_categories(self, category):
        categories = []
        cur_category = category
        while cur_category.parent:
            categories.insert(0, cur_category.parent.id)
            cur_category = cur_category.parent
        categories.append(category.id)
        return self.get_queryset().filter(pk__in=categories)


class Category(models.Model):
    title = models.CharField('카테고리명', max_length=64)
    parent = models.ForeignKey('self', verbose_name='부모 카테고리', blank=True, null=True)
    priority = models.IntegerField('우선도', default=0)

    objects = CategoryManager()

    def __str__(self):
        return '{}'.format(
            self.full_title
        )

    class Meta:
        verbose_name = '카테고리'
        verbose_name_plural = '{} 목록'.format(verbose_name)
        index_together = (
            'parent', 'priority'
        )
        ordering = (
            'parent_id', 'priority',
        )

    @property
    def full_title(self):
        title = ''
        cur_category = self
        while cur_category.parent:
            title = cur_category.parent.title + ' > ' + title
            cur_category = cur_category.parent
        title += self.title
        return title

    @property
    def all_categories(self):
        categories = []
        cur_category = self
        while cur_category.parent:
            categories.insert(0, cur_category.parent.id)
            cur_category = cur_category.parent
        categories.append(self.id)
        return Category.objects.filter(pk__in=categories)


class Product(models.Model):
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=64)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product', blank=True)
    description = models.TextField(blank=True)
    inventory_count = models.IntegerField(default=0)
    score = models.FloatField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '상품'
        verbose_name_plural = '{} 목록'.format(verbose_name)


class DateRangeDiscount(models.Model):
    category = models.ForeignKey(Category)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    rate = models.FloatField()

    def __str__(self):
        return 'Category({category}) {rate:.1%}, [{start_date} - {end_date}]'.format(
            category=self.category.title,
            rate=self.rate,
            start_date=self.start_date,
            end_date=self.end_date
        )
