import random
list = ['サザエの旦那の名前は?','カツオの妹の名前は?','タラオはカツオから見てどんな関係?']
list1 = ['ますお','マスオ']
list2 = ['ワカメ','わかめ']
list3 = ['甥','おい','甥っ子','おいっこ']
question = random.choice(list)
print(question)
answer = input('答えを入力してください')
if question == 'サザエの旦那の名前は?':
    if answer in list1:
        print('正解')
elif question == 'カツオの妹の名前は?':
    if answer in list2:
        print('正解')
elif question == 'タラオはカツオから見てどんな関係?':
    if answer in list3:
        print('正解')
else:
    print('不正解') 