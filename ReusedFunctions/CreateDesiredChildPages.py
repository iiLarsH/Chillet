import sqlite3, discord

def DividePages(all_info: list):
    total_combinations = len(all_info)
    num_pages = (total_combinations + 9) // 10  # Calculate the total number of pages
    pages = []

    for page_num in range(num_pages):
        start_index = page_num * 10
        end_index = min((page_num + 1) * 10, total_combinations)
        page_combinations = all_info[start_index:end_index]

        pages.append(discord.Embed(title=f"Breeding options {page_num + 1}/{num_pages}: "))
        for combination in page_combinations:
            pages[page_num].add_field(name=combination, value="", inline=False)
    return pages
