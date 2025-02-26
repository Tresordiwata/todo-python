from llama_index.core import Document,VectorStoreIndex
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY= os.getenv("OPENAI_KEY")
# OPENAI_API_KEY= os.environ["OPENAI_KEY"]


# cle=os.getenv("OPENAI_KEY")
# print(cle)


documents=[
    Document(text="Je suis Tresor Diwata, née le 05/03/1988 à kinshasa"),
    Document(text="J'ai maintenant 2 fillettes Eluzia et perla"),
    Document(text="j'aime du sport precisement le Basketball et le football, en Basket j'aime Le lakers"),
    Document(text="Je suis informaticien developpeur de carriere"),
    Document(text="J'ai des grands reves."),
    Document(text="Mon pays c'est la RDC"),
    Document(text="La RDC  est un pays d'afrique central en guerre")
]
# print("essaie")
index=VectorStoreIndex(documents)
query_engine=index.as_query_engine()
response1=query_engine.query("qui est Tresor Diwata ?")
response2=query_engine.query("Tu connais la RDC ?")

print(response1)

