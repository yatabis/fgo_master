from django.contrib import admin

from .models import Servant, NoblePhantasm, ActiveSkill, PassiveSkill, Synthesis

# Register your models here.


admin.site.register(Servant)
admin.site.register(NoblePhantasm)
admin.site.register(ActiveSkill)
admin.site.register(PassiveSkill)
admin.site.register(Synthesis)
