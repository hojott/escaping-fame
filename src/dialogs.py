import random

dialogs = [
    [
        {
            "dialog": "kysymys 1",
            "answers": [
                ("Sorry, I can’t right now.", 1),
                [("I’m kind of in a hurry. Just let’s do this quickly.", 0), ("Get out of my way!", -1)],
                ("No, I don’t have time for this!", -1),
                ("*Ignore them*", -1)
            ]
        }
    ],
    [
        {
            "dialog": "kysymys 2",
            "answers": [
                ("I don’t have time for this!", 1),
                ("Please, leave me alone", 0),
                [("O-okay let’s just get this done quickly", 0), ("Get away from me", -1)],
                ("Look at them like you saw a ghost", -1)
            ]
        },
    ],
    [
        {
            "dialog": "kysymys 3",
            "answers": [
                ("I'm really sorry...", 1),
                ("Some other time", 1),
                ("I really dont have the time for this!", 0),
                ("Touch grass", -1)
            ]
        },
    ],
    [
        {
            "dialog": "kysymys 4",
            "answers": [
                ("Go away!", 1),
                ("I CAN’T", 0),
                ("break down and scream “AAAAAAAAAAAAAAAAAAAAAAAAAAA", -1),
                ("...", 0)
            ]
        },
    ]
]

texts = {
    "intro": [
        "You are an idol that knows your future if you continue your career further, you",
        "would lose all the privacy you have left, and the lack of privacy is already",
        "almost too much for you. So you’ve decided that you will change your identity ",
        "and leave your career behind. You’re about to leave to get your identity",
        "changed illegally, your only chance is today. “Alright, I gotta be there ",
        "in 10 minutes, or it’s all over, I won’t have much time to talk with fans”",
        "and you leave your apartment."
    ],
    "bad_ending": [
        "You couldn’t make it in time and lost your only chance at a new life. You’re",
        "going to be stuck on this path as an idol until all of the little privacy you",
        "had left is gone. You go on to be rich and successful, but you don’t find it worth it"
    ],
    "good_ending": [
        "You successfully chenged your identity, you can live your life in peace and quiet.",
        "Sometimes you hear people ask about the birthmark that you were recognized",
        "from as an idol, but they just assume you are a huge fan of yourself."
    ],
    "joke_ending": [
        "You get hit by a car. They drive away out of fear of getting",
        "sued out of existance because of who you are. "
    ],
    "kaarija_ending": [
        "You found the Käärijä car! Lakkasit ajattelemasta huomista ja",
        "aloit tarttumaan tuopista. You found happiness. You now make music",
        "with Käärijä. Et enään pelkääkkään tätä maailmaa."
    ]

}

for i in range(4):
    random.shuffle(dialogs[i])
