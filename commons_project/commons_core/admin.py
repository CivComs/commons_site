from commons_core.models import App, Jurisdiction, Deployment, SSOrganization, SSProduct, SSBudget, SSDependency, Dependency, DependencyType
from django.contrib import admin

class DependencyInline(admin.TabularInline):
    model = Dependency
    extra = 1
    fk_name = "to_app"

class AppAdmin(admin.ModelAdmin):
    inlines = (DependencyInline,)

admin.site.register(App, AppAdmin)
admin.site.register(Jurisdiction)
admin.site.register(Deployment)
admin.site.register(DependencyType)
#admin.site.register(SSOrganization)
#admin.site.register(SSProduct)
#admin.site.register(SSBudget)
#admin.site.register(SSDependency)
