from typing import List, Optional, Sequence
from llama_index.schema import BaseNode

from secgpt.schema import BaseFiling
from secgpt.nodes.utils import parse_text_into_nodes

class FilingNodeParser:
    """Filing node parser.
    
    Given filing object, parse it into nodes using TextSplitter,
    currently support linked list relationship between nodes.

    Args:
        text_splitter: text_splitter to split the text data
        keep_metadata (bool): wether to embed filing metadata into nodes
    """

    def __init__(self, 
                text_splitter = None,
                keep_metadata : bool = True) -> None:

        self.text_splitter = text_splitter

    def parse_nodes_from_filing(
        self, 
        filing : BaseFiling) -> List[BaseNode]:
        """Parse filing into nodes"""

        all_nodes: List[BaseNode] = []
        for section, data in filing.data.items():
            nodes = parse_text_into_nodes(
                data,
                self.text_splitter,
                self.keep_metadata
            )
            all_nodes.extend(nodes)

        return all_nodes
