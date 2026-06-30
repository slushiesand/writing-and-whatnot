
init python:
    import random

    names = {
        "1": "Ai",
        "2": "Eddie",
        "3": "Godfrey",
        "4": "John"
    }

define c = Character("???", color = "#cb7be1")
define s = Character("Friend", color = "#ff0000")
define y = Character("[you]")
define z = Character("???")

image black = "#000"
image conductor = Live2D("images/@2/conductor", height = 0.99, loop = True, seamless = True, default_fade = False)
image stagehand = Live2D("images/@2/stagehand", loop = True, seamless = True, default_fade = False)

define audio.crumple = "zapsplat_foley_paper_bags_pile_scrunched_push_down_compress_squash_001_113503.mp3"
define audio.conDistress = "zapsplat_household_alarm_clock_old_fashioned_ring_very_short_44062.mp3"
define audio.staDistress = "zapsplat_impact_hard_rock_hit_metal_and_glass_crash_smash_break_008_108027.mp3"
define audio.romanceMusic = "Waltz in A flat major 'Farewell', Op. 69 no. 1.mp3"

label start:
    scene cg far1
    with Fade(1.0, 0, 1.0)
    play music master_of_dreams_clock_ticking_337
    c "..."
    play sound crumple
    show cg far2
    c "... No, not good enough. {w=1}{i}Scrap!{/i}"
    c "What does the story have to do with the wider narrative? What's the message I want people to take away?"

    show cg close1
    with dissolve
    c "Think, brain. Think!"
    show cg close2
    play sound zapsplat_foley_footstep_shoe_sandal_single_scrape_wipe_grass_001_101428
    s "Haven't you done enough thinking?"
    show cg close2
    with vpunch
    stop music
    play sound conDistress
    c "{i}?!?{/i}"
    scene bg hill
    with dissolve
    s "Look up, {color=#cb7be1}o' Conductor{/color} of this realm. Your ideas fly like cranes."
    show cg close2
    with dissolve
    s "... & they're getting {i}very{/i} annoying to avoid."
    $ c = Character("Conductor", color="#cb7be1")

    scene bg hill 
    show conductor idle_talk at left
    show stagehand idle at right
    with dissolve

    c "Haah... Well, stories don't write themselves, you know?"
    c "Someone's gotta write them, but that someone doesn't have a lick of imagination right now."
    show conductor write_intro write
    show stagehand idle_talk
    s "What is it you're trying to write, anywho?"
    show conductor think_intro think_talk
    show stagehand idle
    c "Oh! Well, there's a lot I want to write!"
    c "There's this young-looking man who gets snowed in a cabin, but he's actually, like, 700 years old!{nw=.5}"
    c "And this shut-in whose social life consists of artifical intelligences, and--{nw=.5}"
    play sound staDistress
    show conductor idle distress 
    show stagehand smug idle_talk:
        subpixel True 
        xpos 1.0 
        ease_back 0.56 xpos 1.03 
    with Pause(0.66)
    show stagehand smug idle_talk:
        xpos 1.03 
    with dissolve
    s "Apologies. Forget I asked."
    show conductor neutral
    with dissolve
    show stagehand smug idle_talk:
        subpixel True 
        xpos 1.03 
        easein_cubic 0.60 xpos 1.0 
    with Pause(0.66)
    show stagehand smug idle_talk:
        xpos 1.0 
    s "In any case, you clearly haven't gotten very far in your writings."
    show conductor idle_talk
    show stagehand idle
    c "... {w=1}Yeah, I know. It's just..."
    show conductor upset_intro upset_talk
    c """

    None of the words come out right. It's all... {w=1}{i}out of character.{/i}

    These people I try to write-- They're flatter and more cliche on the paper than in my head, and I can't stand it!

    I know the hallmarks of bad writing, and I've read the copy-paste material from copy-paste authors.

    So {i}why{/i} does my pencil still produce amateur work?

    Why can my people only come alive in the confines of my head?

    """
    show conductor upset
    show stagehand idle_talk
    s "{i}Why{/i} do you aim to make a masterpiece?"
    show conductor upset_talk
    show stagehand idle
    c "Shouldn't it be obvious? {w=1}You've been with me forever now."
    show conductor idle_talk
    with dissolve
    c "... {w=1}I want to make something meaningful."
    show conductor idle
    show stagehand pointer_intro pointer_talk
    s "In that case, why don't you take a break and write something new?"
    s "It doesn't have to be fancy, nor something perfect."
    show stagehand happy
    s "Just make something you're proud of. That will give you the \"meaning\" you've been searching for."

    scene bg hill
    with dissolve
    play sound crumple
    show paper
    with easeinbottom
    c "Ah, but I've never been good at making new ideas either..."
    c "Maybe you can help me write?"
    show stagehand paper_intro paper_talk at right:
        subpixel True pos (1.06, 1.05) zrotate -18.0 
    with easeinright
    s "Me? I'm not a creative individual, I'm afraid."
    show stagehand paper
    c """

    We worked together once, as {color=#cb7be1}\"Conductor\"{/color} and {color=#ff0000}\"Stagehand\".{/color}

    \"Designer\" and \"Mathmetician.\" \"Videographer\" and \"Editor.\" Both differently wired, but equally essential.

    It's been a while since we've worked together, you know? It would be nice to hang out more casually!

    Plus, monologuing flowery advice doesn't make you look cool, so you might as well sit down.

    """
    $ s = Character("Stagehand", color="#ff0000")
    show stagehand smug paper_talk:
        subpixel True 
        pos (1.06, 1.05) zrotate -18.0 
        easein_quad 0.35 pos (1.0, 1.0) zrotate 0.0 
    with Pause(0.45)
    show stagehand smug paper_talk:
        pos (1.0, 1.0) zrotate 0.0 
    s "... If you insist."

    show conductor write_intro write at left
    with easeinleft
    show stagehand neutral
    s "So..."
    python:
            banNames = ["Eiax", "Aelred", "Kazan", "Eilhart", "Fuca", "Olivia", "Monochrome", "B1nary", "Mr. Script", "Beatrice", "Moth", "Ceiling"]
            # every name used in a past game of mine, excluding "King" and "Queen" since they are: 1. Common words and 2. Not their real names.
            # "To the Ceiling!!" isn't canon to any of my other games, but since this is more of a "4th wall breaking story," he should probably also be in this list. he isn't my original character anyway!
            special = ["Stagehand", "Conductor", "Ampersand", "Slushie"]

            you = None
            while you == None or not you or you in banNames or you in special:
                renpy.show("stagehand paper")
                you = renpy.input("What is your character's name?")
                you = you.strip().title()

                if not you:
                    renpy.show("stagehand paper_talk")
                    s ("I implore you to try to think of something.")
                elif you in banNames:
                    renpy.show("stagehand paper_talk")
                    s ("Hey now. Originality, remember?")
                elif you in special:
                    renpy.show("stagehand paper_talk")
                    s ("Ah...{w=1} you want to tell {i}that{/i} story? So near and dear to your heart?")
                    renpy.show("stagehand angry_intro angry")
                    s ("Well, I'm afraid we have no time to implement such things, at least not now, {color=#cb7be1}dreamer.{/color}")
    show stagehand paper_talk
    s "[you]... a typical naming scheme. Not to say that is a bad thing."
    $ char1 = 0
    show stagehand paper
    menu:
        s "What kind of character would this \"[you]\" be?"

        "A violin-ing college student, looking to fill their heart.":
            $ char1 = 1
            play music romanceMusic fadein 1.0
            jump rom

        "uhhhhhh!":
            show conductor upset_intro upset_talk
            c "... I only have one idea."
            show stagehand smug paper_talk
            show conductor upset
            s "Seems like someone ran out of time to write the full game."
            show conductor upset_talk
            c "Look, if I didn't rig our hair physics for no reason this wouldn't have been a problem... {size=-10}Probably.{/size}"
            c "So we're just going to go with the only route available, okay?"
            show conductor upset
            show stagehand angry_intro angry
            s "So much for someone with a clock carved into their skull."
            show conductor upset_talk
            c "Whatever. You're annoying, anyway."
            show conductor upset
            s "... & yet you perpetuate my existence."
            show stagehand paper
            show conductor write
            with dissolve
            jump rom

        #"A middle-aged coporate slave whose veins pulse with sorrow.":
            #$ char1 = 2
            #jump trag

        #"The alley-dweller whose mind wavers between contempt and absurdity.":
            #$ char1 = 3
            #jump ed

        #"It doesn't matter who I am. I am the inane and the egoist!":
            #$ char1 = 4
            #jump com

