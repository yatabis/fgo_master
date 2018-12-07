from django.db import models
import os

# Create your models here.


class Servant(models.Model):

    # クラスのセット
    CLASS_SET = (
        ("Shilder", "シールダー"),
        ("Saber", "セイバー"),
        ("Archer", "アーチャー"),
        ("Lancer", "ランサー"),
        ("Rider", "ライダー"),
        ("Caster", "キャスター"),
        ("Assassin", "アサシン"),
        ("Berserker", "バーサーカー"),
        ("Ruler", "ルーラー"),
        ("Avenger", "アベンジャー"),
        ("MoonCancer", "ムーンキャンサー"),
        ("Alterego", "アルターエゴ"),
        ("Foreigner", "フォーリナー"),
    )

    # 相性のセット
    ATTRIBUTE_SET = (
        ("Sky", "天"),
        ("Earth", "地"),
        ("Man", "人"),
        ("Star", "星"),
        ("Beast", "獣"),
    )

    # 方針のセット
    POLICY_SET = (
        ("Lawful", "秩序"),
        ("Chaotic", "混沌"),
        ("Neutral", "中立"),
        ("Other", "その他"),
    )

    # 性格のセット
    CHARACTER_SET = (
        ("Good", "善"),
        ("Evil", "悪"),
        ("Neutral", "中庸"),
        ("Madness", "狂"),
        ("Other", "その他"),
    )

    # 性別のセット
    GENDER_SET = (
        ("Male", "男性"),
        ("Female", "女性"),
        ("Other", "その他"),
    )

    # コマンドカード配分のセット
    CC_DISTRIBUTION = (
        ("Quick3", "QQQAB"),
        ("Arts3", "QAAAB"),
        ("Buster3", "QABBB"),
        ("Quick1", "QAABB"),
        ("Arts1", "QQABB"),
        ("Buster1", "QQAAB"),
    )

    # 番号
    No = models.IntegerField(primary_key=True)
    # 名前
    name = models.CharField(max_length=64)
    name_en = models.CharField(max_length=64)
    # クラス
    class_name = models.CharField(choices=CLASS_SET, default=CLASS_SET[1][0], max_length=16)
    # レアリティ
    rarity = models.IntegerField()
    # コスト
    cost = models.IntegerField()
    # 相性
    attribute = models.CharField(choices=ATTRIBUTE_SET, max_length=8, default=ATTRIBUTE_SET[2][0])
    # 方針
    alignment1 = models.CharField(choices=POLICY_SET, max_length=8, default=POLICY_SET[0][0])
    # 性格
    alignment2 = models.CharField(choices=CHARACTER_SET, max_length=8, default=CHARACTER_SET[0][0])
    # 性別
    gender = models.CharField(choices=GENDER_SET, max_length=8, default=GENDER_SET[1][0])
    # 宝具
    noble_phantasm = models.ManyToManyField('NoblePhantasm', related_name="servant")
    # 保有スキル
    active_skill1 = models.ManyToManyField('ActiveSkill', related_name="servant_for_skill1")
    active_skill2 = models.ManyToManyField('ActiveSkill', related_name="servant_for_skill2")
    active_skill3 = models.ManyToManyField('ActiveSkill', related_name="servant_for_skill3")
    # クラススキル
    passive_skill = models.ManyToManyField('PassiveSkill', related_name="servant")
    # コマンドカード
    command_cards_distribution = models.CharField(max_length=8, choices=CC_DISTRIBUTION, default=CC_DISTRIBUTION[3][0])
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
    ICON_SET = (
        ("ATK_UP", "ATKアップ"),
        ("ATK_DOWN", "ATKダウン"),
        ("Buster_UP", "バスターアップ"),
        ("Arts_UP", "アーツアップ"),
        ("Quick_UP", "クイックアップ"),
        ("Critical_UP", "クリティカルアップ"),
        ("Critical_DOWN", "クリティカルダウン"),
        ("SpecialAttack_UP", "特攻アップ"),
        ("NPStrength_UP", "宝具威力アップ"),
        ("NPStrength_DOWN", "宝具威力ダウン"),
        ("Hits_UP", "ヒット数増加"),
        ("DEF_UP", "防御アップ"),
        ("DEF_DOWN", "防御ダウン"),
        ("Invincible", "無敵"),
        ("InvincibleIgnore", "無敵貫通"),
        ("Evade", "回避"),
        ("SureHit", "必中"),
        ("Guts", "ガッツ"),
        ("Charm", "魅了"),
        ("TargetFocus", "タゲ集中"),
        ("DebuffResist_UP", "弱体耐性アップ"),
        ("DebuffResist_DOWN", "弱体耐性ダウン"),
        ("DebuffRemove", "弱体解除"),
        ("DebuffImmune", "弱体無効"),
        ("BuffImmune", "強化無効"),
        ("HP_UP", "HP回復"),
        ("HP_et", "HP回復状態"),
        ("Healing_UP", "HP回復量アップ"),
        ("MaxHP_UP", "最大HPアップ"),
        ("NP_UP", "NP獲得"),
        ("NP_et", "NP獲得状態"),
        ("NPGain_UP", "NP獲得量アップ"),
        ("Star_UP", "スター獲得"),
        ("Star_et", "スター獲得状態"),
        ("StarDrop_UP", "スター発生率アップ"),
        ("StarGather_UP", "スター集中度アップ"),
        ("StarGather_DOWN", "スター集中度ダウン"),
        ("NPChargeIncrease", "宝具チャージ増加"),
        ("ChargeDecrease", "チャージ減少"),
        ("Poison", "毒"),
        ("DebuffSuccess_UP", "弱体付与成功率アップ"),
        ("DeathSuccess_UP", "即死成功率アップ"),
        ("DeathResist_DOWN", "即死耐性ダウン"),
        ("Stun", "スタン"),
        ("Seal", "封印"),
        ("AD_UP", "攻防アップ"),
        ("AQB_UP", "AQBアップ"),
        ("AB_UP", "ABアップ"),
        ("QB_UP", "QBアップ"),
        ("Turn", "ターン"),
        ("BeautifulAppearance", "麗しの風貌"),
        ("MysticEyes", "直死の魔眼"),
        ("YinYang", "陰陽魚"),
        ("KurNuGiA", "冥界の護り"),
        ("Iseidako", "異星蛸"),
        ("", "平穏の無花果"),
        ("", "無貌の月"),
    )

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
    ICON_SET = (
        ("RidingSkill", "騎乗"),
        ("TerritoryCreation", "陣地作成"),
        ("MadnessEnhancement", "狂化"),
        ("IndependentAction", "単独行動"),
        ("PresenceConcealment", "気配遮断"),
        ("ItemConstruction", "道具作成"),
        ("Divinity", "神性"),
        ("MagicResistance", "対魔力"),
        ("CoreoftheGoddess", "女神の神核"),
        ("Avenger", "復讐者"),
        ("OblivionCorrection", "忘却補正"),
        ("SelfRestoration", "自己回復"),
        ("境界にて", "境界にて"),
        ("領域外の生命", "領域外の生命"),
        ("NoEffect", "効果なし"),
    )

    # 名前
    name = models.CharField(max_length=64, verbose_name="クラススキル名")
    # アイコン
    icon = models.CharField(choices=ICON_SET, max_length=64, default=ICON_SET[0][0], verbose_name="アイコン")
    # ランク
    rank = models.CharField(max_length=8, default="A", verbose_name="ランク")
    # 効果
    effect = models.ManyToManyField('PassiveSkillEffect', related_name="passive_skill", verbose_name="効果")

    def display_text(self):
        text = ""
        prev = None
        for i, effect in enumerate(self.effect.all()):
            if i == 0:
                text += effect.get_target_display()
                text += "に" if effect.text == "apply" else "の"
                text += effect.display_text()
            else:
                if effect.target == prev:
                    text += "＆"
                else:
                    text += effect.get_target_display()
                    text += "に" if effect.text == "apply" else "の"
                text += effect.display_text()
            prev = effect.target
        return text

    def __repr__(self):
        return f"{self.name} {self.rank}"

    def __str__(self):
        return self.__repr__()


