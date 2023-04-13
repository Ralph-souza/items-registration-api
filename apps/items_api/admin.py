from django.contrib import admin

from .models import ItemModel, PrintedItemModel, VideoItemModel

admin.site.register(ItemModel)
admin.site.register(VideoItemModel)
admin.site.register(PrintedItemModel)