label rom:
    $ y = Character("[you]", color="#f260ff")
    show conductor write_talk
    with None
    show rom sad at truecenter
    with easeinbottom
    y "I can't believe it! After 3 years of {i}happiness{/i} and {i}fulfillment{/i}, they just {color=#f260ff}dumped{/color} me!"
    y "Waah... and exams are coming up too!"
    show rom sad:
        subpixel True 
        ypos 0.5 zrotate 0.0 
        easein_quad 0.30 ypos 0.55 zrotate -9.0 
    with Pause(0.40)
    show rom sad:
        ypos 0.55 zrotate -9.0 
    y "What am I going to do... ?"
    show stagehand idle_talk smug
    with dissolve
    show conductor write
    with None
    s "Ah... If that's the character you wish to write."

    show black
    with dissolve
    show rom sad at truecenter:
        subpixel True
        ypos 0.5 zrotate 0.0
    hide black
    show stagehand neutral paper
    show conductor write_talk
    with dissolve

    c "Despite the circumstances, it's a bright and sunny day."
    y "Maybe this means... things will get better."
    show rom neutral:
        subpixel True 
        ypos 0.59 
        spring3 0.38 ypos 0.5 
    with Pause(0.48)
    show rom neutral:
        ypos 0.5 
    y "But I don't really have the time nor the energy to worry about my love life right now. I have to worry about my {color=#f260ff}grades!"
    show rom bother
    y "Let's see... music theory is on Friday. Guess I should study whatever the heck a phrygian is."
    hide rom
    with easeoutright
    y "To the library!"

    show black
    with dissolve
    hide black
    show conductor write
    show stagehand paper_talk
    with dissolve
    show rom neutral at truecenter
    with easeinleft

    s "[you] takes a seat at a lonely table at the local library, but they can't focus for a single second."
    s "It seems today... {w=1}every couple in a 5 mile radius is also studying."
    show rom bother
    show stagehand pointer_talk
    with dissolve
    s "Couples giggling 'round a romance book, couples poking each other with pool cues, even couples taking naps in the valuable bean bags!"
    show stagehand pointer 
    show conductor write_talk
    y "Look at these people living full lives with another human being. {i}Haah!!"
    show rom sad:
        subpixel True 
        ypos 0.5
        easein_quad 0.30 ypos 0.55
    with Pause(0.40)
    show rom sad:
        ypos 0.55
    y "Whatever! Sight-reading is most of the score anyway! I... {size=-10}don't need...{/size}"
    c "The lump in their throat stops them from finishing their sentence."
    c "They walk out quietly-- well, as quietly as someone on the verge of tears can -- onto the bustling street."
    show rom sad:
        subpixel True 
        ypos 0.55
        easein_quad 0.30 ypos 0.5
    with Pause(0.40)
    show rom sad:
        ypos 0.5
    y "I guess I should just go home."
    c "If [you] can just get home, maybe they can do some chores to get their mind off things... or cry into their pillow."
    show stagehand pointer_talk
    show conductor write
    s "But in circumstance, or perhaps fate, [you] stumbles into..."
    show conductor think_intro think_talk
    show rom surprised:
        subpixel True 
        xpos 0.5 
        ease_expo 0.40 xpos 0.39 
    with Pause(0.50)
    show rom surprised:
        xpos 0.39 

    $ char2 = random.randint(1, 4)
    $ char2name = names[str(char2)]
    # determines what person the player character meets. it is Stagehand's character.
    # for demo purposes, this is placed right before the route split, but in the full game, it would be decided upon starting.

    y "Oh! Sorry!"
    if char2 == 1:
        jump .ance
    elif char2 == 2:
        jump .edy
    elif char2 == 3:
        jump .gy
    else:
        jump .edic
    "BUG"

    label rom.ance:

        show ance surprised at truecenter:
            subpixel True
            xpos 0.62
        with easeinright
        show conductor think
        s "... A bright-eyed part-timer at an antique store, run by their grandparents."
        $ z = Character("???", color = "#f260ff")
        show rom neutral
        show conductor write_talk
        with dissolve
        show stagehand pointer
        y "Wait... {w=1}Hey, you're that cute worker at the antique store!\n{color=#777777}(Oops, I didn't mean to say that out loud.)"
        show ance surprised:
            subpixel True 
            ypos 0.59 
            spring3 0.38 ypos 0.5 
        with Pause(0.48)
        show ance surprised:
            ypos 0.5 
        show stagehand paper_talk
        with dissolve
        show conductor write
        z "Er, cute... ? Well, I'm glad you think so!"
        show ance neutral:
            zrotate 0.0 
            easein_quad 0.30 zrotate 9.0 
        with Pause(0.40)
        show ance neutral:
            zrotate 9.0 
        z "Hehe, are you a regular? I don't quite recognize everyone's face yet."

        show stagehand paper
        show conductor think_intro think_talk
        c "... Do antique shops have regulars?"
        show conductor think
        show stagehand pointer_talk
        with dissolve
        s "Anything is possible in fiction."
        show conductor think_talk
        show stagehand pointer
        c "Haha, true. Well then..."

        show conductor idle_talk
        with dissolve
        show rom surprised:
            subpixel True 
            ypos 0.5 
            ease_back 0.28 ypos 0.45 
        with Pause(0.38)
        show rom surprised:
            ypos 0.45 
        show ance neutral:
            easein_quad 0.30 zrotate 0.0
        with Pause(0.38)
        show ance neutral:
            zrotate 0.0
        y "No, I'm not a regular. I just visited with my boyfriend a while ago."
        show rom sad:
            subpixel True
            ypos 0.45
            easein_quad 0.30 ypos 0.5
        with Pause(0.40)
        show rom sad:
            ypos 0.5
        y "I got broken up by my boyfriend, and I don't know why. I thought our relationship was fine, but..."
        y "I could tell he was drawing away. So I took him on more dates, gave him gifts..."
        show rom sad:
            subpixel True 
            zrotate 0.0 
            ease 0.40 zrotate 27.0 
        with Pause(0.50)
        show rom sad:
            zrotate 27.0
        show conductor upset_intro upset_talk
        y "I guess it wasn't enough. I guess {i}I{/i} wasn't enough."
        show rom surprised:
            subpixel True 
            zrotate 27.0 
            ease_back 0.36 zrotate 0.0 
        with Pause(0.46)
        show rom surprised:
            zrotate 0.0
        show conductor idle
        with dissolve
        y "... Oh. Sorry for dumping this all on you."
        show stagehand idle_talk
        with dissolve
        show ance sad:
            subpixel True 
            ypos 0.5 
            ease_back 0.28 ypos 0.45 
        with Pause(0.38)
        show ance sad:
            ypos 0.45 
        z "I'm... {w=1}sorry to hear that. If you ever want to travel to a different era, the store is always open."
        show ance neutral:
            ypos 0.45
            ease_back 0.28 ypos 0.5
        with dissolve
        z "I might not be there all the time, but I'll do all I can to assist you."

        menu:
            "Would you like to go out for coffee?":
                show rom neutral
                with dissolve
                show conductor idle_talk
                y "As an apology for the trauma dump, and like... getting to know each other better."
                show conductor idle
                show stagehand paper_intro paper_talk
                show ance excited:
                    subpixel True 
                    ypos 0.59 
                    spring3 0.38 ypos 0.5 
                with Pause(0.48)
                show ance excited:
                    ypos 0.5 
                z "Oh, thank you! Yes, that sounds nice."
                z "How about... tomorrow for lunch? Or just whenever! I don't work tomorrow, anyway."
            
            "How much do you get paid?":
                show rom bother
                with dissolve
                show conductor idle_talk
                y "I need... something else to do with my life..."
                show stagehand idle_talk
                with dissolve
                show conductor idle
                z "I get paid minimum wage. I'm, uh, sure I'll get paid more when I get a full position, though!"
                show conductor idle_talk
                show stagehand idle
                c "Yeah, I don't think an antique worker will ever get paid much..."
                show stagehand angry_intro angry
                s "What is your problem with my antique store?!"

            "What is the meaning of existence?":
                show rom sad
                show ance sad
                with dissolve
                show stagehand idle_talk
                z "Uhm... I don't think life is that bleak!"
                z "Listen! Life is bigger than one person. Antiques are proof of that!"

            "It says gullible on the ceiling.":
                show ance excited:
                    subpixel True 
                    ypos 0.59 
                    spring3 0.38 ypos 0.5 
                with Pause(0.48)
                show ance excited:
                    ypos 0.5 
                show stagehand idle_talk
                z "Oh? Really?!"
                show rom bother
                with dissolve
                y "... We are outside."
                show ance sad
                with dissolve
                z "... Oh."
        
        show stagehand smug paper_intro paper_talk
        s "This unexpected encounter on the street... feels so warm."
        show rom excited
        with dissolve
        show stagehand paper
        show conductor write_intro write_talk
        y "I... have to see them again."
        y "Maybe, just maybe... they'll be the answer to my heartbreak!"
        show rom neutral:
            subpixel True 
            ypos 0.59 
            spring3 0.38 ypos 0.5 
        with Pause(0.48)
        show rom neutral:
            ypos 0.5 
        y "Please, what is your name?"
        show ance surprised
        with dissolve
        show conductor write
        show stagehand paper_talk
        $ z = Character("Ai", color = "#f260ff")
        z "My name is Ai! It means love and affection."

        jump ending

    label rom.edy:
        show edy neutral at truecenter:
            subpixel True
            xpos 0.62
        with easeinright
        show conductor think
        s "... A scrawny street-performer who borders on packing it up."
        $ z = Character("???", color = "#306cc7")
        s "A somber tune, with occasional dissonant chords, quivers at the street corner."
        show rom sad
        with dissolve
        y "This tune... it feels perfect for what I'm feeling."
        show edy neutral:
            subpixel True 
            xpos 0.62 
            ease_circ 0.41 xpos 0.58 
        with Pause(0.51)
        show edy neutral:
            xpos 0.58 
        z "... Do you like it, stranger?"
        show rom sad:
            subpixel True 
            zrotate 0.0 
            easein_quad 0.40 zrotate 18.0 
        with Pause(0.50)
        show rom sad:
            zrotate 18.0 
        y "Yeah. I... got broken up with a few hours ago."
        show edy neutral:
            subpixel True 
            xpos 0.58
            ease_circ 0.41 xpos 0.62 
        with Pause(0.51)
        show edy neutral:
            xpos 0.62
        show rom sad:
            subpixel True 
            zrotate 18.0 
            easein_quad 0.40 zrotate 0.0
        with Pause(0.50)
        show rom sad:
            zrotate 0.0
        z "That's how it is, huh?"

        show stagehand pointer
        show conductor idle_talk
        with dissolve
        y "I got broken up by my boyfriend, and I don't know why. I thought our relationship was fine, but..."
        y "I could tell he was drawing away. So I took him on more dates, gave him gifts..."
        show rom sad:
            subpixel True 
            zrotate 0.0 
            ease 0.40 zrotate 27.0 
        with Pause(0.50)
        show rom sad:
            zrotate 27.0
        show conductor upset_intro upset_talk
        y "I guess it wasn't enough. I guess {i}I{/i} wasn't enough."
        show rom surprised:
            subpixel True 
            zrotate 27.0 
            ease_back 0.36 zrotate 0.0 
        with Pause(0.46)
        show rom surprised:
            zrotate 0.0
        show conductor idle
        with dissolve
        y "... Oh. Sorry for dumping this all on you."

        show edy sad
        with dissolve
        show stagehand smug pointer_talk
        z "... Something similar happened to me, long ago."
        show edy sad:
            subpixel True 
            ypos 0.5 
            easein_quad 0.35 ypos 0.55 
        with Pause(0.45)
        show edy sad:
            ypos 0.55 
        z "Now I just sing on the street, but I don't even know if I can afford that for much longer."
        show edy neutral:
            subpixel True
            ypos 0.55
            easein_quad 0.35 ypos 0.5
        with Pause(0.45)
        show edy neutral:
            ypos 0.5
        show stagehand pointer

        menu:
            
            "Would you like to go out for coffee?":
                show rom neutral
                with dissolve
                show conductor idle_talk
                y "As an apology for the trauma dump, and like... getting to know each other better."
                show conductor idle
                show stagehand paper_intro paper_talk
                show edy excited:
                    subpixel True 
                    ypos 0.59 
                    spring3 0.38 ypos 0.5 
                with Pause(0.48)
                show edy excited:
                    ypos 0.5 
                z "Oh! It's been so long since I've had high-quality, non-instant coffee."
                z "... Thank you."

            "How much do you get paid?":
                show rom bother
                with dissolve
                show conductor idle_talk
                y "I need... something else to do with my life..."
                show edy sad
                show conductor idle
                show stagehand paper_intro paper_talk
                with dissolve
                z "I live purely off tips. But for the past long while... it has been nothing."
                show rom sad:
                    subpixel True 
                    parallel:
                        xpos 0.39 
                        easein_quad 0.37 xpos 0.44 
                    parallel:
                        zrotate 0.0 
                        ease2 0.37 zrotate 9.0 
                with Pause(0.47)
                show rom sad:
                    xpos 0.44 zrotate 9.0 
                show conductor idle_talk
                y "... Here, since I don't have to pay for dates anymore."
                show rom sad:
                    subpixel True 
                    xpos 0.44 zrotate 9.0 
                    easein_quad 0.39 xpos 0.39 zrotate 0.0 
                with Pause(0.49)
                show rom sad:
                    xpos 0.39 zrotate 0.0 
                show edy neutral
                with dissolve
                show stagehand paper_talk
                z "Hahaha... Thank you."

            "What is the meaning of existence?":
                show edy sad
                with dissolve
                show stagehand paper_intro paper_talk
                z "I... don't know. If life is love, then maybe there is no meaning."
                show stagehand paper
                show conductor upset_intro upset
                y "..."
            
            "It says gullible on the ceiling.":
                show edy sad
                with dissolve
                show stagehand paper_intro paper_talk
                z "I was gullible to think that music could bring me a living."
                show stagehand paper
                show conductor idle_talk
                show rom neutral
                with dissolve
                y "... I believe in you. I'm a music student, you know?"
                show edy excited:
                    subpixel True 
                    ypos 0.59 
                    spring3 0.38 ypos 0.5 
                with Pause(0.48)
                show edy excited:
                    ypos 0.5 
                z "... !"
        
        show stagehand smug paper_intro paper_talk
        s "This unexpected encounter on the street... feels so warm."
        show rom excited
        with dissolve
        show stagehand paper
        show conductor write_intro write_talk
        y "I... have to see them again."
        y "Maybe, just maybe... they'll be the answer to my heartbreak!"
        show rom neutral:
            subpixel True 
            ypos 0.59 
            spring3 0.38 ypos 0.5 
        with Pause(0.48)
        show rom neutral:
            ypos 0.5 
        y "Please, what is your name?"

        show edy bother:
            subpixel True 
            zrotate 0.0 
            easein_quad 0.38 zrotate -9.0 
        with Pause(0.48)
        show edy bother:
            zrotate -9.0 
        $ z = Character("Eddie", color = "#306cc7")
        z "Eddie. Nothing more, nothing less."

        jump ending

    label rom.gy:
        s "godfrey"

        y "I got broken up by my boyfriend, and I don't know why. I thought our relationship was fine, but..."
        y "I could tell he was drawing away. So I took him on more dates, gave him gifts..."
        show rom sad:
            subpixel True 
            zrotate 0.0 
            ease 0.40 zrotate 27.0 
        with Pause(0.50)
        show rom sad:
            zrotate 27.0
        show conductor upset_intro upset_talk
        y "I guess it wasn't enough. I guess {i}I{/i} wasn't enough."
        show rom surprised:
            subpixel True 
            zrotate 27.0 
            ease_back 0.36 zrotate 0.0 
        with Pause(0.46)
        show rom surprised:
            zrotate 0.0
        show conductor idle
        with dissolve
        y "... Oh. Sorry for dumping this all on you."

        show stagehand smug paper_intro paper_talk
        s "This unexpected encounter on the street... feels so warm."
        show rom excited
        with dissolve
        show stagehand paper
        show conductor write_intro write_talk
        y "I... have to see them again."
        y "Maybe, just maybe... they'll be the answer to my heartbreak!"
        show rom neutral:
            subpixel True 
            ypos 0.59 
            spring3 0.38 ypos 0.5 
        with Pause(0.48)
        show rom neutral:
            ypos 0.5 
        y "Please, what is your name?"


        jump ending

    label rom.edic:
        s "john"

        y "I got broken up by my boyfriend, and I don't know why. I thought our relationship was fine, but..."
        y "I could tell he was drawing away. So I took him on more dates, gave him gifts..."
        show rom sad:
            subpixel True 
            zrotate 0.0 
            ease 0.40 zrotate 27.0 
        with Pause(0.50)
        show rom sad:
            zrotate 27.0
        show conductor upset_intro upset_talk
        y "I guess it wasn't enough. I guess {i}I{/i} wasn't enough."
        show rom surprised:
            subpixel True 
            zrotate 27.0 
            ease_back 0.36 zrotate 0.0 
        with Pause(0.46)
        show rom surprised:
            zrotate 0.0
        show conductor idle
        with dissolve
        y "... Oh. Sorry for dumping this all on you."

        show stagehand smug paper_intro paper_talk
        s "This unexpected encounter on the street... feels so warm."
        show rom excited
        with dissolve
        show stagehand paper
        show conductor write_intro write_talk
        y "I... have to see them again."
        y "Maybe, just maybe... they'll be the answer to my heartbreak!"
        show rom neutral:
            subpixel True 
            ypos 0.59 
            spring3 0.38 ypos 0.5 
        with Pause(0.48)
        show rom neutral:
            ypos 0.5 
        y "Please, what is your name?"

        jump ending
  
    return

