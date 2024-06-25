from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from accounts.models import (
	Account,
	Scholar_liked,)



class AccountAdmin(UserAdmin):
	list_display = ('email','username','phone_number','date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('email','username','phone_number',)
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()



class Scholar_likedAdminForm(forms.ModelForm):
    class Meta:
        model = Scholar_liked
        exclude = ['user']

class Scholar_likedAdmin(admin.ModelAdmin):
    form = Scholar_likedAdminForm

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Only set the user on creation, not on updates
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        # Optionally, filter the queryset to only show the user's entries
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def get_readonly_fields(self, request, obj=None):
        # Make the user field read-only if the object exists (for view purposes in admin)
        if obj:
            return ['user']
        return []

admin.site.register(Scholar_liked, Scholar_likedAdmin)


admin.site.register(Account)



