from django.contrib import admin
from .models import CustomUser, Donor, BloodRequest, Notification, ContactMessage
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'phone', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'phone', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'phone', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'username', 'phone',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Donor)
admin.site.register(ContactMessage)

from django.contrib import admin
from .models import BloodRequest, Notification

@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'blood_type', 'city', 'address', 'phone','hospital', 'request_date')
    search_fields = ('user__username', 'blood_type', 'city')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('blood_request', 'status', 'created_at')
    search_fields = ('blood_request__user__username', 'status')
    list_filter = ('status', 'created_at')

# faq.py

from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ('question',)