label trag:
    $ y = Character("[you]", color="#306cc7")
    show trag placeholder 
    with easeinbottom
    y "Every day comes to be the same."
    y "{color=#306cc7}Coffee, computer, crash.{/color} All for fueling the future of society -- and a neverending migrane."
    y "... Do I even care about the future?"
    s "Tell me more. Though, I suppose that's what the rest of the story is."

    if char2 == 1:
        jump .ance
    elif char2 == 2:
        jump .edy
    elif char2 == 3:
        jump .gy
    else:
        jump .edic
    "BUG"

    label trag.ance:
        s "ai"

        jump ending

    label trag.edy:
        s "eddie"

        jump ending

    label trag.gy:
        s "godfrey"

        jump ending

    label trag.edic:
        s "john"

        jump ending

    return

label ed:
    $ y = Character("[you]", color="#00ffdd")
    show ed placeholder 
    with easeinbottom
    y "Hahaha~"
    y "The world spins on an axis -- an axis of darkness and madness."
    y "{color=#00ffdd}All is fiction in my plane of existence."
    s "Truth and fiction are much closer to each other than one may think."

    if char2 == 1:
        jump .ance
    elif char2 == 2:
        jump .edy
    elif char2 == 3:
        jump .gy
    else:
        jump .edic
    "BUG"

    label ed.ance:
        s "ai"

        jump ending

    label ed.edy:
        s "eddie"

        jump ending

    label ed.gy:
        s "godfrey"

        jump ending

    label ed.edic:
        s "john"

        jump ending
    
    return

