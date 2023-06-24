
from langchain.embeddings import CohereEmbeddings
import weaviate
import json

client = weaviate.Client(
    url = "https://llm-chatai-bot-v2-mmelxkrr.weaviate.network",  # Replace with your endpoint
    auth_client_secret=weaviate.AuthApiKey(api_key="RDdL12G2jw7mm8ns7DaDBRkdU2mT8OTAkGOG"),  # Replace w/ your Weaviate instance API key
    additional_headers = {
       "X-Cohere-Api-Key": "PoQqB6c283yGmex4A2cSwQWxYj5oP1rh9bkuqKYy"  # Replace with your inference API key
    }
)
embeddings = CohereEmbeddings(cohere_api_key='PoQqB6c283yGmex4A2cSwQWxYj5oP1rh9bkuqKYy',model='multilingual-22-12')




from langchain.callbacks import get_openai_callback

def count_tokens(agent, query):
    with get_openai_callback() as cb:
        result = agent.run(query)
        print(f'Spent a total of {cb.total_tokens} tokens')

    return result


from pymongo import MongoClient
class Mem:
    def __init__(self) -> None:
        pass
    def bot_memory(self,id_session):
        client = MongoClient('mongodb+srv://Keval:wITlI7TnqdzjQYn2@cluster-bot-app.98wpose.mongodb.net/')
        
        db = client['Bot-history']

        collection = db['Chat-history']

        existing_data = collection.find_one({'Id': id_session})
        if existing_data!=None:
            
            return eval(collection.find_one({'Id': id_session})['msg_history'])

        else:
            data ={ 'Id' :id_session,
            'msg_history':str([])}

            self.insert_or_update_data(data)

            return eval(collection.find_one({'Id': id_session})['msg_history'])
            


    def insert_or_update_data(self,data):
  
        client = MongoClient('mongodb+srv://Keval:wITlI7TnqdzjQYn2@cluster-bot-app.98wpose.mongodb.net/')
    
        try:
          
            db = client['Bot-history']
    
      
            collection = db['Chat-history']
  
            existing_data = collection.find_one({'Id': data['Id']})
    
            if existing_data!=None:
    
         

                exist_list = eval(existing_data['msg_history'])
                new_msg_history = exist_list + data['msg_history']
    
         
                collection.update_one({'Id': data['Id']}, {'$set': {'msg_history': str(new_msg_history)}})
   
            else:

                collection.insert_one(data)
 
        except Exception as e:
            print('Error while inserting/updating data:', e)
        finally:
     
            client.close()





from langchain.vectorstores.weaviate import Weaviate
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain.chains import ChatVectorDBChain



PROMPT = PromptTemplate(

    template="""Your are a helpful assitant, Use the following pieces of context to answer the specific question \
                remaining you will answer from your chat_history \
                at the end. If you don't know the answer, just say that you don't know, \
                don't try to make up an answer. Note you are an assitant created by keval.

                {context}

                {chat_history}             
                Question: {question}
                
          """,
    input_variables=["chat_history","question","context"]
)

chain_type_kwargs = {"prompt": PROMPT}


client = weaviate.Client(
    url = "https://llm-chatai-bot-v2-mmelxkrr.weaviate.network",  # Replace with your endpoint
    auth_client_secret=weaviate.AuthApiKey(api_key="RDdL12G2jw7mm8ns7DaDBRkdU2mT8OTAkGOG"),  # Replace w/ your Weaviate instance API key
    additional_headers = {
       "X-Cohere-Api-Key": "PoQqB6c283yGmex4A2cSwQWxYj5oP1rh9bkuqKYy"  # Replace with your inference API key
    })

vectorstore = Weaviate(client, "Wikipedia", "text")


qa = ConversationalRetrievalChain.from_llm(ChatOpenAI(openai_api_key='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',temperature=0,model='gpt-3.5-turbo'),
                                           vectorstore.as_retriever(),
                                        #    memory=memory,
                                           combine_docs_chain_kwargs=chain_type_kwargs,
                                          #  verbose= True
                                           )



