
init python:
    import random

define c = Character("???", color = "#cb7be1")
define s = Character("Friend", color = "#ff0000")
define y = Character("[you]")
define z = Character("placeholder")
image black = "#000"

define audio.crumple = "zapsplat_foley_paper_bags_pile_scrunched_push_down_compress_squash_001_113503.mp3"
define audio.conDistress = "zapsplat_household_alarm_clock_old_fashioned_ring_very_short_44062.mp3"
define audio.staDistress = "zapsplat_impact_hard_rock_hit_metal_and_glass_crash_smash_break_008_108027.mp3"

label start:
    $ char2 = random.randint(1, 4)
    scene cg far1
    with Fade(1.0, 0, 1.0)
    play music master_of_dreams_clock_ticking_337
    c "..."
    play sound crumple volume 0.4
    show cg far2
    c "... No, not good enough. {w=1}{i}Scrap!{/i}"
    c "What does the story have to do with the wider narrative? What's the message I want people to take away?"

    show cg close1
    with dissolve
    c "Think, brain. Think!"
    show cg close2
    play sound zapsplat_foley_footstep_shoe_sandal_single_scrape_wipe_grass_001_101428 volume 0.4
    s "Haven't you done enough thinking?"
    show cg close2
    with vpunch
    stop music
    play sound conDistress volume 0.5
    c "{i}?!?{/i}"
    scene bg hill
    with dissolve
    s "Look up, {color=#cb7be1}o' Conductor{/color} of this realm. Your ideas fly like cranes."
    show cg close2
    with dissolve
    s "... & they're getting {i}very{/i} annoying to avoid."
    $ c = Character("Conductor", color="#cb7be1")

    scene bg hill 
    show con placeholder at left
    show sta placeholder at right
    with dissolve
    #for now these will be reg sprites, but in the future, they'll be live2d
    c "Haah... Well, stories don't write themselves, you know?"
    c "Someone's gotta write them, but that someone doesn't have a lick of imagination right now."
    s "What is it you're trying to write, anywho?"
    c "Oh! Well, there's a lot I want to write!"
    c "There's this young-looking man who gets snowed in a cabin, but he's actually, like, 700 years old!{nw=.5}"
    c "And this shut-in whose social life consists of artifical intelligences, and--{nw=.5}"
    play sound staDistress volume 0.4
    s "Apologies. Forget I asked."
    s "In any case, you clearly haven't gotten very far in your writings."
    c """

    ... {w=1}Yeah, I know. It's just...

    None of the words come out right. It's all... {w=1}{i}out of character.{/i}

    These people I try to write-- They're flatter and more cliche on the paper than in my head, and I can't stand it!

    I know the hallmarks of bad writing, and I've read the copy-paste material from copy-paste authors.

    So {i}why{/i} does my pencil still produce amateur work?

    Why can my people only come alive in the confines of my head?

    """

    s "{i}Why{/i} do you aim to make a masterpiece?"
    c "Shouldn't it be obvious? {w=1}You've been with me forever now."
    c "... {w=1}I want to make something meaningful."
    s "In that case, why don't you take a break and write something new?"
    s "It doesn't have to be fancy, nor something perfect."
    s "Just make something you're proud of. That will give you the \"meaning\" you've been searching for."

    scene bg paper
    with dissolve
    #crumple
    c "Ah, but I've never been good at making new ideas either..."
    c "Maybe you can help me write?"
    s "Me? I'm not a creative individual, I'm afraid."
    c """

    We worked together once, as {color=#cb7be1}\"Conductor\"{/color} and {color=#ff0000}\"Stagehand\".{/color}

    \"Designer\" and \"Mathmetician.\" \"Videographer\" and \"Editor.\" Both differently wired, but equally essential.

    It's been a while since we've worked together, you know? It would be nice to hang out more casually!

    Plus, monologuing flowery advice doesn't make you look cool, so you might as well sit down.

    """
    #just realized i'll have to seperate this when i add in the poses DANG IT\
    $ s = Character("Stagehand", color="#ff0000")
    #sitting sfx
    s "... If you insist."

    show con placeholder at left
    show sta placeholder at right
    with dissolve
    s "So..."
    python:
            banNames = ["Eiax", "Aelred", "Kazan", "Eilhart", "Fuca", "Olivia", "Monochrome", "B1nary", "Mr. Script", "Beatrice", "Moth", "Ceiling"]
            # every name used in a past game of mine, excluding "King" and "Queen" since they are: 1. Common words and 2. Not their real names.
            # "To the Ceiling!!" isn't canon to any of my other games, but since this is more of a "4th wall breaking story," he should probably also be in this list. he isn't my original character anyway!
            special = ["Stagehand", "Conductor", "Ampersand", "Slushie"]

            you = None
            while you == None or not you or you in banNames or you in special:
                you = renpy.input("What is your character's name?")
                you = you.strip().title()

                if not you:
                    s ("I implore you to try to think of something.")
                elif you in banNames:
                    s ("Hey now. Originality, remember?")
                elif you in special:
                    s ("Ah...{w=1} you want to tell {i}that{/i} story? So near and dear to your heart?")
                    s ("Well, I'm afraid we have no time to implement such things, at least not now, {color=#cb7be1}dreamer.{/color}")
    
    s "[you]... a typical naming scheme. Not to say that is a bad thing."
    menu:
        s "What kind of character would this \"[you]\" be?"

        "A violin-ing college student, looking to fill their heart.":
            jump rom

        "A middle-aged coporate slave whose veins pulse with sorrow.":
            jump trag

        "The alley-dweller whose mind wavers between contempt and absurdity.":
            jump ed

        "It doesn't matter who I am. I am the inane and the egoist!":
            jump com

