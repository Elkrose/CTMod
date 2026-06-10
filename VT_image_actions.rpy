# Home Improvement  MOD:
init 100 python: 
    add_label_hijack("normal_start", "update_VT_mom_office_lobby_background")

label update_VT_mom_office_lobby_background(stack):
    python:
        mom_office_lobby.background_name = "Vandenberg_Lobby_Background"
        lily_bedroom.background_name = "Lily_Start_Bedroom_Background"
        mom_bedroom.background_name = "Mom_Start_Bedroom_Background"
        bedroom.background_name = "MC_Starting_Bedroom_Background"
        execute_hijack_call(stack)
    return


init 5 python:
 
    config.label_overrides["mc_bedroom_renovate_completed_label"] = "CT_mc_bedroom_renovate_completed_label"
    config.label_overrides["lily_bedroom_renovate_completed_label"] = "CT_lily_bedroom_renovate_completed_label"
    config.label_overrides["mom_bedroom_renovate_completed_label"] = "CT_mom_bedroom_renovate_completed_label"
    config.label_overrides["home_shower_renovate_completed_label"] = "CT_home_shower_renovate_completed_label"
    config.label_overrides["dungeon_completed_label"] = "CT_dungeon_completed_label"
    config.label_overrides["harem_completed_label"] = "CT_harem_completed_label"
    config.label_overrides["mc_bedroom_renovate_label"] = "CT_mc_bedroom_renovate_label"
    config.label_overrides["lily_bedroom_renovate_label"] = "CT_lily_bedroom_renovate_label"
    config.label_overrides["mom_bedroom_renovate_label"] = "CT_mom_bedroom_renovate_label"


label CT_mc_bedroom_renovate_label():
    "As thoughts of your bedroom, memories of late-night pizza parties and cram sessions come flooding back. It's time to shed the collegiate vibe and upgrade to a space that reflects your status as a thriving entrepreneur."
    mc.name "Good day, this is [mc.name] [mc.last_name], CEO of [mc.business.name],  I'm looking to give my bedroom a luxurious makeover and I've heard great things about Blossom Construction's attention to detail and professionalism."
    "You spend the next hour discussing the finer points of interior design with the contractor, envisioning a sleek and sophisticated oasis that exudes success. Rich hardwood floors, plush carpeting, and lavish furnishings will soon replace the worn-out relics of your student days."
    python:
        mc.business.change_funds(-mc_bedroom_renovation_cost, stat = "Renovations")
        add_mc_bedroom_renovate_completed_action()
    "With the plans set in motion, you can't wait to unwind in your new sanctuary after a long day of wheeling and dealing."
    return

label CT_lily_bedroom_renovate_label():
    "You've decided it's time to give [lily.title]'s bedroom a lavish makeover. After a heart-to-heart with [lily.possessive_title] about her dream space, you pick up the phone and dial your trusted contractor."
    mc.name "Good morning, I'm [mc.name] [mc.last_name], CEO of [mc.business.name]. I'd like to commission a bespoke renovation for [lily.title]'s bedroom. I want it to be a serene retreat that reflects her personality and our family's refined taste."
    "As you discuss the design with the contractor, you envision a haven that will make [lily.title] feel like royalty. Soft, golden lighting, plush textiles, and elegant furnishings will soon replace the humble decor of her student days."
    python:
        mc.business.change_funds(-mc_bedroom_renovation_cost, stat = "Renovations")
        add_lily_bedroom_renovate_completed_action()
    "With the renovation plans underway, you can't wait to see the look of delight on [lily.title]'s face when she steps into her new sanctuary."
    return

label CT_mom_bedroom_renovate_label():
    "You've decided to surprise [mom.title] with the ultimate gesture of love and appreciation: a stunning bedroom makeover. After a warm conversation with [mom.possessive_title] about her desires, you reach out to your trusted contractor."
    mc.name "Good morning, I'm [mc.name] [mc.last_name], CEO of [mc.business.name]. I'd like to arrange a premium renovation for [mom.title]'s bedroom, incorporating her personal style and preferences."
    "As you discuss the design with the contractor, you picture a serene oasis that will be [mom.title]'s own private haven. Soothing colors, elegant furniture, and thoughtful touches will come together to create a space that's both relaxing and rejuvenating."
    python:
        mc.business.change_funds(-mc_bedroom_renovation_cost, stat = "Renovations")
        add_mom_bedroom_renovate_completed_action()
    "With the renovation plans in motion, you look forward to seeing the joy on [mom.title]'s face when she experiences her beautiful new bedroom for the first time."
    return

