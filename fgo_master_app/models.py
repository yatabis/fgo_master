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
    command_cards_distribution = models.CharField(max_length=8, default=QUICK1)
    quick_hits = models.IntegerField(default=1)
    arts_hits = models.IntegerField(default=1)
    buster_hits = models.IntegerField(default=1)
    extra_hits = models.IntegerField(default=1)
    # 宝具
    noble_phantasm = models.OneToOneField('NoblePhantasm', on_delete=models.CASCADE, null=True)
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
    synthesis = models.OneToOneField('Synthesis', on_delete=models.CASCADE, null=True)
    # 相性
    attribute = models.CharField(choices=SYNASTRY_SET, max_length=8, default=MAN)
    # 方針
    alignment1 = models.CharField(choices=POLICY_SET, max_length=8, default=LAWFUL)
    # 性格
    alignment2 = models.CharField(choices=CHARACTER_SET, max_length=8, default=GOOD)
    # 性別
    sex = models.CharField(choices=SEX_SET, max_length=8, default=MALE)
    # スター発生率
    star_getting_rate = models.IntegerField(default=0)
    # スター集中率
    star_focusing_rate = models.IntegerField(default=0)
    # 即死率
    death_rate = models.IntegerField(default=0)
    # 攻撃時のNP上昇基礎値
    NP_with_attack = models.IntegerField(default=0)
    # 被ダメ時のNP上昇基礎値
    NP_with_damage = models.IntegerField(default=0)

    def __repr__(self):
        return self.name

    __str__ = __repr__


class NoblePhantasm(models.Model):

    # 種類
    card = models.CharField(max_length=8)
    # 名称
    name = models.CharField(max_length=128)
    # 読み
    yomi = models.CharField(max_length=128)
    # ランク
    rank = models.CharField(max_length=2)
    # 種別
    type = models.CharField(max_length=8)
    # ヒット数
    hits = models.IntegerField()
    # 倍率
    value = models.IntegerField()

    def __repr__(self):
        return self.card + self.type

    __str__ = __repr__


class ActiveSkill(models.Model):

    # ID
    skill_id = models.AutoField(primary_key=True)
    # 名前
    name = models.CharField(max_length=64)
    # ランク
    rank = models.CharField(max_length=4)
    # チャージタイム
    charge_time = models.IntegerField()


class PassiveSkill(models.Model):

    # ID
    skill_id = models.AutoField(primary_key=True)
    # 名前
    name = models.IntegerField()
    # ランク
    rank = models.CharField(max_length=4)


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
