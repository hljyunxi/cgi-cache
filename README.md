cgi-cache
=========

我们在写cgi程序的时候，经常遇到查询分页的情况，在数据里上来以后，如果每次访问都
查询数据库返回结果，就可能出现慢查询，导致浏览器出现504等错误，所以对cgi加缓存
有时就显得比较必要。

使用cgi-cache可以很简单的实现上述的需求

```
    @cache("search-{user_name}-{user_id}-{user_sex}-{page}", expires = 5*60)
    def search(user_name, user_id, user_sex, page):
       big sql query
```

上面的代码就实现了对搜索结果缓存5分钟的效果。
