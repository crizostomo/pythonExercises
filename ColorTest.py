print('\033[1;31;43mColor Test\033[m')

name = input('please type your name ')
colors = {'clean':'\033[m',
          'blue':'\033[34m',
          'yellow':'\033[33m',
          'blackAndWhite':'\033[7;30m'}
print('Hello!! So pleased to meet you, {}{}{}!!!'.format('\033[4;34m', name, '\033[m'))
print('Hello!! So pleased to meet you, {}{}{}!!!'.format(colors['blackAndWhite'], name, colors['clean']))