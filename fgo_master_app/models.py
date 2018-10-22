from django.db import models

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

    # 番号
    No = models.AutoField(primary_key=True)
    # 名前
    name = models.CharField(max_length=64)
    # クラス
    class_name = models.CharField(choices=CLASS_SET, default=SABER, max_length=16)
    # レアリティ
    rarity = models.IntegerField()
    # コスト
    cost = models.IntegerField()

    # Detail

    # 相性のセット
    SKY = "sky"
    EARTH = "earth"
    MAN = "man"
    STAR = "star"
    BEAST = "beast"
    SYNASTRY_SET = (
        (SKY, "天"),
        (EARTH, "地"),
        (MAN, "人"),
        (STAR, "星"),
        (BEAST, "獣"),
    )

    # 方針のセット
    LAWFUL = "cosmos"
    CHAOTIC = "chaos"
    NEUTRAL = "neutral"
    OTHER = "other"
    POLICY_SET = (
        (LAWFUL, "秩序"),
        (CHAOTIC, "混沌"),
        (NEUTRAL, "中立"),
        (OTHER, "その他"),
    )

    # 性格のセット
    GOOD = "good"
    EViL = "evil"
    INSANE = "insane"
    CHARACTER_SET = (
        (GOOD, "善"),
        (EViL, "悪"),
        (NEUTRAL, "中庸"),
        (INSANE, "狂"),
        (OTHER, "その他"),
    )

    # 性別のセット
    MALE = "male"
    FEMALE = "female"
    SEX_SET = (
        (MALE, "男性"),
        (FEMALE, "女性"),
        (OTHER, "その他"),
    )

    # コマンドカード配分のセット
    QUICK3 = "quick3"
    ARTS3 = "arts3"
    BUSTER3 = "buster3"
    QUICK1 = "quick1"
    ARTS1 = "arts1"
    BUSTER1 = "buster1"
    CC_DISTRIBUTION = (
        (QUICK3, "QQQAB"),
        (ARTS3, "QAAAB"),
        (BUSTER3, "QABBB"),
        (QUICK1, "QAABB"),
        (ARTS1, "QQABB"),
        (BUSTER1, "QQAAB"),
    )

    # コマンドカード
    command_cards_distribution = models.CharField(max_length=8, choices=CC_DISTRIBUTION, default=QUICK1)
    quick_hits = models.IntegerField(default=1)
    arts_hits = models.IntegerField(default=1)
    buster_hits = models.IntegerField(default=1)
    extra_hits = models.IntegerField(default=1)
    # 保有スキル
    active_skill = models.ManyToManyField('ActiveSkill')
    # クラススキル
    passive_skill = models.ManyToManyField('PassiveSkill')
    # 基礎ステータス
    base_HP = models.IntegerField(default=0)
    max_HP = models.IntegerField(default=0)
    palingenesis_HP = models.IntegerField(default=0)
    base_ATK = models.IntegerField(default=0)
    max_ATK = models.IntegerField(default=0)
    palingenesis_ATK = models.IntegerField(default=0)
    # 強化
    synthesis = models.OneToOneField('Synthesis', on_delete=models.CASCADE, blank=True, null=True)
    # 相性
    attribute = models.CharField(choices=SYNASTRY_SET, max_length=8, default=MAN)
    # 方針
    alignment1 = models.CharField(choices=POLICY_SET, max_length=8, default=LAWFUL)
    # 性格
    alignment2 = models.CharField(choices=CHARACTER_SET, max_length=8, default=GOOD)
    # 性別
    sex = models.CharField(choices=SEX_SET, max_length=8, default=MALE)
    # スター発生率
    star_getting_rate = models.FloatField(default=0)
    # スター集中率
    star_focusing_rate = models.FloatField(default=0)
    # 即死率
    death_rate = models.FloatField(default=100)
    # 攻撃時のNP上昇基礎値
    NP_with_attack = models.FloatField(default=0)
    # 被ダメ時のNP上昇基礎値
    NP_with_damage = models.FloatField(default=0)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


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
    WHOLE = "whole"
    SINGLE = "single"
    SUPPORT = "support"
    TYPE_SET = (
        (WHOLE, "全体"),
        (SINGLE, "単体"),
        (SUPPORT, "補助")
    )

    # サーヴァント
    servant = models.ForeignKey('Servant', on_delete=models.CASCADE, related_name="noble_phantasm", blank=True, null=True)
    # カード
    card = models.CharField(choices=CARD_SET, max_length=8, default=BUSTER)
    # 種類
    type = models.CharField(choices=TYPE_SET, max_length=8, default=WHOLE)
    # 名称
    name = models.CharField(max_length=128)
    # 読み
    yomi = models.CharField(max_length=128)
    # ランク
    rank = models.CharField(max_length=4)
    # 種別
    anti = models.CharField(max_length=8, blank=True, default="")
    # テキスト
    text = models.TextField(blank=True, default="")
    # 持続時間
    duration = models.IntegerField(blank=True, null=True)
    duration_type = models.CharField(choices=(("turn", "ターン"), ("times", "回")), max_length=8, blank=True, null=True)
    # ヒット数
    hits = models.IntegerField(blank=True, null=True)
    # 倍率
    value1 = models.FloatField(blank=True, null=True)
    value2 = models.FloatField(blank=True, null=True)
    value3 = models.FloatField(blank=True, null=True)
    value4 = models.FloatField(blank=True, null=True)
    value5 = models.FloatField(blank=True, null=True)
    # 効果
    effect = models.ManyToManyField('NoblePhantasmEffect', related_name="noble_phantasm")

    def __repr__(self):
        return f"{self.name} ({self.yomi})"

    def __str__(self):
        return f"{self.name} ({self.yomi})"


