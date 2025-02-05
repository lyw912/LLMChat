
MODEL_ROOT_PATH = ""

TEMPERATURE = 0.8

LLM_MODELS = ["zhipu-api"]

# LLM_MODELS = ["chatglm3-6b", "zhipu-api"]
# LLM_MODELS = ["chatglm3-6b"]
MODEL_PATH = {
    # 这里定义 本机服务器上存储的大模型权重存储路径
    "local_model": {
        "chatglm3-6b": "/home/chatglm3-6b",

        # 可扩展其他的开源大模型

    },
    
    # 这里定义 本机服务器上存储的Embedding模型权重存储路径
    "embed_model": {
        "bge-large-zh-v1.5": "/home/embedding",

        # 可扩展其他的Embedding模型
    },
}


ONLINE_LLM_MODEL = {

    # 智谱清言的在线API服务
    "zhipu-api": {
        "api_key": "3112981fb0965044d5f8119e703e7d23.FQyRabW7Ybl01I3n",
        "version": "GLM-4-Air",
        "provider": "ChatGLMWorker",
    },

    # OpenAI GPT模型的在线服务
    "openai-api": {
        "model_name": "gpt-4",
        "api_base_url": "https://api.openai.com/v1",
        "api_key": "",
        "openai_proxy": "",
    },

    # 可扩展其他的模型在线模型
    
}



# 选用的 Embedding 名称
EMBEDDING_MODEL = "bge-large-zh-v1.5"

# Embedding 模型运行设备。设为 "auto" 会自动检测(会有警告)，也可手动设定为 "cuda","mps","cpu","xpu" 其中之一。
EMBEDDING_DEVICE = "auto"