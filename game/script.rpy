
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
    show stagehand paper
    menu:
        s "What kind of character would this \"[you]\" be?"

        "A violin-ing college student, looking to fill their heart.":
            $ char1 = 1
            play music romanceMusic fadein 1.0
            jump rom

        "uhhhhhh!":
            $ char1 = 1
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

        show stagehand paper
        show conductor write_talk
        c "And so, these intertwined souls separate, just for the time being."

        show black
        with dissolve
        hide black
        hide rom 
        hide ance
        show conductor write
        show stagehand paper_talk
        with dissolve

        s "This first act certainly has some interesting threads starting."
        s "I have to ask, however. Is it ethical for [you] to find Ai cute before they broke up with their boyfriend?"
        show conductor write_talk
        show stagehand paper
        c "Eh, I dunno. Never said [you] was an ethical person."
        show conductor think_intro think_talk
        c "I mean, maybe it's fine. It's just a one-word descriptor that hardly means anything. I can say dolls are cute just fine, can't I?"
        show conductor think
        show stagehand smug paper_talk
        s "I suppose we are just playing with dolls, like we once did."
        s "It is debatable whether ethics matter at all."

        show black
        with dissolve
        hide black
        show conductor write_talk
        show stagehand neutral paper
        with dissolve

        show conductor write_talk
        show stagehand paper
        c "A street-corner turned into soda cups, and a chance encounter blossomed into prolonged contact."
        c "[you] has become quite acquainted with [char2name] after all this time. Their boyfriend is just a footnote in their mind with the help of a new friend."
        show stagehand paper_talk
        show conductor write
        show ance neutral at truecenter:
            xpos 0.62
        with easeinright
        z "Hey [you]! We recently stocked some new donations. Come hang out in the store~!"
        show rom neutral at truecenter:
            xpos 0.39
        with easeinleft
        show conductor write_talk
        show stagehand paper
        y "Aah... I have spent so much on trinkets already... !"

        show conductor write
        show stagehand paper_talk
        s "This single life isn't awful, truthfully. A good friend that brings joy at all times is also a good replacement."
        s "[you] could even say that they wouldn't mind [char2name] as a partner..."
        show stagehand smug
        s "Ahem. But they digress."
        show stagehand idle
        with dissolve
        show conductor write_talk
        c "But... this light honeymoon phase can't last forever."
        c "One day, [char2name] comes up to [you], acting a bit out of character."
        show black
        with dissolve
        hide black
        hide ance
        with dissolve  

        show ance neutral at truecenter:
            xpos 0.62
        with easeinright
        show stagehand idle_talk
        z "[you]! I got a proposal for you. Nothing super serious or anything, but... it means a lot to me. Kinda. More than kinda?"
        show conductor write_talk
        show stagehand idle
        show rom neutral:
            subpixel True 
            zrotate 0.0 
            easein_quad 0.45 zrotate 9.0 
        with Pause(0.55)
        show rom neutral:
            zrotate 9.0 
        y "What's up? You usually never concern yourself with stuff like that."
        show stagehand idle_talk
        show conductor write
        show ance bother:
            subpixel True 
            ypos 0.5 
            ease_cubic 0.43 ypos 0.55 
        with Pause(0.53)
        show ance bother:
            ypos 0.55
        z "Uh, well... it's that..."
        show ance bother:
            subpixel True 
            zrotate 0.0 
            easein_elastic 0.47 zrotate -9.0 
        with Pause(0.57)
        show ance bother:
            zrotate -9.0
        s "Ai fidgets with their fingers shyly."
        show ance bother:
            subpixel True 
            ypos 0.55 zrotate -9.0 
            easein_quad 0.39 ypos 0.5 zrotate 0.0 
        with Pause(0.49)
        show ance bother:
            ypos 0.5 zrotate 0.0
        z "... Do you want to hang out at my house? My grandparents live there. You know, the ones that run the shop."
        z "I think it'd be nice to meet them in a non-professional capacity. They're very appreciative of you, since you pop by so much."
        show ance sad:
            subpixel True 
            ypos 0.5 
            ease_cubic 0.43 ypos 0.55 
        with Pause(0.53)
        show ance sad:
            ypos 0.55
        z "Although, is it weird for a college graduate and boomers to be friends? Are my grandparents college graduates?"
        show ance neutral:
            subpixel True 
            ypos 0.59 
            spring3 0.38 ypos 0.5 
        with Pause(0.48)
        show ance neutral:
            ypos 0.5
        z "ANYWAY! Yeah. My house! You can hang out with my grandparents, and then you can hang out with me."
        z "Like, {i}chill{/i} hang out. Since we're not in the city. We live in suburbia. Forget to mention that, sorry!! Hahah..."

        show conductor distress write_talk
        with dissolve
        show stagehand paper_intro paper
        show rom excited:
            subpixel True 
            ypos 0.59 
            spring3 0.38 ypos 0.5 
        with Pause(0.48)
        show rom excited:
            ypos 0.5
        c "Are they... {i}asking you out on a date?!{/i}"
        c "Obviously, they are very nervous about it. [you] has never seen Ai stutter this much in their life, even when dealing with difficult customers."
        c "But meeting parents on a first date? {i}Man.{/i} [you] doesn't know if they're ready for that pressure."
        show conductor neutral
        
        menu:
            c "Although, grandparents aren't actual parents, huh?"

            "It's a date!":
                show stagehand paper_talk
                show conductor write
                show ance excited:
                    subpixel True 
                    xpos 0.62 
                    ease_elastic 0.47 xpos 0.67 
                with Pause(0.57)
                show ance excited:
                    xpos 0.67
                z "A date?!"
                show ance bother:
                    subpixel True 
                    xpos 0.67 
                    easein_quad 0.48 xpos 0.62 
                with Pause(0.58)
                show ance bother:
                    xpos 0.62
                z "Ahahaha... it's not like that! Who said it's like that??"
                show ance excited 
                with dissolve
                z "Well, I guess it's just a term of expression. Hehehe."
                hide conductor
                hide stagehand
                hide ance
                hide rom
                show happy ai
                with fade
                z "I'll send you my address later, okay?"
                z "Tell me what movies you like! & what snacks! I'll make sure to have everything prepared!"
                z "Don't lift a finger! Okay?!"

            "Do you have parents?":
                show rom surprised
                with dissolve
                y "If you work with your grandparents, and you live with your grandparents... are your actual parents {i}alive?{/i}"
                show ance sad
                with dissolve
                show conductor neutral upset_intro upset
                show stagehand angry_intro angry
                play sound staDistress
                s "... {w=1}In {i}what world{/i} would this be acceptable to say to someone who just asked you out on a date?!"
                s "Anyway. I suppose you never claimed {i}[you] had brain cells, either.{/i}"
                show ance sad:
                    subpixel True 
                    xpos 0.62 
                    easein_back 0.46 xpos 0.66 
                with Pause(0.56)
                show ance sad:
                    xpos 0.66
                show stagehand idle_talk
                with dissolve
                s "... Ai is taken aback by [you]'s question"
                show rom sad
                with dissolve
                show ance sad:
                    subpixel True 
                    zrotate 0.0 
                    ease2 0.41 zrotate -9.0 
                with Pause(0.51)
                show ance sad:
                    zrotate -9.0 
                z "... No, they're not."
                z "I knew them, once. But they died in a car accident a long time ago."
                hide ance sad
                with easeoutright
                z "Soon, they'll be dead for longer than I knew them for."
                show conductor upset_talk
                show stagehand idle
                y "... I'm sorry."
                show stagehand angry
                show conductor upset
                with dissolve
                s "It should be very, {i}very{/i} obvious you messed up by saying that."

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

        show stagehand paper
        show conductor write_talk
        c "And so, these intertwined souls separate, just for the time being."

        show black
        with dissolve
        hide black
        hide rom 
        hide edy
        show conductor write
        show stagehand paper_talk
        with dissolve

        s "This first act certainly has some interesting threads starting."
        show conductor write_talk
        show stagehand paper
        c "Eddie is really emo, by the way. I don't think an inflection of a smile graced their speech during that entire conversation."
        show stagehand smug paper_talk
        s "Perhaps they are \"simply nonchalant like that,\" as the kids say."
        show conductor upset_intro upset_talk
        show stagehand paper
        c "... Please never talk like a modenr person again. Stay with your brooding characters and verbose language!"

        show black
        with dissolve
        hide black
        show conductor write_talk
        show stagehand neutral paper
        with dissolve

        show conductor write_talk
        show stagehand paper
        c "A street-corner turned into soda cups, and a chance encounter blossomed into prolonged contact."
        c "[you] has become quite acquainted with [char2name] after all this time. Their boyfriend is just a footnote in their mind with the help of a new friend."
        show stagehand paper_talk
        show conductor write
        show edy neutral at truecenter:
            xpos 0.62
        with easeinright
        z "... Oh! I see you brought your violin with you."
        show rom neutral at truecenter:
            xpos 0.39
        with easeinleft
        show conductor write_talk
        show stagehand paper
        y "Yeah! I'm playing with you today!"

        show conductor write
        show stagehand paper_talk
        s "This single life isn't awful, truthfully. A good friend that brings joy at all times is also a good replacement."
        s "[you] could even say that they wouldn't mind [char2name] as a partner..."
        show stagehand smug
        s "Ahem. But they digress."
        show stagehand idle
        with dissolve
        show conductor write_talk
        c "But... this light honeymoon phase can't last forever."
        c "One day, [char2name] comes up to [you], acting a bit out of character."
        show black
        with dissolve
        hide black
        hide edy
        with dissolve  

        show edy neutral at truecenter:
            xpos 0.62
        with easeinright
        show stagehand idle_talk
        z "[you]... I... need to talk to you. It's important."
        show conductor write_talk
        show stagehand idle
        show rom neutral:
            subpixel True 
            zrotate 0.0 
            easein_quad 0.45 zrotate 9.0 
        with Pause(0.55)
        show rom neutral:
            zrotate 9.0 
        y "What's up? You usually never concern yourself with stuff like that."
        show stagehand idle_talk
        show conductor write
        show edy sad
        with dissolve
        z "... I'm too far behind on my rent. My landlord is going to kick me out."
        show edy sad:
            subpixel True 
            ypos 0.5 
            easein_quad 0.34 ypos 0.55 
        with Pause(0.44)
        show edy sad:
            ypos 0.55
        z "I have to move back home."
        show rom sad:
            subpixel True 
            xpos 0.39 
            ease_back 0.44 xpos 0.43 
        with Pause(0.54)
        show rom sad:
            xpos 0.43
        show conductor upset_intro upset_talk
        show stagehand idle
        y "Home?! But isn't that..."
        show conductor upset
        show stagehand angry_intro angry
        show edy sad:
            subpixel True 
            zrotate 0.0 
            ease_quart 0.37 zrotate -18.0 
        with Pause(0.47)
        show edy sad:
            zrotate -18.0
        z "Yes. The home that kicked me out onto the streets in the first place."
        z "But I have no choice. I have to go back there."
        z "They'll laugh at me for being a street musician, but if I indebt myself to my parents... they'll probably let me stay."
        show rom surprised:
            subpixel True 
            ypos 0.59 
            spring3 0.38 ypos 0.5 
        with Pause(0.48)
        show rom surprised:
            ypos 0.5
        show conductor upset_talk
        y "You can't do that! You can't go back there!"
        y "Isn't there anything I can do to help? How much is your landlord asking of you?"
        show conductor upset
        show edy bother:
            subpixel True 
            zrotate -18.0 
            ease_quart 0.37 zrotate 0.0 
        with Pause(0.47)
        show edy bother:
            zrotate 0.0
        z "... Nah. The landlord wouldn't let me stay even if I paid it all today. It's a trust system, after all."
        show edy bother:
            subpixel True 
            ypos 0.55
            easein_quad 0.34 ypos 0.5
        with Pause(0.44)
        show edy bother:
            ypos 0.5
        z "& you got student loan debt to pay. Don't waste your future on me."
        show conductor upset_talk
        show rom sad:
            subpixel True 
            zrotate 9.0 
            bop_time_warp 0.41 zrotate 0.0 
        with Pause(0.51)
        show rom sad:
            zrotate 0.0 
        y "But I {i}care{/i} for you! You {i}are{/i} worth my future!"
        menu:
            y "I..."

            "You can stay with me.":
                show conductor write_talk
                with dissolve
                show rom neutral:
                    subpixel True 
                    xpos 0.43 
                    easein_circ 0.38 xpos 0.39 
                with Pause(0.48)
                show rom neutral:
                    xpos 0.39
                y "No strings attached! Hang out at my apartment!"
                y "It's not a two-bedroom, sure, but I think we can make it work."
                show edy excited
                show conductor write
                show stagehand happy paper_talk
                with dissolve
                z "... Really?"
                show edy neutral:
                    subpixel True 
                    xpos 0.62 
                    easein_cubic 0.45 xpos 0.66 
                with Pause(0.55)
                show edy neutral:
                    xpos 0.66
                z "But I have no money for rent."
                show stagehand paper
                show conductor write_talk
                show rom excited:
                    subpixel True 
                    ypos 0.59 
                    spring3 0.38 ypos 0.5 
                with Pause(0.48)
                show rom excited:
                    ypos 0.5
                y "No strings attached means no rent, either!"
                y "Worst comes to worst, I can sleep in a sleeping bag. Eternal sleepover and roommate!"
                show black
                hide stagehand
                hide conductor
                hide rom
                hide edy
                with dissolve
                z "Hahaha. You're... too generous."
                hide black
                show happy eddie 
                with dissolve
                z "But I insist. I cannot take for free."
                z "So... I'll play a song for you."
                z "The lyrics... ? How wonderful you are."

            "I'll book you a hotel room.":
                show conductor write_talk
                with dissolve
                show rom neutral:
                    subpixel True 
                    xpos 0.43 
                    easein_circ 0.38 xpos 0.39 
                with Pause(0.48)
                show rom neutral:
                    xpos 0.39
                y "I got enough money to spare to get you somewhere to stay until you can get on your feet."
                y "Library has free computers, so... you can look for a job online there!"
                y "And I can visit, too! If, uh, the hotel doesn't mind. Hehe."
                show edy excited
                show conductor write
                show stagehand happy paper_talk
                with dissolve
                z "I... thank you, [you]."
                z "You really are too kind."
                show edy excited:
                    subpixel True 
                    zrotate 0.0 
                    easein_cubic 0.50 zrotate -9.0 
                with Pause(0.60)
                show edy excited:
                    zrotate -9.0 
                z "When I get the money... I'll repay you every cent you spent on me. I promise."
                hide edy 
                with easeoutright
                show conductor idle
                with dissolve
                show stagehand paper_intro paper_talk
                s "Although [you] did a good thing, they can't help but feel like the missed the opportunity to do something even more alturistic... & perhaps a little selfish, too."





        jump ending

    label rom.gy:
        show gy surprised at truecenter:
            subpixel True
            xpos 0.62
        with easeinright
        show conductor think
        s "... Someone of a secret society, expert exploiter and eyes glinting."
        $ z = Character("???", color = "#00ffdd")
        z "Oh, young person. Watch your step."
        show rom surprised:
            subpixel True 
            zrotate 0.0 
            ease_circ 0.45 zrotate 37.0 
        with Pause(0.55)
        show rom surprised:
            zrotate 37.0
        show stagehand pointer
        show conductor think_talk
        y "Sorry... ! Just in a rush."
        show gy neutral:
            subpixel True 
            xpos 0.62 
            ease_circ 0.36 xpos 0.59 
        with Pause(0.46)
        show gy neutral:
            xpos 0.59 
        show stagehand smug pointer_talk
        show conductor write
        with dissolve
        z "... Pray tell, are you alright? You have tears in your eyes."
        show rom neutral:
            subpixel True 
            zrotate 37.0 
            easein_cubic 0.31 zrotate 0.0 
        with Pause(0.41)
        show rom neutral:
            zrotate 0.0
        show stagehand idle
        with dissolve
        show conductor write_talk
        y "Ah, don't worry about me. I had a hard day."
        show gy neutral:
            subpixel True 
            xpos 0.59
            ease_circ 0.36 xpos 0.62
        with Pause(0.46)
        show gy neutral:
            xpos 0.62
        show conductor write
        show stagehand idle_talk
        z "Talk to me about it."
        
        show rom sad
        with dissolve
        show conductor write_talk
        show stagehand idle
        y "... I got broken up by my boyfriend, and I don't know why. I thought our relationship was fine, but..."
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

        show gy surprised
        with dissolve
        show stagehand angry_intro angry
        z "You know... I can help you. Get him back, I mean. Revenge or otherwise."

        menu:

            "Would you like to go out for coffee?":
                show rom neutral
                with dissolve
                show conductor idle_talk
                y "As an apology for the trauma dump, and like... getting to know each other better."
                show conductor idle
                show stagehand paper_talk
                show gy excited
                with dissolve
                z "Coffee? Sure. I know a place, nice and quiet."

            "How much do you get paid?":
                show rom bother
                with dissolve
                show conductor idle_talk
                y "I need... something else to do with my life..."
                show gy sad
                show conductor idle
                show stagehand paper_talk
                with dissolve
                z "That is confidential, my friend. But I assure you, you won't need it when on the other side."
                y "{color=#777777}(... I'm dying?){/color}"

            "What is the meaning of existence?":
                show gy neutral:
                    subpixel True 
                    zrotate 0.0 
                    bop_out_time_warp 0.36 zrotate 18.0 
                with Pause(0.46)
                show gy neutral:
                    zrotate 18.0 
                z "Hehehe... that's the question we all seek to answer. It's what humanity was {i}made{/i} to answer."
                z "You're not too bad."
                show gy neutral:
                    subpixel True 
                    zrotate 18.0
                    bop_out_time_warp 0.36 zrotate 0.0
                with Pause(0.46)
                show gy neutral:
                    zrotate 0.0
                show rom bother
                with dissolve
                show conductor idle_talk
                y "{color=#777777}(What is that supposed to mean?){/color}"

            "It says gullible on the ceiling.":
                show gy bother
                with dissolve
                z "{color=#00ffdd}...{/color}"
                show rom bother:
                    subpixel True 
                    xpos 0.39 
                    easein_quad 0.31 xpos 0.36 
                with Pause(0.41)
                show rom bother:
                    xpos 0.36 
                show conductor idle_talk
                y "... Sorry..."

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

        show gy neutral:
            subpixel True 
            xpos 0.62 
            ease_circ 0.36 xpos 0.59 
        with Pause(0.46)
        show gy neutral:
            xpos 0.59 
        show conductor write
        show stagehand paper_talk
        $ z = Character("Godfrey", color = "#00ffdd")
        z "Simply... call me Godfrey. We will meet again, [you]."

        show stagehand paper
        show conductor write_talk
        c "And so, these intertwined souls separate, just for the time being."

        show black
        with dissolve
        hide black
        hide rom 
        hide gy
        show conductor write
        show stagehand paper_talk
        with dissolve


        s "This first act certainly has some interesting threads starting."
        show conductor think_intro think_talk
        show stagehand paper
        c "I feel like a secret society might be getting a bit off track for a simple break-up plot."
        show stagehand smug idle_talk
        with dissolve
        s "Haha. Most likely."
        show stagehand angry_intro angry
        s "We'll just have to see if [you] can make it through my trials intact."
        show conductor write_talk
        with dissolve
        c "... I have never known you for being particularly nice..."

        show black
        with dissolve
        hide black
        show conductor write_talk
        show stagehand paper
        with dissolve

        show conductor write_talk
        show stagehand paper
        c "A street-corner turned into soda cups, and a chance encounter blossomed into prolonged contact."
        c "[you] has become quite acquainted with [char2name] after all this time. Their boyfriend is just a footnote in their mind with the help of a new friend."
        show stagehand paper_talk
        show conductor write
        show gy neutral at truecenter:
            xpos 0.62
        with easeinright
        z "I have another scavenger hunt for you today."
        show rom neutral at truecenter:
            xpos 0.39
        with easeinleft
        show conductor write_talk
        show stagehand paper
        y "Does it bring you joy to watch an adult scour around the city like a rat?"

        show conductor write
        show stagehand paper_talk
        s "This single life isn't awful, truthfully. A good friend that brings joy at all times is also a good replacement."
        s "[you] could even say that they wouldn't mind [char2name] as a partner..."
        show stagehand smug
        s "Ahem. But they digress."
        show stagehand idle
        with dissolve
        show conductor write_talk
        c "But... this light honeymoon phase can't last forever."
        c "One day, [char2name] comes up to [you], acting a bit out of character."
        show black
        with dissolve
        hide black
        hide gy
        with dissolve  

        show gy neutral at truecenter:
            xpos 0.62
        with easeinright
        show stagehand neutral idle_talk
        show conductor write
        z "[you], [you]. You've been obedient and successful these past two months. I'd like to applaud you."
        show conductor write_talk
        show stagehand idle
        show rom neutral:
            subpixel True 
            zrotate 0.0 
            easein_quad 0.45 zrotate 9.0 
        with Pause(0.55)
        show rom neutral:
            zrotate 9.0 
        y "What's up? You usually never concern yourself with stuff like that."
        show stagehand idle_talk
        show conductor write
        show gy excited
        with dissolve
        z "We've been watching your progress closely."
        show rom bother:
            subpixel True 
            zrotate 9.0 
            easein_quad 0.42 zrotate 0.0 
        with Pause(0.52)
        show rom bother:
            zrotate 0.0
        show conductor write_talk
        show stagehand idle
        y "I think we've known each other long enough. You can stop being vague now."
        show conductor write
        show stagehand angry_intro angry
        show gy excited:
            subpixel True 
            xpos 0.62 
            ease_cubic 0.45 xpos 0.58 
        with Pause(0.55)
        show gy excited:
            xpos 0.58
        z "The secret society. We believe we can help you now... with your boyfriend."
        show rom sad
        with dissolve
        show conductor think_intro think_talk
        c "[you] can't tell if Godfrey is kidding or not."
        c "Frankly, it {i}does{/i} tracks with the weird things they've been doing the past two months. And Godfrey's own weirdness."
        c "But that's beside the point right now."
        show conductor write_talk
        with dissolve
        show rom neutral:
            subpixel True 
            ypos 0.59 
            spring3 0.38 ypos 0.5 
        with Pause(0.48)
        show rom neutral:
            ypos 0.5
        y "Oh! Don't worry about that. I'm over him now."
        y "I said we were drifting apart, right? Sometimes that just can't be helped."
        show rom neutral:
            subpixel True 
            zrotate 0.0 
            ease_quart 0.46 zrotate 9.0 
        with Pause(0.56)
        show rom neutral:
            zrotate 9.0
        y "Still a shame, though."
        show stagehand idle_talk
        with dissolve
        show conductor write
        show gy surprised:
            subpixel True 
            xpos 0.58
            ease_cubic 0.45 xpos 0.62 
        with Pause(0.55)
        show gy surprised:
            xpos 0.62
        z "... Oh. Well."
        z "I suppose that is good! You are of a healthy mind and self-esteem!"
        show gy surprised:
            subpixel True 
            zrotate 0.0 
            easein_quad 0.40 zrotate -9.0 
        with Pause(0.50)
        show gy surprised:
            zrotate -9.0 
        s "Godfrey ponders for a moment. They had not considered the possibility [you] wouldn't hold a grudge."
        show gy sad:
            subpixel True 
            zrotate -9.0 
            easein_quad 0.40 zrotate 0.0
        with Pause(0.50)
        show gy sad:
            zrotate 0.0
        z "I'm afraid I have nothing to offer you, then."
        show stagehand idle
        show conductor think_intro think_talk
        show rom excited:
            subpixel True 
            zrotate 9.0 
            ease_quart 0.46 zrotate 0.0 
        with Pause(0.56)
        show rom excited:
            zrotate 0.0
        y "Not even an invitation to the secret society? :("
        show conductor think
        show stagehand smug pointer_intro pointer_talk
        show gy sad:
            subpixel True 
            ypos 0.5 
            easein_cubic 0.44 ypos 0.55 
        with Pause(0.54)
        show gy sad:
            ypos 0.55 
        z "Hahaha. Don't look at me like that."
        show gy sad:
            subpixel True 
            ypos 0.55
            easein_cubic 0.44 ypos 0.5
        with Pause(0.54)
        show gy sad:
            ypos 0.5
        z "... {w=1} The plan was to do you a favor so you'd be indebted to join."
        z "But if you're willing, such precautions are unnecessary."
        show stagehand neutral pointer
        show conductor think_talk
        show rom sad
        with dissolve
        y "Relationships... aren't transactions, I think."
        y "Sure, it was rude that my boyfriend left me without a thorough explanation..."
        show rom neutral
        with dissolve
        y "But technically, he doesn't have to."
        y "It's not math or music notes. {w=1}It's just a thing."
        show conductor think
        show stagehand pointer_talk
        show gy bother
        with dissolve
        z "..."
        show gy surprised
        with dissolve
        z "If that is the way you see it."
        z "This... relationship... still feels a bit unequal, however. I ought to provide you with {i}something{/i}."
        
        menu:
            z "Do you wish for anything? As a... friend."

            "Can I see what you look like?":
                show gy bother
                with dissolve
                z "What I look like? What is wrong with my current appearance?"
                show rom bother
                with dissolve
                show stagehand pointer
                show conductor think_talk
                y "I don't think I've ever seen what you look like {i}under{/i} that hood."
                show black
                with dissolve
                z "Are you sure you can handle my grace?"
                y "You cannot be that important."
                hide stagehand
                hide black
                hide conductor
                hide rom
                hide gy
                show happy godfrey
                with fade
                z "Oh, but I am. Do not be fooled, mortal."
                y "Oh man... {i}What the heck are you?{/i}"
                z "I am the God of {color=#00ffdd}Fright and Dark.{/color}"
                z "Are you pleased with yourself? {i}Are your atoms crumbling?{/i}"
                y "... This is way better than a boyfriend, you know?!"
                z "Ah... uhm... I suppose so."
                z "Hehehehe."


            "Coffee please!":
                show gy bother
                with dissolve
                z "I have spent too many funds fueling your coffee addiction."
                show conductor idle_talk
                show stagehand pointer
                with dissolve
                show rom neutral:
                    subpixel True 
                    zrotate 0.0 
                    ease_quart 0.46 zrotate 9.0 
                with Pause(0.56)
                show rom neutral:
                    zrotate 9.0
                y "Well, if you didn't send me on expeditions at 3 am, maybe this is wouldn't be an issue."
                show stagehand smug pointer_talk
                show conductor idle
                z "Ah, so the fault is on me, now?"
                hide rom
                with easeoutright
                show conductor idle_talk
                y "Well... I'd probably blame high school first and foremost, then college, {i}then{/i} your secret society."
                show conductor idle
                show stagehand idle_talk
                with dissolve
                hide gy 
                with easeoutright
                z "I see. We will abolish the school system, then."
                show conductor idle_talk
                show stagehand idle
                y "... That's not gonna retroactively disable my caffeine addiction, though?"
                show conductor idle
                show stagehand paper_intro paper_talk
                s "Although the coffee was good, it feels like [you] missed an opportunity for a better deal..."

        jump ending

    label rom.edic:
        show edic neutral at truecenter:
            subpixel True
            xpos 0.62
        with easeinright
        show conductor upset_intro upset
        s "... A white guy named John."
        $ z = Character("John", color = "#07ce00")
        show conductor upset_talk
        show stagehand pointer
        c "... Is that it?"
        show stagehand idle_talk
        show conductor upset
        with dissolve
        s "Yeah."
        show conductor write_talk
        show stagehand idle
        show rom neutral:
            subpixel True 
            xpos 0.39 
            easein_circ 0.49 xpos 0.51 
        with Pause(0.59)
        show rom neutral:
            xpos 0.51 
        y "Ahem! Sorry, stock photo white man. Coming through."
        show stagehand idle_talk
        show conductor write
        show edic neutral:
            subpixel True 
            zrotate 0.0 
            ease_elastic 0.37 zrotate -9.0 
        with Pause(0.47)
        show edic neutral:
            zrotate -9.0
        z "I have a Doctorate in Psychology."
        show conductor happy think_talk
        with dissolve
        show stagehand idle
        c "Not in marketing?! Oh, uhm, I mean."
        show conductor neutral write_talk
        with dissolve
        show rom excited:
            subpixel True 
            ypos 0.59 
            spring3 0.38 ypos 0.5 
        with Pause(0.48)
        show rom excited:
            ypos 0.5 
        y "What?! Really? Then, if you don't mind me stopping you..."

        show edic neutral:
            subpixel True 
            zrotate -9.0 
            easein_quad 0.40 zrotate 0.0 
        with Pause(0.50)
        show edic neutral:
            zrotate 0.0 
        show rom sad:
            subpixel True 
            xpos 0.51 
            easein_quad 0.51 xpos 0.39 
        with Pause(0.61)
        show rom sad:
            xpos 0.39 
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

        show edic bother
        with dissolve
        show stagehand paper_intro paper_talk
        z "It is not your fault. The human brain is flawed with irrationality."
        show stagehand paper

        menu:

            "Would you like to go out for coffee?":
                show rom neutral
                with dissolve
                show conductor idle_talk
                y "As an apology for the trauma dump, and like... getting to know each other better."
                show conductor idle
                show stagehand paper_talk
                show edic bother:
                    subpixel True 
                    zrotate 0.0 
                    ease_back 0.40 zrotate 9.0 
                with Pause(0.50)
                show edic bother:
                    zrotate 9.0 
                z "I'm not friends with minors."
                show conductor idle_talk
                show stagehand paper
                show rom bother:
                    subpixel True 
                    ypos 0.5 
                    easein_quad 0.33 ypos 0.55 
                with Pause(0.43)
                show rom bother:
                    ypos 0.55 
                y "... I'm a senior in college? I graduate in like, a month."
                show conductor idle
                show stagehand idle_talk
                with dissolve
                show edic surprised:
                    subpixel True 
                    zrotate 9.0 
                    easein_circ 0.32 zrotate 0.0 
                with Pause(0.42)
                show edic surprised:
                    zrotate 0.0
                z "Oh, sorry. Still kind of weird, but okay."

            "How much do you get paid?":
                show rom bother
                with dissolve
                show conductor idle_talk
                y "I need... something else to do with my life..."
                show edic neutral
                show conductor idle
                show stagehand paper_talk
                with dissolve
                z "Six figure salary."
                show stagehand paper
                show conductor think_intro think_talk
                show rom surprised:
                    subpixel True 
                    zrotate 0.0 
                    ease_cubic 0.41 zrotate 18.0 
                with Pause(0.51)
                show rom surprised:
                    zrotate 18.0 
                y "As a psychology major? Who are you working for, the CIA?"
                show conductor think
                show stagehand smug pointer_talk
                show edic excited:
                    subpixel True 
                    ypos 0.59 
                    spring3 0.38 ypos 0.5 
                with Pause(0.48)
                show edic excited:
                    ypos 0.5 
                z "Close! The Queen of England."
                show rom surprised:
                    subpixel True 
                    zrotate 18.0 
                    ease_cubic 0.41 zrotate 0.0 
                with Pause(0.51)
                show rom surprised:
                    zrotate 0.0 

            "What is the meaning of existence?":
                show edic sad
                with dissolve
                show stagehand paper_talk
                z "I don't know. Maybe we're not meant to know."
                show stagehand paper
                show conductor write_intro write_talk
                c "That's surprisingly profound coming from a man named Jo--{nw=1}"
                show conductor distress write
                with dissolve
                show stagehand smug paper_talk
                show edic sad:
                    subpixel True 
                    zrotate 0.0 
                    ease_cubic 0.44 zrotate 9.0 
                with Pause(0.54)
                show edic sad:
                    zrotate 9.0
                z "Or, like, marmalade."
                show conductor neutral upset_intro upset_talk
                show stagehand paper
                show edic sad:
                    subpixel True
                    zrotate 9.0
                    ease_cubic 0.44 zrotate 0.0
                with Pause(0.54)
                show edic sad:
                    zrotate 0.0
                c "... Is he Australian now?"

            "It says gullible on the ceiling.":
                show edic neutral
                show stagehand pointer_talk
                z "No, but it says gullible below your feet."
                show stagehand pointer
                show conductor idle_talk
                show rom excited:
                    subpixel True 
                    ypos 0.5 
                    ease_back 0.36 ypos 0.42 
                with Pause(0.46)
                show rom excited:
                    ypos 0.42
                y "Er, really?"
                show rom sad:
                    subpixel True 
                    ypos 0.42 
                    ease2 0.53 ypos 0.5 
                with Pause(0.63)
                show rom sad:
                    ypos 0.5
                y "... No."
            

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
        show stagehand paper_talk
        show edic neutral:
            subpixel True 
            xpos 0.62 
            easein_quad 0.38 xpos 0.58 
        with Pause(0.48)
        show edic neutral:
            xpos 0.58 
        z "John Comedy. Let us give firm handshakes, as protocol says."

        show stagehand paper
        show conductor write_talk
        c "And so, these intertwined souls separate, just for the time being."

        show black
        with dissolve
        hide black
        hide rom 
        hide edic
        show conductor write
        show stagehand paper_talk
        with dissolve

        s "This first act certainly has some interesting threads starting."
        show conductor write_talk
        show stagehand paper
        c "... Why \"John Comedy?\""
        show stagehand happy paper_talk
        show conductor write
        s "This kind of character simply seemed like one you'd find humor in."
        show stagehand neutral paper
        show conductor think_intro think_talk
        c "Haha, I'm that much of a clown, huh?"
        c "Well... thanks for thinking of me."
        c "... But you can think of yourself next time, too."

        show black
        with dissolve
        hide black
        show conductor write_talk
        show stagehand paper
        with dissolve

        c "A street-corner turned into soda cups, and a chance encounter blossomed into prolonged contact."
        c "[you] has become quite acquainted with [char2name] after all this time. Their boyfriend is just a footnote in their mind with the help of a new friend."
        show stagehand paper_talk
        show conductor write
        show edic neutral at truecenter:
            xpos 0.62
        with easeinright
        z "I brought some souvenirs from England. Here, a feather from the Queen's swans."
        show rom neutral at truecenter:
            xpos 0.39
        with easeinleft
        show conductor write_talk
        show stagehand paper
        y "Wow! Now I can pretend to be a classical composer and hand-write illegible music scores!"

        show conductor write
        show stagehand paper_talk
        s "This single life isn't awful, truthfully. A good friend that brings joy at all times is also a good replacement."
        s "[you] could even say that they wouldn't mind [char2name] as a partner..."
        show stagehand smug
        s "Ahem. But they digress."
        show stagehand idle
        with dissolve
        show conductor write_talk
        c "But... this light honeymoon phase can't last forever."
        c "One day, [char2name] comes up to [you], acting a bit out of character."
        show black
        with dissolve
        hide black
        hide edic
        with dissolve


        show stagehand neutral idle_talk
        show conductor write
        show edic neutral at truecenter:
            xpos 0.62
        with easeinright
        z "Good morning, [you]. The middle of summer approaches."
        show conductor write_talk
        show stagehand idle
        show rom neutral:
            subpixel True 
            zrotate 0.0 
            easein_quad 0.45 zrotate 9.0 
        with Pause(0.55)
        show rom neutral:
            zrotate 9.0 
        y "What's up? You usually never concern yourself with stuff like that."
        show conductor write
        show stagehand pointer_intro pointer_talk
        show edic neutral:
            subpixel True 
            xpos 0.62 
            ease_quart 0.49 xpos 0.58 
        with Pause(0.59)
        show edic neutral:
            xpos 0.58
        z "That is where you are wrong."
        z "During this time, I go up to the mountains to escape the heat."
        z "There is a large cabin near a lake that I rent. The owners always complain about the fact I bring no one to the cabin despite the fact it is multi-bedroom."
        z "But I am a repeat customer, and I have no one to bring, so they do not do anything about it."
        show edic bother:
            subpixel True 
            xpos 0.58
            ease_quart 0.49 xpos 0.62
        with Pause(0.59)
        show edic bother:
            xpos 0.62
        z "However, I catch an exorbitant amount of fish that I can never finish eating."
        show stagehand pointer
        show conductor write_talk
        show rom bother:
            subpixel True 
            zrotate 9.0
            easein_quad 0.45 zrotate 0.0 
        with Pause(0.55)
        show rom bother:
            zrotate 0.0
        y "Can't you just... release the fish?"
        show stagehand angry_intro angry
        show conductor write 
        show edic bother
        z "You see, marmalade is actually really good with fish. So I always toss the marmalade with the fish so I don't have extra marmalade."
        show edic excited
        with dissolve
        z "The owners complain about that, too."
        show conductor upset_intro upset
        show rom bother:
            subpixel True 
            xpos 0.39 
            ease_back 0.46 xpos 0.36 
        with Pause(0.56)
        show rom bother:
            xpos 0.36
        y "..."
        show stagehand idle_talk
        with dissolve
        show edic neutral:
            subpixel True 
            xpos 0.62 
            ease_quart 0.49 xpos 0.58 
        with Pause(0.59)
        show edic neutral:
            xpos 0.58
        z "Anyway, I believe the solution is to bring along someone to eat fish with me."
        z "So I am offering this opportunity to you. Don't worry, you can fish too if you want. Post it on your dating profile."

        show conductor think_talk
        show stagehand idle
        with dissolve
        show rom bother
        c "[you] wouldn't really consider this a date considering that John just said to put fish on their dating profile (which they don't have, by the way.)"
        show rom excited:
            subpixel True 
            xpos 0.36
            ease_quart 0.49 xpos 0.39
        with Pause(0.59)
        show rom excited:
            xpos 0.39
        c "But John is offering {i}them{/i} to go to a cabin in the mountains-- his cabin that he has brought no one else before! How romantic is that?!"
        show rom bother
        with dissolve
        c "At the same time, it's a {i}secluded cabin in the mountains.{/i} That's also a {i}common murder plot.{/i}"
        menu: 
            c "Can a marmalade enjoyer even be trusted... ?"

            "Go fish!":
                show rom neutral
                show conductor write_talk
                with dissolve
                y "Hehe... sure!"
                y "Although, I don't know how to fish."
                show conductor write
                show stagehand idle_talk
                show edic excited:
                    subpixel True 
                    ypos 0.59 
                    spring3 0.38 ypos 0.5 
                with Pause(0.48)
                show edic excited:
                    ypos 0.5 
                z "It is easy. I hope you can stomach worms, however."
                show rom sad:
                    subpixel True 
                    xpos 0.39 
                    ease_back 0.46 xpos 0.36 
                with Pause(0.56)
                show rom sad:
                    xpos 0.36
                show conductor upset_intro upset_talk
                y "{color=#f260ff}I'm eating worms????{/color}"
                show black
                hide conductor
                hide stagehand
                hide edic
                hide rom
                with dissolve
                c "[you] takes a week trip to the Fuca Mountains with John, a well-earned cherry on top of their relationship."
                y "Wow! The water is so clear!"
                hide black
                show happy john
                with dissolve
                z "That is what mountain springs create. Frankly, I'm surprised such abundant fish exist here."
                z "Usually, mountain lakes don't have much dissolved oxygen. I'm a psychology major though. Don't know anything about that."
                y "Waah!! Why are you holding the fish like that?"
                z "This is how I gauge if a fish is good for eating."
                y "... You are very strange, don't you know?"
                z "Ha. You don't seem to mind, though!"

            "no thank you british-australian(?) man":
                y "Sorry, I... don't think I can go."
                y "I'm the, uh, opposite of a pescatarian."
                show stagehand idle_talk
                show conductor think
                show edic surprised:
                    subpixel True 
                    zrotate 0.0 
                    spring3 0.38 zrotate 9.0 
                with Pause(0.48)
                show edic surprised:
                    zrotate 9.0
                z "... Swear I saw you eating sushi the other day."
                show rom neutral:
                    subpixel True 
                    zrotate 0.0 
                    spring3 0.38 zrotate -9.0 
                with Pause(0.48)
                show rom neutral:
                    zrotate -9.0
                show stagehand idle
                show conductor think_talk
                y "Oh, it's not about taste or anything. I just hate dealing with bones."
                show rom neutral:
                    subpixel True 
                    zrotate -9.0 
                    ease2 0.45 zrotate 0.0 
                with Pause(0.55)
                show rom neutral:
                    zrotate 0.0 
                y "So if you can bring a whole fish back, I guess I could find someone to debone it for me."
                show edic neutral:
                    zrotate 0.0
                with dissolve
                show conductor think
                show stagehand idle_talk
                z "Ah. I understand. I will try my best to remember this."
                hide edic
                with easeoutleft
                z "Farewell, then."
                show stagehand pointer_intro pointer_talk
                s "John, the white man, takes his leave to his natural habitat."
                show stagehand smug
                s "Somehow, it feels like something went wrong."

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
    $ y = Character("[you]", color="#07ce00")
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
    show black
    with dissolve
    hide black
    hide happy
    show conductor write_talk at left
    show stagehand paper at right
    with dissolve
    menu:
        c "That's the second act done. And now, there is only one way for this story to end."

        "Bright rays shine down on morning bells...":
            show black
            with dissolve
            c "Adults and children alike cheer for this white day."
            #if char1 == 1:
                #show bellsChar1 rom
            #for when other char1's exist
            
            #if char2 == 1:
                #show bellsChar2 ai 
            #elif char2 == 2:
                #show bellsChar2 eddie 
            #elif char2 == 3:
                #show bellsChar2 godfrey 
            #else: 
                #show bellsChar2 john

            if char1 == 1:
                y "Wow... To think breaking up with my college boyfriend would lead to my marriage..."

            s "Years into the future, the intertwined souls become wedded under a glorious arch."

            if char2 == 1:
                c "Grandparents weep at their grandchild's happiest day."
                z "Mom, dad... are you proud of me? I live on."
            elif char2 == 2:
                c "The venue fills with beautiful music from fellow musicians and graduates."
                z "Life... hasn't ended yet. There is still another repeat in the measure."
            elif char2 == 3:
                s "Cult members chant blessings for the couple."
                z "... I'm not sure how I ended up on this path. But... I don't think it's so bad." 
            else: 
                s "John does a peace sign at the altar."
                z "Humans are not solitary animals, despite the existence of introverts and the like. we cannot have peace without companionship."

            c "It's... a wonderous day."


        "Rolling clouds rain down city walls and gluttinous gutters...":
            scene black
            with dissolve
            c "As I said, nothing can last forever."
            #if char1 == 1:
                #show rainRom
            #for when other char1's exist
            
            #if char2 == 1:
                #show rainAi
            #elif char2 == 2:
                #show rainEddie
            #elif char2 == 3:
                #show rainGod 
            #else: 
                #show rainJohn
  
            with dissolve

            if char1 == 1:
                y "I left two hearts behind when I moved out of the city for graduation. [char2name]'s... and the part of mine that yearns for them."
            #for when other char1's exist
            
            if char2 == 1:
                c "Both [you] and Ai lament what could have been."
                z "I hope [you] comes to visit sometime. So I can... amend my missed chance."
            elif char2 == 2:
                s "Though [you] may live on, something different is to be said for Eddie."
                z "It's all over. There is nothing and nobody here for me. Should I just... ?"
            elif char2 == 3:
                s "But still... it feels like someone is still watching [you]."
                z "You thought you could leave? Hahaha... it was naive to get so close to me, then."
            else: 
                c "Lives drift apart, and people move on in the end. It is an inevitability."
                z "That student... I hope they are alright. Psychologists can only hope for the best once a patient leaves their care."
            
            c "Would there still be a opportunity, if [you] returned to their past?"

        #"Alleys echo the same white noise they always did...":
            #pass

        "The earth rumbles with magma and tension...":
            scene black
            with dissolve

            if char1 == 1:
                y "Eh?! What is going on?"
            #for when other char1's exist
            
            if char2 == 1:
                c "Ai jumps into your arm, quivering but enjoying the warmth of your skin. Actually, it seems everything is warm."
                z "[you]! Hold me!!"
            elif char2 == 2:
                c "Eddie's face turns stone cold and solid as the ceiling crumbles around them."
                z "... Catharsis is here." 
            elif char2 == 3:
                s "Countless figures in cloaks emerge from the darkness."
                z "The almighty day is here! Rejoice! Rejoice!"
            else: 
                s "John scrambles to secure the cabinets."
                z "My marmalade... they can't take you!"


            show bg hill
            show paper
            show earth
            with dissolve
            c "In the wake of human joy and lamenting... the Earth has exploded."

    scene black
    with dissolve
    hide black
    show bg hill
    show conductor write at left
    show stagehand paper_talk at right
    with dissolve
    hide paper
    with easeoutbottom
        
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
    stop music
    play sound crumple
    "???" "..."
    "???" "I guess this light-hearted reprieve ended up meaningful after all."
    "End: A Dream within a Dream."

    return

"HEY HOW DID YOU GET HERE"
return
