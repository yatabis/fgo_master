# Generated by Django 2.1.2 on 2018-12-05 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fgo_master_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassiveSkillEffect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effect', models.CharField(choices=[('Quick', 'Quickカードの性能'), ('Arts', 'Artsカードの性能'), ('Buster', 'Busterカードの性能'), ('Critical', 'クリティカル威力'), ('StarDrop', 'スター発生率'), ('DebuffSuccess', '弱体付与成功率'), ('DamagePlus', '与ダメージプラス状態'), ('DebuffResist', '弱体耐性'), ('DeathResist', '即死耐性'), ('MentalDebuffResist', '精神異常耐性'), ('NPDamaged', '被ダメージ時に獲得するNP'), ('NP_et', '毎ターンNP獲得状態'), ('DeathImmune', '即死無効状態'), ('PowerfulCharmResist', '強力な魅了耐性'), ('DeathEffect', '通常攻撃時に極低確率で即死効果が発生する状態'), ('DEF', '防御力'), ('SpecialAttack', '特攻状態'), ('Healing', 'HP回復量'), ('Star_et', '毎ターンスター2個獲得状態'), ('BurnImmune', 'やけど無効状態')], default='Quick', max_length=32)),
                ('target', models.CharField(choices=[('yourself', '自身'), ('all_in_sub_ex_you', '自信を除く味方全体<控え含む>')], default='yourself', max_length=32)),
                ('limit_type', models.CharField(choices=[('attribute', '特性'), ('class', 'クラス'), ('field', 'フィールド'), ('None', 'なし')], default='None', max_length=16)),
                ('attr_limit', models.CharField(choices=[('Humanoid', '人型'), ('None', 'なし')], default='None', max_length=16)),
                ('class_limit', models.CharField(choices=[('Shilder', 'シールダー'), ('Saber', 'セイバー'), ('Archer', 'アーチャー'), ('Lancer', 'ランサー'), ('Rider', 'ライダー'), ('Caster', 'キャスター'), ('Assassin', 'アサシン'), ('Berserker', 'バーサーカー'), ('Ruler', 'ルーラー'), ('Avenger', 'アベンジャー'), ('MoonCancer', 'ムーンキャンサー'), ('Alterego', 'アルターエゴ'), ('Foreigner', 'フォーリナー'), ('None', 'なし')], default='None', max_length=16)),
                ('field_limit', models.CharField(choices=[('WaterSide', '水辺'), ('None', 'なし')], default='None', max_length=16)),
                ('text', models.CharField(choices=[('apply', '付与'), ('increase', 'アップ'), ('slightly_increase', '少しアップ'), ('decrease', 'ダウン')], default='increase', max_length=32)),
                ('value', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='passiveskill',
            name='text',
        ),
        migrations.RemoveField(
            model_name='passiveskill',
            name='value',
        ),
        migrations.AlterField(
            model_name='passiveskill',
            name='icon',
            field=models.CharField(choices=[('RidingSkill', '騎乗'), ('TerritoryCreation', '陣地作成'), ('MadnessEnhancement', '狂化'), ('IndependentAction', '単独行動'), ('PresenceConcealment', '気配遮断'), ('ItemConstruction', '道具作成'), ('Divinity', '神性'), ('MagicResistance', '対魔力'), ('CoreoftheGoddess', '女神の神核'), ('Avenger', '復讐者'), ('OblivionCorrection', '忘却補正'), ('SelfRestoration', '自己回復'), ('境界にて', '境界にて'), ('領域外の生命', '領域外の生命'), ('NoEffect', '効果なし')], default='RidingSkill', max_length=64),
        ),
        migrations.AlterField(
            model_name='passiveskill',
            name='rank',
            field=models.CharField(default='A', max_length=8),
        ),
        migrations.AlterField(
            model_name='servant',
            name='class_name',
            field=models.CharField(choices=[('Shilder', 'シールダー'), ('Saber', 'セイバー'), ('Archer', 'アーチャー'), ('Lancer', 'ランサー'), ('Rider', 'ライダー'), ('Caster', 'キャスター'), ('Assassin', 'アサシン'), ('Berserker', 'バーサーカー'), ('Ruler', 'ルーラー'), ('Avenger', 'アベンジャー'), ('MoonCancer', 'ムーンキャンサー'), ('Alterego', 'アルターエゴ'), ('Foreigner', 'フォーリナー')], default='Saber', max_length=16),
        ),
        migrations.AddField(
            model_name='passiveskill',
            name='effect',
            field=models.ManyToManyField(related_name='passive_skill', to='fgo_master_app.PassiveSkillEffect'),
        ),
    ]
