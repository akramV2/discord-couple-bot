import os
import logging
import random
from datetime import datetime
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

from pathlib import Path

# Charge le fichier .env situé au même endroit que le script
load_dotenv(dotenv_path=Path(__file__).parent / ".env")

TOKEN = os.getenv("MTUzODg3NDYzMjYxNzE5NzYwOQ.GwtIwI.Imxwf1QekWntCnwDH6c6TTezVXLP2q1Yp3P5qc")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("bot")

# Couleurs
ROSE = 0xF4ACB7
KAKI = 0x6B9080
VIOLET = 0x9B5DE5
ORANGE = 0xF28482
JAUNE = 0xF9C74F
BLEU_LAVANDE = 0xC7CEEA

# Date de début du couple : 01/01/2024 à 00:00:00
DATE_RENCONTRE = datetime(2024, 1, 1, 0, 0, 0)

# Liste de GIFs pour la commande /bisou
GIFS_BISOU = [
    "https://media1.giphy.com/media/G3va39rn8E4A8/giphy.gif",
    "https://media2.giphy.com/media/K1tgb1IUeBO0g/giphy.gif",
    "https://media3.giphy.com/media/PHZ7v9tfQu0o0/giphy.gif",
    "https://media4.giphy.com/media/108M7gCS1JSoO4/giphy.gif"
]

intents = discord.Intents.default()

class MonBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        synced = await self.tree.sync()
        logger.info(f"✅ {len(synced)} commandes synchronisées !")

bot = MonBot()

@bot.event
async def on_ready():
    logger.info(f"🤖 Bot connecté sous le nom de : {bot.user}")

# --- TOUTES LES COMMANDES ---

@bot.tree.command(name="aide", description="Affiche la liste de toutes les commandes")
async def aide(interaction: discord.Interaction):
    embed = discord.Embed(
        title="📜  **Menu des Commandes**",
        description="Voici tout ce que vous pouvez faire à deux :\n\n"
                    "💌 **`/motamour`** — Envoyer une pensée douce\n"
                    "📌 **`/dateimportante`** — Marquer un événement\n"
                    "🌷 **`/date`** — Planifier une sortie ou un rendez-vous\n"
                    "📝 **`/envie`** — Noter une envie ou idée cadeau\n"
                    "🍕 **`/repas`** — Proposer une idée de repas manuelle\n"
                    "🎲 **`/roulette`** — Choisir une idée de repas au hasard\n"
                    "⏳ **`/compteur`** — Voir le temps passé ensemble depuis le 01/01/2024\n"
                    "⚖️ **`/choix`** — Trancher une décision entre deux options\n"
                    "📊 **`/sondage`** — Créer un sondage rapide Oui/Non\n"
                    "💋 **`/bisou`** — Envoyer un câlin/bisou mignon\n"
                    "💡 **`/suggestion`** — Proposer une activité\n"
                    "🎬 **`/film`** — Ajouter un film / série\n"
                    "🎮 **`/gaming`** — Organiser une partie\n"
                    "✈️ **`/voyage`** — Préparer une escapade\n"
                    "💸 **`/depense`** — Noter une dépense",
        color=VIOLET
    )
    # Première image Pinterest (Menu Aide)
    embed.set_image(url="https://i.pinimg.com/736x/50/30/98/5030989c332aba06180870aaaa68aab0.jpg")
    embed.set_footer(text=f"Demandé par {interaction.user.display_name}", icon_url=interaction.user.display_avatar.url)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="date", description="Planifie une nouvelle sortie ou un rendez-vous en amoureux !")
@app_commands.describe(
    titre="Le nom de la sortie (ex: Resto Italien, Cinéma...)",
    details="Les petits détails ou le programme",
    date="La date du rendez-vous (ex: Samedi 25)",
    heure="L'heure du rendez-vous (ex: 20h00)"
)
async def date_command(interaction: discord.Interaction, titre: str, details: str, date: str, heure: str):
    embed = discord.Embed(
        title=f"🌷 ・ Nᴏᴜᴠᴇʟʟᴇ Sᴏʀᴛɪᴇ : {titre}",
        description=f"> **📅 Date :** {date}\n> **⏰ Heure :** {heure}\n\n**📝 Programme :**\n{details}",
        color=VIOLET
    )
    # Deuxième image Pinterest (Date / Sortie)
    embed.set_image(url="https://i.pinimg.com/736x/d5/dd/bd/d5ddbd4ace64c2bd172d91deabfb85ce.jpg")
    embed.set_footer(text=f"Proposé par {interaction.user.display_name} 💌", icon_url=interaction.user.display_avatar.url)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="motamour", description="Envoyer un mot doux")
