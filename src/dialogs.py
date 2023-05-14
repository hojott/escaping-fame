import random

dialogs = [
    [
        {
            "dialog": "kysymys 1",
            "answers": [
                ("hyvä vastaus", 1),
                [("neutraali vastaus", 0), ("huono vastaus", -1)],
                ("huono vastaus", -1),
                ("huono vastaus", -1)
            ]
        }
    ],
    [
        {
            "dialog": "kysymys 2",
            "answers": [
                ("hyvä vastaus", 1),
                ("neutraali vastaus", 0),
                [("neutraali vastaus", 0), ("huono vastaus", -1)],
                ("huono vastaus", -1)
            ]
        },
    ],
    [
        {
            "dialog": "kysymys 3",
            "answers": [
                ("hyvä vastaus", 1),
                ("hyvä vastaus", 1),
                ("neutraali vastaus", 0),
                ("huono vastaus", -1)
            ]
        },
    ],
    [
        {
            "dialog": "kysymys 4",
            "answers": [
                ("hyvä vastaus", 1),
                ("hyvä vastaus", 1),
                ("neutraali vastaus", 0),
                ("neutraali vastaus", 0)
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
