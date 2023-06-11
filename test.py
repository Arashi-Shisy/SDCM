# 「'aaa'と出力してね」という指示
print('aaa')

# 1+1の計算結果を出力
print(1+1)

# 入力した値の倍の数値を出力
raw=int(input('数値を入力してください'))
# ターミナルに'数値を入力してください'と表示されたら好きな数値を入力してEnter
result=raw*2
print(result)

# 後出しじゃんけん君
def janken(player_hand):
    if player_hand =='グー':
        return('パー')
    elif player_hand =='パー':
        return('チョキ')
    elif player_hand =='チョキ':
        return('グー')
    else:
        return('error')
print('私とじゃんけんしましょう')
player_hand = input('グーかチョキかパーを選んでください')
return_hand = janken(player_hand)
if return_hand == 'error':
    print('あなたの反則により私の勝ちです。')
else:
    print('私は'+return_hand+'を出しました。私の勝ちです。')