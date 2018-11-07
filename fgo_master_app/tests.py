from django.test import TestCase

from .models import ActiveSkillEffect, PassiveSkillEffect
from .models import Synthesis
from .models import ActiveSkill

# Create your tests here.


class ActiveSkillEffectTest(TestCase):

    def test_repr(self):
        active_skill_effect = ActiveSkillEffect(text="test text",
                                                duration=3,
                                                duration_type="turn",
                                                value=10,
                                                step=0.5)
        print(active_skill_effect)


class PassiveSkillEffectTest(TestCase):

    def test_repr(self):
        passive_skill_effect = PassiveSkillEffect(text="teset text",
                                                  )


class SynthesisTest(TestCase):

    def test_repr(self):
        synthesis = Synthesis(material="QP",
                              ascension1=1,
                              ascension2=2,
                              ascension3=3,
                              ascension4=4,
                              skill_up1=1,
                              skill_up2=2,
                              skill_up3=3,
                              skill_up4=4,
                              skill_up5=5,
                              skill_up6=6,
                              skill_up7=7,
                              skill_up8=8,
                              skill_up9=9)
        print(synthesis)


class ActiveSkillTest(TestCase):
    print(ActiveSkill.icon_list)
    print(ActiveSkill.ICON_SET)
