priority_list = [
    {
        'name': 'cancel_travel',
        'coords': {
            'x': 0.455,
            'y': 0.4
        },
        'relevancy_indicators': [
            {
                'coords': {
                    'x': 0.455,
                    'y': 0.4
                },
                'valid_colors': {
                    'r': lambda r: r >= 150 and r <= 255,
                    'g': lambda g: g <= 130,
                    'b': lambda b: b <= 130
                }
            }
        ],
    },
    {
        'name': 'roll_dice',
        'coords': {
            'x': 0.85,
            'y': 0.87
        },
        'relevancy_indicators': [
            {
                'coords': {
                    'x': 0.85,
                    'y': 0.87
                },
                'valid_colors': {
                    'r': lambda r: (r >= 156 and r<=161) or r >= 250,
                    'g': lambda g: (g >= 158 and g<=195) or g >= 250,
                    'b': lambda b: b >=145
                }
            }
        ],
    },
    {
        'name': 'fight',
        'coords': {
            'x': 0.8,
            'y': 0.9
        },
        'relevancy_indicators': [
            {
                'coords': {
                    'x': 0.8,
                    'y': 0.9
                },
                'valid_colors': {
                    'r': lambda r: r >= 235 and r<=255,
                    'g': lambda g: g >= 10 and g<=50,
                    'b': lambda b: b >= 0 and b <= 20
                }
            }
        ],
    },
    {
        'name': 'continue',
        'coords': {
            'x': 0.87,
            'y': 0.95
        },
        'relevancy_indicators': [
            {
                'coords': {
                    'x': 0.87,
                    'y': 0.95
                },
                'valid_colors': {
                    'r': lambda r: r >= 15 and r<=50,
                    'g': lambda g: g >= 120 and g<=180,
                    'b': lambda b: b >= 200 and b <= 230
                }
            }
        ],
    },
    {
        'name': 'treasure',
        'coords': {
            'x': 0.51,
            'y': 0.21
        },
        'relevancy_indicators': [
            {
                'coords': {
                    'x': 0.5,
                    'y': 0.2
                },
                'valid_colors': {
                    'r': lambda r: r >= 200 and r<=225,
                    'g': lambda g: g >= 180 and g<=200,
                    'b': lambda b: b >= 75  and b<=85
                }
            }
        ],
    },
    {
        'name': 'experience',
        'coords': {
            'x': 0.6,
            'y': 0.6
        },
        'relevancy_indicators': [
            {
                'coords': {
                    'x': 0.6,
                    'y': 0.6
                },
                'valid_colors': {
                    'r': lambda r: r >= 200 and r<=225,
                    'g': lambda g: g >= 170 and g<=200,
                    'b': lambda b: b >= 120  and b<=160
                }
            }
        ],
    },
    {
        'name': 'skill_check',
        'coords': {
            'x': 0.77,
            'y': 0.85
        },
        'relevancy_indicators': [
            {
                'coords': {
                    'x': 0.77,
                    'y': 0.85
                },
                'valid_colors': {
                    'r': lambda r: r <= 20,
                    'g': lambda g: g <= 150,
                    'b': lambda b: b >= 50
                }
            }
        ],
    },
    {
        'name': 'failed_skill_check',
        'coords': {
            'x': 0.5,
            'y': 0.68
        },
        'relevancy_indicators': [
            {
                'coords': {
                    'x': 0.5,
                    'y': 0.48
                },
                'valid_colors': {
                    'r': lambda r: r >= 220,
                    'g': lambda g: g <= 80 or g >= 220,
                    'b': lambda b: b <= 80 or b >= 220
                }
            }
        ],
    },
    {
        'name': 'succeeded_skill_check',
        'coords': {
            'x': 0.55,
            'y': 0.2
        },
        'relevancy_indicators': [
            {
                'coords': {
                    'x': 0.55,
                    'y': 0.2
                },
                'valid_colors': {
                    'r': lambda r: r <= 80,
                    'g': lambda g: g >= 180,
                    'b': lambda b: b <= 60
                }
            }
        ],
    },
    {
        'name': 'forge',
        'coords': {
            'x': 0.8,
            'y': 0.7
        },
        'relevancy_indicators': [
            {
                'coords': {
                    'x': 0.8,
                    'y': 0.7
                },
                'valid_colors': {
                    'r': lambda r: r >= 220,
                    'g': lambda g: g >= 220,
                    'b': lambda b: b >= 220
                }
            }
        ],
    },
    {
        'name': 'forge_rewards',
        'coords': {
            'x': 0.51,
            'y': 0.18
        },
        'relevancy_indicators': [
            {
                'coords': {
                    'x': 0.51,
                    'y': 0.18
                },
                'valid_colors': {
                    'r': lambda r: r <= 90,
                    'g': lambda g: g <= 90,
                    'b': lambda b: b == 0
                }
            }
        ],
    },
]