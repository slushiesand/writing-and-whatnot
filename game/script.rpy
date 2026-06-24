
define c = Character("???", color = "#cb7be1")
define s = Character("Friend", color = "#ff0000")
define y = Character("([you]")
define z = Character("placeholder")

image black = "#000"

define audio.crumple = "zapsplat_foley_paper_bags_pile_scrunched_push_down_compress_squash_001_113503.mp3"
define audio.conDistress = "zapsplat_household_alarm_clock_old_fashioned_ring_very_short_44062.mp3"
define audio.staDistress = "zapsplat_impact_hard_rock_hit_metal_and_glass_crash_smash_break_008_108027.mp3"

$ banNames = ["Eiax", "Aelred", "Kazan", "Eilhart", "Fuca", "Olivia", "Monochrome", "B1nary", "Mr. Script", "Beatrice", "Moth", "Ceiling"]
# every name used in a past game of mine, excluding "King" and "Queen" since they are: 1. Common words and 2. Not their real names.
# "To the Ceiling!!"" isn't canon to any of my other games, but since this is more of a "4th wall breaking story," he should probably also be in this list. he isn't my original character anyway!

label start:

    scene cg far1
    with Fade(1.0, 0, 1.0)
    play music master_of_dreams_clock_ticking_337
    c "..."
    play sound crumple volume 0.4
    show cg far2
    c "... No, not good enough. {w=1}Scrap!"
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
    c "?!?"
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
    c "Shouldn't it be obvious? {w=1}You've been with me forever."
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

    return
