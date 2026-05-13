from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    # What columns to show in the list view
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    
    # Clicking these will take you to the edit page
    list_display_links = ('email', 'first_name', 'last_name')
    
    # Fields that are read-only
    readonly_fields = ('last_login', 'date_joined')
    
    # How the list should be ordered
    ordering = ('-date_joined',)

    # We MUST set these to empty tuples because we didn't use Groups/Permissions in models.py
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Finally, register the model
admin.site.register(Account, AccountAdmin)