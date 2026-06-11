import jieba
from whoosh.analysis import Tokenizer, Token
from haystack.backends.whoosh_backend import WhooshEngine, WhooshSearchBackend

# 自定义中文分词器
class ChineseTokenizer(Tokenizer):
    def __call__(self, value, positions=False, chars=False,
                 keeporiginal=False, removestops=True,
                 start_pos=0, start_char=0, mode='', **kwargs):
        
        t = Token(positions, chars, removestops=removestops, mode=mode, **kwargs)
        if not isinstance(value, str):
            value = str(value)
            
        # 核心逻辑：使用 jieba 的“搜索引擎模式”，会把词语切得非常细，实现模糊搜索
        seglist = jieba.cut_for_search(value)
        
        for w in seglist:
            t.original = t.text = w
            t.boost = 1.0
            if positions:
                t.pos = start_pos + max(0, value.find(w))
            if chars:
                match_index = max(0, value.find(w))
                t.startchar = start_char + match_index
                t.endchar = start_char + match_index + len(w)
            yield t

def ChineseAnalyzer():
    return ChineseTokenizer()

# 覆盖原生的 Backend，将文本字段强制替换为我们的中文分词器
class CustomWhooshBackend(WhooshSearchBackend):
    def build_schema(self, fields):
        (content_field_name, schema) = super(CustomWhooshBackend, self).build_schema(fields)
        from whoosh.fields import TEXT
        for field_name, field_class in schema.items():
            if isinstance(field_class, TEXT):
                schema[field_name].analyzer = ChineseAnalyzer()
        return (content_field_name, schema)

# 最终暴露给系统的引擎
class CustomWhooshEngine(WhooshEngine):
    backend = CustomWhooshBackend