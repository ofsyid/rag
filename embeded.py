import json
import pandas as pd
import mysql.connector

from sentence_transformers import SentenceTransformer


embedder = SentenceTransformer('BAAI/bge-m3')

db = mysql.connector.connect(
 host = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
  port = 4000,
  user = "2NMeMXHpYJWjnBz.root",
  password = "nbILMEG4ndMHOh0q",
  database = "RAG",
  ssl_ca = r"C:\Users\LENOVO\Desktop\RAG_TIDB\ca.pem",
  ssl_verify_cert = True,
  ssl_verify_identity = True
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