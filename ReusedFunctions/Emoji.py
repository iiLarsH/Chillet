
def get_emoji(key: str):
    emoji_dict = {
        "Mining": "<:Mining:1208243346900910151>",
        "Transporting": "<:Transporting:1208243348771704872>",
        "maxstomach":"<:MaxFood:1208243345672114176>",
        "ATK":"<:ATK:1208242876304195715>",
        "Cooling":"<:Cooling:1208242877822541864>",
        "DEF":"<:DEF:1208242878934159390>",
        "Gen_Electricity":"<:Gen_Electricity:1208242880028737646>",
        "Dark":"<:Dark:1208242881501077584>",
        "Dragon":"<:Dragon:1208242883317071872>",
        "Electricity":"<:Electricity:1208242884772368434>",
        "Fire":"<:Fire:1208242886777503824>",
        "Leaf":"<:Leaf:1208242888102903819>",
        "Earth":"<:Earth:1208243340424773664>",
        "Ice":"<:Ice:1208242891479191594>",
        "Normal":"<:Normal:1208243341578346546>",
        "Water":"<:Water:1208242895870754836>",
        "emptyfood":"<:EmptyFood:1208242899796623360>",
        "Farming":"<:Farming:1208242902296436748>",
        "fullfood":"<:FullFood:1208243343004278824>",
        "Gathering":"<:Gathering:1208242905609805865>",
        "HP":"<:HP:1208242909598720130>",
        "Igniting":"<:Kindling:1208243344522743848>",
        "Logging":"<:Logging:1208242912714825748>",
        "Medicine":"<:Medicine:1208242915793575986>",
        "Planting":"<:Planting:1208242919660851200>",
        "Watering":"<:Watering:1208242927915110410>",
        "Handiwork": "<:Handiwork:1208534651090505788>",
        "None": "❌",
        "Day": "☀️",
        "Night": "🌙",
        "0": "❌",
        "TRUE": "✅",
        "Fly+Land": "🐎🪽",
        "Ground": "🐎",
        "Fly": "🪽",
        "Swim": "🏊"
        }
    return emoji_dict[str(key)]

def get_foodbar(foodamount: int):
    foodamount_emoji = ""

    for i in range(foodamount):
        foodamount_emoji = foodamount_emoji + get_emoji("fullfood")
        i=+1
    for j in range(10-foodamount):
        foodamount_emoji = foodamount_emoji + get_emoji("emptyfood")
        j=+1

    return foodamount_emoji

def get_work(work: dict):
    work_string = ""
    for i in work.keys():
        if(work[i] != 0):
            work_string = work_string + get_emoji(i) + i + ": " + str(work[i]) + "\n"

    return work_string