label CT_mc_bedroom_renovate_completed_label():
    $ man_name = "Elkrose"
    $ play_ring_sound()
    "As you're attending to your daily affairs, your phone rings, and you answer to hear the familiar voice of your contractor."
    man_name "Good day, Sir. This is Elkrose from Blossom Construction. I'm pleased to inform you that our team has completed the renovation work on your bedroom."
    mc.name "Excellent, thank you, Mr. Elkrose. I appreciate your team's hard work and attention to detail."
    "You can't wait to see the transformation for yourself. You make your way to your bedroom, and as you enter, you're struck by the stunning result. The once-familiar space has been reborn into a luxurious retreat, perfectly tailored to your refined taste."
    python:
        bedroom.background_name = "MC_Bedroom_Background"
        mc.business.add_mandatory_crisis(Action("Open up additional home improvement", home_improvement_unlocked_requirement, "home_improvement_unlocked_label", requirement_args = day + 1))
    "With your new sanctuary complete, you feel invigorated and ready to take on the challenges of the day."
    return

label CT_lily_bedroom_renovate_completed_label():
    $ man_name = "Elkrose"
    $ play_ring_sound()
    "As you're attending to your daily affairs, your phone rings, and you answer to hear the familiar voice of your contractor."
    man_name "Good day, Sir. This is Elkrose from Blossom Construction. I'm pleased to inform you that our team has completed the renovation work on [lily.title]'s bedroom."
    mc.name "Excellent, thank you, Mr. Elkrose. I appreciate your team's hard work and attention to detail."
    "You can't wait to see [lily.possessive_title!c]'s reaction to her new bedroom. You make your way to her room, and as you enter, you're struck by the beautiful result. The once-cozy space has been transformed into a lovely retreat, perfectly suited to [lily.title]'s sweet personality."
    python:
        lily_bedroom.background_name = "Lily_Bedroom_Background"
        lily.change_stats(love = 3 + mc.charisma, obedience = 1 + mc.charisma)
    "[lily.title] is overjoyed with her new bedroom, and her eyes sparkle with delight as she thanks you for the wonderful surprise. Your thoughtful gesture has clearly touched her heart, and you can sense a deeper connection growing between you."
    return

label CT_mom_bedroom_renovate_completed_label():
    $ man_name = "Elkrose"
    $ play_ring_sound()
    "As you're attending to your daily affairs, your phone rings, and you answer to hear the familiar voice of your contractor."
    man_name "Good day, Sir. This is Elkrose from Blossom Construction. I'm pleased to inform you that our team has completed the renovation work on [mom.title]'s bedroom."
    mc.name "Excellent, thank you, Mr. Elkrose. I appreciate your team's hard work and attention to detail."
    "You make your way to [mom.title]'s bedroom, eager to see the finished result. As you enter, you're struck by the warm and inviting atmosphere that now fills the space. The renovation has transformed the room into a serene retreat, perfectly suited to [mom.title]'s gentle nature."
    python:
        mom_bedroom.background_name = "MOM_Bedroom_Background"
        mom.change_stats(love = 3 + mc.charisma, obedience = 1 + mc.charisma)
    "[mom.title] is deeply touched by your thoughtful gesture, and her eyes shine with gratitude as she thanks you for the beautiful new bedroom. You can sense a deeper bond growing between you, one that's built on love, respect, and appreciation."
    return

