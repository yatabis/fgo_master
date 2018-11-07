from django.db import models
import os

# Create your models here.


class Servant(models.Model):

    # クラスのセット
    SHIELDER = "Shielder"
    SABER = "Saber"
    ARCHER = "Archer"
    LANCER = "Lancer"
    RIDER = "Rider"
    CASTER = "Caster"
    ASSASSIN = "Assassin"
    BERSERKER = "Berserker"
    RULER = "Ruler"
    AVENGER = "Avenger"
    MOON_CANCER = "MoonCancer"
    ALTEREGO = "Alterego"
    FOREIGNER = "Foreigner"
    CLASS_SET = (
        (SHIELDER, "シールダー"),
        (SABER, "セイバー"),
        (ARCHER, "アーチャー"),
        (LANCER, "ランサー"),
        (RIDER, "ライダー"),
        (CASTER, "キャスター"),
        (ASSASSIN, "アサシン"),
        (BERSERKER, "バーサーカー"),
        (RULER, "ルーラー"),
        (AVENGER, "アベンジャー"),
        (MOON_CANCER, "ムーンキャンサー"),
        (ALTEREGO, "アルターエゴ"),
        (FOREIGNER, "フォーリナー"),
    )

    # 相性のセット
    SKY = "Sky"
    EARTH = "Earth"
    MAN = "Man"
    STAR = "Star"
    BEAST = "Beast"
    SYNASTRY_SET = (
        (SKY, "天"),
        (EARTH, "地"),
        (MAN, "人"),
        (STAR, "星"),
        (BEAST, "獣"),
    )

    # 方針のセット
    LAWFUL = "Lawful"
    CHAOTIC = "Chaotic"
    NEUTRAL = "Neutral"
    OTHER = "Other"
    POLICY_SET = (
        (LAWFUL, "秩序"),
        (CHAOTIC, "混沌"),
        (NEUTRAL, "中立"),
        (OTHER, "その他"),
    )

    # 性格のセット
    GOOD = "Good"
    EViL = "Evil"
    MADNESS = "Madness"
    CHARACTER_SET = (
        (GOOD, "善"),
        (EViL, "悪"),
        (NEUTRAL, "中庸"),
        (MADNESS, "狂"),
        (OTHER, "その他"),
    )

    # 性別のセット
    MALE = "Male"
    FEMALE = "Female"
    GENDER_SET = (
        (MALE, "男性"),
        (FEMALE, "女性"),
        (OTHER, "その他"),
    )

    # コマンドカード配分のセット
    QUICK3 = "Quick3"
    ARTS3 = "Arts3"
    BUSTER3 = "Buster3"
    QUICK1 = "Quick1"
    ARTS1 = "Arts1"
    BUSTER1 = "Buster1"
    CC_DISTRIBUTION = (
        (QUICK3, "QQQAB"),
        (ARTS3, "QAAAB"),
        (BUSTER3, "QABBB"),
        (QUICK1, "QAABB"),
        (ARTS1, "QQABB"),
        (BUSTER1, "QQAAB"),
    )

    # 番号
    No = models.IntegerField(primary_key=True)
    # 名前
    name = models.CharField(max_length=64)
    name_en = models.CharField(max_length=64)
    # クラス
    class_name = models.CharField(choices=CLASS_SET, default=SABER, max_length=16)
    # レアリティ
    rarity = models.IntegerField()
    # コスト
    cost = models.IntegerField()
    # 相性
    attribute = models.CharField(choices=SYNASTRY_SET, max_length=8, default=MAN)
    # 方針
    alignment1 = models.CharField(choices=POLICY_SET, max_length=8, default=LAWFUL)
    # 性格
    alignment2 = models.CharField(choices=CHARACTER_SET, max_length=8, default=GOOD)
    # 性別
    gender = models.CharField(choices=GENDER_SET, max_length=8, default=FEMALE)
    # 宝具
    noble_phantasm = models.ManyToManyField('NoblePhantasm', related_name="servant")
    # 保有スキル
    active_skill1 = models.ManyToManyField('ActiveSkill', related_name="servant_for_skill1")
    active_skill2 = models.ManyToManyField('ActiveSkill', related_name="servant_for_skill2")
    active_skill3 = models.ManyToManyField('ActiveSkill', related_name="servant_for_skill3")
    # クラススキル
    passive_skill = models.ManyToManyField('PassiveSkill', related_name="servant")
    # コマンドカード
    command_cards_distribution = models.CharField(max_length=8, choices=CC_DISTRIBUTION, default=QUICK1)
    quick_hits = models.IntegerField(default=1)
    arts_hits = models.IntegerField(default=1)
    buster_hits = models.IntegerField(default=1)
    extra_hits = models.IntegerField(default=1)

    # Detail

    # プロフィール
    # イラストレーター
    illust = models.CharField(max_length=64, default="")
    # 声優
    cv = models.CharField(max_length=64, default="")

    # パラメーター
    # 筋力
    str = models.CharField(max_length=4, default="A")
    # 敏捷
    agl = models.CharField(max_length=4, default="A")
    # 幸運
    luk = models.CharField(max_length=4, default="A")
    # 耐久
    end = models.CharField(max_length=4, default="A")
    # 魔力
    mp = models.CharField(max_length=4, default="A")
    # 宝具
    np = models.CharField(max_length=4, default="A")
    # 身長
    height = models.IntegerField(default=0)
    # 体重
    weight = models.IntegerField(default=0)
    # 出典
    origin = models.CharField(max_length=64, default="")
    # 地域
    region = models.CharField(max_length=64, default="")
    # ステータス
    HP1 = models.IntegerField(default=0)
    HP10 = models.IntegerField(default=0)
    HP20 = models.IntegerField(default=0)
    HP30 = models.IntegerField(default=0)
    HP40 = models.IntegerField(default=0)
    HP50 = models.IntegerField(default=0)
    HP60 = models.IntegerField(default=0)
    HP70 = models.IntegerField(default=0)
    HP80 = models.IntegerField(default=0)
    HP90 = models.IntegerField(default=0)
    HP100 = models.IntegerField(default=0)
    ATK1 = models.IntegerField(default=0)
    ATK10 = models.IntegerField(default=0)
    ATK20 = models.IntegerField(default=0)
    ATK30 = models.IntegerField(default=0)
    ATK40 = models.IntegerField(default=0)
    ATK50 = models.IntegerField(default=0)
    ATK60 = models.IntegerField(default=0)
    ATK70 = models.IntegerField(default=0)
    ATK80 = models.IntegerField(default=0)
    ATK90 = models.IntegerField(default=0)
    ATK100 = models.IntegerField(default=0)
    # スター発生率
    star_drop_rate = models.FloatField(default=0)
    # スター集中度
    star_gather_rate = models.FloatField(default=0)
    # 即死率
    death_rate = models.FloatField(default=100)
    # 攻撃時のNP上昇基礎値
    NP_with_attack = models.FloatField(default=0)
    # 被ダメ時のNP上昇基礎値
    NP_gain_from_damage = models.FloatField(default=0)

    def __repr__(self):
        return f"{self.name} ({self.class_name})"

    def __str__(self):
        return self.__repr__()


