
from langchain.embeddings import CohereEmbeddings
import weaviate
import json
import os





client = weaviate.Client(
    url = "https://llm-chatai-bot-v2-mmelxkrr.weaviate.network",  # Replace with your endpoint
    auth_client_secret=weaviate.AuthApiKey(api_key=os.environ.get('we')),  # Replace w/ your Weaviate instance API key
    additional_headers = {
       "X-Cohere-Api-Key": os.environ.get('co')  # Replace with your inference API key
    }
)
embeddings = CohereEmbeddings(cohere_api_key=os.environ.get('co'),model='multilingual-22-12')




# from langchain.callbacks import get_openai_callback

# def count_tokens(agent, query):
#     with get_openai_callback() as cb:
#         result = agent.run(query)
#         print(f'Spent a total of {cb.total_tokens} tokens')

#     return result


from pymongo import MongoClient
class Mem:
    def __init__(self) -> None:
        pass

    def init_mem(self,id_session):
        
        client = MongoClient(os.environ.get('mongo_url'))
        
        db = client['Bot-history']

        collection = db['Chat-history']

        existing_data = collection.find_one({'Id': id_session})

        

        if existing_data == None:

            # exist_memory_list = eval(existing_data['msg_history'])
            a1 = f"hello, my name is {id_session}."
            a2 = f"Hello {id_session}! How can I assist you today?"
            new_msg_history = [(a1, a2)]
         
         
            collection.insert_one({'Id': id_session,'msg_history': new_msg_history})

        else:
            pass


    def bot_memory(self,id_session):
        client = MongoClient(os.environ.get('mongo_url'))
        
        db = client['Bot-history']

        collection = db['Chat-history']

        existing_data = collection.find_one({'Id': id_session})
        if existing_data!=None:

            return collection.find_one({'Id': id_session})['msg_history']

        # else:
        #     data ={ 'Id' :id_session,
        #     'msg_history':str([])}

        #     self.insert_or_update_data(data)

        #     return eval(collection.find_one({'Id': id_session})['msg_history'])
            


    def insert_or_update_data(self,data):
  
        client = MongoClient(os.environ.get('mongo_url'))
    
        try:
          
            db = client['Bot-history']
    
      
            collection = db['Chat-history']
  
            existing_data = collection.find_one({'Id': data['Id']})
    
            if existing_data!=None:
    
         

                exist_list = existing_data['msg_history']
                new_msg_history = exist_list + data['msg_history']
    
         
                collection.update_one({'Id': data['Id']}, {'$set': {'msg_history': new_msg_history}})
   
            else:

                collection.insert_one(data)
 
        except Exception as e:
            print('Error while inserting/updating data:', e)
        finally:
     
            client.close()


    def finder(self,id_session):
        client = MongoClient(os.environ.get('mongo_url'))
        
        db = client['Bot-history']

        collection = db['Chat-history']

        existing_data = collection.find_one({'Id': id_session})

        exist_memory_list = existing_data['msg_history']

        if len(exist_memory_list) > 100:
            a1 = f"hello, my name is {id_session}."
            a2 = f"Hello {id_session}! How can I assist you today?"
            new_msg_history = [(a1, a2)]
    
         
            collection.update_one({'Id': id_session}, {'$set': {'msg_history': new_msg_history}})
            




from langchain.vectorstores.weaviate import Weaviate
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
# from langchain.chains import ConversationalRetrievalChain
# from langchain.chains import ChatVectorDBChain
from langchain.chains.question_answering import load_qa_chain


PROMPT = PromptTemplate(

    template="""Your are a smart assitant name tobi.First go through chat_history. Use the following pieces of context to answer \
                or If you don't know the answer, you can provide short answer. \
                remember use chat_hsitory as a conversation flow between you and user, always follow the chat_history flow and  \
                always go through before answering and if user provide new information then override the chat_history according to it.

                {context}

                {chat_history}          
                Question: {question}
                
          """,
    input_variables=["question","context","chat_history"]
)

#{chat_history}

chain_type_kwargs = {"prompt": PROMPT}




vectorstore = Weaviate(client, "Wikipedia", "text")

def docs_result(query,num = 2):
    doc = vectorstore.similarity_search(
        query, 
        k=int(num)
    )

    return doc

# qa = ConversationalRetrievalChain.from_llm(ChatOpenAI(openai_api_key=os.environ.get('openai'),temperature=0,model='gpt-3.5-turbo'),
#                                            vectorstore.as_retriever(),
#                                         #    memory=memory,
#                                            combine_docs_chain_kwargs=chain_type_kwargs,
#                                           #  verbose= True
#                                            )
def qa(query,chat_history):
    doc =docs_result(query)

    # print(doc)
    chain = load_qa_chain(ChatOpenAI(openai_api_key=os.environ.get('openai'),temperature=0.0,model='gpt-3.5-turbo'), chain_type="stuff",prompt=PROMPT)

    
    result2 = chain.run(input_documents=doc, question=query,chat_history= chat_history)  
    return result2


#os.environ.get('openai')