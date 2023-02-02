from django.contrib import admin
from .models import LoanerModel, ItemsModel, VideoItemsModel, PrintedItemsModel


# admin.site.register(UserModel)
admin.site.register(LoanerModel)
admin.site.register(ItemsModel)
admin.site.register(VideoItemsModel)
admin.site.register(PrintedItemsModel)
