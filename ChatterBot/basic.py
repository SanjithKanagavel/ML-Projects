from chatterbot import ChatBot

chatbot = ChatBot(
    'Jarvis',
	silence_performance_warning=True,
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
	input_adapter="chatterbot.adapters.input.TerminalAdapter",
    output_adapter="chatterbot.adapters.output.TerminalAdapter"
)

# Train based on the english corpus
chatbot.train(
	"chatterbot.corpus.english",
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)
print('Welcome. Jarvis here :)');
while True:
    try:
		#print("Me :%s",None)
		response = chatbot.get_response(None)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
