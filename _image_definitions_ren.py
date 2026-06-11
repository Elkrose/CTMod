from __future__ import annotations
import renpy
from renpy.display import im
from renpy.display.im import Image
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -100 python:
"""

modpath = "/CTimages/"

def get_ctmod_file_handle(base_name: str) -> str | None:
    """
    Look for base_name with any of the common image extensions.
    Returns the first matching path from renpy.exports.list_files().
    """
    exts = (".png", ".jpg", ".jpeg", ".webp")
    files = renpy.exports.list_files()
    for ext in exts:
        target = base_name + ext
        # match by “endswith” so we catch paths like ".../CTimages/Name.png"
        found = next((f for f in files if f.endswith(target)), None)
        if found:
            return found
    return None

def load_ctmod_image(base_name: str) -> Image | None:
    handle = get_ctmod_file_handle(base_name)
    if handle:
        return Image(handle)
    else:
        renpy.log.warn(f"No image found for '{base_name}' (.png/.jpg/.jpeg/.webp)")
        return None

#### Background / LR2R Replaced
Apartment_Lobby_Background_image = load_ctmod_image("Apartment_Lobby")
Bathroom_Background_image = load_ctmod_image("Bathroom_Background")
Bar_Background_image = load_ctmod_image("Bar_Background")
Bar_Bathroom_Background_image = load_ctmod_image("Bar_Bathroom_Background")
Beach_Background_image = load_ctmod_image("Beach_Background")
Biotech_Background_image = load_ctmod_image("Biotech_Background")
Break_Room_Background_image = load_ctmod_image("Break_Room_Background")
CEO_Office_Background_image = load_ctmod_image("CEO_Office_Background")
Cloning_Facility_Background_image = load_ctmod_image("Cloning_Facility_Background")
Club_Background_image = load_ctmod_image("Club_Background")
Club_Dressing_Room_Background_image = load_ctmod_image("Club_Dressing_Room_Background")
Cousin_Bedroom_Background_image = load_ctmod_image("Cousin_Bedroom_Background")
Gym_Background_image = load_ctmod_image("Gym_Background")
Lily_Bedroom_Background_image = load_ctmod_image("Lily_Bedroom_Background")
Main_Office_Background_image = load_ctmod_image("Main_Office_Background")
Marketing_Background_image = load_ctmod_image("Marketing_Background")
Office_Lobby_Background_image = load_ctmod_image("Office_Lobby_Background")
Production_Background_image = load_ctmod_image("Production_Background")
RandD_Background_image = load_ctmod_image("RandD_Background")
University_Library_Background_image = load_ctmod_image("University_Library_Background")
MC_Bedroom_Background_image = load_ctmod_image("MC_Bedroom_Background")
MOM_Bedroom_Background_image = load_ctmod_image("MOM_Bedroom_Background")
Vandenberg_Lobby_Background_image = load_ctmod_image("Vandenberg_Lobby_Background")
Home_Shower_Background_image = load_ctmod_image("Home_Shower_Background")
CT_Dungeon_Background_image = load_ctmod_image("CT_Dungeon_Background")
CT_Harem_Background_image = load_ctmod_image("CT_Harem_Background")
Lily_Start_Bedroom_Background_image = load_ctmod_image("Lily_Start_Bedroom_Background")
Mom_Start_Bedroom_Background_image = load_ctmod_image("Mom_Start_Bedroom_Background")
MC_Starting_Bedroom_Background_image = load_ctmod_image("MC_Starting_Bedroom_Background")
Home_Background_image = load_ctmod_image("Home_Background")
Kitchen_Background_image = load_ctmod_image("Kitchen_Background")
Sex_Shop_Background_image = load_ctmod_image("Sex_Shop_Background")
University_Bathroom_Background_image = load_ctmod_image("University_Bathroom_Background")
