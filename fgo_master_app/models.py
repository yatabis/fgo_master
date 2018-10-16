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

    def __repr__(self):
        return self.name

    __str__ = __repr__
