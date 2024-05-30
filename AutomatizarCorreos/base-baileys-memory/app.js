const { createBot, createProvider, createFlow, addKeyword } = require('@bot-whatsapp/bot')

const QRPortalWeb = require('@bot-whatsapp/portal')
const BaileysProvider = require('@bot-whatsapp/provider/baileys')
const MockAdapter = require('@bot-whatsapp/database/mock')

const stopWork = addKeyword(['STOP WORK', '1'])
    .addAnswer('STOP WORK')


const otraOpcion = addKeyword(['OTRA OPCION', '2'])
    .addAnswer('OTRA OPCION')
    
const otraOtraOpcion = addKeyword(['OTRA OPCION OPCION', '3'])
.addAnswer('OTRA OPCION OPCION')

const flowPrincipal = addKeyword(['hola', 'ole', 'alo' , 'ola'])
    .addAnswer('Bienvenido al chat bot de Dilan')
    .addAnswer(
        [
            'Escoja una opcion: ',
            'STOP WORK',
            'OTRA OPCION',
            'OTRA OTRA OPCION'
        ],
        null,
        null,
        [stopWork,otraOpcion,otraOtraOpcion]
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
