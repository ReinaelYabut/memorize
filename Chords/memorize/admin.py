# chords_app/admin.py

from django.contrib import admin
from .models import Key, Chord, ChordImage

# Customizing the Key admin interface
class KeyAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display key name in the admin list

# Customizing the Chord admin interface
class ChordAdmin(admin.ModelAdmin):
    list_display = ('name', 'key', 'description')  # Show chord name, key, and description
    list_filter = ('key',)  # Add a filter by key
    search_fields = ('name',)  # Add a search bar for chord name

# Customizing the ChordImage admin interface
class ChordImageAdmin(admin.ModelAdmin):
    list_display = ('chord',)  # Display chord and image description
    list_filter = ('chord',)  # Filter images by chord

# Registering models to the admin site
admin.site.register(Key, KeyAdmin)
admin.site.register(Chord, ChordAdmin)
admin.site.register(ChordImage, ChordImageAdmin)
