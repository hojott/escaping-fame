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
    ]
}

for i in range(4):
    random.shuffle(dialogs[i])
