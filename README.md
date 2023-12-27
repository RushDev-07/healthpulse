Healthcare Data Retrieval and Management

Description

This project will give you all the required information regarding the home health care agencies in India in a JSON format. The input will be a text file containing all the website links for these agencies.

Note:- For any langchain or localGPT related issues vist the following link to resolve the same.
https://github.com/PromtEngineer/localGPT

Table of Contents
Installation
Usage
Features
Tehnical Features

Installation

Provide step-by-step instructions on how to install and set up your project. Include any dependencies that need to be installed and configuration steps.
1. 📥 Clone the repo using git:
    git clone https://github.com/PromtEngineer/localGPT.git

2. 🐍 Install https://www.anaconda.com/download for virtual environment management. Create and activate a new virtual environment.
    conda create -n localGPT python=3.10.0
    conda activate localGPT
3. 🛠️ Install the dependencies using pip
   To set up your environment to run the code, first install all requirements:

   pip install -r requirements.txt

Installing LLAMA-CPP :

LocalGPT uses LlamaCpp-Python for GGML (you will need llama-cpp-python <=0.1.76) and GGUF (llama-cpp-python >=0.1.83) models.

If you want to use BLAS or Metal with llama-cpp you can set appropriate flags:

For NVIDIA GPUs support, use cuBLAS

# Example: cuBLAS
CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python==0.1.83 --no-cache-dir
For Apple Metal (M1/M2) support, use

# Example: METAL
CMAKE_ARGS="-DLLAMA_METAL=on"  FORCE_CMAKE=1 pip install llama-cpp-python==0.1.83 --no-cache-dir
For more details, please refer to llama-cpp


Usage

To start using the project do the following:-
1. Give all the web links required in a text file named Link_url.txt
2. Run the webscrapper.py. This will update the weblinks.txt with all the text from the web links and its sub links in its raw form. (Note: This will overwrite the previous data.)
3. Ingest the weblinks.py file using the ingest.py file.
4. Run the run_localGPT.py. This will update the output_required.txt with the required information in JSON format.

Note:-
When you will run the run_localGPT.py file it will automatically download the specified llama model in the constants.py. To change the model go in the constants.py file and the required details.

Features

1. Utmost Privacy: Your data remains on your computer, ensuring 100% security.
2. Versatile Model Support: Seamlessly integrate a variety of open-source models, including HF, GPTQ, GGML, and GGUF.
3. Diverse Embeddings: Choose from a range of open-source embeddings.
4. Reuse Your LLM: Once downloaded, reuse your LLM without the need for repeated downloads.
5. Chat History: Remembers your previous conversations (in a session).
6. API: LocalGPT has an API that you can use for building RAG Applications.
7. Graphical Interface: LocalGPT comes with two GUIs, one uses the API and the other is standalone (based on streamlit).
8. GPU, CPU & MPS Support: Supports multiple platforms out of the box, Chat with your data using CUDA, CPU or MPS and more!

Technical Details 🛠️
    
By selecting the right local models and the power of LangChain you can run the entire RAG pipeline locally, without any data leaving your environment, and with reasonable performance.

1. ingest.py uses LangChain tools to parse the document and create embeddings locally using InstructorEmbeddings. It then stores the result in a local vector database using Chroma vector store.
2. run_localGPT.py uses a local LLM to understand questions and create answers. The context for the answers is extracted from the local vector store using a similarity search to locate the right piece of context from the docs.
3. You can replace this local LLM with any other LLM from the HuggingFace. Make sure whatever LLM you select is in the HF format.
4. This project was inspired by the original localGPT.

Acknowledgments

This project uses localGPT (https://github.com/PromtEngineer/localGPT) to extract information and convert it into a JSON format.

Contact

Email: rushg.one@gmail.com
Instagram: @drmehta_07
Phone Number: 9834044354
