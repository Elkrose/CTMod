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

def get_file_handle(base_name: str) -> str | None:
    """
    Look for base_name with any of the common image extensions.
    Returns the first matching path from renpy.exports.list_files().
    """
    exts = (".png", ".jpg", ".jpeg")
    files = renpy.exports.list_files()
    for ext in exts:
        target = base_name + ext
        # match by “endswith” so we catch paths like ".../CTimages/Name.png"
        found = next((f for f in files if f.endswith(target)), None)
        if found:
            return found
    return None

def load_image(base_name: str) -> Image | None:
    handle = get_file_handle(base_name)
    if handle:
        return Image(handle)
    else:
        renpy.log.warn(f"No image found for '{base_name}' (.png/.jpg/.jpeg)")
        return None

#### Background / LR2R Replaced
Apartment_Lobby_Background_image = Image(get_file_handle("Apartment_Lobby"))
Bathroom_Background_image = Image(get_file_handle("Bathroom_Background"))
Bar_Background_image = Image(get_file_handle("Bar_Background"))
Beach_Background_image = Image(get_file_handle("Beach_Background"))
Biotech_Background_image = Image(get_file_handle("Biotech_Background"))
Break_Room_Background_image = Image(get_file_handle("Break_Room_Background"))
CEO_Office_Background_image = Image(get_file_handle("CEO_Office_Background"))
Cloning_Facility_Background_image = Image(get_file_handle("Cloning_Facility_Background"))
Club_Background_image = Image(get_file_handle("Club_Background"))
Club_Dressing_Room_Background_image = Image(get_file_handle("Club_Dressing_Room_Background"))
Cousin_Bedroom_Background_image = Image(get_file_handle("Cousin_Bedroom_Background"))
Gym_Background_image = Image(get_file_handle("Gym_Background"))
Lily_Bedroom_Background_image = Image(get_file_handle("Lily_Bedroom_Background"))
Main_Office_Background_image = Image(get_file_handle("Main_Office_Background"))
Marketing_Background_image = Image(get_file_handle("Marketing_Background"))
Office_Lobby_Background_image = Image(get_file_handle("Office_Lobby_Background"))
Production_Background_image = Image(get_file_handle("Production_Background"))
RandD_Background_image = Image(get_file_handle("RandD_Background"))
University_Library_Background_image = Image(get_file_handle("University_Library_Background"))
MC_Bedroom_Background_image = Image(get_file_handle("MC_Bedroom_Background"))
MOM_Bedroom_Background_image = Image(get_file_handle("MOM_Bedroom_Background"))
Vandenberg_Lobby_Background_image = Image(get_file_handle("Vandenberg_Lobby_Background"))
Home_Shower_Background_image = Image(get_file_handle("Home_Shower_Background"))
CT_Dungeon_Background_image = Image(get_file_handle("CT_Dungeon_Background"))
CT_Harem_Background_image = Image(get_file_handle("CT_Harem_Background"))
Lily_Start_Bedroom_Background_image = Image(get_file_handle("Lily_Start_Bedroom_Background"))
Mom_Start_Bedroom_Background_image = Image(get_file_handle("Mom_Start_Bedroom_Background"))
MC_Starting_Bedroom_Background_image = Image(get_file_handle("MC_Starting_Bedroom_Background"))
Home_Background_image = load_image("Home_Background")
Kitchen_Background_image = load_image("Kitchen_Background")