async def motamour(interaction: discord.Interaction, message: str):
    embed = discord.Embed(
        title="💌  **Message d'Amour**",
        description=f"> *« {message} »*",
        color=ROSE
    )
    embed.set_footer(text=f"Envoyé par {interaction.user.display_name}", icon_url=interaction.user.display_avatar.url)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="dateimportante", description="Ajouter un événement")
async def dateimportante(interaction: discord.Interaction, date: str, raison: str):
    embed = discord.Embed(
        title="📌  **Date Importante**",
        description=f"🗓️ **Date :** `{date}`\n✨ **Événement :** **{raison}**",
        color=KAKI
    )
    embed.set_footer(text=f"Ajouté par {interaction.user.display_name}", icon_url=interaction.user.display_avatar.url)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="envie", description="Ajouter une envie")
async def envie(interaction: discord.Interaction, titre: str, detail: str = "Aucun détail"):
    embed = discord.Embed(
        title="📝  **Nouvelle Envie**",
        description=f"🎁 **{titre}**\n\n> *Détails :* {detail}",
        color=ROSE
    )
    embed.set_footer(text=f"Proposé par {interaction.user.display_name}", icon_url=interaction.user.display_avatar.url)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="repas", description="Proposer une idée de repas")
async def repas(interaction: discord.Interaction, plat: str):
    embed = discord.Embed(
        title="🍕  **Au Menu ce soir ?**",
        description=f"Que penses-tu de manger : **{plat.upper()}** ?",
        color=ORANGE
    )
    embed.set_footer(text=f"Proposé par {interaction.user.display_name}", icon_url=interaction.user.display_avatar.url)
    await interaction.response.send_message(embed=embed)
    msg = await interaction.original_response()
    await msg.add_reaction("😋")
    await msg.add_reaction("🤢")

@bot.tree.command(name="roulette", description="Choisit une idée de repas au hasard quand vous hésitez")
async def roulette(interaction: discord.Interaction):
    idees_repas = [
        "🍕 Pizza", "🍔 Burgers faits maison", "🌮 Tacos", "🍣 Sushis / Japonais",
        "🍝 Pâtes Carbonara", "🥗 Grande salade composée", "🧀 Raclette", 
        "🥙 Kebab", "🍗 Poulet rôti et frites", "🍜 Ramen / Pâtes asiatiques", 
        "🥧 Quiche ou Tarte salée", "🥪 Croque-monsieur"
    ]
    plat_choisi = random.choice(idees_repas)
    embed = discord.Embed(
        title="🎲  **La Roulette des Repas**",
        description=f"Ce soir, le bot a tranché pour :\n\n👉 **{plat_choisi}** 😋",
        color=JAUNE
    )
    embed.set_footer(text=f"Demandé par {interaction.user.display_name}", icon_url=interaction.user.display_avatar.url)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="compteur", description="Affiche le nombre exact de jours/mois/années passés ensemble")
async def compteur(interaction: discord.Interaction):
    maintenant = datetime.now()
    delta = maintenant - DATE_RENCONTRE
    
    jours_totaux = delta.days
    annees = jours_totaux // 365
    mois = (jours_totaux % 365) // 30
    jours_restants = (jours_totaux % 365) % 30
    
    heures = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    
    texte = f"🔒 **Ensemble depuis le 01/01/2024 !**\n\n"
    texte += f"✨ Cela fait exactement **{annees} an(s), {mois} mois et {jours_restants} jour(s)** !\n"
    texte += f"⏱️ (Soit au total **{jours_totaux:,} jours**, {heures}h et {minutes}min d'amour) 💕"
    
    embed = discord.Embed(
        title="⏳  **Notre Compteur d'Amour**",
        description=texte,
        color=ROSE
    )
    # Troisième image Pinterest (Compteur d'amour)
    embed.set_image(url="https://i.pinimg.com/736x/4c/75/a6/4c75a627840fa3cf1c714454fcf4e173.jpg")
    embed.set_footer(text=f"Demandé par {interaction.user.display_name}", icon_url=interaction.user.display_avatar.url)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="choix", description="Tranche une décision entre deux options")
