from random import randint
quiz = ["サザエさんの旦那の名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係？"]
ans_list = [["マスオ","ますお"],["ワカメ","わかめ"],["甥","おい","甥っ子","おいっこ"]]
num = randint(0,3)
print(quiz[num])
ans = input("答えを入力")
if ans in ans_list[num]:
    print("正解")
else:
    print("不正解")