class PassiveSkillEffect(models.Model):

    # 効果のセット
    EFFECT_SET = (
        ("Quick", "Quickカードの性能"),
        ("Arts", "Artsカードの性能"),
        ("Buster", "Busterカードの性能"),
        ("Critical", "クリティカル威力"),
        ("StarDrop", "スター発生率"),
        ("DebuffSuccess", "弱体付与成功率"),
        ("DamagePlus", "与ダメージプラス状態"),
        ("DebuffResist", "弱体耐性"),
        ("DeathResist", "即死耐性"),
        ("MentalDebuffResist", "精神異常耐性"),
        ("NPDamaged", "被ダメージ時に獲得するNP"),
        ("NP_et", "毎ターンNP獲得状態"),
        ("DeathImmune", "即死無効状態"),
        ("PowerfulCharmResist", "強力な魅了耐性"),
        ("DeathEffect", "通常攻撃時に極低確率で即死効果が発生する状態"),
        ("DEF", "防御力"),
        ("SpecialAttack", "特攻状態"),
        ("Healing", "HP回復量"),
        ("Star_et", "毎ターンスター2個獲得状態"),
        ("BurnImmune", "やけど無効状態"),
    )

    # 対象のセット
    TARGET_SET = (
        ("yourself", "自身"),
        ("all_in_sub_ex_you", "自信を除く味方全体<控え含む>"),
    )

    # 程度のセット
    TEXT_SET = (
        ("apply", "付与"),
        ("increase", "アップ"),
        ("slightly_increase", "少しアップ"),
        ("decrease", "ダウン"),
    )

    # 特性のセット
    ATTR_SET = (
        ("Humanoid", "人型"),
        ("None", "なし")
    )

    # クラスのセット
    CLASS_SET = Servant.CLASS_SET + (("None", "なし"),)

    # フィールドのセット
    FIELD_SET = (
        ("WaterSide", "水辺"),
        ("None", "なし")
    )

    # 効果
    effect = models.CharField(max_length=32, choices=EFFECT_SET, default=EFFECT_SET[0][0], verbose_name="効果")
    # 対象
    target = models.CharField(max_length=32, choices=TARGET_SET, default=TARGET_SET[0][0], verbose_name="対象")
    # 制限
    attr_limit = models.CharField(max_length=16, choices=ATTR_SET, default=ATTR_SET[-1][0], verbose_name="特性制限")
    class_limit = models.CharField(max_length=16, choices=CLASS_SET, default=CLASS_SET[-1][0], verbose_name="クラス制限")
    field_limit = models.CharField(max_length=16, choices=FIELD_SET, default=FIELD_SET[-1][0], verbose_name="フィールド制限")
    # 程度
    text = models.CharField(max_length=32, choices=TEXT_SET, default=TEXT_SET[1][0], verbose_name="程度")
    # 値
    value = models.FloatField(blank=True, null=True, verbose_name="値")

    def display_text(self):
        text = ""
        if not self.field_limit == "None":
            text += f"〔{self.get_field_limit_display()}〕のあるフィールドにおいてのみ、{self.get_target_display()}"
            text += "に" if self.text == "apply" else "の"
        if not self.attr_limit == "None":
            text += f"〔{self.get_attr_limit_display()}〕"
        if not self.class_limit == "None":
            text += f"〔{self.get_class_limit_display()}〕クラス"
        if not self.attr_limit == "None" or not self.class_limit == "None":
            if self.effect == "DEF":
                text += "の敵からの攻撃に対する"
            if self.effect == "SpecialAttack":
                text += "への"
        text += self.get_effect_display()
        text += "を"
        text += self.get_text_display()
        return text

    def __repr__(self):
        ret = ""
        if self.field_limit == "None":
            ret += self.get_target_display()
            ret += "に" if self.text == "apply" else "の"
        ret += self.display_text()
        if self.value:
            ret += f"({abs(self.value)})"
        return ret

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
