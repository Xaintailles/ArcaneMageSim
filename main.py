# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 10:43:55 2022

@author: Calixte
"""

import utilities as u

p_xaint = u.Player(4000, 3100, 650)

# %% Spells

s_arcaneblast = u.Spell(name = 'arcaneblast',
                        crit_chance = p_xaint.crit_rating,
                        spell_power_modifier = 1,
                        cast_time = 2,
                        crit_modifier = 2,
                        cooldown = -1,
                        school = 'arcane',
                        charges = -1
                        )

time = 0

while time <= 300:
    