label rom:
    $ y = Character("[you]", color="#f260ff")
    show rom placeholder 
    with easeinbottom
    y "I can't believe it! After 3 years of {i}happiness{/i} and {i}fulfillment{/i}, they just {color=#f260ff}dumped{/color} me!"
    y "Waah... and exams are coming up too!"
    y "What am I going to do... ?"
    s "Ah... If that's the character you wish to write."

    show black
    with dissolve
    hide black
    with dissolve

    c "Despite the circumstances, it's a bright and sunny day."
    y "Maybe this means... things will get better."
    y "But I don't really have the time nor the energy to worry about my love life right now. I have to worry about my {color=#f260ff}grades!"
    y "Let's see... music theory is on Friday. Guess I should study whatever the heck a phrygian is."
    hide rom
    with easeoutright
    y "To the library!"

    show black
    with dissolve
    hide black
    with dissolve
    show rom placeholder
    with easeinleft

    s "[you] takes a seat at a lonely table at the local library, but they can't focus for a single second."
    s "It seems today... {w=1}every couple in a 5 mile radius is also studying."
    s "Couples giggling 'round a romance book, couples poking each other with pool cues, even couples taking naps in the valuable bean bags!"
    y "Look at these people living full lives with another human being. {i}Haah!!"
    y "Whatever! Sight-reading is most of the score anyway! I... {size=-10}don't need...{/size}"
    c "The lump in their throat stops them from finishing their sentence."
    c "They walk out quietly-- well, as quietly as someone on the verge of tears can -- onto the bustling street."
    y "I guess I should just go home."
    c "If [you] can just get home, maybe they can do some chores to get their mind off things... or cry into their pillow."
    s "But in circumstance, or perhaps fate, [you] stumbles into..."
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
        s "ai"

    label rom.edy:
        s "eddie"

    label rom.gy:
        s "godfrey"

    label rom.edic:
        s "john"

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

    label trag.edy:
        s "eddie"

    label trag.gy:
        s "godfrey"

    label trag.edic:
        s "john"

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

    label ed.edy:
        s "eddie"

    label ed.gy:
        s "godfrey"

    label ed.edic:
        s "john"
    
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

    label com.edy:
        s "eddie"

    label com.gy:
        s "godfrey"

    label com.edic:
        s "john"

    return


"HEY HOW DID YOU GET HERE"
return
