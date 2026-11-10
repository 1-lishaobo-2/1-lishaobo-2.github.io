
import random
name = input('请输入男生姓名:')
jnae = input('请输入女生姓名:')

like = random.randint(1,100)
print(f'{name}和{jnae}的缘分值是: {like}')

if like > 80 :
    print('满分缘分')
elif like > 60:
    print('有些缘分')
elif like >40 :
    print('差点意思')
else:
    print('有缘无分')


