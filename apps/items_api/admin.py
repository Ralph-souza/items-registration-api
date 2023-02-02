from django.contrib import admin
from .models import ItemsModel, VideoItemsModel, PrintedItemsModel


admin.site.register(ItemsModel)
admin.site.register(VideoItemsModel)
admin.site.register(PrintedItemsModel)
