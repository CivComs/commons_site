from commons_core.models import App, Jurisdiction, Deployment, SSOrganization, SSProduct, SSBudget, SSDependency, DependencyType
from django.contrib import admin

admin.site.register(App)
admin.site.register(Jurisdiction)
admin.site.register(Deployment)
admin.site.register(SSOrganization)
admin.site.register(SSProduct)
admin.site.register(SSBudget)
admin.site.register(SSDependency)
admin.site.register(DependencyType)

