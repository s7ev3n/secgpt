from typing import Dict
from llama_index.schema import Document
from llama_index.node_parser import SimpleNodeParser


def to_Document(text):
    return Document(text=text)

def parse_text_into_nodes(
    text, 
    text_splitter,
    metadata: Dict = None
):
    # FIXME implement your own parse to node
    
    docs = [to_Document(text)]
    parser = SimpleNodeParser()

    return parser.get_nodes_from_documents(docs)