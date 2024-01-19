from django.contrib import admin
from .models import Author, Article, Comments, CoinFlip


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'publication_date',
        'author',
        'category',
        'views_count',
        'status',
    ]
    # fields = [
    #     'status',
    #     # 'publication_date',
    #     'author',
    #     'category',
    #     'content',
    # ]
    readonly_fields = [
        'publication_date',
    ]
    fieldsets = [
        (
            'Текст статьи:',
            {
                'classes': ['wide'],
                'fields': ['content'],
            }
        )
    ]


# class CommentsAdmin(admin.ModelAdmin):
#     list_display = [
#         'author',
#         'article',
#         'content',
#         'created_date',
#         'updated_date',
#     ]


admin.site.register(Comments)
admin.site.register(CoinFlip)
