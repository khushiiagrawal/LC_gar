from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ['HF_HOME'] = 'Desktop/Hugging_Face'
llm = HuggingFacePipeline.from_model_id(
    model_id='HuggingFaceH4/zephyr-7b-beta',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm=llm)

result =  model.invoke("What is capital of india?")

print(result.content)
