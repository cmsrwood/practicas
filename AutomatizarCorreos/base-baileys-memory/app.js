const { createBot, createProvider, createFlow, addKeyword } = require('@bot-whatsapp/bot')

const QRPortalWeb = require('@bot-whatsapp/portal')
const BaileysProvider = require('@bot-whatsapp/provider/baileys')
const MockAdapter = require('@bot-whatsapp/database/mock')

const flowSecundario = addKeyword(['2', 'siguiente']).addAnswer(['Aquí tenemos el flujo secundario'])

const flowPrincipal = addKeyword(['hola', 'ole', 'alo'])
    .addAnswer('Bienvenido al chat bot de Dilan')
    .addAnswer(
        [
            'Escribe 2 para continuar con el flujo secundario',
        ],
        null,
        null,
        [flowSecundario]
    )

const main = async () => {
    const adapterDB = new MockAdapter()
    const adapterFlow = createFlow([flowPrincipal])
    const adapterProvider = createProvider(BaileysProvider)

    createBot({
        flow: adapterFlow,
        provider: adapterProvider,
        database: adapterDB,
    })

    QRPortalWeb()
}

main()
