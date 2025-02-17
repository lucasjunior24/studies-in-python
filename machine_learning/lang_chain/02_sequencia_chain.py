
from langchain.prompts import ChatPromptTemplate

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
load_dotenv()
from langchain.chains import SimpleSequentialChain
from langchain.chains import LLMChain

modelo_cidade = ChatPromptTemplate.from_template(
    "Sugira uma cidade dado meu interesse por {interesse}"
)

modelo_restaurantes = ChatPromptTemplate.from_template(
    "Sugira restaurantes populares entre locais em {cidade}"
)

modelo_cultural = ChatPromptTemplate.from_template(
    "Sugira atividades e locais culturais em {cidade}"
)
llm = init_chat_model("llama3-8b-8192", model_provider="groq")

cadeia_cidade = LLMChain(prompt=modelo_cidade, llm=llm)
cadeia_restaurantes = LLMChain(prompt=modelo_restaurantes, llm=llm)
cadeia_cultural = LLMChain(prompt=modelo_cultural, llm=llm)

cadeia = SimpleSequentialChain(chains=[cadeia_cidade, cadeia_restaurantes, cadeia_cultural], verbose=True)
data = cadeia.invoke('praias')
print(data['output'])
