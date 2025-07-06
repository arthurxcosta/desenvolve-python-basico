import emoji

print('Emojis disponíveis:')
print('❤️ - :redheart:')
print('👍 - :thumbs_up:')
print('🤔 - :thinking_face:')
print('🥳 - :partying_face:')
print('😀 - :grinning_face:')
print('😎 - :smiling_face_with_sunglasses:')

frase = input('\nDigite uma frase e ela será emojizada:\n')

frase_emojizada = emoji.emojize(frase, language='alias')

print('\nFrase emojizada:')
print(frase_emojizada)