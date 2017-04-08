from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=64)
    parent = models.ForeignKey('self', blank=True, null=True)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return '{:03} | {}{}'.format(
            self.priority,
            self.parent_title,
            self.title
        )

    @property
    def parent_title(self):
        title = ''
        cur_category = self
        while cur_category.parent:
            title = cur_category.parent.title + ' > ' + title
            cur_category = cur_category.parent
        return title

    class Meta:
        index_together = (
            'parent', 'priority'
        )
        ordering = ('priority', )


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
