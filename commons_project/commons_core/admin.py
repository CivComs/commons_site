from commons_core.models import App, Jurisdiction, Deployment, SSOrganization, SSProduct, SSBudget, SSDependency, Dependency, DependencyType, Screenshot, Feature
from django.contrib import admin

class DependencyInline(admin.TabularInline):
    model = Dependency
    extra = 1
    fk_name = "to_app"
    verbose_name_plural = 'Dependencies'

class DependentsInline(admin.TabularInline):
    model = Dependency
    extra = 1
    fk_name = "from_app"
    verbose_name_plural = 'Dependents'

class AppAdmin(admin.ModelAdmin):
    inlines = (DependencyInline,DependentsInline)

# Hide the DependencyTypes from the admin homepage
class MyDependencyTypeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

admin.site.register(DependencyType, MyDependencyTypeAdmin)
admin.site.register(App, AppAdmin)
admin.site.register(Jurisdiction)
admin.site.register(Deployment)
admin.site.register(Screenshot)
admin.site.register(Feature)
#admin.site.register(SSOrganization)
#admin.site.register(SSProduct)
#admin.site.register(SSBudget)
#admin.site.register(SSDependency)
