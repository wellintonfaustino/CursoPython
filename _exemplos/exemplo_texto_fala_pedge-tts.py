import edge_tts
import asyncio

async def gerar_audio():
    texto = "O relatório gerencial de novembro de 2024 do FII BTG Pactual Terras Agrícolas (BTRA11) apresenta os resultados e a estratégia do fundo, que investe em terras agrícolas produtivas e em transformação pelo Brasil. O objetivo é gerar valorização no longo prazo por meio de contratos de cessão de direito real de superfície ajustados pela inflação. O fundo adota a opção de recompra de propriedades, permitindo ao antigo proprietário readquirir o imóvel mediante pagamento de prêmios, desde que as condições contratuais sejam cumpridas. Em termos financeiros, o fundo teve uma receita líquida de R$ 1,511 milhões (R$ 0,45 por cota) em novembro de 2024, com distribuição de R$ 0,30 por cota aos investidores, resultando em um dividend yield anualizado de 8,1%. Apesar disso, o desempenho acumulado em 12 meses registrou queda de 27,2% no valor das cotas, reflexo de oscilações do mercado e do desempenho do índice IFIX. O portfólio do fundo inclui seis propriedades distribuídas em estados como Mato Grosso e Bahia, com foco em culturas como soja, milho e algodão.O fundo ressalta o impacto positivo de condições climáticas favoráveis para a safra 2024/2025, com aumento significativo na produção de grãos, especialmente soja. Apesar do cenário promissor no setor agrícola, a inflação no Brasil (4,87% nos últimos 12 meses) ultrapassou a meta estipulada, refletindo no poder aquisitivo dos investidores. No geral, o relatório enfatiza a estratégia de longo prazo do fundo e os desafios econômicos e climáticos enfrentados." 
    comunicador = edge_tts.Communicate(texto, voice="pt-BR-ThalitaMultilingualNeural")
    await comunicador.save("audio.mp3")
    """
    pt-BR-AntonioNeural                Male      General                Friendly, Positive
    pt-BR-FranciscaNeural              Female    General                Friendly, Positive
    pt-BR-ThalitaMultilingualNeural    Female    General                Friendly, Positive
    """

asyncio.run(gerar_audio())
print("Áudio salvo como audio.mp3")
