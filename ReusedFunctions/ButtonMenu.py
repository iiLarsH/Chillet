import discord
from typing import Optional, List

class ButtonMenu(discord.ui.View):
    def __init__(self, pages: list, timeout: float, user: Optional[discord.Member]=None)->None:
        super().__init__(timeout=timeout)
        self.current_page = 0
        self.pages = pages
        self.user = user
        self.length = len(pages)-1
        self.children[0].disabled, self.children[1].disabled = True, True

    async def update(self, page: int):
        self.current_page = page
        if page == 0:
            self.children[0].disabled = True
            self.children[1].disabled = True
            self.children[2].disabled = False
            self.children[3].disabled = False
        elif page == self.length:
            self.children[0].disabled = False
            self.children[1].disabled = False
            self.children[2].disabled = True
            self.children[3].disabled = True
        else:
            for i in self.children: i.disabled=False

    async def get_page(self, page):
        if isinstance(page, discord.Embed):
            return None, [page], []
        
    async def show_page(self, page: int, interaction: discord.Interaction):
        await self.update(page)
        contents, embeds, files = await self.get_page(self.pages[page])

        await interaction.response.edit_message(
            content=contents,
            embeds=embeds,
            attachments=files or [],
            view=self
        )

    @discord.ui.button(emoji=u"\u23EA", style=discord.ButtonStyle.primary)
    async def first_page(self, interaction, button):
        await self.show_page(0, interaction)

    @discord.ui.button(emoji=u"\u25C0", style=discord.ButtonStyle.primary)
    async def prev_page(self, interaction, button):
        await self.show_page(self.current_page-1, interaction)

    @discord.ui.button(emoji=u"\u25B6", style=discord.ButtonStyle.primary)
    async def next_page(self, interaction, button):
        await self.show_page(self.current_page+1, interaction)
    
    @discord.ui.button(emoji=u"\u23E9", style=discord.ButtonStyle.primary)
    async def last_page(self, interaction, button):
        await self.show_page(self.length, interaction)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if self.user:
            if interaction.user != self.user:
                await interaction.response.send_message("This command is invoked by another person",
                                                         ephemeral=True,)
                return False
        return True
            
