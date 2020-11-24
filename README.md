# iciba Dictionary API (金山词霸词典 API)

# Getting Started

## Installing

```shell
pip install --upgrade git+https://github.com/StephanoGeorge/iciba-API.git
```

See `example.py` and Responses.

# Responses

## English => Chinese

Word: hot

```json
{
    "word_name": "hot",
    "is_CRI": "1",
    "exchange": {
        "word_pl": "",
        "word_third": [
            "hots"
        ],
        "word_past": [
            "hotted"
        ],
        "word_done": [
            "hotted"
        ],
        "word_ing": [
            "hotting"
        ],
        "word_er": [
            "hotter"
        ],
        "word_est": [
            "hottest"
        ]
    },
    "symbols": [
        {
            "ph_en": "h\u0252t",
            "ph_am": "h\u0251t",
            "ph_other": "",
            "ph_en_mp3": "http:\/\/res.iciba.com\/resource\/amp3\/0\/0\/27\/36\/27369b3bf4483e8dcfd85ba9a39a947f.mp3",
            "ph_am_mp3": "http:\/\/res.iciba.com\/resource\/amp3\/1\/0\/27\/36\/27369b3bf4483e8dcfd85ba9a39a947f.mp3",
            "ph_tts_mp3": "http:\/\/res-tts.iciba.com\/2\/7\/3\/27369b3bf4483e8dcfd85ba9a39a947f.mp3",
            "parts": [
                {
                    "part": "adj.",
                    "means": [
                        "\u70ed\u7684",
                        "\u8fa3\u7684",
                        "\u6fc0\u52a8\u7684",
                        "\u70ed\u95e8\u7684"
                    ]
                },
                {
                    "part": "vt.",
                    "means": [
                        "\u4f7f\u5174\u594b\uff0c\u4f7f\u6fc0\u52a8"
                    ]
                },
                {
                    "part": "adv.",
                    "means": [
                        "\u70ed\u7684",
                        "\u7d27\u8feb\u7684"
                    ]
                },
                {
                    "part": "vi.",
                    "means": [
                        "\u53d8\u70ed"
                    ]
                }
            ]
        }
    ]
}
```

## Chinese => English

Word: 热

```json
{
    "word_name": "\u70ed",
    "symbols": [
        {
            "word_symbol": "r\u00e8",
            "symbol_mp3": "http:\/\/res.iciba.com\/hanyu\/zi\/bf90cf2d4e164dd2029d171d24c004f8.mp3",
            "parts": [
                {
                    "part_name": "\u540d",
                    "means": [
                        {
                            "word_mean": "heat",
                            "has_mean": "1",
                            "split": 1
                        },
                        {
                            "word_mean": "fever",
                            "has_mean": "1",
                            "split": 1
                        },
                        {
                            "word_mean": "temperature",
                            "has_mean": "1",
                            "split": 1
                        },
                        {
                            "word_mean": "craze",
                            "has_mean": "1",
                            "split": 0
                        }
                    ]
                },
                {
                    "part_name": "\u5f62",
                    "means": [
                        {
                            "word_mean": "hot",
                            "has_mean": "1",
                            "split": 1
                        },
                        {
                            "word_mean": "ardent",
                            "has_mean": "1",
                            "split": 1
                        },
                        {
                            "word_mean": "warmhearted",
                            "has_mean": "1",
                            "split": 1
                        },
                        {
                            "word_mean": "envious",
                            "has_mean": "1",
                            "split": 0
                        }
                    ]
                },
                {
                    "part_name": "\u52a8",
                    "means": [
                        {
                            "word_mean": "\uff08\u4f7f\u70ed\uff1b \u52a0\u70ed\uff09 heat up",
                            "has_mean": "1",
                            "split": 1
                        },
                        {
                            "word_mean": "warm up",
                            "has_mean": "1",
                            "split": 1
                        },
                        {
                            "word_mean": "warm ",
                            "has_mean": "1",
                            "split": 0
                        }
                    ]
                }
            ],
            "ph_am_mp3": "",
            "ph_en_mp3": "",
            "ph_tts_mp3": "",
            "ph_other": ""
        }
    ]
}
```

## No such word

Word: ooooo

```json
{
    "symbols": [
        {
            "ph_am_mp3": "",
            "ph_en_mp3": "",
            "ph_tts_mp3": "",
            "ph_other": ""
        }
    ]
}
```