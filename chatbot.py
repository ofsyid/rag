import mysql.connector
import json
import ollama

from sentence_transformers import SentenceTransformer

OLLAMA_HOST = "http://127.0.0.1:11434"
OLLAMA_MODEL = "deepseek-llm:latest"

llm_agent = ollama.Client(host=OLLAMA_HOST)
embedder = SentenceTransformer('BAAI/bge-m3')

db = mysql.connector.connect(
 # DIAMBIL DARI TI.DB PASTE DISINI
 # python (MySQL Connector)
)



def search_document(database,query,k_top=5):
      results = []

      query_embedding_list = embedder.encode(query).tolist()
      query_embedding_str = json.dumps(query_embedding_list)

      curr = database.cursor()

      sql_query = f"""
                    SELECT text, vec_cosine_distance(embedding,%s) AS distance 
                    FROM documents
                    ORDER BY distance ASC
                    LIMIT {k_top}

            """
      curr.execute(sql_query,(query_embedding_str,))
      search_results = curr.fetchall()
      database.commit()
      curr.close()

      for result in search_results:
            text,distance = result
            results.append({  
                  'text':text,
                  'distance':distance
            })
      return results

def response_query(database,query):
    retrieved_doc = search_document(database,query)

    context = "\n".join([doc['text']for doc in retrieved_doc])
    prompt = f"Answer the following question based on the provided context{context}\n\nquestion:{query}"
    response = llm_agent.chat(model=OLLAMA_MODEL,messages=[
          {
                'role':'user',
                'content':prompt
          }
    ])

    # print(response)
    return response['message']['content']


if __name__ == "__main__":
    print("CHATBOT DIMULAYYY")
    while True:
            query_text = input("prompt: ")

            if query_text.lower() in ['exit', 'quit','q']:
                    print("Closing Chatbot....")
                    break
            
            response = response_query(database=db,query=query_text)
            print("Chatbot: ",response)

print("CHATBOT SELESAAAII")
