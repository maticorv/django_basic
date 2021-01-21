# Django:
from django.contrib import admin

# Models:
from users.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    # Variable con los campos a mostrar en el dashboard.
    list_display = (
        'pk',
        'user',
        'phone_number',
        'website',
        'picture',
    )

    # Variable con los campos que serán links.
    list_display_links = (
        'pk',
        'user',
    )

    # Variable con los campos editables desde dashboard| Nota: No puede haber campos link y editables a la vez.
    list_editable = (
        'phone_number',
        'website',
        'picture',
    )

    # Variable con los campos por los que podemos realizar una busqueda.
    search_fields = (
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone_number',
    )

    # Variable que añade un campo por el cual filtrar los datos.
    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff',
    )