class NoblePhantasm(models.Model):

    # カードのセット
    QUICK = "Quick"
    ARTS = "Arts"
    BUSTER = "Buster"
    CARD_SET = (
        (QUICK, QUICK),
        (ARTS, ARTS),
        (BUSTER, BUSTER)
    )

    # 種類のセット
    ALL = "whole"
    SINGLE = "single"
    SUPPORT = "support"
    TYPE_SET = (
        (ALL, "全体"),
        (SINGLE, "単体"),
        (SUPPORT, "補助")
    )

    # カード
    card = models.CharField(choices=CARD_SET, max_length=8, default=BUSTER)
    # 種類
    type = models.CharField(choices=TYPE_SET, max_length=8, default=ALL)
    # 名称
    name = models.CharField(max_length=64)
    name_en = models.CharField(max_length=64)
    # 読み
    yomi = models.CharField(max_length=64)
    # ランク
    rank = models.CharField(max_length=4)
    # 種別
    anti = models.CharField(max_length=8, default="")
    # 効果
    effect = models.ManyToManyField('NoblePhantasmEffect', related_name="noble_phantasm")

    def __repr__(self):
        return f"{self.name} ({self.yomi})"

    def __str__(self):
        return self.__repr__()


class NoblePhantasmEffect(models.Model):

    # 対象のセット
    YOURSELF = "yourself"
    ALL_ALLIES = "all_allies"
    SINGLE_ENEMY = "single_enemy"
    ALL_ENEMIES = "all_enemies"
    TARGET_SET = (
        (YOURSELF, "自身"),
        (ALL_ALLIES, "味方全体"),
        (SINGLE_ENEMY, "敵単体"),
        (ALL_ENEMIES, "敵全体")
    )

    # 種類
    target = models.CharField(choices=TARGET_SET, max_length=16, default=ALL_ENEMIES)
    # 効果
    text = models.TextField(default="")
    # ヒット数
    hits = models.IntegerField(blank=True, null=True)
    # 持続時間
    duration = models.IntegerField(blank=True, null=True)
    duration_type = models.CharField(choices=(("turn", "ターン"), ("times", "回")), max_length=8, blank=True, null=True)
    # 効果アップ
    increase = models.CharField(choices=(("Lv", "Lv"), ("OC", "OC")), max_length=2, default="Lv")
    # 数値
    value1 = models.FloatField(blank=True, null=True)
    value2 = models.FloatField(blank=True, null=True)
    value3 = models.FloatField(blank=True, null=True)
    value4 = models.FloatField(blank=True, null=True)
    value5 = models.FloatField(blank=True, null=True)

    def __repr__(self):
        return f"{self.text}[{self.get_increase_display()}]({self.duration}{self.get_duration_type_display()})" \
               f" <{self.value1}→{self.value2}→{self.value3}→{self.value4}→{self.value5}>"

    def __str__(self):
        return self.__repr__()


