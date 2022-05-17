from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot(name='DS Chat Bot', read_only=False)

conversation = [
    'Oi',
    'Olá',
    'Tudo bem?',
    'Tudo ótimo',
    'Você gosta de programar?',
    'Sim, eu programo em Python'
]

list_trainer = ListTrainer(chatbot)
list_trainer.train(conversation)

corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train('chatterbot.corpus.Portuguese')

while True:
    chatbot_input = input("Você >")
    chatbot_response = chatbot.get_response(chatbot_input)

    print(f"{chatbot.name}> {chatbot_response}")