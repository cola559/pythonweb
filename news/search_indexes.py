from haystack import indexes
from .models import News

# 定义针对 News 模型的搜索索引类
class NewsIndex(indexes.SearchIndex, indexes.Indexable):
    # text 是必须的字段，document=True 表示以此字段作为主要检索词源
    # use_template=True 表示我们需要新建一个 txt 模板来告诉引擎具体检索 News 的哪些字段
    text = indexes.CharField(document=True, use_template=True)
    
    # 给搜索结果添加额外字段，方便在前端展示高亮和详情
    title = indexes.CharField(model_attr='title')
    publishDate = indexes.DateTimeField(model_attr='publishDate')

    def get_model(self):
        return News

    def index_queryset(self, using=None):
        # 建立索引时，把所有新闻都扫一遍
        return self.get_model().objects.all()