class NoblePhantasmEffect(models.Model):
    # 効果
    text = models.TextField(default="")
    # 持続時間
    duration = models.IntegerField(blank=True, null=True)
    duration_type = models.CharField(choices=(("turn", "ターン"), ("times", "回")), max_length=8, blank=True, null=True)
    # OC
    OC = models.BooleanField(default=True)
    # 数値
    value1 = models.FloatField(blank=True, null=True)
    value2 = models.FloatField(blank=True, null=True)
    value3 = models.FloatField(blank=True, null=True)
    value4 = models.FloatField(blank=True, null=True)
    value5 = models.FloatField(blank=True, null=True)

    def __repr__(self):
        return f"{self.text}({self.duration}{self.get_duration_type_display})" \
               f" <{self.value1}→{self.value2}→{self.value3}→{self.value4}→{self.value5}>"

    def __str__(self):
        return f"{self.text}({self.duration}{self.get_duration_type_display})" \
               f" <{self.value1}→{self.value2}→{self.value3}→{self.value4}→{self.value5}>"


class ActiveSkill(models.Model):

    # ID
    skill_id = models.AutoField(primary_key=True)
    # 名前
    name = models.CharField(max_length=64)
    # アイコン
    icon = models.ImageField(upload_to='images/', blank=True, null=True)
    # ランク
    rank = models.CharField(max_length=4, blank=True, default="")
    # チャージタイム
    CT = models.IntegerField()
    # 効果
    effect = models.ManyToManyField('NoblePhantasmEffect', related_name="active_skill")

    def __repr__(self):
        return f"{self.name} {self.rank}"

    def __str__(self):
        return f"{self.name} {self.rank}"


class ActiveSkillEffect(models.Model):
    # 効果
    text = models.TextField(default="")
    # 持続時間
    duration = models.IntegerField(blank=True, null=True)
    duration_type = models.CharField(choices=(("turn", "ターン"), ("times", "回")), max_length=8, blank=True, null=True)
    # 数値
    level1 = models.FloatField(blank=True, null=True)
    level2 = models.FloatField(blank=True, null=True)
    level3 = models.FloatField(blank=True, null=True)
    level4 = models.FloatField(blank=True, null=True)
    level5 = models.FloatField(blank=True, null=True)
    level6 = models.FloatField(blank=True, null=True)
    level7 = models.FloatField(blank=True, null=True)
    level8 = models.FloatField(blank=True, null=True)
    level9 = models.FloatField(blank=True, null=True)
    level10 = models.FloatField(blank=True, null=True)

    def __repr__(self):
        return f"{self.text}({self.duration}{self.get_duration_type_display}) <{self.level1}→→{self.level10}>"

    def __str__(self):
        return f"{self.text}({self.duration}{self.get_duration_type_display}) <{self.level1}→→{self.level10}>"


class PassiveSkill(models.Model):

    # ID
    skill_id = models.AutoField(primary_key=True)
    # 名前
    name = models.CharField(max_length=64)
    # アイコン
    icon = models.ImageField(upload_to='images/', blank=True, null=True)
    # ランク
    rank = models.CharField(max_length=4, blank=True, default="")
    # 効果
    effect = models.ManyToManyField('NoblePhantasmEffect', related_name="passive_skill")

    def __repr__(self):
        return f"{self.name} {self.rank}"

    def __str__(self):
        return f"{self.name} {self.rank}"


class PassiveSkillEffect(models.Model):
    # 効果
    text = models.TextField(default="")
    # 持続時間
    duration = models.IntegerField(blank=True, null=True)
    duration_type = models.CharField(choices=(("turn", "ターン"), ("times", "回")), max_length=8, blank=True, null=True)
    # 数値
    value = models.FloatField(blank=True, null=True)

    def __repr__(self):
        return f"{self.text}({self.duration}{self.get_duration_type_display}) <{self.value}>"

    def __str__(self):
        return f"{self.text}({self.duration}{self.get_duration_type_display}) <{self.value}>"


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


class CraftEssence(models.Model):

    # 名前
    name = models.CharField(max_length=64)
    # レアリティ
    rarity = models.IntegerField()
    # アイコン
    icon = models.ImageField(upload_to='images/', blank=True, null=True)
    # テキスト
    text = models.TextField(default="テキスト")


class CommandCode(models.Model):

    # 名前
    name = models.CharField(max_length=64)
    # レアリティ
    rarity = models.IntegerField()


class MysticCode(models.Model):

    # 名前
    name = models.CharField(max_length=64)
