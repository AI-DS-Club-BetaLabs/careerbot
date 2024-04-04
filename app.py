from careerbot.pipeline.chat import Chat


SCRAPE = True 


chat = Chat()
chat.initiate(SCRAPE)

while True:
    query = input("Enter the query: ")
    response = chat.respond(query)
    print(response)
    print("\n\n")
