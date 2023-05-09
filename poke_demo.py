from random import randint
from IPython.display import Image, display_png

class Pokemon(object):
    def __init__(self, name, level, isEnemy=False):
        self.name = name
        if isEnemy:
            print('相手は' + self.name + 'をくりだした！')
        else:
            print('いけ！' + self.name + '！')

        self.level = level

        self.Fainting = False
        
    
    def hit(self, damage):
        self.HP = max(self.HP - damage, 0)
        if self.HP == 0:
            self.Fainting = True
            print(self.name + 'はたおれた！')

    def showStatus(self):
        print('HP：', self.HP, '/', self.max_HP)

        if self.Fainting:
            print('ひんし')

class Charizard(Pokemon):
    Type = ('ほのお', 'ひこう')

    def __init__(self, name, level):
        display_png(Image('PythonTutorialwithPokemon/Images/Charizard.GIF', format='png'))
        super(Charizard, self).__init__(name, level)

        BaseHP = 78
        BaseAtk = 84
        BaseDef = 78
        BaseSpAtk = 109
        BaseSpDef = 85
        BaseSpeed = 100

        self.max_HP = (BaseHP * 2) * level // 100 + 10 + level      
        self.HP = self.max_HP       
        self.Attack = (BaseAtk * 2) * level // 100 + 5
        self.Defense = (BaseDef * 2) * level // 100 + 5
        self.SpAtk = (BaseSpAtk * 2) * level // 100 + 5
        self.SpDef = (BaseSpDef * 2) * level // 100 + 5
        self.Speed = (BaseSpeed * 2) * level // 100 + 5
        
    # かえんほうしゃ
    def Flamethrower(self, enemy):
        print(self.name + 'のかえんほうしゃ！')
        MoveType = 'ほのお'
        Species = 'とくしゅ'
        Power = 90
        Accuracy = 100

        # 1 ~ 100の乱数を生成し, 命中率に応じて外れる.
        if not randint(1, 100) <= Accuracy:
            print('こうげきははずれた')
            return
        
        # ダメージ計算式
        if Species == 'ぶつり':
            damage = int(int(Power * (int(self.level * 2 / 5) + 2) * self.Attack / enemy.Defence) / 50) + 2
        elif Species == 'とくしゅ':
            damage = int(int(Power * (int(self.level * 2 / 5 + 2)) * self.SpAtk / enemy.SpDef) / 50) + 2
        
        # 乱数付与
        damage = damage * randint(217, 255) // 255

        # ダメージ上限計算・定数項
        damage = min(damage, 997) + 2

        # 相性補正
        effective = 0
        for Type in enemy.Type:
            if Type in ['くさ', 'こおり', 'むし', 'はがね']:
                effective += 1
            elif Type in ['ほのお', 'みず', 'いわ', 'ドラゴン']:
                effective -= 1
        damage *= 2**effective

        # タイプ一致
        if MoveType in Charizard.Type:
            damage *= 1.5

        # 急所判定
        if randint(1, 24) == 1:
            critical = True
            damage *= 1.5
        else:
            critical = False

        # ダメージ処理
        print(self.name + 'は' + enemy.name + 'に' + str(round(damage)) + 'のダメージを与えた！')

        if critical:
            print('きゅうしょにあたった！')

        if effective > 0:
            print('こうかはばつぐんだ！')
        elif effective < 0:
            print('こうかはいまひとつのようだ！')

        enemy.hit(round(damage))

class Venusaur(Pokemon):
    Type = ('くさ', 'どく')

    def __init__(self, name, level):
        display_png(Image('PythonTutorialwithPokemon/Images/Venusaur.GIF', format='png'))
        super(Venusaur, self).__init__(name, level)

        BaseHP = 80
        BaseAtk = 82
        BaseDef = 83
        BaseSpAtk = 100
        BaseSpDef = 100
        BaseSpeed = 80

        self.max_HP = (BaseHP * 2) * level // 100 + 10 + level      
        self.HP = self.max_HP       
        self.Attack = (BaseAtk * 2) * level // 100 + 5
        self.Defense = (BaseDef * 2) * level // 100 + 5
        self.SpAtk = (BaseSpAtk * 2) * level // 100 + 5
        self.SpDef = (BaseSpDef * 2) * level // 100 + 5
        self.Speed = (BaseSpeed * 2) * level // 100 + 5