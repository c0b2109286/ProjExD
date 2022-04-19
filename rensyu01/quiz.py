import random
quiz = [["サザエさんの旦那の名前は？","マスオ"],["カツオの妹の名前は？","ワカメ"],["タラオはカツオから見てどんな関係？","甥"]]
num_list = [0,1,2]
num = random.choice(num_list)
print(quiz[num][0])
ans = input("答えを入力")
if ans == quiz[num][1]:
    print("正解")
else:
    print("不正解")