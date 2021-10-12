

blocks = [
    [
        'bamba is awesome',
        'this is it',
        'programming is awesome'
    ],
    [
        "i'm a beast",
    ]
]


for i, block in enumerate(blocks):
    for j, phrase in enumerate(block):
        if 'awesome' in phrase:
            block[j] = phrase.replace('awesome', 'unbelievable')
            #block[j] = 'a'

print(blocks)
