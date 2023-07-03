from typing import List, Optional, Sequence
from llama_index.schema import BaseNode

from secgpt.schema import BaseFiling

class FilingNodeParser:
    """Filing node parser.
    
    Given filing object, parse it into nodes using TextSplitter,
    currently support linked list relationship between nodes.
    TODO: ImageEncoder and TableParser.

    Args:
        text_splitter:
        img_encoder: 
        table_parser:
        keep_metadata (bool):
    """

    def __init__(self, 
                text_splitter = None,
                img_encoder = None,
                table_parser = None,
                keep_metadata : bool = True) -> None:

        self.text_splitter = text_splitter
        self.img_encoder = img_encoder
        self.table_parser = table_parser

    def parse_nodes_from_filing(
        self, 
        filing : BaseFiling) -> List[BaseNode]:
        """Parse filing into nodes"""

        nodes: List[BaseNode] = []
        for section, data in filing.data.items():
           # TODO
           pass 

        return nodes