label CT_home_shower_renovate_completed_label():
    $ man_name = "Elkrose"
    $ play_ring_sound()
    "As you're attending to your daily affairs, your phone rings, and you answer to hear the familiar voice of your contractor."
    man_name "Good day, Sir. This is Elkrose from Blossom Construction. I'm pleased to inform you that our team has completed the renovation work on your shower."
    mc.name "Excellent, thank you, Mr. Elkrose. I appreciate your team's hard work and attention to detail."
    "You make your way to the bathroom, eager to see the finished result. As you enter, you're impressed by the sleek and modern design of the new shower. The rainfall showerhead, glass enclosure, and marble tiles all come together to create a spa-like experience that's sure to leave you feeling refreshed and rejuvenated."
    python:
        home_shower.background_name = "Home_Shower_Background"
        mc.change_max_energy(10)
        lily.change_max_energy(10)
        mom.change_max_energy(10)
    "With the new shower complete, you can't wait to indulge in a relaxing shower and feel the stress of the day melt away. And with the increased energy it brings, you're confident that you and your loved ones will be able to tackle the challenges of the day with renewed vigor and enthusiasm."
    return

label CT_dungeon_completed_label():
    $ man_name = "Elkrose"
    $ play_ring_sound()
    "As you're attending to your daily affairs, your phone rings, and you answer to hear the familiar voice of your contractor."
    man_name "Good day, Sir. This is Elkrose from Blossom Construction. I'm pleased to inform you that our team has completed the construction of the dungeon at your residence."
    mc.name "Excellent, thank you, Mr. Elkrose. I appreciate your team's discretion and attention to detail."
    "You make your way to the dungeon, eager to inspect the finished result. As you enter, you're struck by the stark contrast between the luxurious amenities and the sinister purpose of the space. The cold, dark walls seem to whisper secrets, and the air is thick with anticipation."
    $ mc.event_triggers_dict["dungeon_owned"] = True
    $ dungeon.visible = True
    python:
        dungeon.background_name = "CT_Dungeon_Background"
    "With the dungeon now ready for use, you can't help but feel a sense of excitement and trepidation. The possibilities are endless, and you're eager to explore the depths of your own desires."
    return

label CT_harem_completed_label():
    $ man_name = "Elkrose"
    $ play_ring_sound()
    "As you're attending to your daily affairs, your phone rings, and you answer to hear the familiar voice of your contractor."
    man_name "Good day, Sir. This is Elkrose from Blossom Construction. I'm pleased to inform you that our team has completed the construction of the mansion adjacent to your residence."
    mc.name "Excellent, thank you, Mr. Elkrose. I appreciate your team's dedication to bringing my vision to life."
    "You make your way to the mansion, eager to inspect the finished result. As you enter, you're struck by the opulent decor and lavish amenities. The spacious halls, adorned with intricate artwork, seem to whisper tales of exotic pleasures, and the air is alive with the promise of indulgence."
    $ mc.event_triggers_dict["harem_mansion_build"] = True
    $ harem_mansion.visible = True
    python:
        harem_mansion.background_name = "CT_Harem_Background"
    "With the mansion now ready for use, you can't help but feel a sense of excitement and anticipation. The possibilities are endless, and you're eager to explore the depths of your desires and create unforgettable memories with your loved ones."
    return