label com:
    $ y = Character("[you]", color="#ffc400")
    show com placeholder 
    with easeinbottom
    y "O' senselessness and frivolity. My love, my bane!"
    y "I shall rule this world, and bring about {color=#ffc400}antidisestablishmentarianism!"
    y "{i}Cough...{/i} I don't know what any of those words mean, by the way."
    s "Hahaha. Having fun, are we?"

    if char2 == 1:
        jump .ance
    elif char2 == 2:
        jump .edy
    elif char2 == 3:
        jump .gy
    else:
        jump .edic
    "BUG"

    label com.ance:
        s "ai"

        jump ending

    label com.edy:
        s "eddie"

        jump ending

    label com.gy:
        s "godfrey"

        jump ending

    label com.edic:
        s "john"

        jump ending

    return

label ending:

    menu:
        c "There's only one way for this story to end."

        "Bright rays shine down on morning bells...":
            c "Adults and children alike cheer for this white day."

        "Rolling clouds rain down city walls and gluttinous gutters...":
            pass

        "Alleys echo the same white noise they always did...":
            pass

        "The earth rumbles with magma and tension...":
            pass

    scene black
    with dissolve
    hide black
    show bg hill
    show paper
    show conductor write at left
    show stagehand paper_talk at right
    with dissolve
        
    s "What meaning does a piece of writing have -- to a reader or a writer -- if it is simply \"work?\""
    s "Art is a manifestation of flaws. Perhaps there are \"more flawed\" ways to execute a certain medium, but there are no ways to eliminate flaws."
    show stagehand idle_talk smug
    with dissolve
    s "... Are you proud of what you have done today?"
    show stagehand idle
    show conductor write_talk
    c "It's a bit discontinuous, but it was fun."
    show conductor idle_talk
    with dissolve
    c "Maybe that, too, is valuable."
    show conductor happy
    with dissolve
    c "I'm proud I had fun with an old friend. How about that?"
    show conductor neutral idle
    show stagehand paper_intro paper_talk
    s "It's alright to admit you liked your story."
    show stagehand paper
    show conductor happy idle_talk
    c "Fine! But it's your story, too! So {i}we're{/i} proud of our collective imagination!"
    show conductor neutral think_intro think_talk
    c "... {w=1}Although, aren't you also just a figment of my imagination?"
    show conductor think
    show stagehand idle
    with dissolve
    s "..."
    show stagehand neutral idle_talk
    s "Of course. I have come to terms with that fact since we've met."
    s "I am and always will be \"just your imaginary friend.\""
    show stagehand pointer_intro pointer_talk
    s "But {color=#cb7be1}you{/color} chose to listen to me in the end. It was still {i}your{/i} choice to break {i}your{/i} curse."
    show stagehand idle_talk
    with dissolve
    s "{color=#cb7be1}{i}You,{/i}{/color} the only real being in your mindscape."
    s "Awaken, and create all the stories you like-- unburdened."

    scene black
    "???" "..."
    "???" "I guess this light-hearted reprieve ended up meaningful after all."
    "End: A Dream within a Dream."

    return

"HEY HOW DID YOU GET HERE"
return
