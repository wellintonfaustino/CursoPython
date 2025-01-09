import edge_tts
import asyncio

async def gerar_audio():
    texto = "É que eu aprendi a criar áudios, agora aquelas velhas que não sabem ler podem ouvir. Mas vou cobrar do Renan, obviamente! O Play dele ainda está pra jogo?"
    comunicador = edge_tts.Communicate(texto, voice="pt-BR-ThalitaMultilingualNeural")
    await comunicador.save("audio.wav")
    """
    pt-BR-AntonioNeural                Male      General                Friendly, Positive
    pt-BR-FranciscaNeural              Female    General                Friendly, Positive
    pt-BR-ThalitaMultilingualNeural    Female    General                Friendly, Positive
    """

asyncio.run(gerar_audio())
print("Áudio salvo como audio.mp3")
