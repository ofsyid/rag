import json
import pandas as pd
import mysql.connector

from sentence_transformers import SentenceTransformer


embedder = SentenceTransformer('BAAI/bge-m3')

db = mysql.connector.connect(
 # TEMPEL DISINI, DIAMBIL DARI TI.DB 
 # python (MySQL Connector)
)

curr = db.cursor()

df  = pd.read_csv("data_knowledge.csv")

for index, row in df.iterrows():
        text = str(row['question']) + " " + str(row['answer'])

        try:
                embedding_list = embedder.encode(text).tolist()
                embedding_str = json.dumps(embedding_list)

                sql_query = """
                                INSERT INTO documents (text, embedding) VALUES (%s,%s)
                        """


                curr.execute(sql_query, (text, embedding_str))
                print(f"data index-{index} berhasil ditambah")
        except Exception as e:
                print(f"data index-{index} error: {e}")
                print(f"data index-{index} gagal ditambah")

db.commit()
curr.close()
print("data berhasil ditambahkan")