class ActiveSkill(models.Model):

    # アイコンのセット
    icon_file = "./static/fgo_master_app/images/icon/active_skill"
    icon_list = os.listdir(icon_file)
    ICON_SET = tuple((os.path.splitext(il)[0], il) for il in icon_list)

    # 名前
    name = models.CharField(max_length=64)
    name_en = models.CharField(max_length=64)
    # アイコン
    icon = models.CharField(choices=ICON_SET, max_length=64, blank=True, default="")
    # ランク
    rank = models.CharField(max_length=4, blank=True, default="")
    # チャージタイム
    CT = models.IntegerField()
    # 効果
    effect = models.ManyToManyField('ActiveSkillEffect', related_name="active_skill")

    def __repr__(self):
        return f"{self.name} {self.rank}"

    def __str__(self):
        return f"{self.name} {self.rank}"


class ActiveSkillEffect(models.Model):
    # 効果
    text = models.TextField(default="")
    # 持続時間
    duration = models.IntegerField(blank=True, null=True)
    duration_type = models.CharField(choices=(("turn", "ターン"), ("times", "回")), max_length=8, blank=True, default="")
    # 数値
    value = models.FloatField(blank=True, null=True)
    step = models.FloatField(blank=True, null=True)

    def __repr__(self):
        return f"{self.text}({self.duration}{self.get_duration_type_display()}) [{self.value} + {self.step}]"

    def __str__(self):
        return self.__repr__()


class PassiveSkill(models.Model):

    # アイコンのセット
    icon_file = "./static/fgo_master_app/images/icon/passive_skill"
    icon_list = os.listdir(icon_file)
    ICON_SET = tuple((os.path.splitext(il)[0], il) for il in icon_list)

    # 名前
    name = models.CharField(max_length=64)
    # アイコン
    icon = models.CharField(choices=ICON_SET, max_length=64, blank=True, default="")
    # ランク
    rank = models.CharField(max_length=4, blank=True, default="")
    # 効果
    text = models.TextField(default="")
    # 数値
    value = models.FloatField(blank=True, null=True)

    def __repr__(self):
        return f"{self.name} {self.rank}"

    def __str__(self):
        return self.__repr__()


class Synthesis(models.Model):

    # 素材のセット
    QP = "QP"
    MATERIAL_SET = (
        (QP, "QP"),
    )

    # 素材
    material = models.CharField(choices=MATERIAL_SET, max_length=32)
    # 霊基再臨
    ascension1 = models.IntegerField(default=0)
    ascension2 = models.IntegerField(default=0)
    ascension3 = models.IntegerField(default=0)
    ascension4 = models.IntegerField(default=0)
    # スキルレベル
    skill_up1 = models.IntegerField(default=0)
    skill_up2 = models.IntegerField(default=0)
    skill_up3 = models.IntegerField(default=0)
    skill_up4 = models.IntegerField(default=0)
    skill_up5 = models.IntegerField(default=0)
    skill_up6 = models.IntegerField(default=0)
    skill_up7 = models.IntegerField(default=0)
    skill_up8 = models.IntegerField(default=0)
    skill_up9 = models.IntegerField(default=0)

    def __repr__(self):
        total = self.ascension1 + self.ascension2 + self.ascension3 + self.ascension4 + \
                self.skill_up1 + self.skill_up2 + self.skill_up3 + self.skill_up4 + self.skill_up5 + \
                self.skill_up6 + self.skill_up7 + self.skill_up8 + self.skill_up9
        return f"{self.material} {total}"

    def __str__(self):
        return self.__repr__()


class CraftEssence(models.Model):

    # アイコンのセット
    ICON_SET = ()

    # 名前
    name = models.CharField(max_length=64)
    # レアリティ
    rarity = models.IntegerField()
    # アイコン
    icon = models.CharField(choices=ICON_SET, max_length=64, blank=True, default="")
    # テキスト
    text = models.TextField(default="テキスト")


class CraftEssenceEffect(models.Model):
    pass


class CommandCode(models.Model):

    # 名前
    name = models.CharField(max_length=64)
    # レアリティ
    rarity = models.IntegerField()


class MysticCode(models.Model):

    # 名前
    name = models.CharField(max_length=64)