init 13 python:

    def home_improvement_unlocked_requirement(trigger_day): # Currently ignoring trigger_day
        return bedroom.background_name == "MC_Bedroom_Background"

    def CT_add_mc_bedroom_renovate_completed_action(wrapped_func):
        def wrapping_func(*args, **kwargs):
            finish_day = (day + TIER_1_TIME_DELAY + renpy.random.randint(0,3))
            mc.business.set_event_day("home_improvement_day", finish_day)
            mc_bedroom_renovate_completed_action = Action("Bedroom Renovation Completed", home_renovation_completion_requirement, "CT_mc_bedroom_renovate_completed_label", requirement_args = finish_day)
            mc.business.add_mandatory_crisis(mc_bedroom_renovate_completed_action)
        wrapping_func.__signature__ = inspect.signature(wrapped_func)
        return wrapping_func

    def CT_add_lily_bedroom_renovate_completed_action(wrapped_func):
        def wrapping_func(*args, **kwargs):
            finish_day = (day + TIER_1_TIME_DELAY + renpy.random.randint(0,3))
            mc.business.set_event_day("home_improvement_day", finish_day)
            lily_bedroom_renovate_completed_action = Action("Bedroom Renovation Completed", home_renovation_completion_requirement, "CT_lily_bedroom_renovate_completed_label", requirement_args = finish_day)
            mc.business.add_mandatory_crisis(lily_bedroom_renovate_completed_action)
        wrapping_func.__signature__ = inspect.signature(wrapped_func)
        return wrapping_func

    def CT_add_mom_bedroom_renovate_completed_action(wrapped_func):
        def wrapping_func(*args, **kwargs):
            finish_day = (day + TIER_1_TIME_DELAY + renpy.random.randint(0,3))
            mc.business.set_event_day("home_improvement_day", finish_day)
            mom_bedroom_renovate_completed_action = Action("Bedroom Renovation Completed", home_renovation_completion_requirement, "CT_mom_bedroom_renovate_completed_label", requirement_args = finish_day)
            mc.business.add_mandatory_crisis(mom_bedroom_renovate_completed_action)
        wrapping_func.__signature__ = inspect.signature(wrapped_func)
        return wrapping_func

    def CT_add_home_shower_renovate_completed_action(wrapped_func):
        def wrapping_func(*args, **kwargs):
            finish_day = (day + TIER_2_TIME_DELAY + renpy.random.randint(0,3))
            mc.business.set_event_day("home_improvement_day", finish_day)
            home_shower_renovate_completed_action = Action("Shower Renovation Completed", home_renovation_completion_requirement, "CT_home_shower_renovate_completed_label", requirement_args = finish_day)
            mc.business.add_mandatory_crisis(home_shower_renovate_completed_action)
        wrapping_func.__signature__ = inspect.signature(wrapped_func)
        return wrapping_func

    def CT_add_dungeon_build_completed_action(wrapped_func):
        def wrapping_func(*args, **kwargs):
            finish_day = day + TIER_2_TIME_DELAY + renpy.random.randint(0,3)
            mc.business.set_event_day("home_improvement_day", finish_day)
            dungeon_completed_action = Action("Dungeon Completed", home_renovation_completion_requirement, "CT_dungeon_completed_label", requirement_args = finish_day)
            mc.business.add_mandatory_crisis(dungeon_completed_action)
        wrapping_func.__signature__ = inspect.signature(wrapped_func)
        return wrapping_func

    def CT_add_harem_build_completed_action(wrapped_func):
        def wrapping_func(*args, **kwargs):
            finish_day = day + TIER_3_TIME_DELAY + renpy.random.randint(2, 7)
            mc.business.set_event_day("home_improvement_day", finish_day)
            harem_mansion_completed_action = Action("Harem Mansion Completed", home_renovation_completion_requirement, "CT_harem_completed_label", requirement_args = finish_day)
            mc.business.add_mandatory_crisis(harem_mansion_completed_action)
        wrapping_func.__signature__ = inspect.signature(wrapped_func)
        return wrapping_func

    def mom_bedroom_renovate_requirement():
        if mom_bedroom.background_name == "MOM_Bedroom_Background":
            return False
        if is_home_improvement_in_progress():
            return format_home_improvement_completion_message()
        if not mc.business.is_open_for_business:
            return "Only during business hours"
        if mc.business.has_funds(mc_bedroom_renovation_cost):
            return True
        return f"Requires: ${mc_bedroom_renovation_cost:,.0f}"


    add_mc_bedroom_renovate_completed_action = CT_add_mc_bedroom_renovate_completed_action(add_mc_bedroom_renovate_completed_action)
    add_lily_bedroom_renovate_completed_action = CT_add_lily_bedroom_renovate_completed_action(add_lily_bedroom_renovate_completed_action)
    add_mom_bedroom_renovate_completed_action = CT_add_mom_bedroom_renovate_completed_action(add_mom_bedroom_renovate_completed_action)
    
    add_home_shower_renovate_completed_action = CT_add_home_shower_renovate_completed_action(add_home_shower_renovate_completed_action)
    add_dungeon_build_completed_action = CT_add_dungeon_build_completed_action(add_dungeon_build_completed_action)
    add_harem_build_completed_action = CT_add_harem_build_completed_action(add_harem_build_completed_action)

