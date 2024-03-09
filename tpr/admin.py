from django.contrib import admin
from tpr.models import Tpr

# Register your models here.
# admin.py


class YourModelAdmin(admin.ModelAdmin):
    list_display = ('TPR_NO','segment','customer', 'display_pdf_link')  # Add other fields as needed

    def display_pdf_link(self, obj):
        if obj.pdf_file:
            return f'<a href="{obj.pdf_file.url}" target="_blank">View PDF</a>'
        return 'No PDF file'
    display_pdf_link.allow_tags = True
    display_pdf_link.short_description = 'PDF Link'

admin.site.register(Tpr, YourModelAdmin)
