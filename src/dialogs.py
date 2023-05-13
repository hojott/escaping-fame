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

for i in range(4):
    random.shuffle(dialogs[i])
