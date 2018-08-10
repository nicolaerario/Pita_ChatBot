from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    'Pita', #nome del bot,unico parametro obbligatorio
    storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
    database = './pita_db.sqlite3',
    input_adapter = 'chatterbot.input.VariableInputTypeAdapter',
    output_adapter = 'chatterbot.output.OutputAdapter',
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_first_response"
            }
        ],
    )
#apro il file e lo setto come trainer del bot
with open ('./prima_conversazione.txt') as f:
    conversation = f.readlines()
    bot.set_trainer(ListTrainer)
    bot.train(conversation)

#avvio la conversazione in ciclo infinito
while True:
    try:
        user_input = input('Msg: ')
        response = bot.get_response(user_input)
        print('Pita: ', response)
    except(KeyboardInterrupt, SystemExit):
        print('Arrivederci!')
        break