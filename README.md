# Web Chinese Dictionary SDK (网络中文词典 SDK)

# Getting Started

## Installing

```shell
pip install --upgrade git+https://github.com/StephanoGeorge/Web-Chi-Dict-SDK.git
```

See `example.py` and Responses.

# Responses

## iciba.com

### English => Chinese

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

### Chinese => English

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

### No Such Word

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

## youdao.com

### English => Chinese

Word: hot

```json
{
    "translation": [
        "热"
    ],
    "basic": {
        "us-phonetic": "hɑːt",
        "uk-speech": "http://fanyi.youdao.com/openapi.do?type=data&voice=true&version=1.2&key=1048394636&keyfrom=wangtuizhijia&q=hot&vt=1",
        "speech": "http://fanyi.youdao.com/openapi.do?type=data&voice=true&version=1.2&key=1048394636&keyfrom=wangtuizhijia&q=hot&vt=1",
        "phonetic": "hɒt",
        "uk-phonetic": "hɒt",
        "us-speech": "http://fanyi.youdao.com/openapi.do?type=data&voice=true&version=1.2&key=1048394636&keyfrom=wangtuizhijia&q=hot&vt=2",
        "explains": [
            "adj. 热的；辣的；热情的；激动的；紧迫的",
            "adv. 热；紧迫地",
            "vi. 变热",
            "vt. 增加；给......加温",
            "n. （Hot）（塞）霍特（人名）；（法）奥特（人名）"
        ]
    },
    "query": "hot",
    "errorCode": 0,
    "web": [
        {
            "value": [
                "热的",
                "惹火",
                "热"
            ],
            "key": "hot"
        },
        {
            "value": [
                "热狗",
                "红肠面包",
                "热狗"
            ],
            "key": "hot dog"
        },
        {
            "value": [
                "温泉城",
                "温泉",
                "温泉市"
            ],
            "key": "Hot Springs"
        }
    ]
}
```

### Chinese => English

Word: 热

```json
{
    "translation": [
        "hot"
    ],
    "basic": {
        "explains": [
            "hot（用于水龙头上）"
        ]
    },
    "query": "热",
    "errorCode": 0,
    "web": [
        {
            "value": [
                "hot",
                "Fever",
                "dry heat"
            ],
            "key": "热"
        },
        {
            "value": [
                "Thermionic Emission",
                "heat emission",
                "thermal emission"
            ],
            "key": "热发射"
        },
        {
            "value": [
                "Gex"
            ],
            "key": "热克斯"
        }
    ]
}
```

### Only Web Translation

Word: qqqqqqqqq

```json
{
    "translation": [
        "qqqqqqqqq"
    ],
    "query": "QQQQQQQQQ",
    "errorCode": 0,
    "web": [
        {
            "value": [
                "很喜欢"
            ],
            "key": "QQQQQQQQQ"
        }
    ]
}
```

### No Such Word

Word: qazwsxedcfgjkgkja

```json
{
    "translation": [
        "qazwsxedcfgjkgkja"
    ],
    "query": "qazwsxedcfgjkgkja",
    "errorCode": 0
}
```