@app_commands.describe(option1="Première option", option2="Deuxième option")
async def choix(interaction: discord.Interaction, option1: str, option2: str):
    gagnant = random.choice([option1, option2])
    embed = discord.Embed(
        title="⚖️  **La Décision est Prise !**",
        description=f"Entre **{option1}** et **{option2}**...\n\n👉 Le bot a choisi : **{gagnant}** ! 🎯",
        color=JAUNE
    )
    embed.set_footer(text=f"Demandé par {interaction.user.display_name}", icon_url=interaction.user.display_avatar.url)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="sondage", description="Crée un sondage rapide avec un choix Oui/Non")
@app_commands.describe(question="La question du sondage")
async def sondage(interaction: discord.Interaction, question: str):
    embed = discord.Embed(
        title="📊  **Nouveau Sondage**",
        description=f"**Question :**\n> *{question}*",
        color=BLEU_LAVANDE
    )
    embed.set_footer(text=f"Proposé par {interaction.user.display_name}", icon_url=interaction.user.display_avatar.url)
    await interaction.response.send_message(embed=embed)
    msg = await interaction.original_response()
    await msg.add_reaction("✅")
    await msg.add_reaction("❌")

@bot.tree.command(name="bisou", description="Envoie un GIF de câlin/bisou mignon")
@app_commands.describe(membre="À qui veux-tu faire un bisou ? (Optionnel)")
async def bisou(interaction: discord.Interaction, membre: discord.Member = None):
    gif = random.choice(GIFS_BISOU)
    if membre:
        msg = f"💋 {interaction.user.mention} envoie un gros bisou à {membre.mention} !\n{gif}"
    else:
        msg = f"💋 {interaction.user.mention} envoie un gros bisou plein d'amour !\n{gif}"
    await interaction.response.send_message(msg)

@bot.tree.command(name="suggestion", description="Proposer une idée de sortie")
async def suggestion(interaction: discord.Interaction, idee: str):
    embed = discord.Embed(
        title="💡  **Nouvelle Idée / Sortie**",
        description=f"> **{idee}**",
        color=VIOLET
    )
    embed.set_footer(text=f"Proposé par {interaction.user.display_name}", icon_url=interaction.user.display_avatar.url)
    await interaction.response.send_message(embed=embed)
    msg = await interaction.original_response()
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")

@bot.tree.command(name="film", description="Ajouter un film/série")
async def film(interaction: discord.Interaction, titre: str, plateforme: str = "Non spécifiée"):
    embed = discord.Embed(
        title="🎬  **À Regarder Ensemble**",
        description=f"🍿 **Titre :** **{titre}**\n📺 **Plateforme :** `{plateforme}`",
        color=VIOLET
    )
    embed.set_footer(text=f"Ajouté par {interaction.user.display_name}", icon_url=interaction.user.display_avatar.url)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="gaming", description="Proposer une session de jeu")
async def gaming(interaction: discord.Interaction, jeu: str, heure: str):
    embed = discord.Embed(
        title="🎮  **Session Gaming**",
        description=f"🕹️ **Jeu :** **{jeu}**\n⏰ **Heure :** `{heure}`",
        color=ROSE
    )
    embed.set_footer(text=f"Proposé par {interaction.user.display_name}", icon_url=interaction.user.display_avatar.url)
    await interaction.response.send_message(embed=embed)
    msg = await interaction.original_response()
    await msg.add_reaction("🔥")

@bot.tree.command(name="voyage", description="Proposer un projet de voyage")
async def voyage(interaction: discord.Interaction, destination: str, date: str):
    embed = discord.Embed(
        title="✈️  **Projet Voyage**",
        description=f"📍 **Destination :** **{destination}**\n🗓️ **Période :** `{date}`",
        color=KAKI
    )
    embed.set_footer(text=f"Proposé par {interaction.user.display_name}", icon_url=interaction.user.display_avatar.url)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="depense", description="Noter une dépense")
async def depense(interaction: discord.Interaction, montant: str, description: str):
    embed = discord.Embed(
        title="💳  **Dépense Commune**",
        description=f"💶 **Montant :** `{montant} €`\n🏷️ **Motif :** **{description}**",
        color=ORANGE
    )
    embed.set_footer(text=f"Noté par {interaction.user.display_name}", icon_url=interaction.user.display_avatar.url)
    await interaction.response.send_message(embed=embed)

# --- Lancement du bot ---
if __name__ == "__main__":
    bot.run(TOKEN)