from django.contrib import admin

from .models import Servant
from .models import NoblePhantasm, NoblePhantasmEffect
from .models import ActiveSkill, PassiveSkill, ActiveSkillEffect, PassiveSkillEffect
from .models import Synthesis
from .models import CraftEssence
from .models import CommandCode
from .models import MysticCode

# Register your models here.


admin.site.register(Servant)
admin.site.register(NoblePhantasm)
admin.site.register(ActiveSkill)
admin.site.register(PassiveSkill)
admin.site.register(Synthesis)
