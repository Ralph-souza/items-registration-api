from django.contrib import admin

from .models import (GamesItemModel, PrintedItemModel, UserItemsModel,
                     VideosItemModel)

admin.site.register(UserItemsModel)
admin.site.register(VideosItemModel)
admin.site.register(PrintedItemModel)
admin.site.register(GamesItemModel)
